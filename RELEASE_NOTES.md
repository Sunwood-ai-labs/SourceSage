<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/assets/release-header-v7.2.0.svg" alt="v7.2.0 Release"/>

# v7.2.0 - 多言語対応とリリース通知自動化 / Multilingual Support & Release Notification Automation

**リリース日 / Release Date:** 2025-01-15

---

## 日本語 / Japanese

### 概要

SourceSage v7.2.0 は、**多言語対応**と**リリース通知自動化**に焦点を当てたメジャーアップデートです。

CLI で英語と日本語の出力を選択可能になり、.gitignore と .SourceSageignore を統合した高度な無視ファイル処理が実装されました。さらに、GitHub Actions で Discord と X (Twitter) へのリリース通知を自動化するワークフローが追加されました。

### 新機能

- **🌐 多言語CLI対応**
  - `-l/--lang/--language` オプションで英語 (`en`) または日本語 (`ja`) を選択可能
  - デフォルト言語は `en` に変更
  - CLI のヘルプメッセージを英語に統一

- **🤖 リリース通知自動化**
  - GitHub Actions ワークフローで Discord へのリリース通知を自動送信
  - GitHub Actions ワークフローで X (Twitter) へのリリース通知を自動送信
  - AI 要約機能対応（OpenAI/OpenRouter API）
  - 手動実行（workflow_dispatch）に対応

- **📝 無視ファイルの改善**
  - .gitignore と .SourceSageignore を統合してパターンマッチング
  - デフォルトの無視ファイルを .gitignore から .SourceSageignore に変更
  - パッケージ同梱のデフォルト .SourceSageignore を使用可能

### バグ修正

- **🔧 依存関係の更新**
  - uv.lock の更新

### 変更

- **♻️ リファクタリング**
  - File Pattern Matcher のロジックを簡素化
  - 無視ファイルの初期化処理を改善

- **🧪 テスト強化**
  - 言語オプションのテストを追加
  - .SourceSageignore ハンドリングのテストを追加
  - テストドキュメント（英語・日本語）を追加

### アップグレード方法

```bash
# Git タグからアップグレード
git fetch --tags
git checkout v7.2.0

# または最新の main ブランチから
git pull origin main
```

### Breaking Changes

- デフォルトの無視ファイルが `.gitignore` から `.SourceSageignore` に変更されました
  - 既存の `.gitignore` を引き続き使用する場合は、`--ignore-file .gitignore` オプションを使用してください
  - またはプロジェクトルートに `.SourceSageignore` を作成してください

---

## English

### Overview

SourceSage v7.2.0 is a major update focused on **multilingual support** and **release notification automation**.

The CLI now supports English and Japanese output selection, advanced ignore file handling that integrates .gitignore and .SourceSageignore, and GitHub Actions workflows for automated release notifications to Discord and X (Twitter).

### What's New

- **🌐 Multilingual CLI Support**
  - Select English (`en`) or Japanese (`ja`) with `-l/--lang/--language` option
  - Default language changed to `en`
  - Unified all CLI help messages to English

- **🤖 Release Notification Automation**
  - Automated Discord release notifications via GitHub Actions
  - Automated X (Twitter) release notifications via GitHub Actions
  - AI summarization support (OpenAI/OpenRouter APIs)
  - Manual workflow dispatch support

- **📝 Improved Ignore File Handling**
  - Merges .gitignore and .SourceSageignore for pattern matching
  - Changed default ignore file from .gitignore to .SourceSageignore
  - Package-bundled default .SourceSageignore now available

### Bug Fixes

- **🔧 Dependency Updates**
  - Updated uv.lock

### Changes

- **♻️ Refactoring**
  - Simplified File Pattern Matcher logic
  - Improved ignore file initialization

- **🧪 Enhanced Testing**
  - Added language option tests
  - Added .SourceSageignore handling tests
  - Added test documentation (English & Japanese)

### Upgrade

```bash
# Upgrade from Git tag
git fetch --tags
git checkout v7.2.0

# Or from latest main branch
git pull origin main
```

### Breaking Changes

- Default ignore file changed from `.gitignore` to `.SourceSageignore`
  - To continue using `.gitignore`, use the `--ignore-file .gitignore` option
  - Or create a `.SourceSageignore` file in your project root

---

## Detailed Changes

### Files Changed
- **13 files changed**: 889 insertions(+), 98 deletions(-)
- New GitHub Actions workflows for release notifications
- Enhanced multilingual support across CLI and documentation

### Key Files
- `sourcesage/cli.py`: Multi-language support (212 lines changed)
- `sourcesage/modules/DocuSum/docusum.py`: Language parameter and ignore handling (98 lines changed)
- `.github/workflows/release-to-discord.yml`: Discord notification workflow (new)
- `.github/workflows/release-to-x.yml`: X (Twitter) notification workflow (new)
- `tests/test_language_and_ignore.py`: New test suite (241 lines)

### コントリビューター / Contributors

@Claude (Anthropic)

---

**[Full Changelog](https://github.com/Sunwood-ai-labs/SourceSage/compare/v7.1.1...v7.2.0)**
