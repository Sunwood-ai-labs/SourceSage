import json
import os
from git import Repo

class StagedDiffGenerator:
    def __init__(self, repo_path, output_dir, language_map_file):
        self.repo_path = repo_path
        self.output_dir = output_dir
        self.output_file = os.path.join(output_dir, "STAGED_DIFF.md")
        self.language_map_file = language_map_file
        self.repo = Repo(repo_path)
        self.language_map = self.load_language_map()

    def load_language_map(self):
        with open(self.language_map_file, "r", encoding="utf-8") as lang_file:
            return json.load(lang_file)

    def generate_staged_diff(self):
        previous_commit = self.repo.head.commit
        staged_diff = previous_commit.diff(None, create_patch=True)

        os.makedirs(self.output_dir, exist_ok=True)  # フォルダが存在しない場合は作成

        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write("# Staged Files Diff\n\n")
            for diff_item in staged_diff:
                self.write_file_diff(file, diff_item, previous_commit)

    def write_file_diff(self, file, diff_item, previous_commit):
        file_path = diff_item.a_path or diff_item.b_path
        if file_path:
            _, extension = os.path.splitext(file_path)
            language = self.language_map.get(extension, "bash")
            file.write(f"## {file_path}\n\n")

            try:
                self.write_diff_content(file, diff_item, previous_commit, language, file_path)
            except Exception as e:
                file.write(f"- 内容の取得に失敗しました: {e}\n")
        else:
            file.write("- 有効なファイルパスが見つかりませんでした。\n\n")

    def write_diff_content(self, file, diff_item, previous_commit, language, file_path):
        try:
            if diff_item.new_file:
                blob = self.repo.git.show(f":{file_path}")
                content = self.escape_code_block(blob, language)
                file.write(f"### 追加された内容:\n\n{content}\n\n")
            elif diff_item.deleted_file:
                blob = self.repo.git.show(f"{previous_commit.hexsha}:{file_path}")
                content = self.escape_code_block(blob, language)
                file.write(f"### 削除された内容:\n\n{content}\n\n")
            else:
                diff_content = diff_item.diff.decode('utf-8')
                diff_content_escaped = self.escape_code_block(diff_content, 'diff')
                file.write(f"### 差分:\n\n{diff_content_escaped}\n\n")
        except Exception as e:
            file.write(f"- 内容の取得に失敗しました: {e}\n")

    def escape_code_block(self, content, language):
        # マークダウンのコードブロックをエスケープする
        if '```' in content:
            # 入れ子のコードブロックに対処
            fenced_code_block = f"````{language}\n{content}\n````"
        else:
            fenced_code_block = f"```{language}\n{content}\n```"
        return fenced_code_block

if __name__ == "__main__":
    diff_generator = StagedDiffGenerator(
        repo_path="./",
        output_dir="SourceSageAssets",
        language_map_file="config/language_map.json"
    )
    diff_generator.generate_staged_diff()