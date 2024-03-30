from git import Repo

# リポジトリのパスを指定してRepoオブジェクトを作成
repo = Repo("./")

# 最新のコミットから指定された数のコミットを取得して表示
num_commits_to_display = 5  # 表示したいコミットの数
commits = list(repo.iter_commits('develop', max_count=num_commits_to_display + 1))  # 1つ多く取得する

with open("SourceSageAseets/CHANGELOG_Diff.md", "w", encoding="utf-8") as file:
    for i in range(min(num_commits_to_display, len(commits) - 1)):  # 存在するコミット数と要求された数を考慮
        commit = commits[i]
        formatted_message = commit.message.replace('\n', '\n    ')
        file.write(f"### コミットハッシュ: {commit.hexsha[:5]}...\n\n")
        # file.write(f"- **作者**: {commit.author.name} <{commit.author.email}>\n")
        file.write(f"- **作者**: {commit.author.name}\n")
        file.write(f"- **日時**: {commit.authored_datetime}\n")
        file.write(f"- **メッセージ**: \n\n    {formatted_message}\n\n")
        file.write("#### 変更されたファイル:\n\n")

        previous_commit = commits[i + 1]  # 直前のコミットを取得
        diff = previous_commit.diff(commit, create_patch=True)
        for diff_item in diff:
            file_path = diff_item.a_path or diff_item.b_path  # a_pathがNoneであればb_pathを使用
            if file_path:  # ファイルパスがNoneではないことを確認
                file.write(f"- {file_path}\n")
                
                if diff_item.new_file:
                    file.write("    - 新しく追加されたファイルです。\n")
                    try:
                        blob = repo.git.show(f"{commit.hexsha}:{file_path}")
                        file.write(f"    - **追加された内容:**\n\n```\n{blob}\n```\n\n")
                    except Exception as e:
                        file.write(f"    - ファイル内容の取得に失敗しました: {e}\n")
                elif diff_item.deleted_file:
                    file.write("    - 削除されたファイルです。\n")
                    try:
                        blob = repo.git.show(f"{previous_commit.hexsha}:{file_path}")
                        file.write(f"    - **削除された内容:**\n\n```\n{blob}\n```\n\n")
                    except Exception as e:
                        file.write(f"    - ファイル内容の取得に失敗しました: {e}\n")
                else:
                    # 変更されたファイルの差分を表示
                    try:
                        diff_content = diff_item.diff.decode('utf-8')
                        file.write(f"    - **差分:**\n\n```diff\n{diff_content}\n```\n\n")
                    except Exception as e:
                        file.write(f"    - 差分の表示に失敗しました: {e}\n")
            else:
                file.write("    - 有効なファイルパスが見つかりませんでした。\n\n")
        file.write("\n---\n\n")
