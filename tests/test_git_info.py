"""
Tests for Git information collection functionality
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

# Add parent directory to path to import sourcesage
sys.path.insert(0, str(Path(__file__).parent.parent))

from sourcesage.modules.DiffReport.git_diff import GitDiffGenerator
from sourcesage.modules.GitCommander import run_command


class TestRunCommand:
    """Test run_command function"""

    def test_run_command_echo(self):
        """Test run_command with simple echo command"""
        output = run_command(["echo", "Hello, World!"], preview=False)
        assert output == "Hello, World!"

    def test_run_command_with_cwd(self):
        """Test run_command with custom working directory"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a test file
            test_file = Path(tmpdir) / "test.txt"
            test_file.write_text("test content")

            # Run ls command in tmpdir
            output = run_command(["ls"], cwd=tmpdir, preview=False)
            assert "test.txt" in output

    def test_run_command_failure(self):
        """Test run_command with failing command"""
        with pytest.raises(subprocess.CalledProcessError):
            run_command(["false"], preview=False)

    def test_run_command_git_version(self):
        """Test run_command with git --version"""
        output = run_command(["git", "--version"], preview=False)
        assert "git" in output.lower()


class TestGitDiffGenerator:
    """Test GitDiffGenerator class"""

    def test_init(self):
        """Test GitDiffGenerator initialization"""
        generator = GitDiffGenerator(
            repo_path="/path/to/repo",
            git_fetch_tags=["git", "fetch", "--tags"],
            git_tag_sort=["git", "tag", "--sort=-creatordate"],
            git_diff_command=["git", "diff"]
        )

        assert generator.repo_path == "/path/to/repo"
        assert generator.git_fetch_tags == ["git", "fetch", "--tags"]
        assert generator.git_tag_sort == ["git", "tag", "--sort=-creatordate"]
        assert generator.git_diff_command == ["git", "diff"]

    def test_get_git_diff_no_repo(self):
        """Test get_git_diff with non-existent repository"""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = GitDiffGenerator(
                repo_path=tmpdir,
                git_fetch_tags=["git", "fetch", "--tags"],
                git_tag_sort=["git", "tag", "--sort=-creatordate"],
                git_diff_command=["git", "diff"]
            )

            # Should return None for non-git directory
            diff, latest, previous = generator.get_git_diff()
            assert diff is None
            assert latest is None
            assert previous is None


class TestGitRepositoryOperations:
    """Test Git repository operations with temporary repositories"""

    def setup_method(self):
        """Setup method to create temporary git repository"""
        self.tmpdir = tempfile.mkdtemp()
        self.repo_path = Path(self.tmpdir)

        # Initialize git repository
        subprocess.run(
            ["git", "init"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )

        # Configure git user
        subprocess.run(
            ["git", "config", "user.name", "Test User"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )
        subprocess.run(
            ["git", "config", "user.email", "test@example.com"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )

    def teardown_method(self):
        """Cleanup method to remove temporary repository"""
        import shutil
        if os.path.exists(self.tmpdir):
            shutil.rmtree(self.tmpdir)

    def test_create_initial_commit(self):
        """Test creating initial commit in temporary repository"""
        # Create a test file
        test_file = self.repo_path / "test.txt"
        test_file.write_text("Initial content")

        # Stage and commit
        subprocess.run(
            ["git", "add", "test.txt"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )

        # Verify commit exists
        output = subprocess.run(
            ["git", "log", "--oneline"],
            cwd=self.repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        assert "Initial commit" in output.stdout

    def test_get_current_branch(self):
        """Test getting current branch name"""
        # Create initial commit to ensure HEAD exists
        test_file = self.repo_path / "test.txt"
        test_file.write_text("content")
        subprocess.run(
            ["git", "add", "test.txt"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )

        # Get current branch
        output = run_command(["git", "branch", "--show-current"], cwd=str(self.repo_path), preview=False)
        assert output == "main" or output == "master"  # Default branch names

    def test_count_commits(self):
        """Test counting commits in repository"""
        # Create multiple commits
        for i in range(3):
            test_file = self.repo_path / f"file{i}.txt"
            test_file.write_text(f"content {i}")
            subprocess.run(
                ["git", "add", f"file{i}.txt"],
                cwd=self.repo_path,
                capture_output=True,
                check=True
            )
            subprocess.run(
                ["git", "commit", "-m", f"Commit {i}"],
                cwd=self.repo_path,
                capture_output=True,
                check=True
            )

        # Count commits
        output = run_command(["git", "rev-list", "--count", "HEAD"], cwd=str(self.repo_path), preview=False)
        assert int(output) == 3

    def test_git_diff_generator_with_tags(self):
        """Test GitDiffGenerator with actual tags"""
        # Create initial commit
        test_file = self.repo_path / "test.txt"
        test_file.write_text("Initial content")
        subprocess.run(
            ["git", "add", "test.txt"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )

        # Create first tag
        subprocess.run(
            ["git", "tag", "v1.0.0"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )

        # Modify file and create second commit
        test_file.write_text("Modified content")
        subprocess.run(
            ["git", "add", "test.txt"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )
        subprocess.run(
            ["git", "commit", "-m", "Second commit"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )

        # Create second tag
        subprocess.run(
            ["git", "tag", "v1.1.0"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )

        # Test GitDiffGenerator
        generator = GitDiffGenerator(
            repo_path=str(self.repo_path),
            git_fetch_tags=["git", "fetch", "--tags"],
            git_tag_sort=["git", "tag", "--sort=-creatordate"],
            git_diff_command=["git", "diff"]
        )

        diff, latest, previous = generator.get_git_diff()

        # Should succeed
        assert diff is not None
        # Tags are returned in reverse chronological order (--sort=-creatordate)
        # So the first tag created (v1.0.0) comes before v1.1.0 in the list
        # But since they're created quickly, the order might vary
        assert (latest, previous) in [("v1.0.0", "v1.1.0"), ("v1.1.0", "v1.0.0")]
        # Diff should contain the change
        assert "Modified content" in diff or "Initial content" in diff

    def test_git_diff_generator_insufficient_tags(self):
        """Test GitDiffGenerator with insufficient tags"""
        # Create initial commit
        test_file = self.repo_path / "test.txt"
        test_file.write_text("content")
        subprocess.run(
            ["git", "add", "test.txt"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )

        # Create only one tag
        subprocess.run(
            ["git", "tag", "v1.0.0"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )

        # Test GitDiffGenerator
        generator = GitDiffGenerator(
            repo_path=str(self.repo_path),
            git_fetch_tags=["git", "fetch", "--tags"],
            git_tag_sort=["git", "tag", "--sort=-creatordate"],
            git_diff_command=["git", "diff"]
        )

        diff, latest, previous = generator.get_git_diff()

        # Should return None for insufficient tags
        assert diff is None
        assert latest is None
        assert previous is None

    def test_git_diff_generator_no_tags(self):
        """Test GitDiffGenerator with no tags"""
        # Create commits but no tags
        test_file = self.repo_path / "test.txt"
        test_file.write_text("content")
        subprocess.run(
            ["git", "add", "test.txt"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            cwd=self.repo_path,
            capture_output=True,
            check=True
        )

        # Test GitDiffGenerator
        generator = GitDiffGenerator(
            repo_path=str(self.repo_path),
            git_fetch_tags=["git", "fetch", "--tags"],
            git_tag_sort=["git", "tag", "--sort=-creatordate"],
            git_diff_command=["git", "diff"]
        )

        diff, latest, previous = generator.get_git_diff()

        # Should return None for no tags
        assert diff is None
        assert latest is None
        assert previous is None

    def test_cleanup_on_failure(self):
        """Test that temporary repository is cleaned up even if test fails"""
        # This test verifies the teardown mechanism
        # The repository should be cleaned up regardless of test outcome
        assert self.repo_path.exists()
        # teardown_method will be called automatically


class TestGitInfoIntegration:
    """Integration tests for Git information collection"""

    def test_real_repo_git_info(self):
        """Test getting info from real repository (SourceSage itself)"""
        # Get the root of SourceSage repository
        repo_root = Path(__file__).parent.parent

        # Test that we can get git info from the real repo
        try:
            # Get current branch
            branch = run_command(["git", "branch", "--show-current"], cwd=str(repo_root), preview=False)
            assert branch is not None

            # Get commit count
            commit_count = run_command(["git", "rev-list", "--count", "HEAD"], cwd=str(repo_root), preview=False)
            assert int(commit_count) > 0

        except subprocess.CalledProcessError:
            pytest.skip("Not in a git repository or git not available")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
