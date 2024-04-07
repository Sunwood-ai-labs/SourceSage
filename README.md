<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/SourceSage_icon4.png" width="100%">
<br>
<h1 align="center">SourceSage</h1>
<h2 align="center">～Transforming code for AI～</h2>
</p>

SourceSageは、プロジェクトのソースコードとファイル構成を単一のマークダウンファイルに統合し、AIによる自動修正やドキュメント化を実現するPythonスクリプトです。開発のライフサイクル全体を通して、コードの品質向上と生産性の向上を支援します。


## 更新内容

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6d1eb661b566430f8a9a550de6b6f5ba)](https://app.codacy.com/gh/Sunwood-ai-labs/SourceSage?utm_source=github.com&utm_medium=referral&utm_content=Sunwood-ai-labs/SourceSage&utm_campaign=Badge_Grade)

- [【2024/04/05】 SourceSage 4.0.3](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/4.0.3)
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

```bash
pip install sourcesage
```

### 実行

ターミナルまたはコマンドプロンプトで、プロジェクトのルートディレクトリに移動し、以下のコマンドを実行します：

```bash
sourcesage
```

これにより、以下のファイルが生成されます：

- `SourceSageAssets/SourceSage.md`：AIがプロジェクトの構造と内容を理解しやすい形式のマークダウンファイル
- `SourceSageAssets/Changelog`：Gitの変更履歴を保存するディレクトリ
- `SourceSageAssets/open_issues_filtered.json`：GitHubからフェッチしたオープンなIssueのJSONファイル
- `SourceSageAssets/STAGED_DIFF.md`：ステージされた変更の差分情報を含むマークダウンファイル


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