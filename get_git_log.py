from git import Repo
from datetime import datetime

class ChangelogGenerator:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = self._get_repo()

    def _get_repo(self):
        return Repo(self.repo_path)

    def _get_commits(self):
        return list(self.repo.iter_commits())

    def _format_commit(self, commit):
        message = commit.message.strip()
        sha = commit.hexsha[:7]
        author = commit.author.name
        date = datetime.fromtimestamp(commit.committed_date).strftime("%Y-%m-%d")
        return f"- [{sha}] - {message} ({author}, {date})"

    def generate_changelog(self, branch='master', output_file='CHANGELOG.md'):
        commits = self._get_commits()

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Changelog\n\n")
            f.write(f"## {branch}\n\n")

            for commit in commits:
                formatted_commit = self._format_commit(commit)
                f.write(formatted_commit + "\n")

        print(f"Changelog generated successfully at {output_file}")


repo_path = "./"
generator = ChangelogGenerator(repo_path)
generator.generate_changelog()