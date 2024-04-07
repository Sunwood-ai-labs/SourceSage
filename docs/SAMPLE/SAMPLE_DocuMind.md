# Project: SourceSage

```plaintext
OS: nt
Directory: C:\Prj\SourceSage

├─ demo/
│  ├─ get_diff.py
│  ├─ get_issues.py
│  ├─ make_issue_res.py
├─ docs/
│  ├─ icon/
│  ├─ ISSUES_RESOLVE/
│  │  ├─ ISSUES_RESOLVE_TEMPLATE.md
│  ├─ package_release/
│  │  ├─ README.md
│  ├─ STAGE_INFO/
│  │  ├─ STAGE_INFO_AND_ISSUES_TEMPLATE.md
│  │  ├─ STAGE_INFO_TEMPLATE.md
├─ script/
│  ├─ build.bat
│  ├─ build.sh
│  ├─ build_and_release.bat
├─ sourcesage/
│  ├─ config/
│  │  ├─ ISSUES_RESOLVE/
│  │  │  ├─ ISSUES_RESOLVE_TEMPLATE.md
│  │  ├─ STAGE_INFO/
│  │  │  ├─ STAGE_INFO_AND_ISSUES_TEMPLATE.md
│  │  │  ├─ STAGE_INFO_TEMPLATE.md
│  │  ├─ constants.py
│  │  ├─ language_map.json
│  ├─ modules/
│  │  ├─ ChangelogGenerator.py
│  │  ├─ ChangelogUtils.py
│  │  ├─ DiffChangelogGenerator.py
│  │  ├─ EnvFileHandler.py
│  │  ├─ file_utils.py
│  │  ├─ GitHubIssueRetrieve.py
│  │  ├─ GitHubUtils.py
│  │  ├─ IssuesToMarkdown.py
│  │  ├─ markdown_utils.py
│  │  ├─ source_sage.py
│  │  ├─ StagedDiffGenerator.py
│  │  ├─ StageInfoGenerator.py
│  │  ├─ __init__.py
│  ├─ cli.py
│  ├─ core.py
│  ├─ __init__.py
├─ temp/
│  ├─ sourcesage.yml
├─ tests/
│  ├─ README.md
│  ├─ test_sourcesage.py
├─ conda_activate_ss_test.bat
├─ README.md
├─ setup.py
```

## .

`conda_activate_ss_test.bat`

```plaintext
conda activate ss_test
```

`README.md`

```markdown
<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/SourceSage_icon4.png" width="100%">
<br>
<h1 align="center">SourceSage</h1>
<h2 align="center">
  ～Transforming code for AI～

  <br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/sourcesage">
  <img alt="PyPI - Format" src="https://img.shields.io/pypi/format/sourcesage">
  <img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/sourcesage">
  <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/sourcesage">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/sourcesage">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/sourcesage">
  <a href="https://app.codacy.com/gh/Sunwood-ai-labs/SourceSage/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/77ab7715dd23499d82caca4e7ea3b093"/></a>

  <br>

</h2>


</p>



SourceSageは、プロジェクトのソースコードとファイル構成を単一のマークダウンファイルに統合し、AIによる自動修正やドキュメント化を実現するPythonスクリプトです。開発のライフサイクル全体を通して、コードの品質向上と生産性の向上を支援します。

**このリポジトリ自体もSourceSageを活用しており、リリースノートやREADME、コミットメッセージの9割はSourceSage X クロードで生成しています。**


## 更新内容

- [【2024/04/05】 SourceSage 4.0.3](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/undefined4.0.3)
  - README.mdのセットアップ手順と実行手順を簡素化
  - リポジトリのオーナーと名前をコマンドライン引数で指定可能に
  - テスト実行方法のドキュメントを更新
- [【2024/04/01】 SourceSage 3.1.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/tag3.1.0)
  - コードの品質と保守性を向上させるためのリファクタリングと機能改善
  - コミットメッセージのフォーマットとタイプの説明を追加
  - コマンドラインからソースコードのリポジトリパスを取得するように修正
  - 定数の管理方法を改善し、[`config/constants.py`](config/constants.py)ファイルで一元管理
- [【2024/03/31】 SourceSage 3.0.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/tag3.0.0) 
  - [IssueWise](#1-issuewise開発前の課題解決)機能を追加し、GitHubのオープンIssueを取得してAIによる自動修正をサポート
  - [CommitCraft](#2-commitcraft開発中のコミット管理)機能を追加し、変更差分を追跡してAIが適切なコミットメッセージを生成
  - [DocuMind](#3-documindリリース後のドキュメント化)機能を追加し、プロジェクトの概要とGitの変更履歴を組み合わせてドキュメント化
- [【2024/03/30】 SourceSage 2.0.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/tag2.0.0)
  - ChangelogGenerator classを導入し、コードの可読性と保守性を向上
  - 言語ごとのシンタックスハイライト機能を追加
  - .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外
- 【2024/03/29】 初期リリース

## 主な機能

### [IssueWise（開発前の課題解決）](#1-issuewise開発前の課題解決)

- GitHubのオープンIssueを自動取得し、AIによる課題の自動修正をサポート
- 課題を効率的に特定し、迅速に解決策を見つけられます

### [CommitCraft（開発中のコミット管理）](#2-commitcraft開発中のコミット管理)
- 変更差分を追跡し、AIが適切なコミットメッセージを自動生成
- コミットの内容を正確に記述でき、変更履歴を明確に管理できます

### [DocuMind（リリース後のドキュメント化）](#3-documindリリース後のドキュメント化)
- プロジェクトの概要とGitの変更履歴を組み合わせてドキュメント化
- プロジェクトの全体像を把握しやすく、メンテナンス性が向上します


## 使用方法

### セットアップ

SourceSageを使用するには、まずPythonのパッケージマネージャーであるpipを使ってインストールします。以下のコマンドをターミナルまたはコマンドプロンプトで実行してください：

```bash
pip install sourcesage
```

これにより、SourceSageがシステムにインストールされ、コマンドラインから実行できるようになります。

### クイックスタート

SourceSageをプロジェクトで使用するには、以下の手順に従ってください：

1. ターミナルまたはコマンドプロンプトを開きます。

2. `cd`コマンドを使って、解析対象のプロジェクトのルートディレクトリに移動します。例えば、プロジェクトが`~/my_project`ディレクトリにある場合は、以下のコマンドを実行します：
   ```bash
   cd ~/my_project
   ```

3. 次に、以下のコマンドを実行してSourceSageを起動します：
   ```bash
   sourcesage
   ```

4. SourceSageが実行されると、以下のファイルが`SourceSageAssets`ディレクトリに生成されます：
   - `SourceSage.md`：AIがプロジェクトの構造と内容を理解しやすい形式のマークダウンファイルです。
   - `Changelog`：Gitの変更履歴を保存するディレクトリです。
   - `open_issues_filtered.json`：GitHubからフェッチしたオープンなIssueのJSONファイルです。
   - `STAGED_DIFF.md`：ステージされた変更の差分情報を含むマークダウンファイルです。

これらのファイルを使って、AIによるプロジェクトの解析や自動修正、ドキュメント化などを行うことができます。

### リポジトリのIssueも取得する方法

デフォルトでは、SourceSageは現在のディレクトリをプロジェクトのルートとして解析します。ただし、GitHub上のリポジトリのIssueも取得したい場合は、以下のようにリポジトリのオーナー名とリポジトリ名をコマンドライン引数で指定します：

```bash
sourcesage --owner Sunwood-ai-labs --repository SourceSage
```

上記の例では、`Sunwood-ai-labs`がリポジトリのオーナー名、`SourceSage`がリポジトリ名です。これらの引数を指定することで、SourceSageはGitHub APIを使ってリポジトリのオープンなIssueを取得し、`open_issues_filtered.json`ファイルに保存します。

以上が、SourceSageの基本的な使用方法です。ぜひ自分のプロジェクトでSourceSageを活用して、開発効率の向上を体験してみてください！


## 1. IssueWise：開発前の課題解決

<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/head_icon4.png" width="50%">
</p>

IssueWiseは、GitHubのオープンなIssue(課題)を自動的に取得し、SourceSageが生成したプロジェクトの概要と組み合わせることで、AIによる課題の自動修正を可能にするツールです。これにより、開発者はプロジェクトの課題を効率的に特定し、解決策を迅速に見つけることができます。

`SourceSageAssets/ISSUES_RESOLVE`に生成されるマークダウンファイルを使用します。

例：[`SourceSageAssetsDemo/ISSUES_RESOLVE\ISSUE_7.md`](SourceSageAssetsDemo/ISSUES_RESOLVE\ISSUE_7.md)

このマークダウンファイルをそのままAIに入力することで、AIが課題を解決するためのコードを生成します。

このマークダウンファイルは、下記のファイルのフォーマットで出力されます。
[`docs\ISSUES_RESOLVE\ISSUES_RESOLVE_TEMPLATE.md`](docs\ISSUES_RESOLVE\ISSUES_RESOLVE_TEMPLATE.md)

```bash
    下記のissueについてリポジトリ情報を参照して修正してください。

    # ISSUE {{number}} : {{title}}

    {{body}}


    ## 補足事項

    修正に対するコミットメッセージは日本語にしてください。
    正確にstep-by-stepで処理してください。
    issueの番号も記載してください。

    コミットメッセージは下記のフォーマットにしてください。

    ## フォーマット

    ```markdown
    [種類] 概要

    詳細な説明（必要に応じて）
    ```

    種類は下記を参考にしてください。

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

## 2. CommitCraft：開発中のコミット管理

<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/head_icon5.png" width="50%">
</p>

CommitCraftは、開発中のステージされた変更を追跡し、AIを活用して適切なコミットメッセージを自動生成するツールです。これにより、開発者はコミットの内容を正確に記述することができ、プロジェクトの変更履歴をより明確に管理できます。

`SourceSageAssets/STAGED_DIFF.md`に生成されるマークダウンファイルを使用します。
例：[`SourceSageAssetsDemo/STAGED_DIFF.md`](SourceSageAssetsDemo/STAGED_DIFF.md)

このマークダウンファイルをそのままAIに入力することで、AIがコミットメッセージを生成します。

このマークダウンファイルは、下記のファイルのフォーマットで出力されます。

```bash
    # Staged Files Diff

    ## README.md

    ### 差分:

    ## modules/EnvFileHandler.py

    ### 差分:

    ```diff
    @@ -10,7 +10,7 @@ CONFIG_DIR=config
    DOCS_DIR=docs
    FOLDERS=./
    IGNORE_FILE=.SourceSageignore
    -OUTPUT_FILE=SourceSageAssets/SourceSage.md
    +OUTPUT_FILE=SourceSage.md
    LANGUAGE_MAP_FILE=config/language_map.json
    
    OWNER=Sunwood-ai-labs
    ```
```

## 3. DocuMind：リリース後のドキュメント化

<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/head_icon7.png" width="100%">
</p>

DocuMindは、リリース後のプロジェクトの統合とドキュメント化を支援するツールです。SourceSageが生成するプロジェクトの概要と、自動生成されたGitの変更履歴を組み合わせることで、プロジェクトの全体像を明確に把握できます。これにより、開発者はプロジェクトのドキュメントを効率的に作成し、メンテナンス性を向上させることができます。

`SourceSageAssets/SourceSage.md`に生成されるマークダウンファイルを使用します。
例：[`SourceSageAssetsDemo/SourceSage.md`](SourceSageAssetsDemo/SourceSage.md)

このマークダウンファイルをそのままAIに入力することで、AIがプロジェクトの構造と内容を理解し、ドキュメントを生成します。

このマークダウンファイルは、下記のファイルのフォーマットで出力されます。

```bash
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
    ├─ modules/
    │  ├─ ChangelogGenerator.py
    │  ├─ ChangelogUtils.py
    │  ├─ DiffChangelogGenerator.py
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
    ```
```


## 貢献

SourceSageの改善にご協力ください！バグの報告や機能追加の提案がある場合は、[GitHubリポジトリ](https://github.com/Sunwood-ai-labs/SourceSage)でIssueを開くかプルリクエストを送信してください。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。
```

`setup.py`

```python
from setuptools import setup, find_packages


# READMEファイルの内容を読み込む
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='sourcesage',
    version='4.0.12',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    package_data={
        'sourcesage': ['config/**/**', 
                       'config/.SourceSageignore'],
    },
    entry_points={
        'console_scripts': [
            'sourcesage=sourcesage.cli:main',
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sunwood-ai-labs/SourceSage",
    install_requires=[
        'loguru',
        'GitPython',
        'requests',
        'art',
    ],
)
```

## .vscode

`.vscode\settings.json`

```json
{
    "gitlens.ai.experimental.openai.url": "",
    "gitlens.ai.experimental.provider": "anthropic",
    "gitlens.ai.experimental.anthropic.model": "claude-3-haiku-20240307",
    "gitlens.experimental.generateCommitMessagePrompt": "日本語でシンプルなコミットメッセージ"
}
```

## demo

`demo\get_diff.py`

```python
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

```python
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

```python
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

### docs\icon

### docs\ISSUES_RESOLVE

`docs\ISSUES_RESOLVE\ISSUES_RESOLVE_TEMPLATE.md`

```markdown
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

### docs\package_release

`docs\package_release\README.md`

```markdown
# Package release

## Build

```bash
python setup.py sdist bdist_wheel
```

## release

test
```bash
twine upload  --repository pypitest dist/*
```

main
```bash
twine upload  --repository pypi dist/*  
```
```

### docs\STAGE_INFO

`docs\STAGE_INFO\STAGE_INFO_AND_ISSUES_TEMPLATE.md`

```markdown
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

```markdown
下記はgitはStageの情報です

issueは掲載しないで

見やすくコミットメッセージにして
章やパラグラフ、箇条書きを多用して見やすくして

コミットメッセージは日本語にして
正確にstep-by-stepで処理して

下記のマークダウンフォーマットで出力して

## フォーマット

```markdown

[種類] 概要

詳細な説明（必要に応じて）

```

## 種類

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

## script

`script\build.bat`

```plaintext
@echo off

REM dist ディレクトリが存在する場合は削除
if exist dist rmdir /s /q dist

REM ビルド実行
echo Building distributions...
python setup.py sdist bdist_wheel

echo Build complete.
```

`script\build.sh`

```bash
#!/bin/bash

# dist ディレクトリが存在する場合は削除
if [ -d "dist" ]; then
  echo "Cleaning up dist directory..."
  rm -rf dist/
fi

# ビルド実行
echo "Building distributions..."
python setup.py sdist bdist_wheel

echo "Build complete."
```

`script\build_and_release.bat`

```plaintext
@echo off

REM dist ディレクトリが存在する場合は削除
if exist dist rmdir /s /q dist

REM ビルド実行
echo Building distributions...
python setup.py sdist bdist_wheel
echo Build complete.

REM リリース
twine upload  --repository pypi dist/*  
echo Release complete.
```

## sourcesage

`sourcesage\cli.py`

```python
import argparse
from .core import SourceSage
import os

def main():
    parser = argparse.ArgumentParser(description='SourceSage CLI')
    parser.add_argument('--config', help='Path to the configuration file', default='sourcesage.yml')
    parser.add_argument('--output', help='Output directory for generated files', default='./')
    parser.add_argument('--repo', help='Path to the repository', default='./')
    parser.add_argument('--owner', help='Owner of the repository', default='Sunwood-ai-labs')  # デフォルト値を設定
    parser.add_argument('--repository', help='Name of the repository', default='SourceSage')  # デフォルト値を設定

    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_ignore_file = os.path.join(package_root, 'sourcesage', 'config', '.SourceSageignore')  # 修正
    default_language_map = os.path.join(package_root, 'sourcesage', 'config', 'language_map.json')  # 修正

    parser.add_argument('--ignore-file', help='Path to the ignore file', default=default_ignore_file)  # 修正
    parser.add_argument('--language-map', help='Path to the language map file', default=default_language_map)  # 修正
    
    args = parser.parse_args()

    sourcesage = SourceSage(args.config, args.output, args.repo, args.owner, args.repository, args.ignore_file, args.language_map)
    sourcesage.run()

if __name__ == '__main__':
    main()
```

`sourcesage\core.py`

```python
import os
from .modules.EnvFileHandler import create_or_append_env_file
from .modules.source_sage import SourceSage as SourceSageModule
from .modules.ChangelogGenerator import ChangelogGenerator
from .modules.StageInfoGenerator import StageInfoGenerator
from .modules.GitHubIssueRetrieve import GitHubIssueRetriever
from .modules.StagedDiffGenerator import StagedDiffGenerator
from .modules.IssuesToMarkdown import IssuesToMarkdown

from .config.constants import Constants

from art import *

class SourceSage:
    def __init__(self, config_path, output_dir, repo_path, owner, repository, ignore_file, language_map_file):
        self.config_path = config_path
        self.output_dir = output_dir
        self.repo_path = repo_path
        self.ignore_file = ignore_file
        self.language_map_file = language_map_file

        self.constants = Constants(output_dir, owner, repository) 

    def run(self):
        tprint("SourceSage", font="rnd-medium")
        print("Running SourceSage...")
        
        # Load configuration
        config = self.load_config()

        # Create necessary directories
        os.makedirs(self.constants.ISSUE_LOG_DIR, exist_ok=True)
        os.makedirs(self.constants.ISSUES_RESOLVE_DIR, exist_ok=True)
        os.makedirs(self.constants.STAGE_INFO_DIR, exist_ok=True)
        
        # Generate SourceSage markdown
        sourcesage_module = SourceSageModule(folders=[self.repo_path], ignore_file=self.ignore_file,
                                             output_file=os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.SOURCE_SAGE_MD),
                                             language_map_file=self.language_map_file)
        sourcesage_module.generate_markdown()

        # Generate changelog
        changelog_generator = ChangelogGenerator(self.repo_path, os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.CHANGELOG_DIR))
        changelog_generator.generate_changelog_for_all_branches()
        changelog_generator.integrate_changelogs()

        # Retrieve GitHub issues
        issue_retriever = GitHubIssueRetriever(self.constants.OWNER, self.constants.REPOSITORY, self.constants.ISSUE_LOG_DIR, self.constants.ISSUES_FILE_NAME)
        issue_retriever.run()

        # Generate staged diff
        diff_generator = StagedDiffGenerator(repo_path=self.repo_path, output_dir=self.constants.SOURCE_SAGE_ASSETS_DIR,
                                             language_map_file=self.language_map_file)
        diff_generator.run()

        # Generate stage info and issues
        stage_info_generator = StageInfoGenerator(issue_file_path=os.path.join(self.constants.ISSUE_LOG_DIR, self.constants.ISSUES_FILE_NAME),
                                                  stage_diff_file_path=os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.STAGED_DIFF_MD),
                                                  template_file_path=os.path.join(self.constants.DOCS_DIR, self.constants.TEMPLATE_STAGE_INFO_DIR, self.constants.STAGE_INFO_TEMPLATE_MD),
                                                  output_file_path=os.path.join(self.constants.STAGE_INFO_DIR, self.constants.STAGE_INFO_OUTPUT_MD))
        stage_info_generator.run()

        # Generate stage info
        stage_info_generator = StageInfoGenerator(issue_file_path=os.path.join(self.constants.ISSUE_LOG_DIR, self.constants.ISSUES_FILE_NAME),
                                                  stage_diff_file_path=os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.STAGED_DIFF_MD),
                                                  template_file_path=os.path.join(self.constants.DOCS_DIR, self.constants.TEMPLATE_STAGE_INFO_DIR, self.constants.STAGE_INFO_SIMPLE_TEMPLATE_MD),
                                                  output_file_path=os.path.join(self.constants.STAGE_INFO_DIR, self.constants.STAGE_INFO_SIMPLE_OUTPUT_MD))
        stage_info_generator.run()

        # Convert issues to markdown
        issues_to_markdown = IssuesToMarkdown(issues_file=os.path.join(self.constants.ISSUE_LOG_DIR, self.constants.ISSUES_FILE_NAME),
                                              sourcesage_file=os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.SOURCE_SAGE_MD),
                                              template_file=os.path.join(self.constants.DOCS_DIR, self.constants.TEMPLATE_ISSUES_RESOLVE_DIR, self.constants.ISSUES_RESOLVE_TEMPLATE_MD),
                                              output_folder=self.constants.ISSUES_RESOLVE_DIR)
        issues_to_markdown.load_data()
        issues_to_markdown.create_markdown_files()

        print("SourceSage completed successfully.")

    def load_config(self):
        # Load configuration from YAML file
        # Implement this method based on your configuration file structure
        pass
```

`sourcesage\__init__.py`

```python

```

### sourcesage\config

`sourcesage\config\constants.py`

```python
import os

class Constants:
    def __init__(self, output_dir, owner, repository):
        self.OWNER = owner
        self.REPOSITORY = repository
        self.ISSUES_FILE_NAME = "open_issues_filtered.json"

        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.REPO_PATH = self.BASE_DIR
        self.CONFIG_DIR = os.path.join(self.BASE_DIR, 'config')
        self.DOCS_DIR = os.path.join(self.BASE_DIR, "config")

        self.LANGUAGE_MAP_FILE = os.path.join(self.CONFIG_DIR, 'language_map.json')
        self.IGNORE_FILE = os.path.join(self.CONFIG_DIR, '.SourceSageignore')

        self.SOURCE_SAGE_MD = "DocuMind.md"
        self.CHANGELOG_DIR = "Changelog"
        self.STAGED_DIFF_MD = "STAGED_DIFF.md"

        self.set_output_dir(output_dir)

    def set_output_dir(self, output_dir):
        self.SOURCE_SAGE_ASSETS_DIR = os.path.join(output_dir, "SourceSageAssets")
        self.ISSUE_LOG_DIR = os.path.join(self.SOURCE_SAGE_ASSETS_DIR, "ISSUE_LOG")
        self.ISSUES_RESOLVE_DIR = os.path.join(self.SOURCE_SAGE_ASSETS_DIR, "ISSUE_WISE/ISSUES_RESOLVE")
        self.STAGE_INFO_DIR = os.path.join(self.SOURCE_SAGE_ASSETS_DIR, "COMMIT_CRAFT/STAGE_INFO")

        self.TEMPLATE_ISSUES_RESOLVE_DIR = os.path.join(self.DOCS_DIR, "ISSUES_RESOLVE")
        self.ISSUES_RESOLVE_TEMPLATE_MD = "ISSUES_RESOLVE_TEMPLATE.md"

        self.TEMPLATE_STAGE_INFO_DIR = os.path.join(self.DOCS_DIR, "STAGE_INFO")
        self.STAGE_INFO_OUTPUT_MD = "STAGE_INFO_AND_ISSUES_AND_PROMT.md"
        self.STAGE_INFO_TEMPLATE_MD = "STAGE_INFO_AND_ISSUES_TEMPLATE.md"

        self.STAGE_INFO_SIMPLE_OUTPUT_MD = "STAGE_INFO_AND_PROMT.md"
        self.STAGE_INFO_SIMPLE_TEMPLATE_MD = "STAGE_INFO_TEMPLATE.md"
```

`sourcesage\config\language_map.json`

```json
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

#### sourcesage\config\ISSUES_RESOLVE

`sourcesage\config\ISSUES_RESOLVE\ISSUES_RESOLVE_TEMPLATE.md`

```markdown
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

#### sourcesage\config\STAGE_INFO

`sourcesage\config\STAGE_INFO\STAGE_INFO_AND_ISSUES_TEMPLATE.md`

```markdown
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

`sourcesage\config\STAGE_INFO\STAGE_INFO_TEMPLATE.md`

```markdown
下記はgitはStageの情報です

issueは掲載しないで

見やすくコミットメッセージにして
章やパラグラフ、箇条書きを多用して見やすくして

コミットメッセージは日本語にして
正確にstep-by-stepで処理して

下記のマークダウンフォーマットで出力して

## フォーマット

```markdown

[種類] 概要

詳細な説明（必要に応じて）

```

## 種類

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

### sourcesage\modules

`sourcesage\modules\ChangelogGenerator.py`

```python
# modules/ChangelogGenerator.py (変更後)

import os
from git import Repo
from .ChangelogUtils import ChangelogUtils
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

        # 出力ファイルのディレクトリを確認し、存在しない場合は作成
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

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
            output_file = os.path.join(self.output_dir, f"CHANGELOG_{branch_name}.md").replace("release/", "release_")
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

`sourcesage\modules\ChangelogUtils.py`

```python
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

`sourcesage\modules\DiffChangelogGenerator.py`

```python
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

`sourcesage\modules\EnvFileHandler.py`

```python
# modules/EnvFileHandler.py

import os

def create_or_append_env_file():
    env_file = ".env"
    env_vars = """
    
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
"""

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

`sourcesage\modules\file_utils.py`

```python
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

`sourcesage\modules\GitHubIssueRetrieve.py`

```python
# modules/GitHubIssueRetrieve.py (変更後)

from .GitHubUtils import GitHubUtils

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

`sourcesage\modules\GitHubUtils.py`

```python
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

`sourcesage\modules\IssuesToMarkdown.py`

```python
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

`sourcesage\modules\markdown_utils.py`

```python
import os
from .file_utils import is_excluded, is_excluded_extension

def generate_markdown_for_folder(folder_path, exclude_patterns, language_map):
    markdown_content = "```plaintext\n"
    print(folder_path)
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
    
    print(dir_path)
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

`sourcesage\modules\source_sage.py`

```python
import os
from .file_utils import load_ignore_patterns, load_language_map  # 相対インポートを修正
from .markdown_utils import generate_markdown_for_folder

class SourceSage:
    def __init__(self, folders, ignore_file='.SourceSageignore', output_file='output.md', language_map_file='language_map.json'):
        self.folders = folders
        print(ignore_file)
        print(folders)
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

`sourcesage\modules\StagedDiffGenerator.py`

```python
# modules/StagedDiffGenerator.py (変更後)

import json
import os
from .GitHubUtils import GitHubUtils

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

`sourcesage\modules\StageInfoGenerator.py`

```python
# modules/StageInfoGenerator.py (変更後)

import json
import os
from .GitHubIssueRetrieve import GitHubIssueRetriever
from .StagedDiffGenerator import StagedDiffGenerator

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

`sourcesage\modules\__init__.py`

```python

```

## temp

`temp\sourcesage.yml`

```yaml
exclude_patterns:
  - "*.pyc"
  - "__pycache__"
```

## tests

`tests\README.md`

```markdown
# Test

このドキュメントでは、テストを実行するためのコマンドラインについて説明します。

## テストの実行

ユニットテストを実行するには、以下のコマンドを使用します。

```bash
pytest tests/test_sourcesage.py
```

このコマンドにより、`tests/test_sourcesage.py`ファイルに定義されたテストケースが実行されます。

## 本番環境でのテスト

SourceSageを本番環境でテストするには、以下のコマンドを実行します。

```bash
sourcesage
```

このコマンドにより、SourceSageが実行され、本番環境での動作を確認できます。

## リポジトリの指定

特定のリポジトリに対してSourceSageを実行する場合は、以下のようにオーナー名とリポジトリ名を指定します。

```bash
sourcesage --owner Sunwood-ai-labs --repository SourceSage
```

このコマンドにより、指定されたリポジトリ（この例では`Sunwood-ai-labs/SourceSage`）に対してSourceSageが実行されます。また、このコマンドを使用することで、指定したリポジトリのIssue情報も取得できます。
```

`tests\test_sourcesage.py`

```python
import os
from sourcesage.cli import main
from sourcesage.core import SourceSage
import sys

def ensure_temp_directory():
    """temp フォルダが存在することを確認し、なければ作成します。"""
    temp_path = os.path.join(os.getcwd(), 'temp')
    os.makedirs(temp_path, exist_ok=True)
    return temp_path

def test_sourcesage_cli(capsys):
    temp_dir = ensure_temp_directory()  # tempフォルダの確認/作成

    # テスト用の設定ファイルを作成
    config_path = os.path.join(temp_dir, 'sourcesage.yml')
    with open(config_path, 'w') as f:
        f.write('exclude_patterns:\n  - "*.pyc"\n  - "__pycache__"\n')

    # パッケージのルートディレクトリを取得
    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ignore_file_path = os.path.join(package_root, 'sourcesage', 'config', '.SourceSageignore')  # 修正
    language_map_path = os.path.join(package_root, 'sourcesage', 'config', 'language_map.json')  # 修正

    sys.argv = ['sourcesage', '--config', config_path, '--output', temp_dir, '--repo', package_root, '--owner', 'Sunwood-ai-labs', '--repository', 'SourceSage', '--ignore-file', ignore_file_path, '--language-map', language_map_path]
    main()

    # 出力を確認
    captured = capsys.readouterr()
    assert 'Running SourceSage...' in captured.out
    assert 'SourceSage completed successfully.' in captured.out

    # 出力ファイルが生成されたことを確認
    output_file = os.path.join(temp_dir, 'SourceSage.md')
    # assert os.path.exists(output_file)

    # 出力ファイルの保存場所を表示
    print(f"Output file saved at: {output_file}")

def test_sourcesage_core():
    temp_dir = ensure_temp_directory()  # tempフォルダの確認/作成

    # テスト用の設定ファイルを作成
    config_path = os.path.join(temp_dir, 'sourcesage.yml')
    with open(config_path, 'w') as f:
        f.write('exclude_patterns:\n  - "*.pyc"\n  - "__pycache__"\n')

    # パッケージのルートディレクトリを取得
    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ignore_file_path = os.path.join(package_root, 'sourcesage', 'config', '.SourceSageignore')  # 修正
    language_map_path = os.path.join(package_root, 'sourcesage', 'config', 'language_map.json')  # 修正

    # 必要なディレクトリを作成
    necessary_dirs = ['SourceSageAssets/Changelog', 'SourceSageAssets/ISSUE_LOG', 'SourceSageAssets/ISSUES_RESOLVE', 'SourceSageAssets/STAGE_INFO']
    for dir_path in necessary_dirs:
        os.makedirs(os.path.join(temp_dir, dir_path), exist_ok=True)

    # SourceSageクラスを直接インスタンス化して実行
    sourcesage = SourceSage(config_path, temp_dir, package_root, 'Sunwood-ai-labs', 'SourceSage', ignore_file_path, language_map_path)
    sourcesage.run()

    # 出力ファイルが生成されたことを確認
    output_file = os.path.join(temp_dir, 'SourceSage.md')
    # assert os.path.exists(output_file)

    # 出力ファイルの保存場所を表示
    print(f"Output file saved at: {output_file}")
```



