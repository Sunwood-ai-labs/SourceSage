import requests
import json
import os

# GitHubリポジトリの設定
owner = "Sunwood-ai-labs"
repository = "SourceSage"
save_path = "SourceSageAssets"  # 保存先のディレクトリパス
file_name = "open_issues_filtered.json"  # 保存するファイル名
file_name_full = "open_issues_full.json"  # 保存するファイル名

# GitHub APIのURLを構築（開いているIssueを全て取得する）
api_url = f'https://api.github.com/repos/{owner}/{repository}/issues?state=open'

# APIリクエストを実行し、結果を取得
response = requests.get(api_url)
issues = response.json()

# 必要なデータのみを抽出
filtered_issues = [
    {"number": issue["number"], "title": issue["title"], "body": issue["body"]}
    for issue in issues
    if "pull_request" not in issue  # Pull Requestは除外
]

# 保存先のディレクトリが存在するか確認し、存在しない場合は作成
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 取得したIssueデータをJSON形式で保存
with open(os.path.join(save_path, file_name), 'w', encoding='utf-8') as f:
    json.dump(filtered_issues, f, ensure_ascii=False, indent=4)

# 取得したIssueデータをJSON形式で保存
with open(os.path.join(save_path, file_name_full), 'w', encoding='utf-8') as f:
    json.dump(issues, f, ensure_ascii=False, indent=4)

print(f'Filtered open issues saved to {os.path.join(save_path, file_name)}')
