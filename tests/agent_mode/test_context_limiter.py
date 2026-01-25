"""Tests for ContextLimiter class"""

import pytest
from sourcesage.modules.AgentMode.context_limiter import (
    ContextLimiter,
    TruncateStrategy,
    ContextLimitExceeded
)


class TestContextLimiter:
    """Test cases for ContextLimiter"""

    def test_initialization_defaults(self):
        """Test default initialization values"""
        limiter = ContextLimiter()

        assert limiter.max_total_lines == 10000
        assert limiter.max_file_lines == 1000
        assert limiter.truncate_strategy == TruncateStrategy.MIDDLE

    def test_initialization_custom(self):
        """Test custom initialization values"""
        limiter = ContextLimiter(
            max_total_lines=5000,
            max_file_lines=500,
            truncate_strategy=TruncateStrategy.HEAD
        )

        assert limiter.max_total_lines == 5000
        assert limiter.max_file_lines == 500
        assert limiter.truncate_strategy == TruncateStrategy.HEAD

    def test_can_add_lines(self):
        """Test line budget checking"""
        limiter = ContextLimiter(max_total_lines=100)

        assert limiter.can_add_lines(50) is True
        assert limiter.can_add_lines(100) is True
        assert limiter.can_add_lines(101) is False

    def test_add_lines(self):
        """Test adding lines to counter"""
        limiter = ContextLimiter(max_total_lines=100)

        assert limiter.add_lines(50) is True
        assert limiter.remaining_lines() == 50

        assert limiter.add_lines(30) is True
        assert limiter.remaining_lines() == 20

        assert limiter.add_lines(30) is False  # Would exceed
        assert limiter.remaining_lines() == 20  # Unchanged

    def test_reset(self):
        """Test resetting the limiter"""
        limiter = ContextLimiter(max_total_lines=100)
        limiter.add_lines(50)

        limiter.reset()

        assert limiter.remaining_lines() == 100
        assert len(limiter.get_warnings()) == 0

    def test_truncate_head_strategy(self):
        """Test HEAD truncation strategy"""
        limiter = ContextLimiter(
            max_total_lines=1000,
            max_file_lines=5,
            truncate_strategy=TruncateStrategy.HEAD
        )

        content = '\n'.join([f'Line {i}' for i in range(10)])
        truncated, was_truncated, warning = limiter.truncate_content(
            content, 'test.py', 10
        )

        assert was_truncated is True
        assert 'TRUNCATED' in warning
        assert 'Line 0' in truncated
        assert 'Line 4' in truncated
        assert 'Line 9' not in truncated

    def test_truncate_tail_strategy(self):
        """Test TAIL truncation strategy"""
        limiter = ContextLimiter(
            max_total_lines=1000,
            max_file_lines=5,
            truncate_strategy=TruncateStrategy.TAIL
        )

        content = '\n'.join([f'Line {i}' for i in range(10)])
        truncated, was_truncated, warning = limiter.truncate_content(
            content, 'test.py', 10
        )

        assert was_truncated is True
        assert 'Line 0' not in truncated
        assert 'Line 9' in truncated

    def test_truncate_middle_strategy(self):
        """Test MIDDLE truncation strategy"""
        limiter = ContextLimiter(
            max_total_lines=1000,
            max_file_lines=6,
            truncate_strategy=TruncateStrategy.MIDDLE
        )

        content = '\n'.join([f'Line {i}' for i in range(20)])
        truncated, was_truncated, warning = limiter.truncate_content(
            content, 'test.py', 20
        )

        assert was_truncated is True
        assert 'omitted' in truncated.lower()
        # Should have first and last portions
        assert 'Line 0' in truncated
        assert 'Line 19' in truncated

    def test_no_truncation_needed(self):
        """Test when truncation is not needed"""
        limiter = ContextLimiter(
            max_total_lines=1000,
            max_file_lines=100
        )

        content = '\n'.join([f'Line {i}' for i in range(10)])
        truncated, was_truncated, warning = limiter.truncate_content(
            content, 'test.py', 10
        )

        assert was_truncated is False
        assert warning == ""
        assert truncated == content

    def test_should_include_file_within_budget(self):
        """Test file inclusion when within budget"""
        limiter = ContextLimiter(max_total_lines=1000)

        should_include, reason = limiter.should_include_file('test.py', 100)

        assert should_include is True
        assert reason == ""

    def test_should_include_file_exceeds_budget(self):
        """Test file inclusion when it would exceed budget"""
        limiter = ContextLimiter(max_total_lines=100, max_file_lines=50)
        limiter.add_lines(90)

        should_include, reason = limiter.should_include_file('test.py', 100)

        assert should_include is False
        assert 'limit reached' in reason.lower()

    def test_should_include_file_exclude_large(self):
        """Test file exclusion when exclude_large is enabled"""
        limiter = ContextLimiter(
            exclude_large=True,
            large_threshold=100
        )

        should_include, reason = limiter.should_include_file('test.py', 500)

        assert should_include is False
        assert 'Large file excluded' in reason

    def test_priority_files_not_excluded(self):
        """Test that priority files are not excluded even if large"""
        limiter = ContextLimiter(
            exclude_large=True,
            large_threshold=100,
            priority_patterns=['*.py']
        )

        should_include, reason = limiter.should_include_file('test.py', 500)

        assert should_include is True

    def test_get_warnings(self):
        """Test warning collection"""
        limiter = ContextLimiter(
            max_total_lines=1000,
            max_file_lines=5
        )

        content = '\n'.join([f'Line {i}' for i in range(10)])
        limiter.truncate_content(content, 'test.py', 10)

        warnings = limiter.get_warnings()

        assert len(warnings) == 1
        assert warnings[0]['file'] == 'test.py'
        assert warnings[0]['original_lines'] == 10

    def test_get_status(self):
        """Test status reporting"""
        limiter = ContextLimiter(max_total_lines=1000, max_file_lines=100)
        limiter.add_lines(300)

        status = limiter.get_status()

        assert status['current_lines'] == 300
        assert status['max_total_lines'] == 1000
        assert status['remaining_lines'] == 700

    def test_format_content_with_metadata(self):
        """Test content formatting with metadata"""
        limiter = ContextLimiter()

        content = 'print("hello")'
        result = limiter.format_content_with_metadata(
            content=content,
            file_path='test.py',
            size_bytes=1024,
            total_lines=1,
            language='python'
        )

        assert '## `test.py`' in result
        assert '1.0 KB' in result
        assert '```python' in result
        assert content in result
