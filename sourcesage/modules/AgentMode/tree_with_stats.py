"""
Tree with Statistics Generator for AgentMode

Generates directory tree structure with file statistics (line counts, sizes)
without loading file contents.
"""

import os
from datetime import datetime
from typing import Optional, Dict, List, Any

from loguru import logger


class TreeWithStats:
    """Generates directory tree with file statistics for AI agent consumption"""

    def __init__(self, pattern_matcher, language_detector, file_processor):
        """
        Initialize TreeWithStats.

        Args:
            pattern_matcher: FilePatternMatcher instance for filtering files
            language_detector: LanguageDetector instance for detecting file types
            file_processor: FileProcessor instance for counting lines
        """
        self.pattern_matcher = pattern_matcher
        self.language_detector = language_detector
        self.file_processor = file_processor

    def generate_tree_data(
        self,
        dir_path: str,
        max_depth: Optional[int] = None,
        show_lines: bool = True,
        show_size: bool = True,
        large_threshold: int = 200,
        sort_by: str = "name"
    ) -> Dict[str, Any]:
        """
        Generate tree data structure with statistics.

        Args:
            dir_path: Root directory path to analyze
            max_depth: Maximum tree depth (None for unlimited)
            show_lines: Include line counts
            show_size: Include file sizes
            large_threshold: Lines threshold for marking files as 'large'
            sort_by: Sort criterion ('name', 'lines', 'size', 'modified')

        Returns:
            Dictionary containing tree structure and statistics
        """
        repo_name = os.path.basename(os.path.abspath(dir_path))

        tree_items = []
        summary = {
            "total_files": 0,
            "total_directories": 0,
            "total_lines": 0,
            "total_size_bytes": 0,
        }

        language_stats = {}
        directory_stats = {}
        large_files = []

        def _process_directory(path: str, depth: int = 0) -> List[Dict[str, Any]]:
            """Recursively process directory and collect stats."""
            items = []

            if max_depth is not None and depth > max_depth:
                return items

            try:
                entries = list(os.scandir(path))

                # Sort entries
                if sort_by == "name":
                    entries = sorted(entries, key=lambda e: (not e.is_dir(), e.name.lower()))
                elif sort_by == "modified":
                    entries = sorted(entries, key=lambda e: (not e.is_dir(), -e.stat().st_mtime))
                else:
                    entries = sorted(entries, key=lambda e: (not e.is_dir(), e.name.lower()))

                for entry in entries:
                    if self.pattern_matcher.should_exclude(entry.path):
                        continue

                    rel_path = os.path.relpath(entry.path, dir_path)

                    if entry.is_dir():
                        summary["total_directories"] += 1
                        children = _process_directory(entry.path, depth + 1)
                        children_count = sum(1 for e in os.scandir(entry.path)
                                           if not self.pattern_matcher.should_exclude(e.path))

                        item = {
                            "path": rel_path,
                            "type": "directory",
                            "depth": depth,
                            "children_count": children_count,
                        }
                        items.append(item)
                        tree_items.append(item)

                        # Track directory stats
                        dir_lines = sum(c.get("lines", 0) for c in children if c["type"] == "file")
                        if dir_lines > 0:
                            directory_stats[rel_path] = {
                                "files": len([c for c in children if c["type"] == "file"]),
                                "lines": dir_lines
                            }

                        items.extend(children)
                    else:
                        summary["total_files"] += 1

                        try:
                            stat_info = entry.stat()
                            size_bytes = stat_info.st_size
                            line_count = 0

                            if show_lines:
                                try:
                                    line_count = self.file_processor._count_lines(entry.path) or 0
                                except Exception:
                                    line_count = 0

                            language = self.language_detector.detect_language(entry.path)
                            extension = os.path.splitext(entry.name)[1]
                            is_large = line_count >= large_threshold

                            summary["total_lines"] += line_count
                            summary["total_size_bytes"] += size_bytes

                            # Track language stats
                            if language not in language_stats:
                                language_stats[language] = {
                                    "files": 0,
                                    "lines": 0,
                                    "size_bytes": 0
                                }
                            language_stats[language]["files"] += 1
                            language_stats[language]["lines"] += line_count
                            language_stats[language]["size_bytes"] += size_bytes

                            # Track large files
                            if is_large:
                                large_files.append({
                                    "path": rel_path,
                                    "lines": line_count
                                })

                            item = {
                                "path": rel_path,
                                "type": "file",
                                "depth": depth,
                                "language": language,
                                "extension": extension,
                                "lines": line_count if show_lines else None,
                                "size_bytes": size_bytes if show_size else None,
                                "is_large": is_large,
                            }
                            items.append(item)
                            tree_items.append(item)

                        except Exception as e:
                            logger.warning(f"Error processing file {entry.path}: {e}")

            except PermissionError as e:
                logger.warning(f"Permission denied: {path}: {e}")
            except Exception as e:
                logger.error(f"Error processing directory {path}: {e}")

            return items

        _process_directory(dir_path)

        # Sort large files by line count
        large_files.sort(key=lambda x: x["lines"], reverse=True)

        # Re-sort tree items if needed
        if sort_by == "lines":
            # Keep directories at their original positions but sort files by lines
            tree_items = self._sort_tree_by_lines(tree_items)
        elif sort_by == "size":
            tree_items = self._sort_tree_by_size(tree_items)

        return {
            "repository": repo_name,
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "summary": summary,
            "config": {
                "max_depth": max_depth,
                "large_threshold": large_threshold,
                "show_lines": show_lines,
                "show_size": show_size,
                "sort_by": sort_by,
            },
            "tree": tree_items,
            "statistics": {
                "by_language": language_stats,
                "by_directory": directory_stats,
                "large_files": large_files[:20],  # Top 20 large files
            }
        }

    def _sort_tree_by_lines(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Sort tree items by line count while preserving directory structure."""
        # Group by parent directory
        result = []
        dirs_stack = [{"depth": -1, "items": []}]

        for item in items:
            depth = item["depth"]

            while dirs_stack and dirs_stack[-1]["depth"] >= depth:
                completed = dirs_stack.pop()
                # Sort files in this directory by lines
                files = [i for i in completed["items"] if i["type"] == "file"]
                dirs = [i for i in completed["items"] if i["type"] == "directory"]
                files.sort(key=lambda x: x.get("lines", 0), reverse=True)

                if len(dirs_stack) > 0:
                    dirs_stack[-1]["items"].extend(dirs)
                    dirs_stack[-1]["items"].extend(files)

            if item["type"] == "directory":
                dirs_stack.append({"depth": depth, "items": [item]})
            else:
                dirs_stack[-1]["items"].append(item)

        # Finalize remaining items
        while dirs_stack:
            completed = dirs_stack.pop()
            files = [i for i in completed["items"] if i["type"] == "file"]
            dirs = [i for i in completed["items"] if i["type"] == "directory"]
            files.sort(key=lambda x: x.get("lines", 0), reverse=True)
            result = dirs + files + result

        return result if result else items

    def _sort_tree_by_size(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Sort tree items by size while preserving directory structure."""
        # Similar logic to _sort_tree_by_lines but sort by size
        files = [i for i in items if i["type"] == "file"]
        dirs = [i for i in items if i["type"] == "directory"]
        files.sort(key=lambda x: x.get("size_bytes", 0), reverse=True)
        return dirs + files

    @staticmethod
    def format_size(size_bytes: int) -> str:
        """Convert bytes to human-readable format."""
        for unit in ["B", "KB", "MB", "GB"]:
            if size_bytes < 1024:
                if unit == "B":
                    return f"{size_bytes} {unit}"
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} TB"
