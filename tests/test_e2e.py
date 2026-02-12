"""
E2E Tests for SourceSage CLI

Tests the complete flow from CLI execution to Repository_summary.md generation.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest


# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()

# Find the virtual environment Python
VENV_PYTHON = None
for venv_path in [PROJECT_ROOT / ".venv" / "bin" / "python",
                   PROJECT_ROOT / "venv" / "bin" / "python"]:
    if venv_path.exists():
        VENV_PYTHON = str(venv_path)
        break

# If no venv found, use current python
if VENV_PYTHON is None:
    VENV_PYTHON = sys.executable


class TestE2ECLIExecution:
    """End-to-end tests for CLI execution"""

    def test_cli_generates_repository_summary(self):
        """Test that running CLI generates Repository_summary.md"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a sample repository structure
            repo_path = Path(tmpdir) / "test_repo"
            repo_path.mkdir()

            # Create sample files
            (repo_path / "README.md").write_text("# Test Repository\n\nThis is a test.")
            (repo_path / "src").mkdir()
            (repo_path / "src" / "main.py").write_text("""
def hello():
    print("Hello, World!")

if __name__ == "__main__":
    hello()
""")
            (repo_path / "src" / "utils.py").write_text("""
def add(a, b):
    return a + b
""")

            # Initialize git repository
            subprocess.run(
                ["git", "init"],
                cwd=repo_path,
                capture_output=True,
                check=True
            )
            subprocess.run(
                ["git", "config", "user.email", "test@example.com"],
                cwd=repo_path,
                capture_output=True,
                check=True
            )
            subprocess.run(
                ["git", "config", "user.name", "Test User"],
                cwd=repo_path,
                capture_output=True,
                check=True
            )
            subprocess.run(
                ["git", "add", "."],
                cwd=repo_path,
                capture_output=True,
                check=True
            )
            subprocess.run(
                ["git", "commit", "-m", "Initial commit"],
                cwd=repo_path,
                capture_output=True,
                check=True
            )

            # Prepare environment with PYTHONPATH
            env = os.environ.copy()
            env["PYTHONPATH"] = str(PROJECT_ROOT)

            # Run SourceSage CLI
            result = subprocess.run(
                [VENV_PYTHON, "-m", "sourcesage.cli", "--repo", str(repo_path)],
                capture_output=True,
                text=True,
                cwd=repo_path,
                env=env
            )

            # Check that CLI executed successfully
            if result.returncode != 0:
                print(f"stdout: {result.stdout}")
                print(f"stderr: {result.stderr}")
            assert result.returncode == 0, f"CLI failed: {result.stderr}"

            # Check that Repository_summary.md was generated
            # It could be in the repo root or in .SourceSageAssets
            summary_file = repo_path / "Repository_summary.md"
            assets_summary = repo_path / ".SourceSageAssets" / "Repository_summary.md"

            if not summary_file.exists() and assets_summary.exists():
                summary_file = assets_summary
            assert summary_file.exists(), f"Repository_summary.md not found in {repo_path} or .SourceSageAssets"

            # Verify content has some expected sections
            content = summary_file.read_text()
            assert len(content) > 0, "Repository_summary.md is empty"
            assert "Repository" in content or "リポジトリ" in content

    def test_cli_with_output_option(self):
        """Test CLI with custom output directory"""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_path = Path(tmpdir) / "test_repo"
            output_path = Path(tmpdir) / "custom_output"
            repo_path.mkdir()
            output_path.mkdir()

            # Create minimal repository
            (repo_path / "README.md").write_text("# Test")
            (repo_path / "main.py").write_text("print('test')")

            # Initialize git
            subprocess.run(["git", "init"], cwd=repo_path, capture_output=True, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_path, capture_output=True, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=repo_path, capture_output=True, check=True)
            subprocess.run(["git", "add", "."], cwd=repo_path, capture_output=True, check=True)
            subprocess.run(["git", "commit", "-m", "init"], cwd=repo_path, capture_output=True, check=True)

            # Prepare environment with PYTHONPATH
            env = os.environ.copy()
            env["PYTHONPATH"] = str(PROJECT_ROOT)

            # Run CLI with output option
            result = subprocess.run(
                [VENV_PYTHON, "-m", "sourcesage.cli", "--repo", str(repo_path), "-o", str(output_path)],
                capture_output=True,
                text=True,
                cwd=repo_path,
                env=env
            )

            assert result.returncode == 0, f"CLI failed: {result.stderr}"

            # Check output directory (could be in output_path or output_path/.SourceSageAssets)
            summary_file = output_path / "Repository_summary.md"
            assets_summary = output_path / ".SourceSageAssets" / "Repository_summary.md"

            if not summary_file.exists() and assets_summary.exists():
                summary_file = assets_summary
            assert summary_file.exists(), f"Repository_summary.md not found in {output_path}"

    def test_cli_with_language_option(self):
        """Test CLI with different language options"""
        with tempfile.TemporaryDirectory() as tmpdir:
            for lang in ["en", "ja"]:
                repo_path = Path(tmpdir) / f"test_repo_{lang}"
                repo_path.mkdir()

                # Create minimal repository
                (repo_path / "README.md").write_text("# Test")
                (repo_path / "main.py").write_text("print('test')")

                # Initialize git
                subprocess.run(["git", "init"], cwd=repo_path, capture_output=True, check=True)
                subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_path, capture_output=True, check=True)
                subprocess.run(["git", "config", "user.name", "Test"], cwd=repo_path, capture_output=True, check=True)
                subprocess.run(["git", "add", "."], cwd=repo_path, capture_output=True, check=True)
                subprocess.run(["git", "commit", "-m", "init"], cwd=repo_path, capture_output=True, check=True)

                # Prepare environment with PYTHONPATH
                env = os.environ.copy()
                env["PYTHONPATH"] = str(PROJECT_ROOT)

                # Run CLI with language option
                result = subprocess.run(
                    [VENV_PYTHON, "-m", "sourcesage.cli", "--repo", str(repo_path), "-l", lang],
                    capture_output=True,
                    text=True,
                    cwd=repo_path,
                    env=env
                )

                assert result.returncode == 0, f"CLI failed for language {lang}: {result.stderr}"

                # Check that summary was generated
                summary_file = repo_path / "Repository_summary.md"
                assets_summary = repo_path / ".SourceSageAssets" / "Repository_summary.md"

                if not summary_file.exists() and assets_summary.exists():
                    summary_file = assets_summary
                assert summary_file.exists(), f"Repository_summary.md not found for language {lang}"

    def test_cli_generates_sourcesageignore_by_default(self):
        """Test CLI generates .SourceSageignore by default (v7.2.2 behavior)"""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_path = Path(tmpdir) / "test_repo"
            repo_path.mkdir()

            # Create minimal repository
            (repo_path / "README.md").write_text("# Test")
            (repo_path / "main.py").write_text("print('test')")

            # Initialize git
            subprocess.run(["git", "init"], cwd=repo_path, capture_output=True, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_path, capture_output=True, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=repo_path, capture_output=True, check=True)
            subprocess.run(["git", "add", "."], cwd=repo_path, capture_output=True, check=True)
            subprocess.run(["git", "commit", "-m", "init"], cwd=repo_path, capture_output=True, check=True)

            # Prepare environment with PYTHONPATH
            env = os.environ.copy()
            env["PYTHONPATH"] = str(PROJECT_ROOT)

            # Run CLI
            result = subprocess.run(
                [VENV_PYTHON, "-m", "sourcesage.cli", "--repo", str(repo_path)],
                capture_output=True,
                text=True,
                cwd=repo_path,
                env=env
            )

            assert result.returncode == 0, f"CLI failed: {result.stderr}"

            # Check that .SourceSageignore was generated
            ignore_file = repo_path / ".SourceSageignore"
            assert ignore_file.exists(), f".SourceSageignore not found in {repo_path}"

            # Check that Repository_summary.md was generated
            summary_file = repo_path / "Repository_summary.md"
            assets_summary = repo_path / ".SourceSageAssets" / "Repository_summary.md"

            if not summary_file.exists() and assets_summary.exists():
                summary_file = assets_summary
            assert summary_file.exists(), f"Repository_summary.md not found in {repo_path}"

    def test_cli_respects_existing_sourcesageignore(self):
        """Test that CLI respects existing .SourceSageignore file"""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_path = Path(tmpdir) / "test_repo"
            repo_path.mkdir()

            # Create minimal repository
            (repo_path / "README.md").write_text("# Test")
            (repo_path / "main.py").write_text("print('test')")

            # Create custom .SourceSageignore
            custom_ignore = repo_path / ".SourceSageignore"
            custom_ignore.write_text("# Custom ignore patterns\n*.tmp\n")

            # Initialize git
            subprocess.run(["git", "init"], cwd=repo_path, capture_output=True, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_path, capture_output=True, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=repo_path, capture_output=True, check=True)
            subprocess.run(["git", "add", "."], cwd=repo_path, capture_output=True, check=True)
            subprocess.run(["git", "commit", "-m", "init"], cwd=repo_path, capture_output=True, check=True)

            # Prepare environment with PYTHONPATH
            env = os.environ.copy()
            env["PYTHONPATH"] = str(PROJECT_ROOT)

            # Run CLI
            result = subprocess.run(
                [VENV_PYTHON, "-m", "sourcesage.cli", "--repo", str(repo_path)],
                capture_output=True,
                text=True,
                cwd=repo_path,
                env=env
            )

            assert result.returncode == 0, f"CLI failed: {result.stderr}"

            # Check that existing .SourceSageignore was not overwritten
            ignore_content = custom_ignore.read_text()
            assert "# Custom ignore patterns" in ignore_content
            assert "*.tmp" in ignore_content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
