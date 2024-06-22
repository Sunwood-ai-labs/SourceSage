# sourcesage\modules\ChangelogGenerator.py

import os
try:
    from .ChangelogUtils import ChangelogUtils
    from .GitCommander import run_command
except ImportError:
    from sourcesage.modules.ChangelogUtils import ChangelogUtils
    from sourcesage.modules.GitCommander import run_command
    
from loguru import logger
from git.exc import GitCommandError

from art import *
import sys

import subprocess

from tqdm import tqdm

class ChangelogGenerator:
    def __init__(self, repo_path, output_dir, start_tag=None, end_tag=None):
        self.repo_path = repo_path
        self.output_dir = output_dir
        self.start_tag = start_tag
        self.end_tag = end_tag
        
        tprint("ChangelogGenerator")
        logger.info(f"リポジトリパス: {self.repo_path}")
        logger.info(f"出力ディレクトリ: {self.output_dir}")
        logger.info(f"開始タグ: {self.start_tag}")
        logger.info(f"終了タグ: {self.end_tag}")

    def _get_commits(self, branch):
        commits_output = run_command(["git", "log", "--pretty=format:%H", branch])
        commit_hashes = commits_output.split("\n")
        return commit_hashes

    def generate_changelog(self, branch, output_file):
        if self.start_tag and self.end_tag:
            start_tag = self.start_tag
            end_tag = self.end_tag
        else:
            tags_output = run_command(["git", "tag", "--sort=-creatordate"], cwd=self.repo_path)
            tags = tags_output.split("\n")

            if len(tags) >= 2:
                start_tag = tags[1]
                end_tag = tags[0]
            else:
                logger.warning("タグが2つ未満のため、最新のタグと1つ前のタグを取得できません。")
                return

        try:
            run_command(["git", "show-ref", "--verify", f"refs/tags/{start_tag}"], cwd=self.repo_path)
            run_command(["git", "show-ref", "--verify", f"refs/tags/{end_tag}"], cwd=self.repo_path)
        except subprocess.CalledProcessError:
            logger.error(f"指定されたタグが見つかりません: {start_tag} または {end_tag}")
            return

        logger.info(f"変更履歴の生成範囲: {start_tag} から {end_tag}")

        commits_output = run_command(["git", "log", "--pretty=format:%H", f"{start_tag}..{end_tag}"], cwd=self.repo_path)
        commits = commits_output.split("\n")

        logger.info(f"コミット数: {len(commits)}")

        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# 変更履歴\n\n")
            f.write(f"## {branch} ({start_tag}..{end_tag})\n\n")

            for commit_hash in tqdm(commits, desc="コミットの処理中"):
                commit_details = run_command(["git", "show", "--pretty=format:%an%n%ad%n%s%n%b", "--date=iso", "--no-patch", commit_hash], preview=False)

                commit_info = commit_details.split("\n", 3)
                author = commit_info[0]
                date = commit_info[1]
                subject = commit_info[2]
                body = commit_info[3] if len(commit_info) > 3 else ""
                
                if subject.startswith("Merge"):
                    continue  # "Merge"で始まるコミットメッセージをスキップ
                
                formatted_commit = f"### [{commit_hash[:7]}] - {subject}\n\n"
                formatted_commit += f"  - 作者: {author}\n"
                formatted_commit += f"  - 日時: {date}\n"
                
                body_lines = body.split("\n")
                filtered_body = "\n".join("\t\t" + line for line in body_lines if not line.startswith("diff --git"))
                formatted_commit += f"  - 詳細:\n{filtered_body}\n\n"
                
                diff_output = run_command(["git", "show", commit_hash], preview=False)
                diff_lines = diff_output.split("\n")
                diff_section = "  - 差分:\n\n```diff\n"
                for line in diff_lines:
                    if line.startswith("+") or line.startswith("-") or line.startswith("@"):
                        diff_section += f"{line}\n"
                diff_section += "```\n\n"
                
                formatted_commit += diff_section
                
                if "release" in branch:
                    if "Merge branch" in formatted_commit and "release/" in formatted_commit:
                        break  # ループを中断
                        
                f.write(formatted_commit + "---\n")

        logger.success(f"ブランチ '{branch}' の変更履歴が {output_file} に生成されました。")
        
    def generate_changelog_for_all_branches(self):
        branches_output = run_command(["git", "branch"])
        branches = [branch.strip().replace("*", "").replace("remotes/", "").replace("origin/", "") for branch in branches_output.split("\n") if branch.strip()]
        
        logger.info("ブランチ一覧:")
        for branch in branches:
            logger.info(f"- {branch}")

        feature_branches = [branch for branch in branches if 'feature/' in branch]
        other_branches = [branch for branch in branches if 'feature/' not in branch]

        logger.info("変更履歴の生成を開始します...")

        for _branch_name in other_branches:
            branch_name = _branch_name.replace(" ", "")
            output_file = os.path.join(self.output_dir, f"CHANGELOG_{branch_name}.md").replace("release/", "release_").replace("bugfix/", "bugfix_")
            logger.info(f"ブランチ '{branch_name}' の変更履歴を生成しています...")
            self.generate_changelog(branch_name, output_file)

        if feature_branches:
            output_file = os.path.join(self.output_dir, "CHANGELOG_features.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# 機能ブランチの変更履歴\n\n")
                for branch_name in feature_branches:
                    branch_name = branch_name.replace('origin/', '').replace('remotes/', '')
                    f.write(f"## {branch_name}\n\n")
                    self.generate_changelog(branch_name, output_file)
                    f.write("\n")
            logger.success(f"機能ブランチの変更履歴が {output_file} に生成されました。")
            
    def integrate_changelogs(self):
        
        # CHANGELOG_integrated.mdファイルが存在する場合は削除
        integrated_changelog_path = os.path.join(self.output_dir, "CHANGELOG_integrated.md")
        if os.path.exists(integrated_changelog_path):
            os.remove(integrated_changelog_path)
            logger.info(f"既存の {integrated_changelog_path} ファイルを削除しました。")
        os.makedirs(self.output_dir, exist_ok=True)
            
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

        with open(integrated_changelog_path, 'w', encoding='utf-8') as f:
            f.write(integrated_changelog)

        logger.success(f"統合された変更履歴が {integrated_changelog_path} に生成されました。")


if __name__ == "__main__":
    
    from loguru import logger
    import sys

    logger.level("SUBPROCESS", no=15, color="<cyan>", icon="🔍")
    
    repo_path = "./"
    output_dir = "docs/Changelog"
    os.makedirs(output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    logger.add("changelog_generator.log", rotation="1 MB", retention="10 days")

    generator = ChangelogGenerator(repo_path, output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()