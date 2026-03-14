"""
Tests for Git information collection functionality.
"""
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from sourcesage.modules.DiffReport.git_diff import GitDiffGenerator
from sourcesage.modules.GitCommander import run_command


def force_rmtree(path):
    def onexc(func, failed_path, _excinfo):
        os.chmod(failed_path, stat.S_IWRITE)
        func(failed_path)

    try:
        shutil.rmtree(path, onexc=onexc)
    except TypeError:
        shutil.rmtree(path, onerror=onexc)


class TestRunCommand:
    """Test run_command function."""

    def test_run_command_echo(self):
        output = run_command(
            [sys.executable, "-c", "print('Hello, World!')"],
            preview=False,
        )
        assert output == "Hello, World!"

    def test_run_command_with_cwd(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = Path(tmpdir) / "test.txt"
            test_file.write_text("test content", encoding="utf-8")

            output = run_command(
                [sys.executable, "-c", "import os; print('\\n'.join(sorted(os.listdir('.'))))"],
                cwd=tmpdir,
                preview=False,
            )
            assert "test.txt" in output

    def test_run_command_failure(self):
        with pytest.raises(subprocess.CalledProcessError):
            run_command([sys.executable, "-c", "import sys; sys.exit(1)"], preview=False)

    def test_run_command_git_version(self):
        output = run_command(["git", "--version"], preview=False)
        assert "git" in output.lower()


class TestGitDiffGenerator:
    """Test GitDiffGenerator class."""

    def test_init(self):
        generator = GitDiffGenerator(
            repo_path="/path/to/repo",
            git_fetch_tags=["git", "fetch", "--tags"],
            git_tag_sort=["git", "tag", "--sort=-creatordate"],
            git_diff_command=["git", "diff"],
        )

        assert generator.repo_path == "/path/to/repo"
        assert generator.git_fetch_tags == ["git", "fetch", "--tags"]
        assert generator.git_tag_sort == ["git", "tag", "--sort=-creatordate"]
        assert generator.git_diff_command == ["git", "diff"]

    def test_get_git_diff_no_repo(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = GitDiffGenerator(
                repo_path=tmpdir,
                git_fetch_tags=["git", "fetch", "--tags"],
                git_tag_sort=["git", "tag", "--sort=-creatordate"],
                git_diff_command=["git", "diff"],
            )

            diff, latest, previous = generator.get_git_diff()
            assert diff is None
            assert latest is None
            assert previous is None


class TestGitRepositoryOperations:
    """Test Git repository operations with temporary repositories."""

    def setup_method(self):
        self.tmpdir = tempfile.mkdtemp()
        self.repo_path = Path(self.tmpdir)

        subprocess.run(["git", "init"], cwd=self.repo_path, capture_output=True, check=True)
        subprocess.run(
            ["git", "config", "user.name", "Test User"],
            cwd=self.repo_path,
            capture_output=True,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.email", "test@example.com"],
            cwd=self.repo_path,
            capture_output=True,
            check=True,
        )

    def teardown_method(self):
        if os.path.exists(self.tmpdir):
            force_rmtree(self.tmpdir)

    def test_create_initial_commit(self):
        test_file = self.repo_path / "test.txt"
        test_file.write_text("Initial content", encoding="utf-8")

        subprocess.run(["git", "add", "test.txt"], cwd=self.repo_path, capture_output=True, check=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            cwd=self.repo_path,
            capture_output=True,
            check=True,
        )

        output = subprocess.run(
            ["git", "log", "--oneline"],
            cwd=self.repo_path,
            capture_output=True,
            text=True,
            check=True,
        )
        assert "Initial commit" in output.stdout

    def test_get_current_branch(self):
        test_file = self.repo_path / "test.txt"
        test_file.write_text("content", encoding="utf-8")
        subprocess.run(["git", "add", "test.txt"], cwd=self.repo_path, capture_output=True, check=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            cwd=self.repo_path,
            capture_output=True,
            check=True,
        )

        output = run_command(
            ["git", "branch", "--show-current"],
            cwd=str(self.repo_path),
            preview=False,
        )
        assert output in {"main", "master"}

    def test_count_commits(self):
        for index in range(3):
            test_file = self.repo_path / f"file{index}.txt"
            test_file.write_text(f"content {index}", encoding="utf-8")
            subprocess.run(
                ["git", "add", f"file{index}.txt"],
                cwd=self.repo_path,
                capture_output=True,
                check=True,
            )
            subprocess.run(
                ["git", "commit", "-m", f"Commit {index}"],
                cwd=self.repo_path,
                capture_output=True,
                check=True,
            )

        output = run_command(
            ["git", "rev-list", "--count", "HEAD"],
            cwd=str(self.repo_path),
            preview=False,
        )
        assert int(output) == 3

    def test_git_diff_generator_with_tags(self):
        test_file = self.repo_path / "test.txt"
        test_file.write_text("Initial content", encoding="utf-8")
        subprocess.run(["git", "add", "test.txt"], cwd=self.repo_path, capture_output=True, check=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            cwd=self.repo_path,
            capture_output=True,
            check=True,
        )
        subprocess.run(["git", "tag", "v1.0.0"], cwd=self.repo_path, capture_output=True, check=True)

        test_file.write_text("Modified content", encoding="utf-8")
        subprocess.run(["git", "add", "test.txt"], cwd=self.repo_path, capture_output=True, check=True)
        subprocess.run(
            ["git", "commit", "-m", "Second commit"],
            cwd=self.repo_path,
            capture_output=True,
            check=True,
        )
        subprocess.run(["git", "tag", "v1.1.0"], cwd=self.repo_path, capture_output=True, check=True)

        generator = GitDiffGenerator(
            repo_path=str(self.repo_path),
            git_fetch_tags=["git", "fetch", "--tags"],
            git_tag_sort=["git", "tag", "--sort=-creatordate"],
            git_diff_command=["git", "diff"],
        )

        diff, latest, previous = generator.get_git_diff()

        assert diff is not None
        assert {latest, previous} == {"v1.0.0", "v1.1.0"}
        assert "Modified content" in diff or "Initial content" in diff

    def test_git_diff_generator_insufficient_tags(self):
        test_file = self.repo_path / "test.txt"
        test_file.write_text("Initial content", encoding="utf-8")
        subprocess.run(["git", "add", "test.txt"], cwd=self.repo_path, capture_output=True, check=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            cwd=self.repo_path,
            capture_output=True,
            check=True,
        )
        subprocess.run(["git", "tag", "v1.0.0"], cwd=self.repo_path, capture_output=True, check=True)

        generator = GitDiffGenerator(
            repo_path=str(self.repo_path),
            git_fetch_tags=["git", "fetch", "--tags"],
            git_tag_sort=["git", "tag", "--sort=-creatordate"],
            git_diff_command=["git", "diff"],
        )

        diff, latest, previous = generator.get_git_diff()
        assert diff is None
        assert latest is None
        assert previous is None

    def test_git_diff_generator_no_tags(self):
        test_file = self.repo_path / "test.txt"
        test_file.write_text("Initial content", encoding="utf-8")
        subprocess.run(["git", "add", "test.txt"], cwd=self.repo_path, capture_output=True, check=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            cwd=self.repo_path,
            capture_output=True,
            check=True,
        )

        generator = GitDiffGenerator(
            repo_path=str(self.repo_path),
            git_fetch_tags=["git", "fetch", "--tags"],
            git_tag_sort=["git", "tag", "--sort=-creatordate"],
            git_diff_command=["git", "diff"],
        )

        diff, latest, previous = generator.get_git_diff()
        assert diff is None
        assert latest is None
        assert previous is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
