import json
from git import Repo
import os

# 言語マッピングを読み込む
with open("config/language_map.json", "r", encoding="utf-8") as lang_file:
    language_map = json.load(lang_file)

# リポジトリのパスを指定してRepoオブジェクトを作成
repo = Repo("./")

# 最新のコミットから指定された数のコミットを取得して表示
num_commits_to_display = 5
commits = list(repo.iter_commits('develop', max_count=num_commits_to_display + 1))

with open("SourceSageAseets/CHANGELOG_Diff.md", "w", encoding="utf-8") as file:
    for i in range(min(num_commits_to_display, len(commits) - 1)):
        commit = commits[i]
        formatted_message = commit.message.replace('\n', '\n    ')
        file.write(f"### コミットハッシュ: {commit.hexsha[:5]}...\n\n")
        file.write(f"- **作者**: {commit.author.name}\n")
        file.write(f"- **日時**: {commit.authored_datetime}\n")
        file.write(f"- **メッセージ**: \n\n    {formatted_message}\n\n")
        file.write("#### 変更されたファイル:\n\n")

        previous_commit = commits[i + 1]
        diff = previous_commit.diff(commit, create_patch=True)
        for diff_item in diff:
            file_path = diff_item.a_path or diff_item.b_path
            if file_path:
                # ファイル拡張子またはファイル名から言語を決定
                _, extension = os.path.splitext(file_path)
                language = language_map.get(extension, "bash")  # マッピングになければplaintextを使用
                file.write(f"- {file_path}\n")
                
                # 追加された内容、削除された内容、または差分の表示
                try:
                    if diff_item.new_file or diff_item.deleted_file:
                        blob = repo.git.show(f"{commit.hexsha if diff_item.new_file else previous_commit.hexsha}:{file_path}")
                        file.write(f"    - **{'追加された内容' if diff_item.new_file else '削除された内容'}:**\n\n```{language}\n{blob}\n```\n\n")
                    else:
                        diff_content = diff_item.diff.decode('utf-8')
                        file.write(f"    - **差分:**\n\n```diff\n{diff_content}\n```\n\n")
                except Exception as e:
                    file.write(f"    - 内容の取得に失敗しました: {e}\n")
            else:
                file.write("    - 有効なファイルパスが見つかりませんでした。\n\n")
        file.write("\n---\n\n")
