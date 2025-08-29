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



SourceSageは、リポジトリの構造と内容を包括的に分析し、AIフレンドリーなドキュメントを生成するツールです。主にRepository_summary.mdの生成とRELEASE_REPORTの作成機能を提供します。


>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。

## 更新内容

- [【2025/02/02】 SourceSage 5.1.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/v5.1.0)
  - DocuSumモジュールをコア機能として統合
- [【2024/06/18】 SourceSage 4.0.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/v4.0.0)
  - [ReleaseDiffReportGenerator](https://github.com/Sunwood-ai-labs/SourceSage/#2-releasediffreportgenerator-%E3%83%AA%E3%83%AA%E3%83%BC%E3%82%B9%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%AE%E8%87%AA%E5%8B%95%E7%94%9F%E6%88%90)機能を追加し、2つのタグ間の差分をマークダウンレポート形式で生成
- [【2024/06/16】 SourceSage 3.5.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/v3.5.0)
  - [IssueWise](https://github.com/Sunwood-ai-labs/SourceSage/#4-issuewisenew-llm%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9Fissue%E4%BD%9C%E6%88%90)機能を追加し、プロジェクトの概要からGitHub Issue作成を自動化
- [【2024/05/17】 SourceSage 3.0.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/v3.0.0)
  - [CommitCraft](https://github.com/Sunwood-ai-labs/SourceSage/#2-commitcraft%E9%96%8B%E7%99%BA%E4%B8%AD%E3%81%AE%E3%82%B3%E3%83%9F%E3%83%83%E3%83%88%E7%AE%A1%E7%90%86)機能を追加し、ステージングエリアの変更を自動解析
- [【2024/04/13】 SourceSage 2.5.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/v2.5.0)
    - [DocuMind](https://github.com/Sunwood-ai-labs/SourceSage/#3-documindリリース後のドキュメント化)機能を追加し、プロジェクトの概要とGitの変更履歴を組み合わせてドキュメント化
- [【2024/03/30】 SourceSage 2.0.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/tag2.0.0)
  - ChangelogGenerator classを導入し、コードの可読性と保守性を向上
  - 言語ごとのシンタックスハイライト機能を追加
  - .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外
- 【2024/03/29】 初期リリース


## 🎯 主な機能

SourceSageはシンプルで軽量なリポジトリ分析ツールで、以下の2つの主要機能を提供します：

### 1. 📋 Repository Summary Generation

リポジトリの構造、コミット情報、ファイル統計を包括的に分析し、AIフレンドリーなマークダウンドキュメントを生成します。

**出力ファイル**: `.SourceSageAssets/DOCUMIND/Repository_summary.md`

**含まれる情報**:
- 🌳 プロジェクトツリー構造
- 📋 Gitリポジトリ情報
- 📈 ファイルサイズと行数統計
- 📝 ファイル内容の詳細

### 2. 📄 Release Report Generation  

Gitタグ間の差分を分析し、リリースレポートを自動生成します。

**出力ファイル**: `.SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md`

**含まれる情報**:
- 🏷️ バージョン比較
- 🔄 変更差分の詳細
- 📋 コミット履歴


## 🚀 クイックスタート

### 📦 インストール

#### pipでのインストール

```bash
pip install sourcesage
```

#### uvでの環境構築（推奨）

```bash
# プロジェクトをクローン
 git clone https://github.com/Sunwood-ai-labs/SourceSage.git
 cd SourceSage

# 環境構築と依存関係のインストール
uv sync

# 実行
uv run sourcesage
# または短縮コマンド
uv run ss
```

### 🗺️ 基本的な使用方法

#### Repository Summaryの生成

```bash
# フルコマンド
sourcesage

# 短縮コマンド
ss
```

**出力**: `.SourceSageAssets/DOCUMIND/Repository_summary.md`

#### Release Reportの生成

```bash
# Repository Summary + Release Reportを同時生成
sourcesage --ss-mode GenerateReport

# 短縮コマンド
ss --ss-mode GenerateReport
```

**出力**: `.SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md`

#### 主なオプション

```bash
# 特定のモードで実行
ss --ss-mode Sage                 # Repository Summaryのみ
ss --ss-mode GenerateReport       # Release Reportのみ  
ss --ss-mode all                  # すべての機能（デフォルト）

# 出力ディレクトリの指定
ss --ss-output ./custom-output/

# 無視ファイルの指定
ss --ignore-file .gitignore
```

### 📊 生成される内容例

#### Repository Summary

```markdown
# Project: SourceSage

```plaintext
OS: posix
Directory: /path/to/project

├── .SourceSageignore
├── pyproject.toml
├── sourcesage/
│   ├── __init__.py
│   ├── cli.py
│   └── modules/
│       ├── DocuSum/
│       └── DiffReport/
│           ├── __init__.py
│           ├── git_diff.py
│           └── markdown_report.py
└── README.md
```

## 📊 プロジェクト統計

- 📅 作成日時: 2025-02-02 16:22:31
- 📁 総ディレクトリ数: 5
- 📄 総ファイル数: 15
- 📏 最大深度: 3
```

## 🛠️ 開発環境

SourceSageは現代的なPython開発環境をサポートしています：

- **Python**: 3.8以降
- **パッケージ管理**: uv / pip
- **ビルドシステム**: hatchling
- **設定ファイル**: pyproject.toml

### 開発用セットアップ

```bash
# uvを使った開発環境構築
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync

# テスト実行
uv run pytest

# コードフォーマット
uv run black sourcesage/
uv run isort sourcesage/

# パッケージビルド
uv build
```

## 💡 使用例

### CI/CDでの活用

```yaml
- name: Generate Repository Summary
  run: |
    pip install sourcesage
    ss
    
- name: Generate Release Report  
  run: |
    ss --ss-mode GenerateReport
```

### プロジェクト分析の自動化

```bash
#!/bin/bash
# 複数プロジェクトの一括分析
for dir in */; do
    cd "$dir"
    ss --ss-output "../analysis/$dir"
    cd ..
done
```

## 貢献

SourceSageの改善にご協力ください！バグの報告や機能追加の提案がある場合は、[GitHubリポジトリ](https://github.com/Sunwood-ai-labs/SourceSage)でIssueを開くかプルリクエストを送信してください。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。
