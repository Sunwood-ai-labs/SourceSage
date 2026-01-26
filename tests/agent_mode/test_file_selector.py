"""Tests for FileSelector class"""

import os
import tempfile
import pytest


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

        # Create files with varying content
        files = {
            'README.md': '# Test Project\n\nDescription here.\n',
            'src/__init__.py': '',
            'src/main.py': '\n'.join([f'# Line {i}' for i in range(100)]),
            'src/utils.py': '\n'.join([f'# Util {i}' for i in range(50)]),
            'src/config.json': '{"key": "value"}',
            'tests/__init__.py': '',
            'tests/test_main.py': '\n'.join([f'# Test {i}' for i in range(30)]),
        }

        for path, content in files.items():
            full_path = os.path.join(tmpdir, path)
            with open(full_path, 'w') as f:
                f.write(content)

        yield tmpdir


@pytest.fixture
def file_selector():
    """Create FileSelector instance with mocks"""
    from sourcesage.modules.AgentMode.file_selector import FileSelector

    pattern_matcher = MockPatternMatcher(['__pycache__', '.git'])
    language_detector = MockLanguageDetector()
    file_processor = MockFileProcessor()

    return FileSelector(pattern_matcher, language_detector, file_processor)


class TestFileSelector:
    """Test cases for FileSelector"""

    def test_select_all_files(self, file_selector, temp_repo):
        """Test selecting all files without filters"""
        files = file_selector.select_files(temp_repo)

        assert len(files) == 7
        paths = [f['path'] for f in files]
        assert any('main.py' in p for p in paths)
        assert any('README.md' in p for p in paths)

    def test_select_specific_files(self, file_selector, temp_repo):
        """Test selecting specific files by path"""
        files = file_selector.select_files(
            temp_repo,
            file_paths=['src/main.py', 'README.md']
        )

        assert len(files) == 2
        paths = [f['path'] for f in files]
        assert any('main.py' in p for p in paths)
        assert any('README.md' in p for p in paths)

    def test_select_by_include_pattern(self, file_selector, temp_repo):
        """Test selecting files by include pattern"""
        files = file_selector.select_files(
            temp_repo,
            include_patterns=['**/*.py']
        )

        assert len(files) == 5  # 5 .py files (includes __init__.py files)
        for f in files:
            assert f['path'].endswith('.py')

    def test_select_with_exclude_pattern(self, file_selector, temp_repo):
        """Test selecting files with exclude pattern"""
        files = file_selector.select_files(
            temp_repo,
            include_patterns=['**/*.py'],
            exclude_patterns=['**/test_*.py']
        )

        assert len(files) == 4  # Exclude test_main.py
        for f in files:
            assert 'test_' not in f['path']

    def test_select_by_min_lines(self, file_selector, temp_repo):
        """Test selecting files by minimum line count"""
        files = file_selector.select_files(
            temp_repo,
            min_lines=50
        )

        for f in files:
            assert f['lines'] >= 50

    def test_select_by_max_lines(self, file_selector, temp_repo):
        """Test selecting files by maximum line count"""
        files = file_selector.select_files(
            temp_repo,
            max_lines=50
        )

        for f in files:
            assert f['lines'] <= 50

    def test_select_by_language(self, file_selector, temp_repo):
        """Test selecting files by language"""
        files = file_selector.select_files(
            temp_repo,
            languages=['python']
        )

        for f in files:
            assert f['language'] == 'python'

    def test_get_file_content(self, file_selector, temp_repo):
        """Test getting content of a specific file"""
        result = file_selector.get_file_content(temp_repo, 'README.md')

        assert result is not None
        assert 'content' in result
        assert '# Test Project' in result['content']
        assert result['language'] == 'markdown'

    def test_get_file_content_with_max_lines(self, file_selector, temp_repo):
        """Test getting content with line limit"""
        result = file_selector.get_file_content(
            temp_repo,
            'src/main.py',
            max_lines=10
        )

        assert result is not None
        assert result.get('truncated') is True
        lines = result['content'].split('\n')
        assert len(lines) == 10

    def test_get_file_content_not_found(self, file_selector, temp_repo):
        """Test getting content of non-existent file"""
        result = file_selector.get_file_content(temp_repo, 'nonexistent.py')

        assert result is None

    def test_get_multiple_file_contents(self, file_selector, temp_repo):
        """Test getting contents of multiple files"""
        results = file_selector.get_multiple_file_contents(
            temp_repo,
            ['src/main.py', 'README.md']
        )

        assert len(results) == 2
        for r in results:
            assert 'content' in r

    def test_file_info_structure(self, file_selector, temp_repo):
        """Test that file info has correct structure"""
        files = file_selector.select_files(temp_repo)

        for f in files:
            assert 'path' in f
            assert 'full_path' in f
            assert 'size_bytes' in f
            assert 'lines' in f
            assert 'language' in f
            assert 'extension' in f
            assert 'modified' in f

    def test_format_files_output(self, file_selector, temp_repo):
        """Test formatting files as markdown output"""
        files = file_selector.select_files(
            temp_repo,
            file_paths=['README.md']
        )

        # Add content to files
        for f in files:
            content_info = file_selector.get_file_content(temp_repo, f['path'])
            if content_info:
                f['content'] = content_info['content']

        output = file_selector.format_files_output(files)

        assert '# Selected Files' in output
        assert 'README.md' in output
        assert '```markdown' in output

    def test_combined_filters(self, file_selector, temp_repo):
        """Test combining multiple filters"""
        files = file_selector.select_files(
            temp_repo,
            include_patterns=['**/*.py'],
            exclude_patterns=['**/__init__.py'],
            min_lines=10
        )

        for f in files:
            assert f['path'].endswith('.py')
            assert '__init__.py' not in f['path']
            assert f['lines'] >= 10
