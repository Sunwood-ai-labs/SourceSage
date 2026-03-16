# SourceSage Agent Mode Workflow

このドキュメントでは、AIエージェントがSourceSageを効果的に使用するためのワークフローを説明します。

## 推奨ワークフロー

### Phase 1: 構造把握（コンテキスト最小）

```bash
# Step 1: ツリー構造のみを取得（内容なし）
sage --agent-mode tree --show-lines --format tree
```

このステップでは:
- ファイル内容を読み込まない
- リポジトリ全体の構造を把握
- 各ファイルの行数を確認
- 大きなファイル（200行以上）にマークがつく

### Phase 2: 選択的取得（必要なファイルのみ）

```bash
# Step 2a: 特定のファイルを取得
sage --agent-mode files --files "src/cli.py,src/core.py"

# Step 2b: パターンで取得
sage --agent-mode files --pattern "**/*.py" --exclude-pattern "**/test_*.py"

# Step 2c: 行数でフィルタ
sage --agent-mode files --min-lines 50 --max-lines 300
```

### Phase 3: 必要に応じて全体取得（制限付き）

```bash
# Step 3: コンテキスト制限付きで全体を取得
sage --agent-mode full \
  --max-total-lines 5000 \
  --max-file-lines 500 \
  --truncate-strategy middle \
  --priority-files "*.py" \
  --exclude-large
```

## JSON形式の活用

JSON出力を使用して、プログラマブルにファイルを選択できます：

```python
import json
import subprocess

# ツリーをJSON形式で取得
result = subprocess.run(
    ["sage", "--agent-mode", "tree", "--format", "json"],
    capture_output=True,
    text=True
)
data = json.loads(result.stdout)

# 200行以上のPythonファイルを抽出
large_py_files = [
    f["path"] for f in data["tree"]
    if f["type"] == "file"
    and f.get("language") == "python"
    and f.get("lines", 0) >= 200
]

# 必要なファイルを取得
files_arg = ",".join(large_py_files)
subprocess.run(["sage", "--agent-mode", "files", "--files", files_arg])
```

## コンテキスト管理のベストプラクティス

### 推奨制限値

| 項目 | 推奨値 | 理由 |
|-----|-------|------|
| 全体行数 | 5,000行以下 | LLMコンテキストの15-20%を超えない |
| ファイル行数 | 500行以下 | 1ファイルで圧迫しない |
| large閾値 | 200行 | 一般的なモジュールサイズ |

### 切り詰め戦略の選択

| 戦略 | 使用場面 |
|------|---------|
| `head` | クラス定義やインポートを見たい時 |
| `tail` | 最近の変更や末尾の関数を見たい時 |
| `middle` | 全体構造を把握したい時（推奨デフォルト） |

## トラブルシューティング

### 出力が大きすぎる場合

```bash
# 1. まずツリーで構造を確認
sage --agent-mode tree

# 2. 必要最小限のファイルを特定して取得
sage --agent-mode files --files "core.py,main.py"
```

### 特定のファイルが見つからない場合

```bash
# パターンで検索
sage --agent-mode tree --format json | grep -i "filename"
```

### コンテキストがまだ大きい場合

```bash
# より厳しい制限を適用
sage --agent-mode full \
  --max-total-lines 2000 \
  --max-file-lines 200 \
  --exclude-large
```

## CLIリファレンス

### 共通オプション

| オプション | 説明 |
|-----------|------|
| `--repo` | 対象リポジトリパス（デフォルト: ./） |
| `--format` | 出力形式: tree, json |
| `--ignore-file` | 無視パターンファイルのパス |

### tree モードオプション

| オプション | 説明 |
|-----------|------|
| `--max-depth` | ツリーの最大深度 |
| `--show-lines` | 行数を表示 |
| `--show-size` | ファイルサイズを表示 |
| `--sort-by` | ソート基準: name, lines, size, modified |
| `--large-threshold` | "large"マークの閾値（行数） |

### files モードオプション

| オプション | 説明 |
|-----------|------|
| `--files` | カンマ区切りのファイルパス |
| `--pattern` | 含めるglobパターン |
| `--exclude-pattern` | 除外するglobパターン |
| `--min-lines` | 最小行数フィルタ |
| `--max-lines` | 最大行数フィルタ |
| `--max-file-lines` | 出力する最大行数/ファイル |

### full モードオプション

| オプション | 説明 |
|-----------|------|
| `--max-total-lines` | 全体の最大行数 |
| `--max-file-lines` | ファイルごとの最大行数 |
| `--truncate-strategy` | 切り詰め戦略: head, tail, middle |
| `--priority-files` | 優先するファイルパターン |
| `--exclude-large` | 大きなファイルを自動除外 |
