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
