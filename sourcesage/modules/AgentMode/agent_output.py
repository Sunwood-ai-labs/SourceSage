"""
Agent Output - Main orchestrator for AgentMode

Provides unified interface for AI agent-optimized repository analysis.
"""

import os
from typing import Optional, List, Dict, Any
from enum import Enum

from loguru import logger

from .tree_with_stats import TreeWithStats
from .context_limiter import ContextLimiter, TruncateStrategy
from .file_selector import FileSelector
from .formats.tree_format import TreeFormatter
from .formats.json_format import JsonFormatter


class AgentModeType(Enum):
    """Available agent mode types."""
    TREE = "tree"       # Tree structure with stats only
    FILES = "files"     # Selective file content retrieval
    FULL = "full"       # Full output with context limits


class OutputFormat(Enum):
    """Output format options."""
    TREE = "tree"       # ASCII tree format
    JSON = "json"       # JSON format


class AgentOutput:
    """Main orchestrator for AgentMode functionality"""

    def __init__(
        self,
        pattern_matcher,
        language_detector,
        file_processor
    ):
        """
        Initialize AgentOutput.

        Args:
            pattern_matcher: FilePatternMatcher instance
            language_detector: LanguageDetector instance
            file_processor: FileProcessor instance
        """
        self.pattern_matcher = pattern_matcher
        self.language_detector = language_detector
        self.file_processor = file_processor

        # Initialize components
        self.tree_generator = TreeWithStats(
            pattern_matcher, language_detector, file_processor
        )
        self.file_selector = FileSelector(
            pattern_matcher, language_detector, file_processor
        )

    def generate_tree(
        self,
        dir_path: str,
        output_format: OutputFormat = OutputFormat.TREE,
        max_depth: Optional[int] = None,
        show_lines: bool = True,
        show_size: bool = True,
        sort_by: str = "name",
        large_threshold: int = 200,
    ) -> str:
        """
        Generate tree output with statistics.

        Args:
            dir_path: Directory to analyze
            output_format: Output format (tree or json)
            max_depth: Maximum tree depth
            show_lines: Include line counts
            show_size: Include file sizes
            sort_by: Sort criterion (name, lines, size, modified)
            large_threshold: Threshold for marking files as 'large'

        Returns:
            Formatted output string
        """
        logger.info(f"Generating tree for {dir_path} (format: {output_format.value})")

        tree_data = self.tree_generator.generate_tree_data(
            dir_path=dir_path,
            max_depth=max_depth,
            show_lines=show_lines,
            show_size=show_size,
            large_threshold=large_threshold,
            sort_by=sort_by,
        )

        if output_format == OutputFormat.JSON:
            formatter = JsonFormatter()
            return formatter.format(tree_data)
        else:
            formatter = TreeFormatter(large_threshold=large_threshold)
            return formatter.format(tree_data)

    def generate_files(
        self,
        dir_path: str,
        file_paths: Optional[List[str]] = None,
        include_patterns: Optional[List[str]] = None,
        exclude_patterns: Optional[List[str]] = None,
        min_lines: Optional[int] = None,
        max_lines: Optional[int] = None,
        languages: Optional[List[str]] = None,
        max_file_lines: Optional[int] = None,
        output_format: OutputFormat = OutputFormat.TREE,
    ) -> str:
        """
        Generate selective file content output.

        Args:
            dir_path: Base directory path
            file_paths: Specific file paths to include
            include_patterns: Glob patterns to include
            exclude_patterns: Glob patterns to exclude
            min_lines: Minimum line count filter
            max_lines: Maximum line count filter
            languages: Filter by languages
            max_file_lines: Maximum lines per file
            output_format: Output format

        Returns:
            Formatted output string
        """
        logger.info(f"Selecting files from {dir_path}")

        # Select files
        selected_files = self.file_selector.select_files(
            dir_path=dir_path,
            file_paths=file_paths,
            include_patterns=include_patterns,
            exclude_patterns=exclude_patterns,
            min_lines=min_lines,
            max_lines=max_lines,
            languages=languages,
        )

        # Get file contents
        files_with_content = []
        for file_info in selected_files:
            content_info = self.file_selector.get_file_content(
                dir_path, file_info['path'], max_file_lines
            )
            if content_info:
                files_with_content.append(content_info)

        # Format output
        if output_format == OutputFormat.JSON:
            import json
            output = {
                "total_files": len(files_with_content),
                "files": files_with_content
            }
            return json.dumps(output, indent=2, ensure_ascii=False)
        else:
            return self.file_selector.format_files_output(
                files_with_content, include_content=True
            )

    def generate_full(
        self,
        dir_path: str,
        max_total_lines: int = 10000,
        max_file_lines: int = 1000,
        truncate_strategy: str = "middle",
        priority_files: Optional[List[str]] = None,
        exclude_large: bool = False,
        large_threshold: int = 500,
        output_format: OutputFormat = OutputFormat.TREE,
    ) -> str:
        """
        Generate full repository output with context limits.

        Args:
            dir_path: Directory to analyze
            max_total_lines: Maximum total lines in output
            max_file_lines: Maximum lines per file
            truncate_strategy: How to truncate files (head, tail, middle)
            priority_files: Glob patterns for priority files
            exclude_large: Exclude large files automatically
            large_threshold: Lines threshold for 'large' classification
            output_format: Output format

        Returns:
            Formatted output string
        """
        logger.info(f"Generating full output for {dir_path} (max lines: {max_total_lines})")

        # Parse truncate strategy
        strategy_map = {
            "head": TruncateStrategy.HEAD,
            "tail": TruncateStrategy.TAIL,
            "middle": TruncateStrategy.MIDDLE,
            "summary": TruncateStrategy.SUMMARY,
        }
        strategy = strategy_map.get(truncate_strategy, TruncateStrategy.MIDDLE)

        # Initialize context limiter
        limiter = ContextLimiter(
            max_total_lines=max_total_lines,
            max_file_lines=max_file_lines,
            truncate_strategy=strategy,
            priority_patterns=priority_files or [],
            exclude_large=exclude_large,
            large_threshold=large_threshold,
        )

        # First, get tree structure
        tree_data = self.tree_generator.generate_tree_data(
            dir_path=dir_path,
            show_lines=True,
            show_size=True,
            large_threshold=large_threshold,
        )

        # Estimate tree overhead (about 2 lines per file/dir)
        tree_overhead = len(tree_data['tree']) * 2 + 20
        limiter.add_lines(tree_overhead)

        # Collect files with content
        files_with_content = []
        skipped_files = []

        # Sort files by priority and size
        file_items = [item for item in tree_data['tree'] if item['type'] == 'file']

        # Process priority files first
        if priority_files:
            priority_items = []
            other_items = []
            for item in file_items:
                if self._matches_patterns(item['path'], priority_files):
                    priority_items.append(item)
                else:
                    other_items.append(item)
            file_items = priority_items + other_items

        for item in file_items:
            file_path = item['path']
            line_count = item.get('lines', 0)

            # Check if file should be included
            should_include, reason = limiter.should_include_file(
                file_path, line_count, item.get('language')
            )

            if not should_include:
                skipped_files.append({"path": file_path, "reason": reason})
                continue

            # Get file content
            content_info = self.file_selector.get_file_content(
                dir_path, file_path, max_file_lines
            )

            if content_info and 'content' in content_info:
                # Apply truncation if needed
                content, was_truncated, warning = limiter.truncate_content(
                    content_info['content'],
                    file_path,
                    line_count
                )

                content_info['content'] = content
                content_info['was_truncated'] = was_truncated
                content_info['truncation_warning'] = warning

                # Update line count
                actual_lines = len(content.split('\n'))
                limiter.add_lines(actual_lines + 5)  # +5 for markdown formatting

                files_with_content.append(content_info)

        # Format output
        if output_format == OutputFormat.JSON:
            import json
            output = {
                "repository": tree_data['repository'],
                "summary": tree_data['summary'],
                "context_status": limiter.get_status(),
                "files": files_with_content,
                "skipped_files": skipped_files,
            }
            return json.dumps(output, indent=2, ensure_ascii=False)
        else:
            return self._format_full_output(
                tree_data, files_with_content, skipped_files, limiter
            )

    def _format_full_output(
        self,
        tree_data: Dict[str, Any],
        files_with_content: List[Dict[str, Any]],
        skipped_files: List[Dict[str, Any]],
        limiter: ContextLimiter
    ) -> str:
        """Format full output as markdown."""
        lines = []

        # Header
        lines.append(f"# Repository: {tree_data['repository']}")
        lines.append("")

        # Summary
        summary = tree_data['summary']
        lines.append(f"**Files**: {summary['total_files']} | "
                    f"**Directories**: {summary['total_directories']} | "
                    f"**Total Lines**: {summary['total_lines']:,}")
        lines.append("")

        # Context status
        status = limiter.get_status()
        lines.append(f"> Context: {status['current_lines']:,}/{status['max_total_lines']:,} lines used")
        lines.append("")

        # Tree section (minimal)
        lines.append("## Directory Structure")
        lines.append("")
        formatter = TreeFormatter()
        tree_output = formatter._build_tree_lines(tree_data['tree'][:50], tree_data['config'])
        lines.extend(tree_output)
        if len(tree_data['tree']) > 50:
            lines.append(f"... ({len(tree_data['tree']) - 50} more items)")
        lines.append("")

        # Files section
        lines.append("## File Contents")
        lines.append("")

        for file_info in files_with_content:
            lines.append(f"### `{file_info['path']}`")
            lines.append(
                f"**Size**: {self._format_size(file_info['size_bytes'])} | "
                f"**Lines**: {file_info['lines']}"
            )
            lines.append("")
            lines.append(f"```{file_info['language']}")
            lines.append(file_info['content'])
            lines.append("```")

            if file_info.get('was_truncated'):
                lines.append(f"> {file_info['truncation_warning']}")

            lines.append("")

        # Skipped files section
        if skipped_files:
            lines.append("## Skipped Files")
            lines.append("")
            for skipped in skipped_files[:20]:
                lines.append(f"- `{skipped['path']}`: {skipped['reason']}")
            if len(skipped_files) > 20:
                lines.append(f"- ... and {len(skipped_files) - 20} more")
            lines.append("")

        return '\n'.join(lines)

    def _matches_patterns(self, path: str, patterns: List[str]) -> bool:
        """Check if path matches any patterns."""
        import fnmatch
        for pattern in patterns:
            if fnmatch.fnmatch(path, pattern):
                return True
            if fnmatch.fnmatch(os.path.basename(path), pattern):
                return True
        return False

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
