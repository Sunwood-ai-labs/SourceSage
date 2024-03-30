import json
import os
from git import Repo

class RepositoryChangelogGenerator:
    def __init__(self, repo_path, changelog_dir, language_map_file):
        self.repo_path = repo_path
        self.changelog_dir = changelog_dir
        self.changelog_file = os.path.join(changelog_dir, "CHANGELOG_Diff.md")  # チェンジログのファイル名を含めたパス
        self.language_map_file = language_map_file
        self.repo = Repo(repo_path)
        self.language_map = self.load_language_map()

    def load_language_map(self):
        with open(self.language_map_file, "r", encoding="utf-8") as lang_file:
            return json.load(lang_file)

    def generate_changelog(self, branch='main', num_commits=2):
        self.ensure_directory_exists(self.changelog_dir)
        commits = list(self.repo.iter_commits(branch, max_count=num_commits + 1))

        with open(self.changelog_file, "w", encoding="utf-8") as file:
            # Git ログのツリー表示を追加
            git_tree = self.generate_git_tree(branch, num_commits)
            file.write(git_tree + "\n\n")

            for i in range(min(num_commits, len(commits) - 1)):
                self.write_commit_details(file, commits, i)

    def generate_git_tree(self, branch, num_commits):
        # ツリー表示用のテキストを生成
        tree_text = "```\n"
        tree_text += "Git Commit Log Tree:\n"
        commits = list(self.repo.iter_commits(branch, max_count=num_commits))
        for i, commit in enumerate(commits, start=1):
            if i == len(commits):  # 最後のコミット
                prefix = "└──"
            else:
                prefix = "├──"
            tree_text += f"{prefix} {commit.hexsha[:7]} - {commit.summary}\n"
        tree_text += "```\n"
        return tree_text

    def ensure_directory_exists(self, path):
        os.makedirs(path, exist_ok=True)

    def write_commit_details(self, file, commits, index):
        commit = commits[index]
        formatted_message = commit.message.replace('\n', '\n    ')
        file.write(f"### コミットハッシュ: {commit.hexsha[:5]}...\n\n")
        file.write(f"- **作者**: {commit.author.name}\n")
        file.write(f"- **日時**: {commit.authored_datetime}\n")
        file.write(f"- **メッセージ**: \n\n    {formatted_message}\n\n")
        self.write_changed_files(file, commits, index)

    def write_changed_files(self, file, commits, index):
        commit = commits[index]
        previous_commit = commits[index + 1]
        diff = previous_commit.diff(commit, create_patch=True)
        file.write("#### 変更されたファイル:\n\n")

        for diff_item in diff:
            self.write_file_diff(file, diff_item, commit, previous_commit)

    def write_file_diff(self, file, diff_item, commit, previous_commit):
        file_path = diff_item.a_path or diff_item.b_path
        if file_path:
            _, extension = os.path.splitext(file_path)
            language = self.language_map.get(extension, "bash")
            file.write(f"- {file_path}\n")

            try:
                self.write_diff_content(file, diff_item, commit, previous_commit, language, file_path)
            except Exception as e:
                file.write(f"    - 内容の取得に失敗しました: {e}\n")
        else:
            file.write("    - 有効なファイルパスが見つかりませんでした。\n\n")

    def write_diff_content(self, file, diff_item, commit, previous_commit, language, file_path):
        try:
            if diff_item.new_file or diff_item.deleted_file:
                blob = self.repo.git.show(f"{commit.hexsha if diff_item.new_file else previous_commit.hexsha}:{file_path}")
                content = self.escape_code_block(blob, language)
                action = '追加された内容' if diff_item.new_file else '削除された内容'
                file.write(f"    - **{action}:**\n\n{content}\n\n")
            else:
                diff_content = diff_item.diff.decode('utf-8')
                diff_content_escaped = self.escape_code_block(diff_content, 'diff')
                file.write(f"    - **差分:**\n\n{diff_content_escaped}\n\n")
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
