import os
from git import Repo
from datetime import datetime
from loguru import logger

class ChangelogGenerator:
    def __init__(self, repo_path, output_dir):
        self.repo_path = repo_path
        self.output_dir = output_dir
        self.repo = self._get_repo()

    def _get_repo(self):
        return Repo(self.repo_path)

    def _get_commits(self, branch):
        return list(self.repo.iter_commits(branch))

    def _format_commit(self, commit):
        message = commit.message.strip()
        sha = commit.hexsha[:7]
        author = commit.author.name
        date = datetime.fromtimestamp(commit.committed_date).strftime("%Y-%m-%d")
        return f"- [{sha}] - {message} ({author}, {date})"

    def generate_changelog(self, branch, output_file):
        commits = self._get_commits(branch)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Changelog\n\n")
            f.write(f"## {branch}\n\n")

            for commit in commits:
                formatted_commit = self._format_commit(commit)
                f.write(formatted_commit + "\n")

        logger.info(f"Changelog generated successfully for branch '{branch}' at {output_file}")

    def generate_changelog_for_all_branches(self):
        local_branches = [ref.name for ref in self.repo.branches]
        remote_branches = [ref.name for ref in self.repo.remote().refs]

        branches = local_branches + remote_branches
        print(branches)

        feature_branches = [branch for branch in branches if 'feature/' in branch]
        other_branches = [branch for branch in branches if 'feature/' not in branch]

        for branch in other_branches:
            branch_name = branch.replace('origin/', '')
            output_file = os.path.join(self.output_dir, f"CHANGELOG_{branch_name}.md")
            logger.info(f"Generating changelog for branch '{branch_name}'...")
            self.generate_changelog(branch_name, output_file)

        if feature_branches:
            output_file = os.path.join(self.output_dir, "CHANGELOG_features.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# Changelog - Features\n\n")
                for branch in feature_branches:
                    branch_name = branch.replace('origin/', '')
                    f.write(f"## {branch_name}\n\n")
                    commits = self._get_commits(branch)
                    for commit in commits:
                        formatted_commit = self._format_commit(commit)
                        f.write(formatted_commit + "\n")
                    f.write("\n")
            logger.info(f"Changelog generated successfully for feature branches at {output_file}")

    def integrate_changelogs(self):
        changelog_files = [file for file in os.listdir(self.output_dir) if file.startswith("CHANGELOG_")]
        integrated_changelog = "# Integrated Changelog\n\n"

        for file in changelog_files:
            with open(os.path.join(self.output_dir, file), 'r', encoding='utf-8') as f:
                content = f.read()
                integrated_changelog += f"{content}\n\n"

        output_file = os.path.join(self.output_dir, "CHANGELOG_integrated.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(integrated_changelog)

        logger.info(f"Integrated changelog generated successfully at {output_file}")


if __name__ == "__main__":
    repo_path = "./"
    output_dir = "docs/Changelog"
    os.makedirs(output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    logger.add("changelog_generator.log", rotation="1 MB", retention="10 days")

    generator = ChangelogGenerator(repo_path, output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()