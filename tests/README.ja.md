# SourceSage テスト

## テスト概要

このディレクトリには SourceSage の機能テストが含まれています。

## テストファイル

### 1. `test_cli.py`
CLI 引数パース、既定動作、ignore ファイル生成、バージョン表示のテスト。

**テスト数:** 21

### 2. `test_language_and_ignore.py`
言語切り替えと `.gitignore` / `.SourceSageignore` の統合処理のテスト。

**テスト数:** 18

### 3. `test_git_info.py`
Git コマンド実行、リポジトリ情報取得、タグ処理、diff レポート前提条件のテスト。

**テスト数:** 12

### 4. `test_e2e.py`
一時リポジトリを使った CLI のエンドツーエンドテスト。

**テスト数:** 5

### 5. `test_docusum_markdown_structure.py`
Repository Summary の構造、表、UTF-8 出力、除外挙動のテスト。

**テスト数:** 12

## 検証スナップショット

今回の整備でローカル検証したコマンド:

```bash
uv run pytest -q
```

結果:

- 68 テスト成功
- 0 テスト失敗

## テストの実行

### すべてのテストを実行:
```bash
uv run pytest tests/ -v
```

### 特定のテストファイルを実行:
```bash
uv run pytest tests/test_cli.py -v
uv run pytest tests/test_language_and_ignore.py -v
```

### 特定のテストクラスを実行:
```bash
uv run pytest tests/test_language_and_ignore.py::TestLanguageOption -v
```

### カバレッジ付きで実行:
```bash
uv run pytest tests/ --cov=sourcesage --cov-report=html
```

## 主なカバレッジ

### 1. CLI の振る舞い
- 引数パース、出力先、レポート関連フラグ、バージョン表示
- `sage` と `sourcesage` の両エントリポイントの後方互換性

### 2. 言語と ignore 処理
- 英語 / 日本語の既定値と明示指定
- `.gitignore` と `.SourceSageignore` の統合挙動
- ワイルドカード、ディレクトリ、include パターンの判定

### 3. Git と diff レポート前提条件
- コマンド実行の成功系と失敗系
- ブランチ、コミット、タグの取得
- diff レポート前提が足りない場合の安全な扱い

### 4. エンドツーエンド出力
- 一時リポジトリでの Repository Summary 生成
- カスタム出力先と言語切り替え
- `.SourceSageignore` の自動生成と再利用

### 5. Markdown 品質
- 必須見出しと統計テーブル
- UTF-8 出力とプロジェクト名
- 除外対象ファイルや `.git` の非掲載
