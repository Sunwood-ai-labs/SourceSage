"""
Tests for SourceSage CLI functionality
"""
import argparse
import subprocess
import sys
from pathlib import Path

import pytest

# Add parent directory to path to import sourcesage
sys.path.insert(0, str(Path(__file__).parent.parent))

from sourcesage import __version__
from sourcesage.cli import add_arguments

UTF8 = "utf-8"


class TestCLIArguments:
    """Test CLI argument parsing"""

    def test_short_output_option(self):
        """Test -o short option for output"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["-o", "./test_output"])
        assert args.output == "./test_output"

    def test_long_output_option(self):
        """Test --output long option"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["--output", "./test_output"])
        assert args.output == "./test_output"

    def test_diff_option(self):
        """Test --diff option for diff report generation"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["--diff"])
        assert args.diff is True

    def test_default_values(self):
        """Test default values for arguments"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args([])

        assert args.output == "./"
        assert args.repo == "./"
        assert args.diff is False
        assert args.language == "en"
        assert ".SourceSageignore" in args.ignore_file

    def test_diff_output_option(self):
        """Test --diff-output option"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["--diff-output", "./custom_diff"])
        assert args.diff_output == "./custom_diff"

    def test_combined_options(self):
        """Test combining multiple options"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args([
            "-o", "./output",
            "--diff",
            "--repo", "./myrepo"
        ])

        assert args.output == "./output"
        assert args.diff is True
        assert args.repo == "./myrepo"


class TestSourceSageignoreGeneration:
    """Test .SourceSageignore file generation"""

    def test_sourcesageignore_template_exists(self):
        """Test that the .SourceSageignore template exists in config"""
        package_root = Path(__file__).parent.parent
        template_path = package_root / "sourcesage" / "config" / ".SourceSageignore"
        assert template_path.exists(), f"Template not found at {template_path}"

    def test_sourcesageignore_has_sections(self):
        """Test that .SourceSageignore has proper sections"""
        package_root = Path(__file__).parent.parent
        template_path = package_root / "sourcesage" / "config" / ".SourceSageignore"

        content = template_path.read_text(encoding="utf-8")

        # Check for key sections
        assert "# バージョン管理システム" in content or "Version control" in content
        assert "# Python関連" in content or "Python" in content
        assert "# 仮想環境" in content or "virtual environment" in content.lower()
        assert "# パッケージマネージャーのロックファイル" in content or "lock file" in content

    def test_sourcesageignore_has_venv_patterns(self):
        """Test that .SourceSageignore includes virtual environment patterns"""
        package_root = Path(__file__).parent.parent
        template_path = package_root / "sourcesage" / "config" / ".SourceSageignore"

        content = template_path.read_text(encoding="utf-8")

        # Check for virtual environment patterns
        assert ".venv" in content or "venv" in content
        assert "ENV" in content or "env/" in content

    def test_sourcesageignore_has_lock_files(self):
        """Test that .SourceSageignore includes lock file patterns"""
        package_root = Path(__file__).parent.parent
        template_path = package_root / "sourcesage" / "config" / ".SourceSageignore"

        content = template_path.read_text(encoding="utf-8")

        # Check for lock file patterns
        assert "uv.lock" in content
        assert "package-lock.json" in content or "yarn.lock" in content

    def test_sourcesageignore_has_node_modules(self):
        """Test that .SourceSageignore includes Node.js patterns"""
        package_root = Path(__file__).parent.parent
        template_path = package_root / "sourcesage" / "config" / ".SourceSageignore"

        content = template_path.read_text(encoding="utf-8")

        # Check for Node.js patterns
        assert "node_modules/" in content
        assert "# Node.js" in content or "# Node.js関連" in content


class TestCLIOptions:
    """Test various CLI option combinations"""

    def test_repo_path_option(self):
        """Test --repo-path option for diff generation"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["--repo-path", "/path/to/repo"])
        assert args.repo_path == "/path/to/repo"

    def test_report_title_option(self):
        """Test --report-title option"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["--report-title", "My Custom Report"])
        assert args.report_title == "My Custom Report"

    def test_ignore_file_option(self):
        """Test --ignore-file option"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["--ignore-file", ".custom_ignore"])
        assert args.ignore_file == ".custom_ignore"


class TestBackwardCompatibility:
    """Test backward compatibility"""

    def test_sourcesage_command_name_in_pyproject(self):
        """Test that 'sourcesage' command is still available"""
        pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
        content = pyproject_path.read_text(encoding="utf-8")

        assert "sourcesage = " in content
        assert "sage = " in content

    def test_old_options_removed(self):
        """Test that old options are properly removed"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)

        # These should not exist anymore
        with pytest.raises(SystemExit):
            parser.parse_args(["--ss-mode", "Sage"])

        with pytest.raises(SystemExit):
            parser.parse_args(["--ss-output", "./out"])

        with pytest.raises(SystemExit):
            parser.parse_args(["--use-sourcesage-ignore"])

        with pytest.raises(SystemExit):
            parser.parse_args(["--generate-diff-report"])


class TestVersionDisplay:
    """Test version display functionality"""

    def test_version_module_exists(self):
        """Test that __version__ is accessible from sourcesage module"""
        assert __version__ is not None
        assert __version__ != "0.0.0"

    def test_version_matches_pyproject(self):
        """Test that __version__ matches pyproject.toml"""
        pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
        pyproject_content = pyproject_path.read_text(encoding="utf-8")

        # Extract version from pyproject.toml
        for line in pyproject_content.splitlines():
            if line.startswith("version ="):
                pyproject_version = line.split("=")[1].strip().strip('"').strip("'")
                break
        else:
            pyproject_version = None

        assert pyproject_version is not None
        assert __version__ == pyproject_version

    def test_version_short_option(self):
        """Test -v option for version display"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["-v"])
        assert args.version is True

    def test_version_long_option(self):
        """Test --version long option"""
        parser = argparse.ArgumentParser(add_help=False)
        add_arguments(parser)
        args = parser.parse_args(["--version"])
        assert args.version is True

    def test_version_uses_importlib_metadata(self):
        """Test that version is retrieved from importlib.metadata"""
        from importlib.metadata import version as metadata_version

        try:
            metadata_ver = metadata_version("sourcesage")
            assert __version__ == metadata_ver
        except Exception:
            # If package is not installed, __version__ should still work
            # and return the version from pyproject.toml
            assert __version__ != "0.0.0"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
