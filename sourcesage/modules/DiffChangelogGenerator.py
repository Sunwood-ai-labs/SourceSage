# modules/DiffChangelogGenerator.py (変更後)

import json
import os
from .ChangelogUtils import ChangelogUtils
from loguru import logger
from .GitCommander import run_command
from art import *

class RepositoryChangelogGenerator:
    def __init__(self, repo_path, changelog_dir, language_map_file):
        self.repo_path = repo_path
        self.changelog_dir = changelog_dir
        self.changelog_file = os.path.join(changelog_dir, "CHANGELOG_Diff.md")  # チェンジログのファイル名を含めたパス
        self.language_map_file = language_map_file
        self.language_map = self.load_language_map()
        tprint("RepositoryChangelogGenerator")
        logger.info(f"repo_path : {self.repo_path}")
        logger.info(f"changelog_dir : {self.changelog_dir}")
        logger.info(f"language_map_file : {self.language_map_file}")
        
        
    def load_language_map(self):
        with open(self.language_map_file, "r", encoding="utf-8") as lang_file:
            return json.load(lang_file)

    def generate_changelog(self, branch='main', num_commits=2):
        self.ensure_directory_exists(self.changelog_dir)
        
        # GitCommanderのrun_commandを使ってコミットを取得
        commits_output = run_command(["git", "log", "--pretty=format:%H", "-n", str(num_commits + 1), branch])
        commit_hashes = commits_output.split("\n")

        with open(self.changelog_file, "w", encoding="utf-8") as file:
            # Git ログのツリー表示を追加
            git_tree = self.generate_git_tree(branch, num_commits)
            file.write(git_tree + "\n\n")

            for i in range(min(num_commits, len(commit_hashes) - 1)):
                self.write_commit_details(file, commit_hashes, i)
                self.write_changed_files(file, commit_hashes, i)

    def ensure_directory_exists(self, path):
        os.makedirs(path, exist_ok=True)

    def generate_git_tree(self, branch, num_commits):
        # GitCommanderのrun_commandを使ってGitのコミットツリーを取得
        tree_output = run_command(["git", "log", "--graph", "--pretty=format:%s", "--abbrev-commit", "-n", str(num_commits), branch])
        return f"```\nGit Commit Log Tree:\n{tree_output}\n```"

    def write_commit_details(self, file, commit_hashes, index):
        commit_hash = commit_hashes[index]
        
        # GitCommanderのrun_commandを使ってコミットの詳細を取得
        commit_details = run_command(["git", "show", "--pretty=format:%an%n%ad%n%s%n%b", "--date=iso", commit_hash])
        author, date, subject, body = commit_details.split("\n", 3)
        
        file.write(f"### コミットハッシュ: {commit_hash[:5]}...\n\n")
        file.write(f"- **作者**: {author}\n")
        file.write(f"- **日時**: {date}\n")
        file.write(f"- **メッセージ**: \n\n    {subject}\n\n    {body}\n\n")

    def write_changed_files(self, file, commit_hashes, index):
        commit_hash = commit_hashes[index]
        previous_commit_hash = commit_hashes[index + 1]
        
        # GitCommanderのrun_commandを使ってdiffを取得
        diff_output = run_command(["git", "diff", "--name-status", "--diff-filter=d", f"{previous_commit_hash}..{commit_hash}"])
        changed_files = diff_output.split("\n")
        
        file.write("#### 変更されたファイル:\n\n")

        for changed_file in changed_files:
            if changed_file:
                status, file_path = changed_file.split("\t", 1)
                self.write_file_diff(file, status, file_path, commit_hash, previous_commit_hash)

    def write_file_diff(self, file, status, file_path, commit_hash, previous_commit_hash):
        _, extension = os.path.splitext(file_path)
        language = self.language_map.get(extension, "bash")
        file.write(f"- {file_path}\n")

        try:
            self.write_diff_content(file, status, file_path, commit_hash, previous_commit_hash, language)
        except Exception as e:
            file.write(f"    - 内容の取得に失敗しました: {e}\n")

    def write_diff_content(self, file, status, file_path, commit_hash, previous_commit_hash, language):
        try:
            if status == 'A':  # 追加されたファイル
                # GitCommanderのrun_commandを使ってファイル内容を取得
                blob = run_command(["git", "show", f"{commit_hash}:{file_path}"])
                content = self.escape_code_block(blob, language)
                file.write(f"    - 追加された内容:\n\n{content}\n\n")
            elif status == 'D':  # 削除されたファイル
                # GitCommanderのrun_commandを使ってファイル内容を取得
                blob = run_command(["git", "show", f"{previous_commit_hash}:{file_path}"])
                content = self.escape_code_block(blob, language)
                file.write(f"    - 削除された内容:\n\n{content}\n\n")
            else:  # 変更されたファイル
                # GitCommanderのrun_commandを使ってdiffを取得
                diff_content = run_command(["git", "diff", f"{previous_commit_hash}..{commit_hash}", "--", file_path])
                diff_content_escaped = self.escape_code_block(diff_content, 'diff')
                file.write(f"    - 差分:\n\n{diff_content_escaped}\n\n")
        except Exception as e:
            file.write(f"    - 内容の取得に失敗しました: {e}\n")

    def escape_code_block(self, content, language):
        # マークダウンのコードブロックをエスケープする
        if '```' in content:
            # 入れ子のコードブロックに対処
            fenced_code_block = f"````{language}\n{content}\n````"
        else:
            fenced_code_block = f"```{language}\n{content}\n```"
        return fenced_code_block

if __name__ == "__main__":
    changelog_generator = RepositoryChangelogGenerator(
        repo_path="./",
        changelog_dir="SourceSageAssets",
        language_map_file="config/language_map.json"
    )
    changelog_generator.generate_changelog(branch='main', num_commits=10)