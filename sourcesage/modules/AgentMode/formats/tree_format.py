"""
Tree Format Output for AgentMode

Generates ASCII tree representation with file statistics.
"""

from typing import Dict, Any, List


class TreeFormatter:
    """Formats tree data as ASCII tree output"""

    def __init__(self, large_threshold: int = 200):
        """
        Initialize TreeFormatter.

        Args:
            large_threshold: Lines threshold for marking files as 'large'
        """
        self.large_threshold = large_threshold

    def format(self, tree_data: Dict[str, Any]) -> str:
        """
        Format tree data as ASCII tree string.

        Args:
            tree_data: Tree data from TreeWithStats.generate_tree_data()

        Returns:
            Formatted ASCII tree string
        """
        lines = []

        # Header
        lines.append("=" * 80)
        lines.append(f"Repository: {tree_data['repository']}")
        lines.append("=" * 80)
        lines.append("")

        # Summary
        summary = tree_data["summary"]
        lines.append(
            f"Summary: {summary['total_files']} files | "
            f"{summary['total_directories']} directories | "
            f"{summary['total_lines']:,} total lines"
        )
        lines.append("")

        # Directory Tree
        lines.append("-" * 80)
        lines.append("Directory Tree")
        lines.append("-" * 80)
        lines.append("")

        # Build tree structure
        tree_lines = self._build_tree_lines(tree_data["tree"], tree_data["config"])
        lines.extend(tree_lines)

        lines.append("")

        # Legend
        lines.append("-" * 80)
        lines.append(f"Legend: * large = {self.large_threshold}+ lines (configurable via --large-threshold)")
        lines.append("-" * 80)

        # Statistics section
        if tree_data.get("statistics"):
            lines.append("")
            lines.extend(self._format_statistics(tree_data["statistics"]))

        return "\n".join(lines)

    def _build_tree_lines(self, tree_items: List[Dict[str, Any]], config: Dict[str, Any]) -> List[str]:
        """Build ASCII tree lines from tree items."""
        lines = []

        # Group items by parent path for proper tree rendering
        items_by_depth = {}
        for item in tree_items:
            depth = item["depth"]
            if depth not in items_by_depth:
                items_by_depth[depth] = []
            items_by_depth[depth].append(item)

        # Track parent paths for prefix calculation
        prefix_stack = []
        last_at_depth = {}

        # Determine which items are last in their parent
        for i, item in enumerate(tree_items):
            depth = item["depth"]
            # Find next item at same or lower depth
            is_last = True
            for j in range(i + 1, len(tree_items)):
                if tree_items[j]["depth"] <= depth:
                    if tree_items[j]["depth"] == depth:
                        is_last = False
                    break
            last_at_depth[i] = is_last

        # Build prefix stack state
        prefix_states = [False] * 20  # Max depth tracking

        for i, item in enumerate(tree_items):
            depth = item["depth"]
            is_last = last_at_depth.get(i, True)

            # Build prefix
            prefix = ""
            for d in range(depth):
                if prefix_states[d]:
                    prefix += "    "
                else:
                    prefix += "│   "

            # Update prefix state for current depth
            prefix_states[depth] = is_last

            # Current item prefix
            if is_last:
                item_prefix = "└── "
            else:
                item_prefix = "├── "

            # Format the item
            line = prefix + item_prefix + self._format_item(item, config)
            lines.append(line)

        return lines

    def _format_item(self, item: Dict[str, Any], config: Dict[str, Any]) -> str:
        """Format a single tree item."""
        if item["type"] == "directory":
            name = item["path"].split("/")[-1] if "/" in item["path"] else item["path"]
            return f"{name}/".ljust(40) + f"[dir]".ljust(10) + f"{item['children_count']} items"
        else:
            name = item["path"].split("/")[-1] if "/" in item["path"] else item["path"]
            ext = item.get("extension", "")
            if ext.startswith("."):
                ext = ext[1:]

            parts = [name.ljust(40)]
            parts.append(f"[{ext}]".ljust(10) if ext else "[file]".ljust(10))

            if config.get("show_lines") and item.get("lines") is not None:
                parts.append(f"{item['lines']:,} lines".ljust(12))

            if config.get("show_size") and item.get("size_bytes") is not None:
                parts.append(self._format_size(item["size_bytes"]).rjust(8))

            if item.get("is_large"):
                parts.append("  * large")

            return "".join(parts)

    def _format_statistics(self, statistics: Dict[str, Any]) -> List[str]:
        """Format statistics section."""
        lines = []

        # Language statistics
        if statistics.get("by_language"):
            lines.append("Language Statistics:")
            lines.append("-" * 60)
            lines.append(f"{'Language':<20} {'Files':>8} {'Lines':>12} {'Size':>12}")
            lines.append("-" * 60)

            sorted_langs = sorted(
                statistics["by_language"].items(),
                key=lambda x: x[1]["lines"],
                reverse=True
            )
            for lang, stats in sorted_langs[:15]:  # Top 15 languages
                lines.append(
                    f"{lang:<20} {stats['files']:>8} {stats['lines']:>12,} "
                    f"{self._format_size(stats['size_bytes']):>12}"
                )
            lines.append("")

        # Large files
        if statistics.get("large_files"):
            lines.append("Large Files (by line count):")
            lines.append("-" * 60)
            for f in statistics["large_files"][:10]:  # Top 10
                lines.append(f"  {f['path']:<50} {f['lines']:>6,} lines")
            lines.append("")

        return lines

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
