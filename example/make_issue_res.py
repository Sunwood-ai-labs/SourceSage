import json
import os

# open_issues_filtered.jsonを読み込む
with open("SourceSageAssets\\open_issues_filtered.json", "r", encoding="utf-8") as f:
    issues = json.load(f)

# SourceSage.mdを読み込む
with open("SourceSageAssets\\SourceSage.md", "r", encoding="utf-8") as f:
    sourcesage_md = f.read()

# テンプレートを読み込む
with open("docs\\ISSUES_RESOLVE\\ISSUES_RESOLVE_TEMPLATE.md", "r", encoding="utf-8") as f:
    template = f.read()

# 各issueに対してマークダウンファイルを作成
for issue in issues:
    number = issue["number"]
    title = issue["title"]
    body = issue["body"]

    # テンプレートの変数を置換
    content = template.replace("{{number}}", str(number))
    content = content.replace("{{title}}", title)
    content = content.replace("{{body}}", body or "")
    content = content.replace("{{sourcesage_md}}", sourcesage_md)

    # マークダウンファイルを保存
    filename = f"docs\\ISSUES_RESOLVE\\ISSUE_{number}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Issue {number}のマークダウンファイルを作成しました。")

print("全てのissueのマークダウンファイルを作成しました。")