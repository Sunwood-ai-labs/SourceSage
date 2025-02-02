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

  [![SourceSage - Sunwood-ai-labs](https://img.shields.io/static/v1?label=SourceSage&message=Sunwood-ai-labs&color=blue&logo=github)](https://github.com/Sunwood-ai-labs/SourceSage "Go to GitHub repo")
![GitHub Repo stars](https://img.shields.io/github/stars/Sunwood-ai-labs/SourceSage)
[![forks - Sunwood-ai-labs](https://img.shields.io/github/forks/SourceSage/Sunwood-ai-labs?style=social)](https://github.com/Sunwood-ai-labs/SourceSage)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Sunwood-ai-labs/SourceSage)](https://github.com/Sunwood-ai-labs/SourceSage)
[![GitHub Top Language](https://img.shields.io/github/languages/top/Sunwood-ai-labs/SourceSage)](https://github.com/Sunwood-ai-labs/SourceSage)
![GitHub Release](https://img.shields.io/github/v/release/Sunwood-ai-labs/SourceSage?color=red)
![GitHub Tag](https://img.shields.io/github/v/tag/Sunwood-ai-labs/SourceSage?sort=semver&color=orange)
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/SourceSage/publish-to-pypi.yml">
  <br>

<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/tag/sourcesage/"><b>[🍀 Official Blog]</b></a>
</p>

</h2>


</p>



SourceSageは、AIを活用してソフトウェア開発を支援するツールです。開発前の課題解決、開発中のコミット管理、リリース後のドキュメント化など、開発のあらゆる場面でAIの力を活用できます。


>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。

## 更新内容

- [【2025/02/02】 SourceSage 5.1.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/v5.1.0)
  - DocuSumモジュールをコア機能として統合
  - リポジトリ解析機能の強化とAIフレンドリーなドキュメント生成を実現

- [【2024/06/10】 SourceSage 5.0.2](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/v5.0.2)
  - AIRA と Harmon.AI の設定を追加し、コード生成機能を追加(`DocuMind`、`CommitCraft`)
- [【2024/05/12】 SourceSage 4.2.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/v4.2.0)
  - ステージング情報のテンプレートに絵文字と[GAIAH](https://github.com/Sunwood-ai-labs/Gaiah)に対応
- [【2024/04/30】 SourceSage 4.1.2](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/vv4.1.2)
  - GitHub ActionsによるPyPIへの自動パブリッシュ設定を追加し、リリースプロセスを自動化
- [【2024/04/07】 SourceSage 4.1.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/undefined4.1.1)
  - CLI引数の追加とコアモジュールの修正、プロジェクトの構成とファイルの変更によるシンプル化
  - セットアップ手順、実行方法、クイックスタートセクション、テストドキュメントの更新
- [【2024/04/05】 SourceSage 4.0.3](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/undefined4.0.3)
  - README.mdのセットアップ手順と実行手順を簡素化
  - リポジトリのオーナーと名前をコマンドライン引数で指定可能に
  - テスト実行方法のドキュメントを更新
- [【2024/03/31】 SourceSage 3.0.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/tag3.0.0)
  - 下記3つの機能の構成を提案
    - [IssueWise](https://github.com/Sunwood-ai-labs/SourceSage/#1-issuewise開発前の課題解決)機能を追加し、GitHubのオープンIssueを取得してAIによる自動修正をサポート
    - [CommitCraft](https://github.com/Sunwood-ai-labs/SourceSage/#2-commitcraft開発中のコミット管理)機能を追加し、変更差分を追跡してAIが適切なコミットメッセージを生成
    - [DocuMind](https://github.com/Sunwood-ai-labs/SourceSage/#3-documindリリース後のドキュメント化)機能を追加し、プロジェクトの概要とGitの変更履歴を組み合わせてドキュメント化
- [【2024/03/30】 SourceSage 2.0.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/tag2.0.0)
  - ChangelogGenerator classを導入し、コードの可読性と保守性を向上
  - 言語ごとのシンタックスハイライト機能を追加
  - .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外
- 【2024/03/29】 初期リリース


## 🎯 主な機能：DocuSum

[DocuSum](sourcesage/modules/DocuSum/README.md)は、リポジトリ構造とファイル内容を包括的に分析し、AIフレンドリーなマークダウンドキュメントを生成するSourceSageのコア機能です。

### 使用方法

```bash
sourcesage
```

生成されるマークダウンファイルには以下の情報が含まれます：

> [!NOTE]
>**.SourceSageAssets/DOCUMIND/Repository_summary.md** にマークダウンファイルが生成されます。

```markdown
    # Project: DocuSum

    ```plaintext
    OS: posix
    Directory: /path/to/project

    ├── .SourceSageignore
    ├── __init__.py
    └── src/
        ├── main.py
        └── utils/
            └── helper.py
    ```

    ## 📊 プロジェクト統計

    - 📅 作成日時: 2025-02-02 16:22:31
    - 📁 総ディレクトリ数: 2
    - 📄 総ファイル数: 4
    - 📏 最大深度: 2
```

詳しくは[こちら`sourcesage/modules/DocuSum/README.md`](sourcesage/modules/DocuSum/README.md)

## 🧪 実験的機能

SourceSageには、AIを活用した開発支援のための実験的機能が含まれています。これらの機能の詳細については、[実験的機能のドキュメント](docs/EXPERIMENTAL_FEATURES.md)を参照してください。

## 🚀 クイックスタート

### インストール

```bash
pip install sourcesage
```

### 基本的な使用方法

```bash
sourcesage
```

**.SourceSageAssets/DOCUMIND/Repository_summary.md** にマークダウンファイルが生成されます。


## 貢献

SourceSageの改善にご協力ください！バグの報告や機能追加の提案がある場合は、[GitHubリポジトリ](https://github.com/Sunwood-ai-labs/SourceSage)でIssueを開くかプルリクエストを送信してください。

開発者向けの情報は[貢献ガイド](CONTRIBUTING.md)を参照してください。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。
