import os

from loguru import logger


class TreeGenerator:
    """Generate a directory tree and collect tree statistics."""

    def __init__(self, pattern_matcher):
        self.pattern_matcher = pattern_matcher

    def generate_tree(self, dir_path, max_depth=None):
        """Generate a plaintext directory tree."""
        tree = ["```plaintext", f"OS: {os.name}", f"Directory: {os.path.abspath(dir_path)}", ""]

        def _build_tree(path, prefix="", depth=0):
            if max_depth is not None and depth > max_depth:
                return

            try:
                entries = [
                    entry
                    for entry in sorted(
                        os.scandir(path), key=lambda item: (not item.is_dir(), item.name.lower())
                    )
                    if not self.pattern_matcher.should_exclude(entry.path)
                ]

                for index, entry in enumerate(entries):
                    is_last = index == len(entries) - 1
                    branch = "└── " if is_last else "├── "
                    tree.append(f"{prefix}{branch}{entry.name}{'/' if entry.is_dir() else ''}")
                    if entry.is_dir():
                        next_prefix = prefix + ("    " if is_last else "│   ")
                        _build_tree(entry.path, next_prefix, depth + 1)
            except PermissionError as exc:
                logger.warning(f"Permission denied while scanning {path}: {exc}")
            except Exception as exc:
                logger.error(f"Tree generation error for {path}: {exc}")

        try:
            _build_tree(dir_path)
        except Exception as exc:
            logger.error(f"Tree generation error for {dir_path}: {exc}")
            tree.append(f"Error: {exc}")

        tree.append("```")
        tree.append("")
        return "\n".join(tree)

    def get_tree_stats(self, dir_path):
        """Collect basic tree statistics."""
        stats = {
            "total_dirs": 0,
            "total_files": 0,
            "max_depth": 0,
            "largest_dir": ("", 0),
        }

        def _count_entries(path, depth=0):
            try:
                dir_count = 0
                file_count = 0

                with os.scandir(path) as entries:
                    for entry in entries:
                        if self.pattern_matcher.should_exclude(entry.path):
                            continue

                        if entry.is_dir():
                            dir_count += 1
                            sub_dir_count, sub_file_count = _count_entries(entry.path, depth + 1)
                            dir_count += sub_dir_count
                            file_count += sub_file_count
                        else:
                            file_count += 1

                stats["max_depth"] = max(stats["max_depth"], depth)
                if dir_count + file_count > stats["largest_dir"][1]:
                    stats["largest_dir"] = (path, dir_count + file_count)

                return dir_count, file_count
            except Exception as exc:
                logger.error(f"Failed to collect tree stats for {path}: {exc}")
                return 0, 0

        total_dirs, total_files = _count_entries(dir_path)
        stats["total_dirs"] = total_dirs
        stats["total_files"] = total_files
        return stats
