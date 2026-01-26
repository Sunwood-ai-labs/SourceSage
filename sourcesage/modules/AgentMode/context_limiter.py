"""
Context Limiter for AgentMode

Manages output size limits to prevent context window overflow in AI agents.
"""

import os
from typing import Optional, List, Dict, Any, Tuple
from enum import Enum

from loguru import logger


class TruncateStrategy(Enum):
    """Strategy for truncating file content when it exceeds limits."""
    HEAD = "head"       # Show first N lines
    TAIL = "tail"       # Show last N lines
    MIDDLE = "middle"   # Show first and last, omit middle
    SUMMARY = "summary" # AI summary (future implementation)


class ContextLimitExceeded(Exception):
    """Raised when context limit would be exceeded."""
    pass


class ContextLimiter:
    """Manages context size limits for AI agent output"""

    # Default limit values
    DEFAULT_MAX_TOTAL_LINES = 10000
    DEFAULT_MAX_FILE_LINES = 1000
    DEFAULT_LARGE_FILE_THRESHOLD = 500

    def __init__(
        self,
        max_total_lines: int = DEFAULT_MAX_TOTAL_LINES,
        max_file_lines: int = DEFAULT_MAX_FILE_LINES,
        truncate_strategy: TruncateStrategy = TruncateStrategy.MIDDLE,
        priority_patterns: Optional[List[str]] = None,
        exclude_large: bool = False,
        large_threshold: int = DEFAULT_LARGE_FILE_THRESHOLD
    ):
        """
        Initialize ContextLimiter.

        Args:
            max_total_lines: Maximum total lines in output
            max_file_lines: Maximum lines per file
            truncate_strategy: How to truncate long files
            priority_patterns: Glob patterns for priority files (included first)
            exclude_large: Automatically exclude large files
            large_threshold: Lines threshold for 'large' classification
        """
        self.max_total_lines = max_total_lines
        self.max_file_lines = max_file_lines
        self.truncate_strategy = truncate_strategy
        self.priority_patterns = priority_patterns or []
        self.exclude_large = exclude_large
        self.large_threshold = large_threshold

        self._current_lines = 0
        self._warnings = []

    def reset(self):
        """Reset line counter and warnings."""
        self._current_lines = 0
        self._warnings = []

    def can_add_lines(self, line_count: int) -> bool:
        """Check if adding lines would exceed the limit."""
        return (self._current_lines + line_count) <= self.max_total_lines

    def add_lines(self, line_count: int) -> bool:
        """
        Add lines to the counter.

        Returns:
            True if successful, False if would exceed limit
        """
        if not self.can_add_lines(line_count):
            return False
        self._current_lines += line_count
        return True

    def remaining_lines(self) -> int:
        """Get remaining line budget."""
        return max(0, self.max_total_lines - self._current_lines)

    def truncate_content(
        self,
        content: str,
        file_path: str,
        total_lines: int
    ) -> Tuple[str, bool, str]:
        """
        Truncate file content according to strategy.

        Args:
            content: Original file content
            file_path: Path to file (for warning messages)
            total_lines: Total lines in original file

        Returns:
            Tuple of (truncated_content, was_truncated, warning_message)
        """
        lines = content.split('\n')
        actual_lines = len(lines)

        # Check if truncation is needed
        max_lines = min(self.max_file_lines, self.remaining_lines())

        if actual_lines <= max_lines:
            return content, False, ""

        # Truncate based on strategy
        truncated_lines = actual_lines - max_lines
        warning = ""

        if self.truncate_strategy == TruncateStrategy.HEAD:
            result_lines = lines[:max_lines]
            warning = f"TRUNCATED: {truncated_lines} more lines (showing first {max_lines})"

        elif self.truncate_strategy == TruncateStrategy.TAIL:
            result_lines = lines[-max_lines:]
            warning = f"TRUNCATED: {truncated_lines} lines omitted (showing last {max_lines})"

        elif self.truncate_strategy == TruncateStrategy.MIDDLE:
            # Show first half and last half
            first_half = max_lines // 2
            last_half = max_lines - first_half
            result_lines = lines[:first_half]
            result_lines.append(f"\n... [{truncated_lines} lines omitted] ...\n")
            result_lines.extend(lines[-last_half:])
            warning = f"TRUNCATED: {truncated_lines} lines omitted from middle"

        else:  # SUMMARY (not yet implemented)
            result_lines = lines[:max_lines]
            warning = f"TRUNCATED: {truncated_lines} more lines (use --truncate-strategy to adjust)"

        self._warnings.append({
            "file": file_path,
            "original_lines": actual_lines,
            "shown_lines": max_lines,
            "truncated_lines": truncated_lines,
            "strategy": self.truncate_strategy.value
        })

        return '\n'.join(result_lines), True, warning

    def should_include_file(
        self,
        file_path: str,
        line_count: int,
        language: Optional[str] = None
    ) -> Tuple[bool, str]:
        """
        Determine if a file should be included in output.

        Args:
            file_path: Path to the file
            line_count: Number of lines in the file
            language: Detected language of the file

        Returns:
            Tuple of (should_include, reason)
        """
        # Check if file matches priority patterns
        is_priority = self._matches_patterns(file_path, self.priority_patterns)

        # Check if file is too large
        is_large = line_count >= self.large_threshold

        if is_large and self.exclude_large and not is_priority:
            return False, f"Large file excluded ({line_count} lines > {self.large_threshold})"

        # Check if we have budget for this file
        if not self.can_add_lines(min(line_count, self.max_file_lines)):
            return False, f"Context limit reached ({self._current_lines}/{self.max_total_lines} lines)"

        return True, ""

    def _matches_patterns(self, file_path: str, patterns: List[str]) -> bool:
        """Check if file path matches any of the given patterns."""
        import fnmatch

        for pattern in patterns:
            if fnmatch.fnmatch(file_path, pattern):
                return True
            # Also check just the filename
            if fnmatch.fnmatch(os.path.basename(file_path), pattern):
                return True
        return False

    def get_warnings(self) -> List[Dict[str, Any]]:
        """Get list of truncation warnings."""
        return self._warnings

    def format_content_with_metadata(
        self,
        content: str,
        file_path: str,
        size_bytes: int,
        total_lines: int,
        language: str,
        was_truncated: bool = False,
        truncation_warning: str = ""
    ) -> str:
        """
        Format file content with metadata header.

        Args:
            content: File content (possibly truncated)
            file_path: Relative file path
            size_bytes: File size in bytes
            total_lines: Original total lines
            language: Detected language
            was_truncated: Whether content was truncated
            truncation_warning: Warning message if truncated

        Returns:
            Formatted markdown with metadata
        """
        size_str = self._format_size(size_bytes)
        shown_lines = len(content.split('\n'))

        lines = []
        lines.append(f"## `{file_path}`")

        if was_truncated:
            lines.append(f"**Size**: {size_str} | **Lines**: {total_lines} (showing {shown_lines})")
        else:
            lines.append(f"**Size**: {size_str} | **Lines**: {total_lines}")

        lines.append("")
        lines.append(f"```{language}")
        lines.append(content)
        lines.append("```")

        if was_truncated and truncation_warning:
            lines.append("")
            lines.append(f"> {truncation_warning}")

        return '\n'.join(lines)

    @staticmethod
    def _format_size(size_bytes: int) -> str:
        """Convert bytes to human-readable format."""
        for unit in ["B", "KB", "MB", "GB"]:
            if size_bytes < 1024:
                if unit == "B":
                    return f"{size_bytes} {unit}"
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} TB"

    def get_status(self) -> Dict[str, Any]:
        """Get current limiter status."""
        return {
            "current_lines": self._current_lines,
            "max_total_lines": self.max_total_lines,
            "max_file_lines": self.max_file_lines,
            "remaining_lines": self.remaining_lines(),
            "truncate_strategy": self.truncate_strategy.value,
            "warnings_count": len(self._warnings),
            "exclude_large": self.exclude_large,
            "large_threshold": self.large_threshold,
        }
