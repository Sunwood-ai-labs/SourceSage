"""
E2E tests for SourceSage CLI.

Tests the complete flow from CLI execution to Repository_summary.md generation.
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).parent.parent.absolute()
UTF8 = "utf-8"


def resolve_venv_python():
    candidates = [
        PROJECT_ROOT / ".venv" / "Scripts" / "python.exe",
        PROJECT_ROOT / ".venv" / "bin" / "python",
        PROJECT_ROOT / "venv" / "Scripts" / "python.exe",
        PROJECT_ROOT / "venv" / "bin" / "python",
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return sys.executable


VENV_PYTHON = resolve_venv_python()


def init_git_repo(repo_path: Path, commit_message: str = "Initial commit"):
    subprocess.run(["git", "init"], cwd=repo_path, capture_output=True, check=True)
    subprocess.run(
        ["git", "config", "user.email", "test@example.com"],
        cwd=repo_path,
        capture_output=True,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Test User"],
        cwd=repo_path,
        capture_output=True,
        check=True,
    )
    subprocess.run(["git", "add", "."], cwd=repo_path, capture_output=True, check=True)
    subprocess.run(
        ["git", "commit", "-m", commit_message],
        cwd=repo_path,
        capture_output=True,
        check=True,
    )


def run_cli(repo_path: Path, *args: str):
    env = os.environ.copy()
    env["PYTHONPATH"] = str(PROJECT_ROOT)
    env["PYTHONIOENCODING"] = UTF8

    return subprocess.run(
        [VENV_PYTHON, "-m", "sourcesage.cli", "--repo", str(repo_path), *args],
        capture_output=True,
        text=True,
        encoding=UTF8,
        cwd=repo_path,
        env=env,
    )


def resolve_summary_file(base_path: Path) -> Path:
    summary_file = base_path / "Repository_summary.md"
    assets_summary = base_path / ".SourceSageAssets" / "Repository_summary.md"
    if not summary_file.exists() and assets_summary.exists():
        return assets_summary
    return summary_file


class TestE2ECLIExecution:
    """End-to-end tests for CLI execution."""

    def test_cli_generates_repository_summary(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_path = Path(tmpdir) / "test_repo"
            repo_path.mkdir()

            (repo_path / "README.md").write_text(
                "# Test Repository\n\nThis is a test.", encoding=UTF8
            )
            (repo_path / "src").mkdir()
            (repo_path / "src" / "main.py").write_text(
                "def hello():\n    print('Hello, World!')\n",
                encoding=UTF8,
            )
            (repo_path / "src" / "utils.py").write_text(
                "def add(a, b):\n    return a + b\n",
                encoding=UTF8,
            )

            init_git_repo(repo_path)
            result = run_cli(repo_path)

            assert result.returncode == 0, f"CLI failed: {result.stderr}"

            summary_file = resolve_summary_file(repo_path)
            assert summary_file.exists(), f"Repository_summary.md not found in {repo_path}"

            content = summary_file.read_text(encoding=UTF8)
            assert "# Project: test_repo" in content
            assert "## Project Statistics" in content
            assert "## File Contents" in content
            assert ".git/" not in content
            assert ".git\\objects" not in content

    def test_cli_with_output_option(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_path = Path(tmpdir) / "test_repo"
            output_path = Path(tmpdir) / "custom_output"
            repo_path.mkdir()
            output_path.mkdir()

            (repo_path / "README.md").write_text("# Test", encoding=UTF8)
            (repo_path / "main.py").write_text("print('test')", encoding=UTF8)
            init_git_repo(repo_path, commit_message="init")

            result = run_cli(repo_path, "-o", str(output_path))
            assert result.returncode == 0, f"CLI failed: {result.stderr}"

            summary_file = resolve_summary_file(output_path)
            assert summary_file.exists(), f"Repository_summary.md not found in {output_path}"

    def test_cli_with_language_option(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            for lang, expected_heading in [
                ("en", "## Project Statistics"),
                ("ja", "## プロジェクト統計"),
            ]:
                repo_path = Path(tmpdir) / f"test_repo_{lang}"
                repo_path.mkdir()

                (repo_path / "README.md").write_text("# Test", encoding=UTF8)
                (repo_path / "main.py").write_text("print('test')", encoding=UTF8)
                init_git_repo(repo_path, commit_message="init")

                result = run_cli(repo_path, "-l", lang)
                assert result.returncode == 0, f"CLI failed for language {lang}: {result.stderr}"

                summary_file = resolve_summary_file(repo_path)
                assert summary_file.exists(), f"Repository_summary.md not found for language {lang}"
                content = summary_file.read_text(encoding=UTF8)
                assert expected_heading in content

    def test_cli_generates_sourcesageignore_by_default(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_path = Path(tmpdir) / "test_repo"
            repo_path.mkdir()

            (repo_path / "README.md").write_text("# Test", encoding=UTF8)
            (repo_path / "main.py").write_text("print('test')", encoding=UTF8)
            init_git_repo(repo_path, commit_message="init")

            result = run_cli(repo_path)
            assert result.returncode == 0, f"CLI failed: {result.stderr}"

            ignore_file = repo_path / ".SourceSageignore"
            assert ignore_file.exists(), f".SourceSageignore not found in {repo_path}"

            summary_file = resolve_summary_file(repo_path)
            assert summary_file.exists(), f"Repository_summary.md not found in {repo_path}"

    def test_cli_respects_existing_sourcesageignore(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_path = Path(tmpdir) / "test_repo"
            repo_path.mkdir()

            (repo_path / "README.md").write_text("# Test", encoding=UTF8)
            (repo_path / "main.py").write_text("print('test')", encoding=UTF8)
            custom_ignore = repo_path / ".SourceSageignore"
            custom_ignore.write_text("# Custom ignore patterns\n*.tmp\n", encoding=UTF8)
            init_git_repo(repo_path, commit_message="init")

            result = run_cli(repo_path)
            assert result.returncode == 0, f"CLI failed: {result.stderr}"

            ignore_content = custom_ignore.read_text(encoding=UTF8)
            assert "# Custom ignore patterns" in ignore_content
            assert "*.tmp" in ignore_content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
