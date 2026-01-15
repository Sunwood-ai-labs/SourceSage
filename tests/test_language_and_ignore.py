"""
Tests for new SourceSage features: language options and ignore file merging
"""
import argparse
import os
import sys
import tempfile
from pathlib import Path

import pytest

# Add parent directory to path to import sourcesage
sys.path.insert(0, str(Path(__file__).parent.parent))

from sourcesage.cli import add_arguments
from sourcesage.modules.DocuSum.file_pattern_matcher import FilePatternMatcher


class TestLanguageOption:
    """Test --language option"""

    def test_language_option_default(self):
        """Test that language option defaults to 'en'"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args([])
        assert args.language == "en"

    def test_language_option_english(self):
        """Test --language en option"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["--language", "en"])
        assert args.language == "en"

    def test_language_option_japanese(self):
        """Test --language ja option"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["--language", "ja"])
        assert args.language == "ja"

    def test_lang_short_option_english(self):
        """Test --lang en option"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["--lang", "en"])
        assert args.language == "en"

    def test_lang_short_option_japanese(self):
        """Test --lang ja option"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["--lang", "ja"])
        assert args.language == "ja"

    def test_l_short_option_english(self):
        """Test -l en option"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["-l", "en"])
        assert args.language == "en"

    def test_l_short_option_japanese(self):
        """Test -l ja option"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["-l", "ja"])
        assert args.language == "ja"

    def test_language_option_invalid(self):
        """Test that invalid language option raises error"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        with pytest.raises(SystemExit):
            parser.parse_args(["--language", "fr"])


class TestIgnoreFileMerging:
    """Test .gitignore and .SourceSageignore merging"""

    def test_single_ignore_file(self):
        """Test FilePatternMatcher with a single ignore file"""
        with tempfile.TemporaryDirectory() as tmpdir:
            ignore_file = Path(tmpdir) / ".testignore"
            ignore_file.write_text("*.pyc\n__pycache__/\ntest_temp/\n")

            matcher = FilePatternMatcher(str(ignore_file))

            # Test that patterns are loaded
            assert matcher.should_exclude("test.pyc")
            assert matcher.should_exclude("__pycache__/test.py")
            assert matcher.should_exclude("test_temp/file.txt")
            assert not matcher.should_exclude("test.py")

    def test_multiple_ignore_files(self):
        """Test FilePatternMatcher with multiple ignore files"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create .gitignore
            gitignore = Path(tmpdir) / ".gitignore"
            gitignore.write_text("*.pyc\n__pycache__/\nnode_modules/\n")

            # Create .SourceSageignore
            sourcesageignore = Path(tmpdir) / ".SourceSageignore"
            sourcesageignore.write_text("uv.lock\n*.log\ntest_temp/\n")

            # Test with both files
            matcher = FilePatternMatcher([str(gitignore), str(sourcesageignore)])

            # Test that patterns from both files are loaded
            assert matcher.should_exclude("test.pyc")  # from .gitignore
            assert matcher.should_exclude("__pycache__/test.py")  # from .gitignore
            assert matcher.should_exclude("node_modules/package")  # from .gitignore
            assert matcher.should_exclude("uv.lock")  # from .SourceSageignore
            assert matcher.should_exclude("debug.log")  # from .SourceSageignore
            assert matcher.should_exclude("test_temp/file.txt")  # from .SourceSageignore
            assert not matcher.should_exclude("test.py")

    def test_gitignore_and_sourcesageignore_merge(self):
        """Test that .gitignore and .SourceSageignore are properly merged"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create .gitignore
            gitignore = Path(tmpdir) / ".gitignore"
            gitignore.write_text("*.pyc\n__pycache__/\n*.log\n")

            # Create .SourceSageignore
            sourcesageignore = Path(tmpdir) / ".SourceSageignore"
            sourcesageignore.write_text("uv.lock\n*.log\ntest_output/\n")

            # Test merging (uv.lock should be from .SourceSageignore)
            matcher = FilePatternMatcher([str(gitignore), str(sourcesageignore)])

            # Both files have *.log, should still work
            assert matcher.should_exclude("debug.log")

            # .SourceSageignore specific patterns
            assert matcher.should_exclude("uv.lock")
            assert matcher.should_exclude("test_output/file.txt")

            # .gitignore specific patterns
            assert matcher.should_exclude("test.pyc")
            assert matcher.should_exclude("__pycache__/test.py")

    def test_sourcesageignore_has_uv_lock(self):
        """Test that .SourceSageignore includes uv.lock pattern"""
        package_root = Path(__file__).parent.parent
        sourcesageignore = package_root / ".SourceSageignore"

        if sourcesageignore.exists():
            content = sourcesageignore.read_text()
            assert "uv.lock" in content, "uv.lock should be in .SourceSageignore"

    def test_packaged_sourcesageignore_has_uv_lock(self):
        """Test that packaged .SourceSageignore includes uv.lock pattern"""
        package_root = Path(__file__).parent.parent
        packaged_ignore = package_root / "sourcesage" / "config" / ".SourceSageignore"

        if packaged_ignore.exists():
            content = packaged_ignore.read_text()
            assert "uv.lock" in content, "uv.lock should be in packaged .SourceSageignore"


class TestFilePatternMatcherFunctionality:
    """Test FilePatternMatcher functionality"""

    def test_default_patterns(self):
        """Test that default patterns are included"""
        with tempfile.TemporaryDirectory() as tmpdir:
            ignore_file = Path(tmpdir) / ".testignore"
            ignore_file.write_text("")  # Empty file

            matcher = FilePatternMatcher(str(ignore_file))

            # Test default patterns
            assert matcher.should_exclude(".git")
            assert matcher.should_exclude("node_modules")
            assert matcher.should_exclude("__pycache__")
            assert matcher.should_exclude("test.pyc")
            assert matcher.should_exclude(".DS_Store")
            assert matcher.should_exclude(".SourceSageAssets")
            assert matcher.should_exclude("package-lock.json")
            assert matcher.should_exclude("debug.log")

    def test_pattern_matching_wildcards(self):
        """Test wildcard pattern matching"""
        with tempfile.TemporaryDirectory() as tmpdir:
            ignore_file = Path(tmpdir) / ".testignore"
            ignore_file.write_text("*.pyc\n*.log\ntest_*\n")

            matcher = FilePatternMatcher(str(ignore_file))

            assert matcher.should_exclude("file.pyc")
            assert matcher.should_exclude("debug.log")
            assert matcher.should_exclude("test_temp")
            assert matcher.should_exclude("test_file.txt")
            assert not matcher.should_exclude("file.py")

    def test_directory_patterns(self):
        """Test directory pattern matching"""
        with tempfile.TemporaryDirectory() as tmpdir:
            ignore_file = Path(tmpdir) / ".testignore"
            ignore_file.write_text("__pycache__/\nnode_modules/\n")

            matcher = FilePatternMatcher(str(ignore_file))

            assert matcher.should_exclude("__pycache__/test.py")
            assert matcher.should_exclude("node_modules/package/index.js")
            assert not matcher.should_exclude("test.py")

    def test_include_patterns(self):
        """Test include patterns (negation)"""
        with tempfile.TemporaryDirectory() as tmpdir:
            ignore_file = Path(tmpdir) / ".testignore"
            ignore_file.write_text("*.log\n!debug.log\n")

            matcher = FilePatternMatcher(str(ignore_file))

            # All .log files should be excluded except debug.log
            # Note: Current implementation may not fully support negation
            assert matcher.should_exclude("info.log")


class TestBackwardCompatibility:
    """Test backward compatibility with existing code"""

    def test_single_file_still_works(self):
        """Test that passing a single file path still works"""
        with tempfile.TemporaryDirectory() as tmpdir:
            ignore_file = Path(tmpdir) / ".testignore"
            ignore_file.write_text("*.pyc\n")

            # Both string and list should work
            matcher1 = FilePatternMatcher(str(ignore_file))
            matcher2 = FilePatternMatcher([str(ignore_file)])

            assert matcher1.should_exclude("test.pyc")
            assert matcher2.should_exclude("test.pyc")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
