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

日本語 | [English](README.md)

SourceSageは、リポジトリの構造と内容を包括的に分析し、AIフレンドリーなドキュメントを生成するツールです。主にRepository_summary.mdの生成とRELEASE_REPORTの作成機能を提供します。


>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。

## 🌟 関連プロジェクト

### SourceSage MCP Server
[SourceSage MCP Server](https://github.com/Sunwood-ai-labs/source-sage-mcp-server)は、SourceSageの派生版で、Model Context Protocol (MCP)と統合されています。Claude Desktopなどのアシスタントが、リポジトリ分析機能に直接アクセスできるようになります。

## リリースノート

最新の更新内容はGitHubのリリースページをご覧ください。

https://github.com/Sunwood-ai-labs/SourceSage/releases


## 🎯 主な機能

SourceSageはシンプルで軽量なリポジトリ分析ツールで、以下の2つの主要機能を提供します：

### 1. 📋 Repository Summary Generation

リポジトリの構造、コミット情報、ファイル統計を包括的に分析し、AIフレンドリーなマークダウンドキュメントを生成します。

**出力ファイル**: `.SourceSageAssets/Repository_summary.md`

**含まれる情報**:
- 🌳 プロジェクトツリー構造
- 📋 Gitリポジトリ情報
- 📈 ファイルサイズと行数統計
- 📝 ファイル内容の詳細

### 2. 📄 Release Report Generation (オプション機能 - 非推奨)

> ⚠️ **非推奨機能**: この機能は将来削除される予定です。LLMのコマンド実行能力の向上により、差分レポートの自動生成は不要になりつつあります。

Gitタグ間の差分を分析し、リリースレポートを自動生成します（`--diff`フラグで有効化）。

**出力ファイル**: `.SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md`

**含まれる情報**:
- 🏷️ バージョン比較
- 🔄 変更差分の詳細
- 📋 コミット履歴
  - 📂 リポジトリ基本情報（リモートURL、ブランチ、最新コミットなど）
  - 📖 READMEの内容（オプション）


## 🚀 クイックスタート

### 📦 インストール（最短）

```bash
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync
uv run sage
```

備考: パッケージとして利用する場合は `pip install sourcesage` 後に `sage`（または `sourcesage`）を実行できます。

### 🗺️ 基本的な使用方法（必要最小限）

```bash
# リポジトリサマリを生成（デフォルトは.gitignoreを使用）
uv run sage

# .SourceSageignoreファイルを使用/生成する場合
uv run sage --use-ignore

# リリースレポートを生成（オプション - 非推奨）
uv run sage --diff
```

出力先:
- Repository Summary: `.SourceSageAssets/Repository_summary.md`
- Release Report: `.SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md`（`--diff`使用時のみ）

よく使うオプション（抜粋）:

```bash
uv run sage -o ./out                     # 出力先を変更
uv run sage --ignore-file .gitignore     # 無視ルールを指定（デフォルト）
uv run sage --use-ignore                 # .SourceSageignoreを使用/生成
uv run sage --diff                       # 差分レポート生成（非推奨）
```

メモ:

- v7.2.0以降、デフォルトでは`.gitignore`を使用します。カスタムignoreファイルが必要な場合は`--use-ignore`を使用してください。
- `--language-map`を省略すると、同梱デフォルト（`sourcesage/config/`）を自動的に利用します。
- Release Reportはタグが2つ以上ある場合に生成されます（`--diff`使用時のみ）。

### 🔄 アップグレード

```bash
# PyPIからインストールしている場合
pip install --upgrade sourcesage

# git cloneしている場合
git pull origin main

# uvをローカルクローンで使用している場合
uv sync
```

### 🔍 トラブルシューティング

#### uvxのキャッシュ問題

`uvx sourcesage`で古いバージョンが使われる場合、キャッシュをクリアしてください：

```bash
# 強制リフレッシュ（推奨）
uvx --refresh sourcesage --repo tmp

# uvのキャッシュをすべてクリア
uv cache clean

# 特定のパッケージのキャッシュのみクリア
uv cache clean sourcesage

# キャッシュを使わずに実行
uvx --no-cache sourcesage --repo tmp
```

#### キャッシュ管理

```bash
# キャッシュサイズを確認
uv cache size

# キャッシュディレクトリの場所を確認
uv cache dir

# 使われていないキャッシュを削除
uv cache prune
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

    ## 📊 Project Statistics

    - 📅 Created: 2025-02-02 16:22:31
    - 📁 Total directories: 5
    - 📄 Total files: 15
    - 📏 Max depth: 3

    ### 📊 File Size and Line Count

    | File | Size | Lines | Language |
    |------|------|-------|----------|
    | pyproject.toml | 1.2 KB | 30 | TOML |
    | **Total** |  | **1234** |  |

    ### 📈 Language Statistics

    | Language | Files | Total Lines | Total Size |
    |----------|-------|-------------|-----------|
    | Python | 15 | 1234 | 45.6 KB |
    | Markdown | 3 | 150 | 5.2 KB |
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

```bash
# 1) リポジトリサマリを出力（デフォルト: .gitignore使用）
uv run sage

# 2) .SourceSageignoreを使用してサマリを出力
uv run sage --use-ignore

# 3) 差分レポートを生成（非推奨機能）
uv run sage --diff

# 4) 出力先を変更
uv run sage -o ./analysis
```

## 貢献

SourceSageの改善にご協力ください！バグの報告や機能追加の提案がある場合は、[GitHubリポジトリ](https://github.com/Sunwood-ai-labs/SourceSage)でIssueを開くかプルリクエストを送信してください。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

---

<p align="center">
<a href="https://orynth.dev/projects/sourcesage" target="_blank" rel="noopener">
  <img src="https://orynth.dev/api/badge/sourcesage?theme=light&style=default" alt="Featured on Orynth" width="260" height="80" />
</a>
</p>

## 公式リンクと検証 (SSAGE)

- **Orynth プロジェクト**: https://www.orynth.dev/projects/sourcesage
- **GitHub リポジトリ**: https://github.com/Sunwood-ai-labs/SourceSage

**SSAGE** (Solana mint):
`1QaAfN81sYjenLGeiPa9NW1s6FND4A36R3ASKKxVory`

**プライマリプール** (SSAGE/USDC, Meteora):
https://www.geckoterminal.com/solana/pools/A4oHVtJxGRRYvqfRuUGPwfxFVdBmPJnYZtcqew5Y8HoH

**Dexscreener**:
https://dexscreener.com/solana/a4ohvtjxgrryvqfruugpwfxfvdbmpjnyztcqew5y8hoh

> **注意**: SSAGEは、Orynth上のSourceSageプロジェクトのコミュニティマーケットトークン/識別子です。株式、所有権、またはプロジェクトに対する請求権ではありません。投資助言ではありません。
