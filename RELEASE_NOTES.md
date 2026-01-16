# v7.2.1 - Bug Fix & Workflow Improvements / バグ修正とワークフロー改善

**Release Date:** 2026-01-16

---

## Japanese

### 概要
i18nのバグ修正とリリース通知ワークフローの改善を含むマイナーアップデート。

### バグ修正
- **i18n**: Repository Summaryの出力に含まれていたハードコードされた日本語テキストを英語に統一
  - `markdown_writer.py` 内のすべての日本語ラベルを英語に変更
  - "Gitリポジトリ情報" → "Git Repository Information"
  - "基本情報" → "Basic Information"
  - "最新のコミット" → "Latest Commit"
  - その他すべてのセクション見出しとラベル

### ワークフロー改善
- **release-to-discord.yml** の更新:
  - `release-note-x` リポジトリをクローンして使用するように変更
  - `workflow_dispatch` （手動実行）時のパラメータ処理を改善
  - AI要約の実行条件を `workflow_dispatch` のみに変更
  - リリースノートを一時ファイルで安全に処理
  - クリーンアップ処理を追加

- **release-to-x.yml** の更新:
  - 上記と同様の改善を適用

### ドキュメント
- **README.md / README.ja.md**: アップグレードガイドとトラブルシューティングセクションを追加

### その他
- **.SourceSageignore**: パス追加
- **RELEASE_NOTES.md**: 削除（リリースプロセスの簡素化）

---

## English

### Overview
Minor update including i18n bug fixes and improvements to release notification workflows.

### Bug Fixes
- **i18n**: Unified hardcoded Japanese text in Repository Summary output to English
  - Changed all Japanese labels in `markdown_writer.py` to English
  - "Gitリポジトリ情報" → "Git Repository Information"
  - "基本情報" → "Basic Information"
  - "最新のコミット" → "Latest Commit"
  - All other section headings and labels

### Workflow Improvements
- **Updated release-to-discord.yml**:
  - Changed to clone and use `release-note-x` repository
  - Improved parameter handling for `workflow_dispatch` (manual execution)
  - Changed AI summarization execution condition to `workflow_dispatch` only
  - Safe handling of release notes using temp files
  - Added cleanup process

- **Updated release-to-x.yml**:
  - Applied the same improvements as above

### Documentation
- **README.md / README.ja.md**: Added upgrade guide and troubleshooting sections

### Other
- **.SourceSageignore**: Added paths
- **RELEASE_NOTES.md**: Removed (simplified release process)
