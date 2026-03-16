"""
JSON Format Output for AgentMode

Generates structured JSON output for programmatic consumption by AI agents.
"""

import json
from typing import Dict, Any


class JsonFormatter:
    """Formats tree data as JSON output"""

    def __init__(self, indent: int = 2, compact: bool = False):
        """
        Initialize JsonFormatter.

        Args:
            indent: JSON indentation level (None for compact)
            compact: If True, output minimal JSON
        """
        self.indent = None if compact else indent
        self.compact = compact

    def format(self, tree_data: Dict[str, Any]) -> str:
        """
        Format tree data as JSON string.

        Args:
            tree_data: Tree data from TreeWithStats.generate_tree_data()

        Returns:
            Formatted JSON string
        """
        if self.compact:
            # Remove null values and minimize output
            output = self._compact_data(tree_data)
        else:
            output = tree_data

        return json.dumps(output, indent=self.indent, ensure_ascii=False)

    def _compact_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Remove null values and minimize data for compact output."""
        if isinstance(data, dict):
            return {
                k: self._compact_data(v)
                for k, v in data.items()
                if v is not None and v != [] and v != {}
            }
        elif isinstance(data, list):
            return [self._compact_data(item) for item in data]
        else:
            return data

    def format_minimal(self, tree_data: Dict[str, Any]) -> str:
        """
        Format tree data with minimal information (paths and lines only).

        Useful for very large repositories where full JSON would be too large.

        Args:
            tree_data: Tree data from TreeWithStats.generate_tree_data()

        Returns:
            Minimal JSON string with essential information
        """
        minimal = {
            "repository": tree_data["repository"],
            "summary": tree_data["summary"],
            "files": [
                {
                    "path": item["path"],
                    "lines": item.get("lines", 0),
                    "lang": item.get("language", "unknown")
                }
                for item in tree_data["tree"]
                if item["type"] == "file"
            ]
        }
        return json.dumps(minimal, indent=self.indent, ensure_ascii=False)
