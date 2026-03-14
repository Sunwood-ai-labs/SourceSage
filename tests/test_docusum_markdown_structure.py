"""
Tests for DocuSum Markdown structure validation.
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sourcesage.modules.DocuSum.docusum import DocuSum

UTF8 = "utf-8"


class TestDocuSumMarkdownStructure:
    """Test DocuSum generated Markdown structure."""

    def test_markdown_has_project_title(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "test.py").write_text("print('hello')\n", encoding=UTF8)
            output_file = Path(tmpdir) / "output.md"

            DocuSum(folders=[tmpdir], output_file=str(output_file), git_path=None).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert content.startswith("# Project:")

    def test_markdown_has_required_sections(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "test.py").write_text("print('hello')\n", encoding=UTF8)
            output_file = Path(tmpdir) / "output.md"

            DocuSum(folders=[tmpdir], output_file=str(output_file), git_path=None).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert "## Project Statistics" in content
            assert "## File Contents" in content

    def test_markdown_has_stats_subsections(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "test.py").write_text("print('hello')\n", encoding=UTF8)
            (Path(tmpdir) / "test.js").write_text("console.log('hello');\n", encoding=UTF8)
            output_file = Path(tmpdir) / "output.md"

            DocuSum(folders=[tmpdir], output_file=str(output_file), git_path=None).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert "### File Size and Line Count" in content
            assert "### Language Statistics" in content

    def test_markdown_file_stats_table_structure(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "test.py").write_text("print('hello')\n", encoding=UTF8)
            output_file = Path(tmpdir) / "output.md"

            DocuSum(folders=[tmpdir], output_file=str(output_file), git_path=None).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert "| File | Size | Lines | Language |" in content
            assert "|------|------|-------|----------|" in content

    def test_markdown_language_stats_table_structure(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "test.py").write_text("print('hello')\n", encoding=UTF8)
            (Path(tmpdir) / "test.js").write_text("console.log('hello');\n", encoding=UTF8)
            output_file = Path(tmpdir) / "output.md"

            DocuSum(folders=[tmpdir], output_file=str(output_file), git_path=None).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert "| Language | Files | Total Lines | Total Size |" in content
            assert "|----------|-------|-------------|-----------|" in content

    def test_markdown_file_contents_section(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "test.py").write_text("print('hello')\n", encoding=UTF8)
            output_file = Path(tmpdir) / "output.md"

            DocuSum(folders=[tmpdir], output_file=str(output_file), git_path=None).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert "`test.py`" in content
            assert "```python" in content

    def test_markdown_lite_mode_keeps_root_readme_only(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "README.md").write_text("# Demo\n\nHello README\n", encoding=UTF8)
            (Path(tmpdir) / "test.py").write_text("print('hello')\n", encoding=UTF8)
            output_file = Path(tmpdir) / "output.md"

            DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=None,
                lite=True,
            ).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert "## README" in content
            assert "## File Contents" not in content
            assert "`README.md`" in content
            assert "Hello README" in content
            assert "print('hello')" not in content

    def test_markdown_with_git_info(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_path = Path(tmpdir)
            (repo_path / "test.py").write_text("print('hello')\n", encoding=UTF8)
            self._init_repo(repo_path)
            output_file = repo_path / "output.md"

            DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=os.path.join(tmpdir, ".git"),
            ).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert "## Git Repository Information" in content

    def test_markdown_ignores_excluded_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "test.py").write_text("print('hello')\n", encoding=UTF8)
            (Path(tmpdir) / "test.pyc").write_text("compiled\n", encoding=UTF8)
            ignore_file = Path(tmpdir) / ".SourceSageignore"
            ignore_file.write_text("*.pyc\n", encoding=UTF8)
            output_file = Path(tmpdir) / "output.md"

            DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                ignore_file=str(ignore_file),
                git_path=None,
            ).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert "test.py" in content
            assert "test.pyc" not in content

    def test_markdown_excludes_git_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_path = Path(tmpdir)
            (repo_path / "test.py").write_text("print('hello')\n", encoding=UTF8)
            self._init_repo(repo_path)
            output_file = repo_path / "output.md"

            DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=os.path.join(tmpdir, ".git"),
            ).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert ".git/" not in content
            assert ".git\\objects" not in content

    def test_markdown_project_name(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "test.py").write_text("print('hello')\n", encoding=UTF8)
            output_file = Path(tmpdir) / "output.md"

            DocuSum(folders=[tmpdir], output_file=str(output_file), git_path=None).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert f"# Project: {os.path.basename(tmpdir)}" in content

    @staticmethod
    def _init_repo(repo_path: Path):
        subprocess.run(["git", "init"], cwd=repo_path, capture_output=True, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_path, capture_output=True, check=True)
        subprocess.run(["git", "config", "user.name", "Test User"], cwd=repo_path, capture_output=True, check=True)
        subprocess.run(["git", "add", "."], cwd=repo_path, capture_output=True, check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=repo_path, capture_output=True, check=True)


class TestDocuSumMarkdownContent:
    """Test DocuSum generated Markdown content quality."""

    def test_markdown_is_valid_utf8(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "test.py").write_text("print('こんにちは')\n", encoding=UTF8)
            output_file = Path(tmpdir) / "output.md"

            DocuSum(folders=[tmpdir], output_file=str(output_file), git_path=None).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert len(content) > 0

    def test_markdown_has_statistics_data(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "test.py").write_text("print('hello')\n", encoding=UTF8)
            output_file = Path(tmpdir) / "output.md"

            DocuSum(folders=[tmpdir], output_file=str(output_file), git_path=None).generate_markdown()
            content = output_file.read_text(encoding=UTF8)

            assert "Total directories:" in content
            assert "Total files:" in content
            assert "Max depth:" in content
