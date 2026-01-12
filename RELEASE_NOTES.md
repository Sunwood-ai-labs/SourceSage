<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/assets/release-header-v7.1.0.svg" alt="v7.1.0 Release"/>

# v7.1.0 - 洗練された進化 / Refined Evolution

**リリース日 / Release Date:** 2026-01-13

---

## 日本語 / Japanese

### 概要

v7.1.0では、CLIの大幅な簡素化と使いやすさの向上、ドキュメント構造の整理、そして国際化対応を実現しました。コマンド名を`sage`に変更し、デフォルト動作を改善することで、より直感的で堅牢なツールへと進化しています。

### 新機能

- **✨ バイリンガルREADMEサポート**: 英語版と日本語版のREADMEを提供し、国際的なユーザーベースに対応
- **✨ Orynthバッジの追加**: READMEにOrynthバッジとSSAGEトークン情報を追加
- **✨ オプショナルな差分レポート生成**: 差分レポートの生成をオプション化し、デフォルトで.gitignoreを使用
- **✨ 改善された無視ファイル処理**: .SourceSageignoreをカレントワーキングディレクトリ(CWD)デフォルトに変更し、指定パスを尊重

### 改善・変更

- **🔧 DiffReportの堅牢性向上**: タグ取得や差分生成が失敗した場合に警告を出力してスキップするように改善
- **🔄 CLIの簡素化**: コマンド名を`ss`から`sage`に変更し、`--ss-mode`引数を削除してシンプルに
- **🔄 .SourceSageignoreファイルの整理**: 無視ファイルの構成を整理し、より管理しやすく改善
- **🔄 ドキュメントフォルダのクリーンアップ**: docsフォルダを整理し、アイコンディレクトリのみを保持
- **🔄 サンプルディレクトリの整理**: 不要なサンプルを削除し、Repository_summary.mdを追加

### テスト

- **🧪 包括的なCLIテスト**: 最近の変更に対応した包括的なCLIテストを追加

### スタイル・チェック

- **🎨 Codacy静的解析の警告修正**: コード品質向上のためCodacy警告を修正

### その他

- **📦 依存関係の更新**: テスト実行後にuv.lockを更新
- **🔀 複数のマージ**: 機能ブランチの統合とリリース準備

---

## English

### Overview

v7.1.0 brings significant CLI simplification and improved usability, documentation structure reorganization, and internationalization support. By changing the command name to `sage` and improving default behaviors, the tool has evolved into a more intuitive and robust solution.

### What's New

- **✨ Bilingual README Support**: Provides both English and Japanese README files to serve an international user base
- **✨ Orynth Badge Addition**: Added Orynth badge and SSAGE token information to README
- **✨ Optional Diff Report Generation**: Made diff report generation optional and use .gitignore by default
- **✨ Improved Ignore File Handling**: Changed .SourceSageignore to use current working directory (CWD) as default and respect specified paths

### Improvements & Changes

- **🔧 Enhanced DiffReport Robustness**: Improved to output warnings and skip when tag retrieval or diff generation fails
- **🔄 CLI Simplification**: Changed command name from `ss` to `sage` and removed `--ss-mode` argument for simplicity
- **🔄 .SourceSageignore Organization**: Cleaned up and organized ignore file structure for better maintainability
- **🔄 Documentation Folder Cleanup**: Reorganized docs folder, keeping only the icon directory
- **🔄 Example Directory Cleanup**: Removed unnecessary samples and added Repository_summary.md

### Testing

- **🧪 Comprehensive CLI Tests**: Added comprehensive CLI tests covering recent changes

### Style & Quality

- **🎨 Codacy Static Analysis Fixes**: Fixed Codacy warnings to improve code quality

### Others

- **📦 Dependency Updates**: Updated uv.lock after running tests
- **🔀 Multiple Merges**: Integrated feature branches and prepared for release

---

## Detailed Changes

### Files Changed
- **40 files changed**: 2,124 insertions(+), 6,298 deletions(-)
- Major documentation cleanup with removal of obsolete samples and reorganization
- CLI interface modernization with simplified command structure
- Enhanced internationalization support

### Key Files
- `sourcesage/cli.py`: Major CLI refactoring (133 lines changed)
- `README.md` & `README.ja.md`: Bilingual documentation support
- `sourcesage/modules/DiffReport/git_diff.py`: Improved error handling
- `tests/test_cli.py`: New comprehensive test suite (184 lines)

### Contributors
- maki
- Claude

---

**Full Changelog**: https://github.com/Sunwood-ai-labs/SourceSage/compare/v7.0.2...v7.1.0
