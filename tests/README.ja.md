# SourceSage テスト

## テスト概要

このディレクトリには SourceSage の機能テストが含まれています。

## テストファイル

### 1. `test_cli.py`
CLI 引数パースと基本機能のテスト。

**テストクラス:**
- `TestCLIArguments` - CLI 引数パースのテスト
- `TestSourceSageignoreGeneration` - .SourceSageignore ファイル生成のテスト
- `TestCLIOptions` - 様々な CLI オプションのテスト
- `TestBackwardCompatibility` - 後方互換性のテスト

**テスト数:** 16

### 2. `test_language_and_ignore.py`
言語オプションと ignore ファイルマージ機能のテスト。

**テストクラス:**
- `TestLanguageOption` - `--language` オプション (en/ja) のテスト
- `TestIgnoreFileMerging` - .gitignore と .SourceSageignore のマージのテスト
- `TestFilePatternMatcherFunctionality` - FilePatternMatcher 機能のテスト
- `TestBackwardCompatibility` - 単一ファイル入力との後方互換性のテスト

**テスト数:** 14

## テスト結果

### 最新テスト実行 (2026-01-15)

```
============================= test session starts ==============================
platform linux -- Python 3.13.9, pytest-8.4.1, pluggy-1.6.0
collected 30 items

tests/test_cli.py::TestCLIArguments::test_short_output_option PASSED     [  3%]
tests/test_cli.py::TestCLIArguments::test_long_output_option PASSED      [  6%]
tests/test_cli.py::TestCLIArguments::test_diff_option PASSED             [ 10%]
tests/test_cli.py::TestCLIArguments::test_use_ignore_option PASSED       [ 13%]
tests/test_cli.py::TestCLIArguments::test_default_values PASSED          [ 16%]
tests/test_cli.py::TestCLIArguments::test_diff_output_option PASSED      [ 20%]
tests/test_cli.py::TestCLIArguments::test_combined_options PASSED        [ 23%]
tests/test_cli.py::TestSourceSageignoreGeneration::test_sourcesageignore_template_exists PASSED [ 26%]
tests/test_cli.py::TestSourceSageignoreGeneration::test_sourcesageignore_has_sections PASSED [ 30%]
tests/test_cli.py::TestSourceSageignoreGeneration::test_sourcesageignore_has_venv_patterns PASSED [ 33%]
tests/test_cli.py::TestSourceSageignoreGeneration::test_sourcesageignore_has_lock_files PASSED [ 36%]
tests/test_cli.py::TestCLIOptions::test_repo_path_option PASSED          [ 40%]
tests/test_cli.py::TestCLIOptions::test_report_title_option PASSED       [ 43%]
tests/test_cli.py::TestCLIOptions::test_ignore_file_option PASSED        [ 46%]
tests/test_cli.py::TestBackwardCompatibility::test_sourcesage_command_name_in_pyproject PASSED [ 50%]
tests/test_cli.py::TestBackwardCompatibility::test_old_options_removed PASSED [ 53%]
tests/test_language_and_ignore.py::TestLanguageOption::test_language_option_default PASSED [ 56%]
tests/test_language_and_ignore.py::TestLanguageOption::test_language_option_english PASSED [ 60%]
tests/test_language_and_ignore.py::TestLanguageOption::test_language_option_japanese PASSED [ 63%]
tests/test_language_and_ignore.py::TestLanguageOption::test_language_option_invalid PASSED [ 66%]
tests/test_language_and_ignore.py::TestIgnoreFileMerging::test_single_ignore_file PASSED [ 70%]
tests/test_language_and_ignore.py::TestIgnoreFileMerging::test_multiple_ignore_files PASSED [ 73%]
tests/test_language_and_ignore.py::TestIgnoreFileMerging::test_gitignore_and_sourcesageignore_merge PASSED [ 76%]
tests/test_language_and_ignore.py::TestIgnoreFileMerging::test_sourcesageignore_has_uv_lock PASSED [ 80%]
tests/test_language_and_ignore.py::TestIgnoreFileMerging::test_packaged_sourcesageignore_has_uv_lock PASSED [ 83%]
tests/test_language_and_ignore.py::TestFilePatternMatcherFunctionality::test_default_patterns PASSED [ 86%]
tests/test_language_and_ignore.py::TestFilePatternMatcherFunctionality::test_pattern_matching_wildcards PASSED [ 90%]
tests/test_language_and_ignore.py::TestFilePatternMatcherFunctionality::test_directory_patterns PASSED [ 93%]
tests/test_language_and_ignore.py::TestFilePatternMatcherFunctionality::test_include_patterns PASSED [ 96%]
tests/test_language_and_ignore.py::TestBackwardCompatibility::test_single_file_still_works PASSED [100%]

============================== 30 passed in 0.41s ==============================
```

**サマリー:**
- **総テスト数:** 30
- **成功:** 30
- **失敗:** 0
- **スキップ:** 0
- **成功率:** 100%

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

## テストされる主な機能

### 1. 言語オプション
- デフォルト言語は `en` (英語)
- `--language ja` オプションで日本語に切り替え
- 無効な言語オプションは拒否される

### 2. Ignore ファイルのマージ
- `.gitignore` と `.SourceSageignore` が正しくマージされる
- 両方のファイルのパターンが尊重される
- `uv.lock` は `.SourceSageignore` 経由で正しく除外される

### 3. ファイルパターンマッチング
- デフォルトパターンが正しく動作
- ワイルドカードパターン (`*.pyc`, `*.log`) が期待通り動作
- ディレクトリパターン (`__pycache__/`, `node_modules/`) が正しく動作
- インクルードパターン（否定）がサポートされている

### 4. 後方互換性
- 単一ファイルパスが `FilePatternMatcher` でまだ動作する
- 既存の CLI オプションが引き続き機能する
- 削除された古いオプションは適切にエラーを出す

## 最近の改善点

1. **言語サポート**: 英語と日本語の出力をサポートする `--language` オプションを追加
2. **Ignore ファイルのマージ**: `.gitignore` と `.SourceSageignore` のマージ処理を改善
3. **より良いテスト**: 新機能の包括的なテストを追加

## 今後の改善予定

- エンドツーエンド機能の統合テストを追加
- 大規模リポジトリのパフォーマンステストを追加
- マークダウン生成品質のテストを追加
- Git 情報収集のテストを追加
- 言語検出のテストを追加
