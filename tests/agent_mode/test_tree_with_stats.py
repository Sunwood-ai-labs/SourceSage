"""Tests for TreeWithStats class"""

import os
import tempfile
import pytest
from unittest.mock import MagicMock, patch


class MockPatternMatcher:
    """Mock pattern matcher for testing"""
    def __init__(self, exclude_patterns=None):
        self.exclude_patterns = exclude_patterns or []

    def should_exclude(self, path):
        for pattern in self.exclude_patterns:
            if pattern in path:
                return True
        return False


class MockLanguageDetector:
    """Mock language detector for testing"""
    def detect_language(self, file_path):
        ext = os.path.splitext(file_path)[1]
        mapping = {
            '.py': 'python',
            '.js': 'javascript',
            '.json': 'json',
            '.md': 'markdown',
            '.txt': 'text',
        }
        return mapping.get(ext, 'text')


class MockFileProcessor:
    """Mock file processor for testing"""
    def _count_lines(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return sum(1 for _ in f)
        except Exception:
            return 0


@pytest.fixture
def temp_repo():
    """Create a temporary repository structure for testing"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create directory structure
        os.makedirs(os.path.join(tmpdir, 'src'))
        os.makedirs(os.path.join(tmpdir, 'tests'))
        os.makedirs(os.path.join(tmpdir, 'docs'))

        # Create files
        files = {
            'README.md': '# Test Project\n\nThis is a test.\n',
            'src/__init__.py': '',
            'src/main.py': '\n'.join([f'# Line {i}' for i in range(100)]),
            'src/utils.py': '\n'.join([f'# Util {i}' for i in range(50)]),
            'tests/__init__.py': '',
            'tests/test_main.py': '\n'.join([f'# Test {i}' for i in range(30)]),
            'docs/guide.md': '# Guide\n\n## Section 1\n\nContent here.\n',
        }

        for path, content in files.items():
            full_path = os.path.join(tmpdir, path)
            with open(full_path, 'w') as f:
                f.write(content)

        yield tmpdir


@pytest.fixture
def tree_generator():
    """Create TreeWithStats instance with mocks"""
    from sourcesage.modules.AgentMode.tree_with_stats import TreeWithStats

    pattern_matcher = MockPatternMatcher(['__pycache__', '.git'])
    language_detector = MockLanguageDetector()
    file_processor = MockFileProcessor()

    return TreeWithStats(pattern_matcher, language_detector, file_processor)


class TestTreeWithStats:
    """Test cases for TreeWithStats"""

    def test_generate_tree_data_basic(self, tree_generator, temp_repo):
        """Test basic tree data generation"""
        result = tree_generator.generate_tree_data(temp_repo)

        assert 'repository' in result
        assert 'generated_at' in result
        assert 'summary' in result
        assert 'tree' in result
        assert 'statistics' in result

    def test_summary_counts(self, tree_generator, temp_repo):
        """Test that summary contains correct counts"""
        result = tree_generator.generate_tree_data(temp_repo)
        summary = result['summary']

        assert summary['total_files'] == 7
        assert summary['total_directories'] == 3
        assert summary['total_lines'] > 0
        assert summary['total_size_bytes'] > 0

    def test_tree_items_structure(self, tree_generator, temp_repo):
        """Test that tree items have correct structure"""
        result = tree_generator.generate_tree_data(temp_repo)

        for item in result['tree']:
            assert 'path' in item
            assert 'type' in item
            assert item['type'] in ['file', 'directory']

            if item['type'] == 'file':
                assert 'language' in item
                assert 'lines' in item
                assert 'size_bytes' in item

    def test_large_file_detection(self, tree_generator, temp_repo):
        """Test that large files are correctly identified"""
        result = tree_generator.generate_tree_data(
            temp_repo,
            large_threshold=50
        )

        # src/main.py has 100 lines, should be marked as large
        main_py = next(
            (item for item in result['tree']
             if item['type'] == 'file' and 'main.py' in item['path']),
            None
        )
        assert main_py is not None
        assert main_py['is_large'] is True

    def test_max_depth_limit(self, tree_generator, temp_repo):
        """Test max_depth parameter limits tree depth"""
        result = tree_generator.generate_tree_data(temp_repo, max_depth=0)

        # With max_depth=0, should only include root level items
        for item in result['tree']:
            assert item['depth'] == 0

    def test_show_lines_option(self, tree_generator, temp_repo):
        """Test show_lines parameter"""
        result = tree_generator.generate_tree_data(temp_repo, show_lines=False)

        for item in result['tree']:
            if item['type'] == 'file':
                assert item['lines'] is None

    def test_show_size_option(self, tree_generator, temp_repo):
        """Test show_size parameter"""
        result = tree_generator.generate_tree_data(temp_repo, show_size=False)

        for item in result['tree']:
            if item['type'] == 'file':
                assert item['size_bytes'] is None

    def test_language_statistics(self, tree_generator, temp_repo):
        """Test language statistics collection"""
        result = tree_generator.generate_tree_data(temp_repo)
        lang_stats = result['statistics']['by_language']

        assert 'python' in lang_stats
        assert lang_stats['python']['files'] == 5  # 5 .py files (includes __init__.py files)
        assert lang_stats['python']['lines'] > 0

    def test_large_files_list(self, tree_generator, temp_repo):
        """Test large files list in statistics"""
        result = tree_generator.generate_tree_data(
            temp_repo,
            large_threshold=50
        )
        large_files = result['statistics']['large_files']

        assert len(large_files) > 0
        assert all('path' in f and 'lines' in f for f in large_files)

    def test_format_size(self, tree_generator):
        """Test size formatting utility"""
        from sourcesage.modules.AgentMode.tree_with_stats import TreeWithStats

        assert TreeWithStats.format_size(500) == "500 B"
        assert TreeWithStats.format_size(1024) == "1.0 KB"
        assert TreeWithStats.format_size(1024 * 1024) == "1.0 MB"
        assert TreeWithStats.format_size(1024 * 1024 * 1024) == "1.0 GB"
