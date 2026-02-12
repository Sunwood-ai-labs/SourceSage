"""
Tests for DocuSum Markdown structure validation

Tests the structure of generated Markdown documents to ensure
all required sections and headings are present.
"""
import os
import sys
import tempfile
from pathlib import Path

import pytest

# Add parent directory to path to import sourcesage
sys.path.insert(0, str(Path(__file__).parent.parent))

from sourcesage.modules.DocuSum.docusum import DocuSum


class TestDocuSumMarkdownStructure:
    """Test DocuSum generated Markdown structure"""

    def test_markdown_has_project_title(self):
        """Test that generated Markdown has project title heading"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create minimal test structure
            test_file = Path(tmpdir) / "test.py"
            test_file.write_text("print('hello')\n")

            # Create temporary output file
            output_file = Path(tmpdir) / "output.md"

            # Generate Markdown
            docusum = DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=None,  # Skip git info
            )
            docusum.generate_markdown()

            # Read generated Markdown
            content = output_file.read_text()

            # Check for project title
            assert "# Project:" in content, "Project title heading is missing"
            assert content.startswith("# Project:"), "Document should start with project title"

    def test_markdown_has_required_sections(self):
        """Test that all required section headings are present"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create minimal test structure
            test_file = Path(tmpdir) / "test.py"
            test_file.write_text("print('hello')\n")

            output_file = Path(tmpdir) / "output.md"

            # Generate Markdown
            docusum = DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=None,
            )
            docusum.generate_markdown()

            content = output_file.read_text()

            # Check for required level-2 sections
            assert "## 📊 Project Statistics" in content, "Project Statistics section is missing"
            # Note: File Contents section does not have a heading; files are listed directly

    def test_markdown_has_stats_subsections(self):
        """Test that statistics subsections are present"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test files
            (Path(tmpdir) / "test.py").write_text("print('hello')\n")
            (Path(tmpdir) / "test.js").write_text("console.log('hello');\n")

            output_file = Path(tmpdir) / "output.md"

            # Generate Markdown
            docusum = DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=None,
            )
            docusum.generate_markdown()

            content = output_file.read_text()

            # Check for statistics subsections
            assert "### 📊 File Size and Line Count" in content, "File Size and Line Count table is missing"
            assert "### 📈 Language Statistics" in content, "Language Statistics table is missing"

    def test_markdown_file_stats_table_structure(self):
        """Test that file stats table has correct structure"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test file
            (Path(tmpdir) / "test.py").write_text("print('hello')\n")

            output_file = Path(tmpdir) / "output.md"

            # Generate Markdown
            docusum = DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=None,
            )
            docusum.generate_markdown()

            content = output_file.read_text()

            # Check table structure
            assert "| File | Size | Lines | Language |" in content, "File stats table header is missing"
            assert "|------|------|-------|----------|" in content, "File stats table separator is missing"

    def test_markdown_language_stats_table_structure(self):
        """Test that language stats table has correct structure"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test files
            (Path(tmpdir) / "test.py").write_text("print('hello')\n")
            (Path(tmpdir) / "test.js").write_text("console.log('hello');\n")

            output_file = Path(tmpdir) / "output.md"

            # Generate Markdown
            docusum = DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=None,
            )
            docusum.generate_markdown()

            content = output_file.read_text()

            # Check table structure
            assert "| Language | Files | Total Lines | Total Size |" in content, "Language stats table header is missing"
            assert "|----------|-------|-------------|-----------|" in content, "Language stats table separator is missing"

    def test_markdown_file_contents_section(self):
        """Test that file contents section includes file details"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test file
            test_file = Path(tmpdir) / "test.py"
            test_file.write_text("print('hello')\n")

            output_file = Path(tmpdir) / "output.md"

            # Generate Markdown
            docusum = DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=None,
            )
            docusum.generate_markdown()

            content = output_file.read_text()

            # Check that file contents are included
            # File contents appear after statistics tables without a section heading
            assert "test.py" in content, "File name should be in contents"
            # Check for code block formatting
            assert "```python" in content, "File content should be in a code block"

    def test_markdown_with_git_info(self):
        """Test Markdown structure with Git information"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create minimal test structure with git
            test_file = Path(tmpdir) / "test.py"
            test_file.write_text("print('hello')\n")

            # Initialize git repo
            import subprocess
            subprocess.run(["git", "init"], cwd=tmpdir, capture_output=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=tmpdir, capture_output=True)
            subprocess.run(["git", "config", "user.name", "Test User"], cwd=tmpdir, capture_output=True)
            subprocess.run(["git", "add", "."], cwd=tmpdir, capture_output=True)
            subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=tmpdir, capture_output=True)

            output_file = Path(tmpdir) / "output.md"

            # Generate Markdown with git info
            docusum = DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=os.path.join(tmpdir, ".git"),
            )
            docusum.generate_markdown()

            content = output_file.read_text()

            # Check for Git information section
            assert "## 📂 Git Repository Information" in content, "Git Repository Information section is missing"

    def test_markdown_ignores_excluded_files(self):
        """Test that excluded files are not in the generated Markdown"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test files
            (Path(tmpdir) / "test.py").write_text("print('hello')\n")
            (Path(tmpdir) / "test.pyc").write_text("compiled\n")

            # Create ignore file
            ignore_file = Path(tmpdir) / ".SourceSageignore"
            ignore_file.write_text("*.pyc\n")

            output_file = Path(tmpdir) / "output.md"

            # Generate Markdown
            docusum = DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                ignore_file=str(ignore_file),
                git_path=None,
            )
            docusum.generate_markdown()

            content = output_file.read_text()

            # Check that .pyc files are excluded
            assert "test.py" in content, "Python file should be included"
            assert "test.pyc" not in content, "Compiled Python file should be excluded"

    def test_markdown_project_name(self):
        """Test that project name is correctly extracted"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test file
            (Path(tmpdir) / "test.py").write_text("print('hello')\n")

            output_file = Path(tmpdir) / "output.md"

            # Generate Markdown
            docusum = DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=None,
            )
            docusum.generate_markdown()

            content = output_file.read_text()

            # Project name should be the basename of the folder
            project_name = os.path.basename(tmpdir)
            assert f"# Project: {project_name}" in content, f"Project name should be '{project_name}'"


class TestDocuSumMarkdownContent:
    """Test DocuSum generated Markdown content quality"""

    def test_markdown_is_valid_utf8(self):
        """Test that generated Markdown is valid UTF-8"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test file with unicode content
            (Path(tmpdir) / "test.py").write_text("print('こんにちは')\n")

            output_file = Path(tmpdir) / "output.md"

            # Generate Markdown
            docusum = DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=None,
            )
            docusum.generate_markdown()

            # Read and verify UTF-8 encoding
            content = output_file.read_text(encoding='utf-8')
            assert len(content) > 0, "Generated file should not be empty"

    def test_markdown_has_statistics_data(self):
        """Test that statistics sections contain actual data"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test files
            (Path(tmpdir) / "test.py").write_text("print('hello')\n")

            output_file = Path(tmpdir) / "output.md"

            # Generate Markdown
            docusum = DocuSum(
                folders=[tmpdir],
                output_file=str(output_file),
                git_path=None,
            )
            docusum.generate_markdown()

            content = output_file.read_text()

            # Check for statistics data
            assert "Total directories:" in content, "Should show total directories"
            assert "Total files:" in content, "Should show total files"
            assert "Max depth:" in content, "Should show max depth"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
