"""Tests for JsonFormatter class"""

import json
import pytest
from sourcesage.modules.AgentMode.formats.json_format import JsonFormatter


@pytest.fixture
def sample_tree_data():
    """Create sample tree data for testing"""
    return {
        "repository": "test-repo",
        "generated_at": "2026-01-25T10:00:00Z",
        "summary": {
            "total_files": 3,
            "total_directories": 1,
            "total_lines": 200,
            "total_size_bytes": 5000
        },
        "config": {
            "max_depth": None,
            "large_threshold": 200,
            "show_lines": True,
            "show_size": True
        },
        "tree": [
            {
                "path": "src",
                "type": "directory",
                "depth": 0,
                "children_count": 2
            },
            {
                "path": "src/main.py",
                "type": "file",
                "depth": 1,
                "language": "python",
                "extension": ".py",
                "lines": 150,
                "size_bytes": 3000,
                "is_large": False
            },
            {
                "path": "src/utils.py",
                "type": "file",
                "depth": 1,
                "language": "python",
                "extension": ".py",
                "lines": 50,
                "size_bytes": 2000,
                "is_large": False
            }
        ],
        "statistics": {
            "by_language": {
                "python": {"files": 2, "lines": 200, "size_bytes": 5000}
            },
            "by_directory": {},
            "large_files": []
        }
    }


class TestJsonFormatter:
    """Test cases for JsonFormatter"""

    def test_initialization_default(self):
        """Test default initialization"""
        formatter = JsonFormatter()
        assert formatter.indent == 2
        assert formatter.compact is False

    def test_initialization_compact(self):
        """Test compact initialization"""
        formatter = JsonFormatter(compact=True)
        assert formatter.indent is None
        assert formatter.compact is True

    def test_initialization_custom_indent(self):
        """Test custom indent"""
        formatter = JsonFormatter(indent=4)
        assert formatter.indent == 4

    def test_format_valid_json(self, sample_tree_data):
        """Test that output is valid JSON"""
        formatter = JsonFormatter()
        output = formatter.format(sample_tree_data)

        # Should be parseable as JSON
        parsed = json.loads(output)
        assert parsed is not None

    def test_format_preserves_data(self, sample_tree_data):
        """Test that data is preserved in output"""
        formatter = JsonFormatter()
        output = formatter.format(sample_tree_data)
        parsed = json.loads(output)

        assert parsed["repository"] == "test-repo"
        assert parsed["summary"]["total_files"] == 3
        assert len(parsed["tree"]) == 3

    def test_format_compact(self, sample_tree_data):
        """Test compact output format"""
        formatter = JsonFormatter(compact=True)
        output = formatter.format(sample_tree_data)

        # Compact should have no extra whitespace
        parsed = json.loads(output)
        assert parsed["repository"] == "test-repo"

    def test_format_removes_nulls_in_compact(self):
        """Test that compact mode removes null values"""
        formatter = JsonFormatter(compact=True)
        data = {
            "repository": "test",
            "empty_field": None,
            "empty_list": [],
            "empty_dict": {},
            "valid_field": "value"
        }

        output = formatter.format(data)
        parsed = json.loads(output)

        assert "empty_field" not in parsed
        assert "empty_list" not in parsed
        assert "empty_dict" not in parsed
        assert parsed["valid_field"] == "value"

    def test_format_minimal(self, sample_tree_data):
        """Test minimal output format"""
        formatter = JsonFormatter()
        output = formatter.format_minimal(sample_tree_data)
        parsed = json.loads(output)

        # Should only have essential fields
        assert "repository" in parsed
        assert "summary" in parsed
        assert "files" in parsed
        assert "tree" not in parsed
        assert "statistics" not in parsed

    def test_format_minimal_file_info(self, sample_tree_data):
        """Test minimal format includes correct file info"""
        formatter = JsonFormatter()
        output = formatter.format_minimal(sample_tree_data)
        parsed = json.loads(output)

        files = parsed["files"]
        assert len(files) == 2  # Only files, not directories

        for f in files:
            assert "path" in f
            assert "lines" in f
            assert "lang" in f
            # Should not have extra fields
            assert "size_bytes" not in f
            assert "extension" not in f

    def test_format_unicode(self):
        """Test handling of Unicode characters"""
        formatter = JsonFormatter()
        data = {
            "repository": "test-repo",
            "description": "Contains unicode: Japanese, emoji"
        }

        output = formatter.format(data)
        parsed = json.loads(output)

        assert "Japanese" in parsed["description"]
        assert "emoji" in parsed["description"]

    def test_format_nested_structures(self):
        """Test handling of deeply nested structures"""
        formatter = JsonFormatter()
        data = {
            "level1": {
                "level2": {
                    "level3": {
                        "value": "deep"
                    }
                }
            }
        }

        output = formatter.format(data)
        parsed = json.loads(output)

        assert parsed["level1"]["level2"]["level3"]["value"] == "deep"

    def test_format_with_indentation(self, sample_tree_data):
        """Test that indentation is applied"""
        formatter_2 = JsonFormatter(indent=2)
        formatter_4 = JsonFormatter(indent=4)

        output_2 = formatter_2.format(sample_tree_data)
        output_4 = formatter_4.format(sample_tree_data)

        # 4-space indent should produce longer output
        assert len(output_4) > len(output_2)
        # Both should be valid JSON
        assert json.loads(output_2) is not None
        assert json.loads(output_4) is not None
