
下記のissueについてリポジトリ情報を参照して修正して

# ISSUE 7 : READMEの更新と生成物のリンクの対応

- リポジトリ全体の変更に合わせてREADMEの大幅変更
- SourceSage.py の生成物に合わせて生成物へのリンクをREADMEに記載


下記の内容を盛り込んで、必要に応じて内容を修正して

```
開発前

課題の確認とAIによる自動修正

- GitHubのオープンなissueを取得し、JSONファイルに保存する
- SourceSage.pyを使用して現在のプロジェクトのソースコードとファイル構成を1つのマークダウンファイル(SourceSageAssetsDemo\ISSUES_RESOLVE\ISSUE_7.md)に統合する
- issueデータとSourceSage.pyで生成したマークダウンをClaude AIに入力する
- AIがissueの内容を理解し、現在のソースコードを分析して自動的にissueの修正を提案する
- 提案された修正内容を確認し、必要に応じて手動で調整を行う

開発中

ステージされた変更の確認とコミットメッセージの自動生成

- StagedDiffGeneratorクラスを使用してステージされた差分を取得し、マークダウンファイルに出力する
- ステージされた変更とissueの情報をAIに入力し、適切なコミットメッセージを生成する
- get_issues.pyで取得したissueデータとStagedDiffGeneratorで生成したマークダウン（SourceSageAssetsDemo\STAGED_DIFF.md）をClaude AIに入力する
- AIが既存のissueを考慮してコミットメッセージを自動生成する


リリース後

プロジェクトの統合とドキュメント化

- SourceSage.pyを使用してプロジェクト全体のソースコードとファイル構成をAIが理解しやすい形式で統合する
- プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイル（SourceSageAssetsDemo\SourceSage.md）にまとめる
- 不要なファイルやディレクトリを除外するための設定が可能
- 複数のプログラミング言語に対応し、シンタックスハイライト機能を提供
- Gitの変更履歴を自動生成し、ドキュメント化する
- ブランチごとに変更履歴をマークダウンファイルに出力する
- すべてのブランチの変更履歴を1つのファイルに統合する
```


## 補足事項

修正に対するコミットメッセージは日本語にして
正確にstep-by-stepで処理して
issueの番号も記載して

コミットメッセージは下記のフォーマットにして

## フォーマット

```markdown

[種類] 概要

詳細な説明（必要に応じて）

```

種類は下記を参考にして

例：
  - feat: 新機能
  - fix: バグ修正
  - docs: ドキュメントのみの変更
  - style: コードの動作に影響しない変更（空白、フォーマット、セミコロンの欠落など） 
  - refactor: バグの修正も機能の追加も行わないコードの変更
  - perf: パフォーマンスを向上させるコードの変更
  - test: 欠けているテストの追加や既存のテストの修正
  - chore: ビルドプロセスやドキュメント生成などの補助ツールやライブラリの変更



# リポジトリ情報

# Project: SourceSage

```plaintext
OS: nt
Directory: C:\Prj\SourceSage

├─ config/
│  ├─ language_map.json
├─ demo/
│  ├─ get_diff.py
│  ├─ get_issues.py
│  ├─ make_issue_res.py
├─ docs/
│  ├─ css/
│  │  ├─ style.css
│  ├─ Diff_Changelog/
│  ├─ HTML/
│  │  ├─ timeline_sample.md
│  ├─ icon/
│  ├─ ISSUES_RESOLVE/
│  │  ├─ ISSUES_RESOLVE_TEMPLATE.md
│  ├─ STAGE_INFO/
│  │  ├─ STAGE_INFO_AND_ISSUES_TEMPLATE.md
│  │  ├─ STAGE_INFO_TEMPLATE.md
├─ modules/
│  ├─ ChangelogGenerator.py
│  ├─ ChangelogUtils.py
│  ├─ DiffChangelogGenerator.py
│  ├─ EnvFileHandler.py
│  ├─ file_utils.py
│  ├─ GitHubIssueRetrieve.py
│  ├─ GitHubUtils.py
│  ├─ IssuesToMarkdown.py
│  ├─ markdown_utils.py
│  ├─ source_sage.py
│  ├─ StagedDiffGenerator.py
│  ├─ StageInfoGenerator.py
│  ├─ __init__.py
├─ README.md
├─ SourceSage.py
```

## .

`.env`

```plaintext
REPO_PATH=./
SOURCE_SAGE_ASSETS_DIR=SourceSageAssets
CONFIG_DIR=config
DOCS_DIR=docs
FOLDERS=./
IGNORE_FILE=.SourceSageignore
OUTPUT_FILE=SourceSage.md
LANGUAGE_MAP_FILE=config/language_map.json
ISSUE_LOG_DIR=ISSUE_LOG

OWNER=Sunwood-ai-labs
REPOSITORY=SourceSage
ISSUES_FILE_NAME=open_issues_filtered.json

ISSUES_RESOLVE_DIR=ISSUES_RESOLVE
STAGE_INFO_DIR=STAGE_INFO
```

`.env.example`

```plaintext
REPO_PATH=./
SOURCE_SAGE_ASSETS_DIR=SourceSageAssets
CONFIG_DIR=config
DOCS_DIR=docs
FOLDERS=./
IGNORE_FILE=.SourceSageignore
OUTPUT_FILE=SourceSageAssets/SourceSage.md
LANGUAGE_MAP_FILE=config/language_map.json

OWNER=Sunwood-ai-labs
REPOSITORY=SourceSage
ISSUES_FILE_NAME=open_issues_filtered.json
```

`README.md`

```plaintext
<p align="center">

<img src="docs/icon/SourceSage_icon4.png" width="100%">

<br>

<h1 align="center">SourceSage</h1>

<h2 align="center">～Transforming code for AI～</h2>

</p>

SourceSageは、プロジェクトのソースコードとファイル構成を単一のマークダウンファイルに統合するPythonスクリプトです。これにより、大規模言語モデル（AI）がプロジェクト全体の構造と内容を容易に理解できるようになります。




## 更新内容

- [【2024/03/30】 SourceSage 2.0.0 ](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/tag2.0.0)
  - ChangelogGenerator classを導入し、コードの可読性と保守性を向上
  - 言語ごとのシンタックスハイライト機能を追加
  - 対象フォルダの指定やファイルの除外設定を複数行対応
  - コード生成時のエラー処理を改善
  - 設定ファイルの場所を外部化し、柔軟性を向上
  - .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外
- 【2024/03/29】 初期リリース

## 特徴

- プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイルにまとめます
- AIがプロジェクトの概要を素早く把握できる構造化された形式で出力します
- 不要なファイルやディレクトリを除外する設定が可能です
- プロジェクトの全体像を明確かつ読みやすい方法で提示します
- 複数のプログラミング言語に対応し、シンタックスハイライト機能を提供します
- 設定ファイルを外部化することで、柔軟性と保守性を向上させています
- Gitの変更履歴を自動生成し、ドキュメント化することができます

## 主な使い方


<div class="cp_timeline04">
 <div class="timeline_item">
   <div class="time_date">
     <p class="time">開発前</p>
     <p class="flag">課題の確認とAIによる自動修正</p>
   </div>
   <div class="desc">
     <p>
       - <code>get_issues.py</code>を使用してGitHubのオープンなissueを取得し、JSONファイルに保存する<br>
       - issueの内容と現在のソースコードの情報をClaude AIに入力し、自動でissueの修正を行う<br>
         - <code>SourceSage.py</code>を使用して現在のプロジェクトのソースコードとファイル構成を1つのマークダウンファイルに統合する<br>
         - <code>get_issues.py</code>で取得したissueデータと<code>SourceSage.py</code>で生成したマークダウンをClaude AIに入力する<br>
         - AIがissueの内容を理解し、現在のソースコードを分析して自動的にissueの修正を提案する<br>
         - 提案された修正内容を確認し、必要に応じて手動で調整を行う
     </p>
   </div>
 </div>

 <div class="timeline_item">
   <div class="time_date">
     <p class="time">開発中</p>
     <p class="flag">ステージされた変更の確認とコミットメッセージの自動生成</p>
   </div>
   <div class="desc">
     <p>
       - <code>StagedDiffGenerator</code>クラスを使用してステージされた差分を取得し、マークダウンファイルに出力する<br>
       - ステージされた変更とissueの情報をAIに入力し、適切なコミットメッセージを生成する<br>
         - <code>get_issues.py</code>で取得したissueデータと<code>StagedDiffGenerator</code>で生成したマークダウンをClaude AIに入力する<br>
         - AIが既存のissueを考慮してコミットメッセージを自動生成する<br>
     </p>
   </div>
 </div>

 <div class="timeline_item">
   <div class="time_date">
     <p class="time">リリース後</p>
     <p class="flag">プロジェクトの統合とドキュメント化</p>
   </div>
   <div class="desc">
     <p>
       - <code>SourceSage.py</code>を使用してプロジェクト全体のソースコードとファイル構成をAIが理解しやすい形式で統合する<br>
         - プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイルにまとめる<br>
         - 不要なファイルやディレクトリを除外するための設定が可能<br>
         - 複数のプログラミング言語に対応し、シンタックスハイライト機能を提供<br>
       - Gitの変更履歴を自動生成し、ドキュメント化する<br>
         - ブランチごとに変更履歴をマークダウンファイルに出力する<br>
         - すべてのブランチの変更履歴を1つのファイルに統合する<br>
     </p>
   </div>
 </div>
</div>

## 使用方法

プロジェクトでSourceSageを使用するには、次の手順に従います：

1. `SourceSage.py`ファイルと`modules`フォルダを、分析対象のプロジェクトのルートディレクトリにコピーします。

2. 必要に応じて、`.SourceSageignore`ファイルを作成し、除外したいファイルやフォルダのパターンを記述します。

3. `config/language_map.json`ファイルを編集し、必要なプログラミング言語とそれに対応するシンタックスハイライトの識別子を設定します。

4. 必要に応じて、`SourceSage.py`内の以下の設定を変更します：

```python
folders = ['./'] # 分析対象のディレクトリ（現在のディレクトリを指定）
ignore_file = '.SourceSageignore' # 無視するファイル/フォルダのパターンを記述したファイル
output_file = 'docs/SourceSage.md' # 出力するマークダウンファイル名
language_map_file = 'config/language_map.json' # 言語マッピングの設定ファイル
```

5. ターミナルまたはコマンドプロンプトで、プロジェクトのルートディレクトリに移動し、以下のコマンドを実行します：

```bash
python SourceSage.py
```

これにより、AIがプロジェクトの構造と内容を理解しやすい形式のマークダウンファイル（デフォルトでは `docs/SourceSage.md`）が生成されます。また、Gitの変更履歴が`docs/Changelog`ディレクトリに自動生成されます。

## 出力例

生成される[マークダウンファイル(docs/SourceSage.md)](docs/SourceSage.md)の例は次のようになります：

````markdown
# Project: YourProjectName

```plaintext
OS: nt
Directory: C:\Prj\YourProjectName

├─ src/
│  ├─ main.py
│  ├─ utils/
│  │  ├─ helper.py
│  │  └─ constants.py
│  └─ tests/
│     └─ test_main.py
├─ docs/
│  └─ README.md
├─ .gitignore
└─ README.md
```

## src

### main.py

```python
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```

### utils

#### helper.py

```python
def greet(name):
    return f"Hello, {name}!"
```

#### constants.py

```python 
PI = 3.14159
```

...

## docs

### README.md

```markdown
# YourProjectName Documentation

This is the documentation for YourProjectName.

...
```
````

## 変更履歴の統合

SourceSageは、Gitリポジトリの変更履歴を自動的に生成し、ブランチごとに[マークダウンファイルに出力(docs/Changelog)](docs/Changelog)します。さらに、[すべてのブランチの変更履歴を1つのファイルに統合する(docs/Changelog/CHANGELOG_integrated.md)](docs/Changelog/CHANGELOG_integrated.md)ことができます。

生成される変更履歴の例は次のようになります：

````markdown
# Integrated Changelog

# Changelog

## develop

- [f26fca5] - Merge branch 'feature/modules' into develop (John Doe, 2023-03-30)
- [36d6a4a] - Refactor SourceSage.py to use modules (John Doe, 2023-03-30)
- [60ccecb] - Update SourceSage.md (John Doe, 2023-03-30)
- [6796a56] - Create language_map.json (John Doe, 2023-03-30)
- [d6e1af6] - Delete language_map.json (John Doe, 2023-03-30)

...

# Changelog - Features

## feature/add-git-logs

- [c346a22] - Introduce ChangelogGenerator class for improved readability and maintainability (Jane Smith, 2023-03-30)
- [0344765] - Update CHANGELOG.md (Jane Smith, 2023-03-30)
- [5c5e6ac] - Create get_git_log.py (Jane Smith, 2023-03-30)
- [8d4a253] - Create CHANGELOG.md (Jane Smith, 2023-03-30)

...
````

## 貢献

SourceSageの改善にご協力ください！バグの報告や機能追加の提案がある場合は、[GitHubリポジトリ](https://github.com/yourusername/SourceSage)でIssueを開くかプルリクエストを送信してください。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

---
```

`SourceSage.py`

```plaintext
import os
import sys
from modules.EnvFileHandler import create_or_append_env_file
from modules.source_sage import SourceSage
from modules.ChangelogGenerator import ChangelogGenerator
from modules.StageInfoGenerator import StageInfoGenerator
from modules.GitHubIssueRetrieve import GitHubIssueRetriever
from modules.StagedDiffGenerator import StagedDiffGenerator
from modules.IssuesToMarkdown import IssuesToMarkdown

create_or_append_env_file()  # .envファイルがない場合は作成、ある場合は追記

try:
    from dotenv import load_dotenv
    # .envファイルから環境変数を読み込む
    load_dotenv()
except ImportError:
    pass


if __name__ == "__main__":
    repo_path = os.getenv("REPO_PATH")
    source_sage_assets_dir = os.path.join(repo_path, os.getenv("SOURCE_SAGE_ASSETS_DIR"))
    config_dir = os.path.join(repo_path, os.getenv("CONFIG_DIR"))
    docs_dir = os.path.join(repo_path, os.getenv("DOCS_DIR"))
    issue_log_dir = os.path.join(source_sage_assets_dir, os.getenv("ISSUE_LOG_DIR"))
    issues_resolve_dir = os.path.join(source_sage_assets_dir, os.getenv("ISSUES_RESOLVE_DIR"))
    stage_info_dir = os.path.join(source_sage_assets_dir, os.getenv("STAGE_INFO_DIR"))

    os.makedirs(issue_log_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する
    os.makedirs(issues_resolve_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する
    os.makedirs(stage_info_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    folders = [os.path.join(repo_path, folder) for folder in os.getenv("FOLDERS").split(",")]  # カンマ区切りの文字列をリストに変換
    source_sage = SourceSage(folders, ignore_file=os.path.join(config_dir, os.getenv("IGNORE_FILE")),
                             output_file=os.path.join(source_sage_assets_dir, os.getenv("OUTPUT_FILE")),
                             language_map_file=os.path.join(config_dir, os.getenv("LANGUAGE_MAP_FILE")))
    source_sage.generate_markdown()

    changelog_output_dir = os.path.join(source_sage_assets_dir, "Changelog")
    os.makedirs(changelog_output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    generator = ChangelogGenerator(repo_path, changelog_output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()

    owner = os.getenv("OWNER")
    repository = os.getenv("REPOSITORY")
    issues_file_name = os.getenv("ISSUES_FILE_NAME")

    issue_retriever = GitHubIssueRetriever(owner, repository, issue_log_dir, issues_file_name)
    issue_retriever.run()

    diff_generator = StagedDiffGenerator(
        repo_path=repo_path,
        output_dir=source_sage_assets_dir,
        language_map_file=os.path.join(config_dir, "language_map.json")
    )
    diff_generator.run()

    stage_info_generator = StageInfoGenerator(
        issue_file_path=os.path.join(issue_log_dir, issues_file_name),
        stage_diff_file_path=os.path.join(source_sage_assets_dir, "STAGED_DIFF.md"),
        template_file_path=os.path.join(docs_dir, os.getenv("STAGE_INFO_DIR"), "STAGE_INFO_AND_ISSUES_TEMPLATE.md"),
        output_file_path=os.path.join(stage_info_dir, "STAGE_INFO_AND_ISSUES_AND_PROMT.md")
    )
    stage_info_generator.run()

    stage_info_generator = StageInfoGenerator(
        issue_file_path=os.path.join(issue_log_dir, issues_file_name),
        stage_diff_file_path=os.path.join(source_sage_assets_dir, "STAGED_DIFF.md"),
        template_file_path=os.path.join(docs_dir, os.getenv("STAGE_INFO_DIR"), "STAGE_INFO_TEMPLATE.md"),
        output_file_path=os.path.join(stage_info_dir, "STAGE_INFO_AND_PROMT.md")
    )
    stage_info_generator.run()

    converter = IssuesToMarkdown(
        issues_file=os.path.join(issue_log_dir, issues_file_name),
        sourcesage_file=os.path.join(source_sage_assets_dir, "SourceSage.md"),
        template_file=os.path.join(docs_dir, os.getenv("ISSUES_RESOLVE_DIR"), "ISSUES_RESOLVE_TEMPLATE.md"),
        output_folder=issues_resolve_dir
    )
    converter.load_data()
    converter.create_markdown_files()
```

## .vscode

`.vscode\settings.json`

```plaintext
{
    "gitlens.ai.experimental.openai.url": "",
    "gitlens.ai.experimental.provider": "anthropic",
    "gitlens.ai.experimental.anthropic.model": "claude-3-haiku-20240307",
    "gitlens.experimental.generateCommitMessagePrompt": "日本語でシンプルなコミットメッセージ"
}
```

## config

`config\language_map.json`

```plaintext
{
    ".py": "python",
    ".js": "javascript",
    ".java": "java",
    ".c": "c",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".go": "go",
    ".php": "php",
    ".rb": "ruby",
    ".rs": "rust",
    ".ts": "typescript",
    ".html": "html",
    ".css": "css",
    ".json": "json",
    ".xml": "xml",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".md": "markdown",
    ".txt": "plaintext",
    ".sh": "bash",
    ".sql": "sql",
    "Dockerfile": "dockerfile",
    ".dockerfile": "dockerfile",
    "docker-compose.yml": "yaml",
    "docker-compose.yaml": "yaml"
}
```

## demo

`demo\get_diff.py`

```plaintext
import git

# 現在のリポジトリのパスを指定
repo_path = './'

try:
    # リポジトリオブジェクトの初期化
    repo = git.Repo(repo_path)
    print(repo)

    # インデックス（ステージングエリア）にある変更を取得
    diff = repo.index.diff('HEAD')
    print(diff)
    # 差分を表示
    for diff_item in diff:
        print(f'差分があるファイル: {diff_item.a_path}')
        print(diff_item.diff.decode('utf-8'))
        
except Exception as e:
    print(f'エラーが発生しました: {e}')
```

`demo\get_issues.py`

```plaintext
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
```

`demo\make_issue_res.py`

```plaintext
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
```

## docs

### docs\css

`docs\css\style.css`

```plaintext
.cp_timeline04 {
    position: relative;
    margin: 3em auto;
    padding-bottom: 2em;
 }
 .cp_timeline04:before {
    position: absolute;
    top: 0px;
    left: 45px;
    width: 3px;
    height: 100%;
    content: '';
    background: #6588A6;
 }
 .cp_timeline04 .timeline_item {
    margin: 0px 0px 0px 80px;
 }
 .cp_timeline04 .timeline_item .time_date .time {
    font-family: serif;
    font-size: 6em;
    font-weight: bold;
    position: relative;
    margin: 0;
    letter-spacing: 3px;
    color: rgba(156,162,166,0.5);
 }
 .cp_timeline04 .timeline_item .time_date .time:before {
    position: absolute;
    top: 50%;
    left: -42px;
    width: 10px;
    height: 10px;
    content: '';
    -webkit-transform: rotate(45deg);
            transform: rotate(45deg);
    border: 3px solid #6588A6;
    background: #fff;
 }
 .cp_timeline04 .timeline_item .time_date .flag {
    font-size: 1.5em;
    font-weight: bold;
    margin: 0;
    margin-top: -60px;
    color: #6588A6;
 }
 .cp_timeline04 .timeline_item .desc {
    font-size: 1em;
    line-height: 20px;
    margin-top: 10px;
    padding-left: 20px;
    border-left: 5px solid #D0D7D9;
 }
 @media only screen and (max-width: 767px) {
    .cp_timeline04:before {
        left: 15px;
    }
    .cp_timeline04 .timeline_item .time_date .time:before {
        left: -32px;
    }
    .cp_timeline04 .timeline_item {
        margin: 0px 0px 0px 40px;
    }
    .cp_timeline04 .timeline_item .desc {
        padding-left: 0px;
        border-top: 1px solid #6588A6;
        border-left: none;
    }
 }
```

### docs\Diff_Changelog

### docs\HTML

`docs\HTML\timeline_sample.md`

```plaintext
<style>
.cp_timeline04 {
   position: relative;
   margin: 3em auto;
   padding-bottom: 2em;
}
.cp_timeline04:before {
   position: absolute;
   top: 0px;
   left: 45px;
   width: 3px;
   height: 100%;
   content: '';
   background: #6588A6;
}
.cp_timeline04 .timeline_item {
   margin: 0px 0px 0px 80px;
}
.cp_timeline04 .timeline_item .time_date .time {
   font-family: serif;
   font-size: 6em;
   font-weight: bold;
   position: relative;
   margin: 0;
   letter-spacing: 3px;
   color: rgba(156,162,166,0.5);
}
.cp_timeline04 .timeline_item .time_date .time:before {
   position: absolute;
   top: 50%;
   left: -42px;
   width: 10px;
   height: 10px;
   content: '';
   -webkit-transform: rotate(45deg);
           transform: rotate(45deg);
   border: 3px solid #6588A6;
   background: #fff;
}
.cp_timeline04 .timeline_item .time_date .flag {
   font-size: 1.5em;
   font-weight: bold;
   margin: 0;
   margin-top: -60px;
   color: #6588A6;
}
.cp_timeline04 .timeline_item .desc {
   font-size: 1em;
   line-height: 20px;
   margin-top: 10px;
   padding-left: 20px;
   border-left: 5px solid #D0D7D9;
}
@media only screen and (max-width: 767px) {
   .cp_timeline04:before {
   	left: 15px;
   }
   .cp_timeline04 .timeline_item .time_date .time:before {
   	left: -32px;
   }
   .cp_timeline04 .timeline_item {
   	margin: 0px 0px 0px 40px;
   }
   .cp_timeline04 .timeline_item .desc {
   	padding-left: 0px;
   	border-top: 1px solid #6588A6;
   	border-left: none;
   }
}
</style>

<div class="cp_timeline04">
 <div class="timeline_item">
   <div class="time_date">
     <p class="time">開発前</p>
     <p class="flag">課題の確認とAIによる自動修正</p>
   </div>
   <div class="desc">
     <p>
       - <code>get_issues.py</code>を使用してGitHubのオープンなissueを取得し、JSONファイルに保存する<br>
       - issueの内容と現在のソースコードの情報をClaude AIに入力し、自動でissueの修正を行う<br>
         - <code>SourceSage.py</code>を使用して現在のプロジェクトのソースコードとファイル構成を1つのマークダウンファイルに統合する<br>
         - <code>get_issues.py</code>で取得したissueデータと<code>SourceSage.py</code>で生成したマークダウンをClaude AIに入力する<br>
         - AIがissueの内容を理解し、現在のソースコードを分析して自動的にissueの修正を提案する<br>
         - 提案された修正内容を確認し、必要に応じて手動で調整を行う
     </p>
   </div>
 </div>

 <div class="timeline_item">
   <div class="time_date">
     <p class="time">開発中</p>
     <p class="flag">ステージされた変更の確認とコミットメッセージの自動生成</p>
   </div>
   <div class="desc">
     <p>
       - <code>StagedDiffGenerator</code>クラスを使用してステージされた差分を取得し、マークダウンファイルに出力する<br>
       - ステージされた変更とissueの情報をAIに入力し、適切なコミットメッセージを生成する<br>
         - <code>get_issues.py</code>で取得したissueデータと<code>StagedDiffGenerator</code>で生成したマークダウンをClaude AIに入力する<br>
         - AIが既存のissueを考慮してコミットメッセージを自動生成する<br>
     </p>
   </div>
 </div>

 <div class="timeline_item">
   <div class="time_date">
     <p class="time">リリース後</p>
     <p class="flag">プロジェクトの統合とドキュメント化</p>
   </div>
   <div class="desc">
     <p>
       - <code>SourceSage.py</code>を使用してプロジェクト全体のソースコードとファイル構成をAIが理解しやすい形式で統合する<br>
         - プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイルにまとめる<br>
         - 不要なファイルやディレクトリを除外するための設定が可能<br>
         - 複数のプログラミング言語に対応し、シンタックスハイライト機能を提供<br>
       - Gitの変更履歴を自動生成し、ドキュメント化する<br>
         - ブランチごとに変更履歴をマークダウンファイルに出力する<br>
         - すべてのブランチの変更履歴を1つのファイルに統合する<br>
     </p>
   </div>
 </div>
</div>
```

### docs\icon

### docs\ISSUES_RESOLVE

`docs\ISSUES_RESOLVE\ISSUES_RESOLVE_TEMPLATE.md`

```plaintext
下記のissueについてリポジトリ情報を参照して修正して

# ISSUE {{number}} : {{title}}

{{body}}


## 補足事項

修正に対するコミットメッセージは日本語にして
正確にstep-by-stepで処理して
issueの番号も記載して

コミットメッセージは下記のフォーマットにして

## フォーマット

```markdown

[種類] 概要

詳細な説明（必要に応じて）

```

種類は下記を参考にして

例：
  - feat: 新機能
  - fix: バグ修正
  - docs: ドキュメントのみの変更
  - style: コードの動作に影響しない変更（空白、フォーマット、セミコロンの欠落など） 
  - refactor: バグの修正も機能の追加も行わないコードの変更
  - perf: パフォーマンスを向上させるコードの変更
  - test: 欠けているテストの追加や既存のテストの修正
  - chore: ビルドプロセスやドキュメント生成などの補助ツールやライブラリの変更



# リポジトリ情報

{{sourcesage_md}}
```

### docs\STAGE_INFO

`docs\STAGE_INFO\STAGE_INFO_AND_ISSUES_TEMPLATE.md`

```plaintext
下記はissuesの情報です


```json

[open_issues_filtered.json]

```

また、下記はgitはStageの情報です

issueを解決していればそれも含めてコミットメッセージを書いて
解決していないissueは掲載しないで

見やすくコミットメッセージにして
章やパラグラフ、箇条書きを多用して見やすくして

コミットメッセージは日本語にして
正確にstep-by-stepで処理して

コミットメッセージは下記のフォーマットにして

## フォーマット

```markdown

[種類] 概要

詳細な説明（必要に応じて）

```

種類は下記を参考にして

例：
  - feat: 新機能
  - fix: バグ修正
  - docs: ドキュメントのみの変更
  - style: コードの動作に影響しない変更（空白、フォーマット、セミコロンの欠落など） 
  - refactor: バグの修正も機能の追加も行わないコードの変更
  - perf: パフォーマンスを向上させるコードの変更
  - test: 欠けているテストの追加や既存のテストの修正
  - chore: ビルドプロセスやドキュメント生成などの補助ツールやライブラリの変更


## Stageの情報

```markdown
[STAGED_DIFF.md]

```
```

`docs\STAGE_INFO\STAGE_INFO_TEMPLATE.md`

```plaintext
下記はgitはStageの情報です

issueは掲載しないで

見やすくコミットメッセージにして
章やパラグラフ、箇条書きを多用して見やすくして

コミットメッセージは日本語にして
正確にstep-by-stepで処理して

コミットメッセージは下記のフォーマットにして

## フォーマット

```markdown

[種類] 概要

詳細な説明（必要に応じて）

```

種類は下記を参考にして

例：
  - feat: 新機能
  - fix: バグ修正
  - docs: ドキュメントのみの変更
  - style: コードの動作に影響しない変更（空白、フォーマット、セミコロンの欠落など） 
  - refactor: バグの修正も機能の追加も行わないコードの変更
  - perf: パフォーマンスを向上させるコードの変更
  - test: 欠けているテストの追加や既存のテストの修正
  - chore: ビルドプロセスやドキュメント生成などの補助ツールやライブラリの変更


## Stageの情報

```markdown
[STAGED_DIFF.md]

```
```

## modules

`modules\ChangelogGenerator.py`

```plaintext
# modules/ChangelogGenerator.py (変更後)

import os
from git import Repo
from modules.ChangelogUtils import ChangelogUtils
from loguru import logger

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
        commits = self._get_commits(branch)

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
        print(branches)

        feature_branches = [branch for branch in branches if 'feature/' in branch]
        other_branches = [branch for branch in branches if 'feature/' not in branch]

        for branch in other_branches:
            branch_name = branch.replace('origin/', '')
            output_file = os.path.join(self.output_dir, f"CHANGELOG_{branch_name}.md")
            logger.info(f"Generating changelog for branch '{branch_name}'...")
            self.generate_changelog(branch_name, output_file)

        if feature_branches:
            output_file = os.path.join(self.output_dir, "CHANGELOG_features.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# Changelog - Features\n\n")
                for branch in feature_branches:
                    branch_name = branch.replace('origin/', '')
                    f.write(f"## {branch_name}\n\n")
                    commits = self._get_commits(branch)
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
```

`modules\ChangelogUtils.py`

```plaintext
# modules/ChangelogUtils.py (新規作成)

from datetime import datetime

class ChangelogUtils:
    @staticmethod
    def format_commit(commit):
        message = commit.message.strip()
        sha = commit.hexsha[:7]
        author = commit.author.name
        date = datetime.fromtimestamp(commit.committed_date).strftime("%Y-%m-%d")
        return f"- [{sha}] - {message} ({author}, {date})"

    @staticmethod
    def generate_git_tree(repo, branch, num_commits):
        tree_text = "```\n"
        tree_text += "Git Commit Log Tree:\n"
        commits = list(repo.iter_commits(branch, max_count=num_commits))
        for i, commit in enumerate(commits, start=1):
            if i == len(commits):  # 最後のコミット
                prefix = "└──"
            else:
                prefix = "├──"
            tree_text += f"{prefix} {commit.hexsha[:7]} - {commit.summary}\n"
        tree_text += "```\n"
        return tree_text

    @staticmethod
    def write_commit_details(file, commits, index):
        commit = commits[index]
        formatted_message = commit.message.replace('\n', '\n    ')
        file.write(f"### コミットハッシュ: {commit.hexsha[:5]}...\n\n")
        file.write(f"- **作者**: {commit.author.name}\n")
        file.write(f"- **日時**: {commit.authored_datetime}\n")
        file.write(f"- **メッセージ**: \n\n    {formatted_message}\n\n")
```

`modules\DiffChangelogGenerator.py`

```plaintext
# modules/DiffChangelogGenerator.py (変更後)

import json
import os
from git import Repo
from modules.ChangelogUtils import ChangelogUtils

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
            git_tree = ChangelogUtils.generate_git_tree(self.repo, branch, num_commits)
            file.write(git_tree + "\n\n")

            for i in range(min(num_commits, len(commits) - 1)):
                ChangelogUtils.write_commit_details(file, commits, i)
                self.write_changed_files(file, commits, i)

    def ensure_directory_exists(self, path):
        os.makedirs(path, exist_ok=True)

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
                file.write(f"    - {action}:\n\n{content}\n\n")
                else:
                diff_content = diff_item.diff.decode('utf-8')
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

if name == "main":
    changelog_generator = RepositoryChangelogGenerator(
        repo_path="./",
        changelog_dir="SourceSageAssets",
        language_map_file="config/language_map.json"
    )
    changelog_generator.generate_changelog(branch='main', num_commits=10)
```

`modules\EnvFileHandler.py`

```plaintext
# modules/EnvFileHandler.py

import os

def create_or_append_env_file():
    env_file = ".env"
    env_vars = """REPO_PATH=./
SOURCE_SAGE_ASSETS_DIR=SourceSageAssets
CONFIG_DIR=config
DOCS_DIR=docs
FOLDERS=./
IGNORE_FILE=.SourceSageignore
OUTPUT_FILE=SourceSage.md
LANGUAGE_MAP_FILE=config/language_map.json

OWNER=Sunwood-ai-labs
REPOSITORY=SourceSage
ISSUES_FILE_NAME=open_issues_filtered.json"""

    if not os.path.exists(env_file):
        with open(env_file, "w") as f:
            f.write(env_vars)
        print(f"{env_file} created successfully.")
    else:
        with open(env_file, "r") as f:
            existing_vars = f.read()
        if not all(var in existing_vars for var in env_vars.split("\n")):
            with open(env_file, "a") as f:
                f.write("\n" + env_vars)
            print(f"{env_file} updated successfully.")
        else:
            print(f"{env_file} already contains the required variables.")
```

`modules\file_utils.py`

```plaintext
import os
import fnmatch
import json

def load_ignore_patterns(ignore_file):
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    else:
        return []

def load_language_map(language_map_file):
    if os.path.exists(language_map_file):
        with open(language_map_file, 'r') as f:
            return json.load(f)
    else:
        return {}

def is_excluded(path, exclude_patterns):
    for pattern in exclude_patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
        if fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
    return False

def is_excluded_extension(filename, exclude_patterns):
    _, extension = os.path.splitext(filename)
    return any(fnmatch.fnmatch(extension, pattern) for pattern in exclude_patterns)
```

`modules\GitHubIssueRetrieve.py`

```plaintext
# modules/GitHubIssueRetrieve.py (変更後)

from modules.GitHubUtils import GitHubUtils

class GitHubIssueRetriever:
    def __init__(self, owner, repository, save_path, file_name):
        self.owner = owner
        self.repository = repository
        self.save_path = save_path
        self.file_name = file_name

    def run(self):
        issues = GitHubUtils.retrieve_issues(self.owner, self.repository)
        filtered_issues = GitHubUtils.filter_issues(issues)
        GitHubUtils.save_issues(filtered_issues, self.save_path, self.file_name)


if __name__ == "__main__":
    owner = "Sunwood-ai-labs"
    repository = "SourceSage"
    save_path = "SourceSageAssets"
    file_name = "open_issues_filtered.json"

    retriever = GitHubIssueRetriever(owner, repository, save_path, file_name)
    retriever.run()
```

`modules\GitHubUtils.py`

```plaintext
# modules/GitHubUtils.py (新規作成)

import requests
import json
import os
from git import Repo

class GitHubUtils:
    @staticmethod
    def retrieve_issues(owner, repository):
        api_url = f'https://api.github.com/repos/{owner}/{repository}/issues?state=open'
        response = requests.get(api_url)
        issues = response.json()
        return issues

    @staticmethod
    def filter_issues(issues):
        filtered_issues = [
            {"number": issue["number"], "title": issue["title"], "body": issue["body"]}
            for issue in issues
            if "pull_request" not in issue
        ]
        return filtered_issues

    @staticmethod
    def save_issues(issues, save_path, file_name):
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        with open(os.path.join(save_path, file_name), 'w', encoding='utf-8') as f:
            json.dump(issues, f, ensure_ascii=False, indent=4)

        print(f'Filtered open issues saved to {os.path.join(save_path, file_name)}')

    @staticmethod
    def get_staged_diff(repo_path):
        repo = Repo(repo_path)
        previous_commit = repo.head.commit
        staged_diff = previous_commit.diff(None, create_patch=True)
        return staged_diff
```

`modules\IssuesToMarkdown.py`

```plaintext
import json
import os
from loguru import logger

class IssuesToMarkdown:
    def __init__(self, issues_file, sourcesage_file, template_file, output_folder):
        self.issues_file = issues_file
        self.sourcesage_file = sourcesage_file
        self.template_file = template_file
        self.output_folder = output_folder

    def load_data(self):
        logger.info("Loading data...")
        with open(self.issues_file, "r", encoding="utf-8") as f:
            self.issues = json.load(f)
        logger.info(f"Loaded {len(self.issues)} issues from {self.issues_file}")

        with open(self.sourcesage_file, "r", encoding="utf-8") as f:
            self.sourcesage_md = f.read()
        logger.info(f"Loaded SourceSage markdown from {self.sourcesage_file}")

        with open(self.template_file, "r", encoding="utf-8") as f:
            self.template = f.read()
        logger.info(f"Loaded template from {self.template_file}")

    def create_markdown_files(self):
        logger.info("Creating markdown files for issues...")
        for issue in self.issues:
            number = issue["number"]
            title = issue["title"]
            body = issue["body"]

            content = self.template.replace("{{number}}", str(number))
            content = content.replace("{{title}}", title)
            content = content.replace("{{body}}", body or "")
            content = content.replace("{{sourcesage_md}}", self.sourcesage_md)

            filename = os.path.join(self.output_folder, f"ISSUE_{number}.md")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)

            logger.info(f"Created markdown file for issue {number}")

        logger.info("Created markdown files for all issues")

if __name__ == "__main__":
    issues_file = "SourceSageAssets\\open_issues_filtered.json"
    sourcesage_file = "SourceSageAssets\\SourceSage.md"
    template_file = "docs\\ISSUES_RESOLVE\\ISSUES_RESOLVE_TEMPLATE.md"
    output_folder = "docs\\ISSUES_RESOLVE"

    converter = IssuesToMarkdown(issues_file, sourcesage_file, template_file, output_folder)
    converter.load_data()
    converter.create_markdown_files()
```

`modules\markdown_utils.py`

```plaintext
import os
from modules.file_utils import is_excluded, is_excluded_extension

def generate_markdown_for_folder(folder_path, exclude_patterns, language_map):
    markdown_content = "```plaintext\n"
    markdown_content += _display_tree(dir_path=folder_path, exclude_patterns=exclude_patterns)
    markdown_content += "\n```\n\n"
    base_level = folder_path.count(os.sep)
    for root, dirs, files in os.walk(folder_path, topdown=True):
        dirs[:] = [d for d in dirs if not is_excluded(os.path.join(root, d), exclude_patterns)]
        files = [f for f in files if not is_excluded(os.path.join(root, f), exclude_patterns) and not is_excluded_extension(f, exclude_patterns)]
        level = root.count(os.sep) - base_level + 1
        header_level = '#' * (level + 1)
        relative_path = os.path.relpath(root, folder_path)
        markdown_content += f"{header_level} {relative_path}\n\n"
        for f in files:
            file_path = os.path.join(root, f)
            relative_file_path = os.path.relpath(file_path, folder_path)
            try:
                with open(file_path, 'r', encoding='utf-8') as file_content:
                    content = file_content.read().strip()
                    language = _get_language_for_file(f, language_map)
                    markdown_content += f"`{relative_file_path}`\n\n```{language}\n{content}\n```\n\n"
            except Exception as e:
                markdown_content += f"`{relative_file_path}` - Error reading file: {e}\n\n"
    return markdown_content

def _display_tree(dir_path='.', exclude_patterns=None, string_rep=True, header=True, max_depth=None, show_hidden=False):
    tree_string = ""
    if header:
        tree_string += f"OS: {os.name}\nDirectory: {os.path.abspath(dir_path)}\n\n"
    tree_string += _build_tree_string(dir_path, max_depth, show_hidden, exclude_patterns, depth=0)
    if string_rep:
        return tree_string.strip()
    else:
        print(tree_string.strip())

def _build_tree_string(dir_path, max_depth, show_hidden, exclude_patterns, depth=0):
    tree_string = ""
    if depth == max_depth:
        return tree_string
    dir_contents = [(item, os.path.join(dir_path, item)) for item in os.listdir(dir_path)]
    dirs = [(item, path) for item, path in dir_contents if os.path.isdir(path) and not is_excluded(path, exclude_patterns)]
    files = [(item, path) for item, path in dir_contents if os.path.isfile(path) and not is_excluded(path, exclude_patterns) and not is_excluded_extension(item, exclude_patterns)]
    for item, path in dirs:
        if not show_hidden and item.startswith('.'):
            continue
        tree_string += '│  ' * depth + '├─ ' + item + '/\n'
        tree_string += _build_tree_string(path, max_depth, show_hidden, exclude_patterns, depth + 1)
    for item, path in files:
        if not show_hidden and item.startswith('.'):
            continue
        tree_string += '│  ' * depth + '├─ ' + item + '\n'
    return tree_string

def _get_language_for_file(filename, language_map):
    _, extension = os.path.splitext(filename)
    extension = extension.lower()
    return language_map.get(extension, 'plaintext')
```

`modules\source_sage.py`

```plaintext
import os
from modules.file_utils import load_ignore_patterns, load_language_map
from modules.markdown_utils import generate_markdown_for_folder

class SourceSage:
    def __init__(self, folders, ignore_file='.SourceSageignore', output_file='output.md', language_map_file='language_map.json'):
        self.folders = folders
        print(ignore_file)
        self.ignore_file = ignore_file
        self.output_file = output_file
        self.exclude_patterns = load_ignore_patterns(ignore_file)
        print(self.exclude_patterns)
        self.language_map = load_language_map(language_map_file)

    def generate_markdown(self):
        with open(self.output_file, 'w', encoding='utf-8') as md_file:
            project_name = os.path.basename(os.path.abspath(self.folders[0]))
            md_file.write(f"# Project: {project_name}\n\n")
            for folder in self.folders:
                markdown_content = generate_markdown_for_folder(folder, self.exclude_patterns, self.language_map)
                md_file.write(markdown_content + '\n\n')
```

`modules\StagedDiffGenerator.py`

```plaintext
# modules/StagedDiffGenerator.py (変更後)

import json
import os
from modules.GitHubUtils import GitHubUtils

class StagedDiffGenerator:
    def __init__(self, repo_path, output_dir, language_map_file):
        self.repo_path = repo_path
        self.output_dir = output_dir
        self.output_file = os.path.join(output_dir, "STAGED_DIFF.md")
        self.language_map_file = language_map_file
        self.language_map = self.load_language_map()

    def load_language_map(self):
        with open(self.language_map_file, "r", encoding="utf-8") as lang_file:
            return json.load(lang_file)

    def generate_staged_diff(self):
        staged_diff = GitHubUtils.get_staged_diff(self.repo_path)

        os.makedirs(self.output_dir, exist_ok=True)  # フォルダが存在しない場合は作成

        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write("# Staged Files Diff\n\n")
            for diff_item in staged_diff:
                self.write_file_diff(file, diff_item)

    def write_file_diff(self, file, diff_item):
        file_path = diff_item.a_path or diff_item.b_path
        if file_path:
            _, extension = os.path.splitext(file_path)
            language = self.language_map.get(extension, "bash")
            file.write(f"## {file_path}\n\n")

            try:
                self.write_diff_content(file, diff_item, language, file_path)
            except Exception as e:
                file.write(f"- 内容の取得に失敗しました: {e}\n")
        else:
            file.write("- 有効なファイルパスが見つかりませんでした。\n\n")

    def write_diff_content(self, file, diff_item, language, file_path):
        try:
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

    def run(self):
        self.generate_staged_diff()

if __name__ == "__main__":
    diff_generator = StagedDiffGenerator(
        repo_path="./",
        output_dir="SourceSageAssets",
        language_map_file="config/language_map.json"
    )
    diff_generator.generate_staged_diff()
```

`modules\StageInfoGenerator.py`

```plaintext
# modules/StageInfoGenerator.py (変更後)

import json
import os
from modules.GitHubIssueRetrieve import GitHubIssueRetriever
from modules.StagedDiffGenerator import StagedDiffGenerator

class StageInfoGenerator:
    def __init__(self, issue_file_path, stage_diff_file_path, template_file_path, output_file_path):
        self.issue_file_path = issue_file_path
        self.stage_diff_file_path = stage_diff_file_path
        self.template_file_path = template_file_path
        self.output_file_path = output_file_path

    def load_issues(self):
        with open(self.issue_file_path, "r", encoding="utf-8") as issue_file:
            return json.load(issue_file)

    def load_stage_diff(self):
        with open(self.stage_diff_file_path, "r", encoding="utf-8") as diff_file:
            return diff_file.read()

    def load_template(self):
        with open(self.template_file_path, "r", encoding="utf-8") as template_file:
            return template_file.read()

    def generate_stage_info(self):
        issues = self.load_issues()
        stage_diff = self.load_stage_diff()
        template = self.load_template()

        output_dir = os.path.dirname(self.output_file_path)
        os.makedirs(output_dir, exist_ok=True)

        # テンプレートの [open_issues_filtered.json] の位置に issues を挿入
        template = template.replace("[open_issues_filtered.json]", json.dumps(issues, indent=2, ensure_ascii=False))

        # テンプレートの [STAGED_DIFF.md] の位置に stage_diff を挿入
        template = template.replace("[STAGED_DIFF.md]", stage_diff)

        with open(self.output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(template)

    def run(self):
        self.generate_stage_info()

if __name__ == "__main__":
    owner = "Sunwood-ai-labs"
    repository = "SourceSage"
    save_path = "SourceSageAssets"
    file_name = "open_issues_filtered.json"

    issue_retriever = GitHubIssueRetriever(owner, repository, save_path, file_name)
    issue_retriever.run()

    diff_generator = StagedDiffGenerator(
        repo_path="./",
        output_dir="SourceSageAssets",
        language_map_file="config/language_map.json"
    )
    diff_generator.run()

    stage_info_generator = StageInfoGenerator(
        issue_file_path="SourceSageAssets/open_issues_filtered.json",
        stage_diff_file_path="SourceSageAssets/STAGED_DIFF.md",
        template_file_path="docs/STAGE_INFO/STAGE_INFO_AND_ISSUES_TEMPLATE.md",
        output_file_path="SourceSageAssets/STAGE_INFO_AND_ISSUES_AND_PROMT.md"
    )
    stage_info_generator.run()

    stage_info_generator = StageInfoGenerator(
        issue_file_path="SourceSageAssets/open_issues_filtered.json",
        stage_diff_file_path="SourceSageAssets/STAGED_DIFF.md",
        template_file_path="docs/STAGE_INFO/STAGE_INFO_TEMPLATE.md",
        output_file_path="SourceSageAssets/STAGE_INFO_AND_PROMT.md"
    )
    stage_info_generator.run()
```

`modules\__init__.py`

```plaintext

```




