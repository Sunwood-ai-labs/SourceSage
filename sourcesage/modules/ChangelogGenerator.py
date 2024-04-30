# modules/ChangelogGenerator.py (変更後)

import os
from git import Repo
from .ChangelogUtils import ChangelogUtils
from loguru import logger
from git.exc import GitCommandError

import sys

class ChangelogGenerator:
    def __init__(self, repo_path, output_dir):
        self.repo_path = repo_path
        self.output_dir = output_dir
        self.repo = self._get_repo()

    def _get_repo(self):
        return Repo(self.repo_path)

    def _get_commits(self, branch):
        return list(self.repo.iter_commits(branch))

    def generate_changelog(self, branch, output_file):
        try:
            commits = self._get_commits(branch)
        except GitCommandError:
            logger.warning(f"Skipping branch '{branch}' as it does not exist.")
            return

        # 出力ファイルのディレクトリを確認し、存在しない場合は作成
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Changelog\n\n")
            f.write(f"## {branch}\n\n")

            for commit in commits:
                formatted_commit = ChangelogUtils.format_commit(commit)
                f.write(formatted_commit + "\n")

        logger.info(f"Changelog generated successfully for branch '{branch}' at {output_file}")

    def generate_changelog_for_all_branches(self):
        local_branches = [ref.name for ref in self.repo.branches]
        remote_branches = [ref.name for ref in self.repo.remote().refs]

        branches = local_branches + remote_branches
        logger.info(branches)

        feature_branches = [branch for branch in branches if 'feature/' in branch]
        other_branches = [branch for branch in branches if 'feature/' not in branch]

        for branch in other_branches:
            branch_name = branch.replace('origin/', '')
            output_file = os.path.join(self.output_dir, f"CHANGELOG_{branch_name}.md").replace("release/", "release_").replace("bugfix/", "bugfix_")
            logger.info(f"Generating changelog for branch '{branch_name}'...")
            self.generate_changelog(branch_name, output_file)

        if feature_branches:
            output_file = os.path.join(self.output_dir, "CHANGELOG_features.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# Changelog - Features\n\n")
                for branch in feature_branches:
                    branch_name = branch.replace('origin/', '')
                    try:
                        commits = self._get_commits(branch)
                    except GitCommandError:
                        logger.warning(f"Skipping feature branch '{branch_name}' as it does not exist.")
                        continue

                    f.write(f"## {branch_name}\n\n")
                    for commit in commits:
                        formatted_commit = ChangelogUtils.format_commit(commit)
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