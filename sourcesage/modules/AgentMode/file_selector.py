"""
File Selector for AgentMode

Enables selective file retrieval based on paths, patterns, and filters.
"""

import os
import fnmatch
from pathlib import Path
from typing import Optional, List, Dict, Any

from loguru import logger


class FileSelector:
    """Selects files based on patterns, paths, and filters"""

    def __init__(self, pattern_matcher, language_detector, file_processor):
        """
        Initialize FileSelector.

        Args:
            pattern_matcher: FilePatternMatcher instance for filtering
            language_detector: LanguageDetector instance
            file_processor: FileProcessor instance for reading files
        """
        self.pattern_matcher = pattern_matcher
        self.language_detector = language_detector
        self.file_processor = file_processor

    def select_files(
        self,
        dir_path: str,
        file_paths: Optional[List[str]] = None,
        include_patterns: Optional[List[str]] = None,
        exclude_patterns: Optional[List[str]] = None,
        min_lines: Optional[int] = None,
        max_lines: Optional[int] = None,
        languages: Optional[List[str]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Select files based on various criteria.

        Args:
            dir_path: Base directory path
            file_paths: Specific file paths to include
            include_patterns: Glob patterns to include (e.g., "**/*.py")
            exclude_patterns: Glob patterns to exclude (e.g., "**/test_*.py")
            min_lines: Minimum line count filter
            max_lines: Maximum line count filter
            languages: Filter by detected languages

        Returns:
            List of selected file info dictionaries
        """
        selected_files = []
        dir_path = os.path.abspath(dir_path)

        # If specific files are provided, process them directly
        if file_paths:
            for file_path in file_paths:
                full_path = self._resolve_path(dir_path, file_path)
                if full_path and os.path.isfile(full_path):
                    file_info = self._get_file_info(full_path, dir_path)
                    if file_info and self._passes_filters(
                        file_info, min_lines, max_lines, languages
                    ):
                        selected_files.append(file_info)
                else:
                    logger.warning(f"File not found: {file_path}")
            return selected_files

        # Otherwise, walk directory and apply patterns
        for root, dirs, files in os.walk(dir_path):
            # Skip excluded directories
            dirs[:] = [d for d in dirs
                      if not self.pattern_matcher.should_exclude(os.path.join(root, d))]

            for filename in files:
                full_path = os.path.join(root, filename)
                rel_path = os.path.relpath(full_path, dir_path)

                # Skip if excluded by pattern matcher
                if self.pattern_matcher.should_exclude(full_path):
                    continue

                # Apply include patterns
                if include_patterns and not self._matches_any_pattern(rel_path, include_patterns):
                    continue

                # Apply exclude patterns
                if exclude_patterns and self._matches_any_pattern(rel_path, exclude_patterns):
                    continue

                # Get file info and apply filters
                file_info = self._get_file_info(full_path, dir_path)
                if file_info and self._passes_filters(file_info, min_lines, max_lines, languages):
                    selected_files.append(file_info)

        return selected_files

    def get_file_content(
        self,
        dir_path: str,
        file_path: str,
        max_lines: Optional[int] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Get content of a specific file.

        Args:
            dir_path: Base directory path
            file_path: Relative or absolute path to file
            max_lines: Maximum lines to return

        Returns:
            Dictionary with file info and content, or None if not found
        """
        full_path = self._resolve_path(dir_path, file_path)
        if not full_path or not os.path.isfile(full_path):
            return None

        file_info = self._get_file_info(full_path, dir_path)
        if not file_info:
            return None

        try:
            with open(full_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()

            if max_lines:
                lines = content.split('\n')
                if len(lines) > max_lines:
                    content = '\n'.join(lines[:max_lines])
                    file_info['truncated'] = True
                    file_info['truncated_lines'] = len(lines) - max_lines

            file_info['content'] = content
            return file_info

        except Exception as e:
            logger.error(f"Error reading file {file_path}: {e}")
            return None

    def get_multiple_file_contents(
        self,
        dir_path: str,
        file_paths: List[str],
        max_lines_per_file: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Get contents of multiple files.

        Args:
            dir_path: Base directory path
            file_paths: List of file paths
            max_lines_per_file: Maximum lines per file

        Returns:
            List of file info dictionaries with content
        """
        results = []
        for file_path in file_paths:
            result = self.get_file_content(dir_path, file_path, max_lines_per_file)
            if result:
                results.append(result)
        return results

    def _resolve_path(self, dir_path: str, file_path: str) -> Optional[str]:
        """Resolve a file path relative to directory."""
        if os.path.isabs(file_path):
            return file_path if os.path.exists(file_path) else None

        # Try relative to dir_path
        full_path = os.path.join(dir_path, file_path)
        if os.path.exists(full_path):
            return full_path

        # Try finding by filename in subdirectories
        filename = os.path.basename(file_path)
        for root, _, files in os.walk(dir_path):
            if filename in files:
                found_path = os.path.join(root, filename)
                # If the relative path partially matches, prefer it
                if file_path in os.path.relpath(found_path, dir_path):
                    return found_path

        return None

    def _get_file_info(self, full_path: str, base_path: str) -> Optional[Dict[str, Any]]:
        """Get information about a file."""
        try:
            rel_path = os.path.relpath(full_path, base_path)
            stat_info = os.stat(full_path)
            line_count = self.file_processor._count_lines(full_path) or 0
            language = self.language_detector.detect_language(full_path)
            extension = os.path.splitext(full_path)[1]

            return {
                "path": rel_path,
                "full_path": full_path,
                "size_bytes": stat_info.st_size,
                "lines": line_count,
                "language": language,
                "extension": extension,
                "modified": stat_info.st_mtime,
            }
        except Exception as e:
            logger.warning(f"Error getting file info for {full_path}: {e}")
            return None

    def _matches_any_pattern(self, path: str, patterns: List[str]) -> bool:
        """Check if path matches any of the given glob patterns."""
        for pattern in patterns:
            # Handle ** patterns
            if '**' in pattern:
                # Convert ** to work with fnmatch
                if fnmatch.fnmatch(path, pattern):
                    return True
                # Try with Path for more robust matching
                try:
                    if Path(path).match(pattern):
                        return True
                except Exception:
                    pass
            else:
                if fnmatch.fnmatch(path, pattern):
                    return True
                if fnmatch.fnmatch(os.path.basename(path), pattern):
                    return True
        return False

    def _passes_filters(
        self,
        file_info: Dict[str, Any],
        min_lines: Optional[int],
        max_lines: Optional[int],
        languages: Optional[List[str]]
    ) -> bool:
        """Check if file passes all filters."""
        # Line count filter
        if min_lines is not None and file_info["lines"] < min_lines:
            return False
        if max_lines is not None and file_info["lines"] > max_lines:
            return False

        # Language filter
        if languages:
            file_lang = file_info["language"].lower()
            if not any(lang.lower() in file_lang or file_lang in lang.lower()
                      for lang in languages):
                return False

        return True

    def format_files_output(
        self,
        files: List[Dict[str, Any]],
        include_content: bool = True
    ) -> str:
        """
        Format selected files as markdown output.

        Args:
            files: List of file info dictionaries
            include_content: Whether to include file content

        Returns:
            Formatted markdown string
        """
        lines = []
        lines.append(f"# Selected Files ({len(files)} files)")
        lines.append("")

        for file_info in files:
            lines.append(f"## `{file_info['path']}`")
            lines.append(
                f"**Size**: {self._format_size(file_info['size_bytes'])} | "
                f"**Lines**: {file_info['lines']} | "
                f"**Language**: {file_info['language']}"
            )
            lines.append("")

            if include_content and 'content' in file_info:
                lang = file_info['language']
                lines.append(f"```{lang}")
                lines.append(file_info['content'])
                lines.append("```")

                if file_info.get('truncated'):
                    lines.append(
                        f"> TRUNCATED: {file_info['truncated_lines']} more lines"
                    )

            lines.append("")

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
