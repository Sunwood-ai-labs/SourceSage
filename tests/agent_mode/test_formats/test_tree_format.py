"""Tests for TreeFormatter class"""

import pytest
from sourcesage.modules.AgentMode.formats.tree_format import TreeFormatter


@pytest.fixture
def sample_tree_data():
    """Create sample tree data for testing"""
    return {
        "repository": "test-repo",
        "generated_at": "2026-01-25T10:00:00Z",
        "summary": {
            "total_files": 5,
            "total_directories": 2,
            "total_lines": 500,
            "total_size_bytes": 10240
        },
        "config": {
            "max_depth": None,
            "large_threshold": 200,
            "show_lines": True,
            "show_size": True,
            "sort_by": "name"
        },
        "tree": [
            {
                "path": "src",
                "type": "directory",
                "depth": 0,
                "children_count": 3
            },
            {
                "path": "src/main.py",
                "type": "file",
                "depth": 1,
                "language": "python",
                "extension": ".py",
                "lines": 250,
                "size_bytes": 5120,
                "is_large": True
            },
            {
                "path": "src/utils.py",
                "type": "file",
                "depth": 1,
                "language": "python",
                "extension": ".py",
                "lines": 100,
                "size_bytes": 2048,
                "is_large": False
            },
            {
                "path": "README.md",
                "type": "file",
                "depth": 0,
                "language": "markdown",
                "extension": ".md",
                "lines": 50,
                "size_bytes": 1024,
                "is_large": False
            }
        ],
        "statistics": {
            "by_language": {
                "python": {"files": 2, "lines": 350, "size_bytes": 7168},
                "markdown": {"files": 1, "lines": 50, "size_bytes": 1024}
            },
            "by_directory": {},
            "large_files": [
                {"path": "src/main.py", "lines": 250}
            ]
        }
    }


class TestTreeFormatter:
    """Test cases for TreeFormatter"""

    def test_initialization(self):
        """Test formatter initialization"""
        formatter = TreeFormatter()
        assert formatter.large_threshold == 200

        formatter_custom = TreeFormatter(large_threshold=500)
        assert formatter_custom.large_threshold == 500

    def test_format_basic_output(self, sample_tree_data):
        """Test basic output formatting"""
        formatter = TreeFormatter()
        output = formatter.format(sample_tree_data)

        assert 'Repository: test-repo' in output
        assert 'Summary:' in output
        assert '5 files' in output
        assert '2 directories' in output
        assert '500 total lines' in output

    def test_format_includes_tree_header(self, sample_tree_data):
        """Test that output includes tree header"""
        formatter = TreeFormatter()
        output = formatter.format(sample_tree_data)

        assert 'Directory Tree' in output
        assert '=' * 80 in output

    def test_format_includes_legend(self, sample_tree_data):
        """Test that output includes legend"""
        formatter = TreeFormatter()
        output = formatter.format(sample_tree_data)

        assert 'Legend:' in output
        assert 'large' in output.lower()

    def test_format_shows_large_files(self, sample_tree_data):
        """Test that large files are marked"""
        formatter = TreeFormatter(large_threshold=200)
        output = formatter.format(sample_tree_data)

        # main.py has 250 lines, should be marked as large
        assert '* large' in output

    def test_format_shows_statistics(self, sample_tree_data):
        """Test that statistics section is included"""
        formatter = TreeFormatter()
        output = formatter.format(sample_tree_data)

        assert 'Language Statistics:' in output
        assert 'python' in output.lower()

    def test_format_shows_large_files_list(self, sample_tree_data):
        """Test that large files list is included"""
        formatter = TreeFormatter()
        output = formatter.format(sample_tree_data)

        assert 'Large Files' in output
        assert 'src/main.py' in output
        assert '250' in output

    def test_format_item_file(self, sample_tree_data):
        """Test file item formatting"""
        formatter = TreeFormatter()
        config = sample_tree_data['config']

        file_item = {
            "path": "test.py",
            "type": "file",
            "extension": ".py",
            "lines": 100,
            "size_bytes": 2048,
            "is_large": False
        }

        result = formatter._format_item(file_item, config)

        assert 'test.py' in result
        assert '[py]' in result
        assert '100' in result

    def test_format_item_directory(self, sample_tree_data):
        """Test directory item formatting"""
        formatter = TreeFormatter()
        config = sample_tree_data['config']

        dir_item = {
            "path": "src",
            "type": "directory",
            "children_count": 5
        }

        result = formatter._format_item(dir_item, config)

        assert 'src/' in result
        assert '[dir]' in result
        assert '5 items' in result

    def test_format_size_utility(self):
        """Test size formatting utility"""
        assert TreeFormatter._format_size(500) == "500 B"
        assert TreeFormatter._format_size(1024) == "1.0 KB"
        assert TreeFormatter._format_size(1536) == "1.5 KB"
        assert TreeFormatter._format_size(1024 * 1024) == "1.0 MB"

    def test_empty_tree(self):
        """Test formatting empty tree"""
        formatter = TreeFormatter()
        empty_data = {
            "repository": "empty-repo",
            "generated_at": "2026-01-25T10:00:00Z",
            "summary": {
                "total_files": 0,
                "total_directories": 0,
                "total_lines": 0,
                "total_size_bytes": 0
            },
            "config": {
                "show_lines": True,
                "show_size": True
            },
            "tree": [],
            "statistics": {
                "by_language": {},
                "by_directory": {},
                "large_files": []
            }
        }

        output = formatter.format(empty_data)

        assert 'Repository: empty-repo' in output
        assert '0 files' in output
