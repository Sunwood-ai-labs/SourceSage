# sourcesage\modules\ChangelogGenerator.py

import os
from .ChangelogUtils import ChangelogUtils
from loguru import logger
from .GitCommander import run_command

from git.exc import GitCommandError

from art import *
import sys

from tqdm import tqdm
class ChangelogGenerator:
    def __init__(self, repo_path, output_dir):
        self.repo_path = repo_path
        self.output_dir = output_dir
        
        tprint("ChangelogGenerator")
        logger.debug(f"repo_path : {self.repo_path}")
        logger.debug(f"output_dir : {self.output_dir}")

    def _get_commits(self, branch):
        # GitCommanderのrun_commandを使ってコミットを取得
        commits_output = run_command(["git", "log", "--pretty=format:%H", branch])
        commit_hashes = commits_output.split("\n")
        return commit_hashes

    def generate_changelog(self, branch, output_file):
        logger.debug(f"--------------------------------------------")
        logger.debug(f"branch : [{branch}]")
        commits = self._get_commits(branch)
        
        logger.info(f"コミットの数:{len(commits)}")
        # 出力ファイルのディレクトリを確認し、存在しない場合は作成
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# 変更履歴\n\n")
            f.write(f"## {branch}\n\n")

            for commit_hash in tqdm(commits):
                # GitCommanderのrun_commandを使ってコミットの詳細を取得
                # commit_details = run_command(["git", "show", "--pretty=format:%an%n%ad%n%s%n%b", "--date=iso", commit_hash])
                commit_details = run_command(["git", "show", "--pretty=format:%an%n%ad%n%s%n%b", "--date=iso", "--no-patch", commit_hash], preview=False)
                # commit_details = run_command(["git", "show", "--pretty=format:%an%n%ad%n%s%n%b", "--date=iso", commit_hash], preview=False)
                # print(commit_details)

                commit_info = commit_details.split("\n", 3)
                author = commit_info[0]
                date = commit_info[1]
                subject = commit_info[2]
                body = commit_info[3] if len(commit_info) > 3 else ""
                
                formatted_commit = f"### [{commit_hash[:7]}] - {subject}\n\n"
                formatted_commit += f"  - 作者: {author}\n"
                formatted_commit += f"  - 日時: {date}\n"
                
                # 差分情報を除外して詳細情報を取得
                body_lines = body.split("\n")
                filtered_body = "\n".join("\t\t" + line for line in body_lines if not line.startswith("diff --git"))
                formatted_commit += f"  - 詳細:\n{filtered_body}\n\n"
                
                # 差分情報を取得
                diff_output = run_command(["git", "show", commit_hash], preview=False)
                diff_lines = diff_output.split("\n")
                diff_section = "  - 差分:\n\n```diff\n"
                for line in diff_lines:
                    if line.startswith("+") or line.startswith("-") or line.startswith("@"):
                        diff_section += f"{line}\n"
                diff_section += "```\n\n"
                
                formatted_commit += diff_section
                
                # for commit_msg in formatted_commit.split("\n"):
                #     logger.debug(commit_msg)
                
                if "release" in branch:
                    if "Merge branch" in formatted_commit and "release/" in formatted_commit:
                        break  # ループを中断
                f.write(formatted_commit + "---\n")

        logger.info(f"ブランチ '{branch}' の変更履歴が {output_file} に正常に生成されました。")
        
    def generate_changelog_for_all_branches(self):
        # GitCommanderのrun_commandを使ってブランチ一覧を取得
        branches_output = run_command(["git", "branch"])
        branches = [branch.strip().replace("*", "").replace("remotes/", "").replace("origin/", "") for branch in branches_output.split("\n") if branch.strip()]
        
        logger.debug("------ branches list ------")
        for ibranches in branches:
            logger.debug(ibranches)

        feature_branches = [branch for branch in branches if 'feature/' in branch]
        other_branches = [branch for branch in branches if 'feature/' not in branch]

        for _branch_name in other_branches:
            branch_name = _branch_name.replace(" ", "")
            # branch_name = branch_name.replace("[HEAD->main]", "main")
            output_file = os.path.join(self.output_dir, f"CHANGELOG_{branch_name}.md").replace("release/", "release_").replace("bugfix/", "bugfix_")
            logger.info(f"ブランチ '{branch_name}' の変更履歴を生成しています...")
            self.generate_changelog(branch_name, output_file)
            logger.info(f"生成しました... '{output_file}'")

        if feature_branches:
            output_file = os.path.join(self.output_dir, "CHANGELOG_features.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# 機能ブランチの変更履歴\n\n")
                for branch_name in feature_branches:
                    branch_name = branch_name.replace('origin/', '').replace('remotes/', '')
                    f.write(f"## {branch_name}\n\n")
                    self.generate_changelog(branch_name, output_file)
                    f.write("\n")
            logger.info(f"機能ブランチの変更履歴が {output_file} に正常に生成されました。")
            
    def integrate_changelogs(self):
        changelog_files = [file for file in os.listdir(self.output_dir) if file.startswith("CHANGELOG_")]
        integrated_changelog = "# 統合された変更履歴\n\n"

        for file in changelog_files:
            file_path = os.path.join(self.output_dir, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    integrated_changelog += f"{content}\n\n"
            except UnicodeDecodeError as e:
                logger.warning(f"ファイル '{file_path}' のデコードエラーをスキップします: {str(e)}")

        output_file = os.path.join(self.output_dir, "CHANGELOG_integrated.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(integrated_changelog)

        logger.info(f"統合された変更履歴が {output_file} に正常に生成されました。")


if __name__ == "__main__":
    repo_path = "./"
    output_dir = "docs/Changelog"
    os.makedirs(output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    logger.add("changelog_generator.log", rotation="1 MB", retention="10 days")

    generator = ChangelogGenerator(repo_path, output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()