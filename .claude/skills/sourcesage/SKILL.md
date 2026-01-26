---
name: sourcesage
description: |
  Analyze repository structure with context-aware output limits.
  Use when exploring a new codebase, understanding project structure,
  or when you need to gather code context efficiently without
  exceeding token limits.
allowed-tools: Bash(sage:*, python:*)
---

# SourceSage - Repository Structure Analyzer

SourceSageはAIエージェント向けに最適化されたリポジトリ解析ツールです。

## 基本ワークフロー

### Step 1: ツリー構造を取得（まずこれを実行）

```bash
sage --agent-mode tree --show-lines
```

これにより、ファイル内容を読み込まずにリポジトリ全体の構造と各ファイルの行数を把握できます。

### Step 2: 必要なファイルのみ取得

ツリーを確認後、重要そうなファイルのみを取得：

```bash
sage --agent-mode files --files "src/cli.py,src/core.py"
```

### Step 3: コンテキスト制限付きで全体取得（必要な場合）

```bash
sage --agent-mode full --max-total-lines 5000 --max-file-lines 500
```

## コンテキスト管理のベストプラクティス

- 全体で **5000行以下** を目安に
- 1ファイル **500行以下** を推奨
- 大きいファイルは `--truncate-strategy middle` で中間省略

## 出力形式

- `--format tree`: 従来のASCIIツリー形式（デフォルト）
- `--format json`: プログラマブルなJSON形式

## 使用例

### ツリー構造のみを確認

```bash
sage --agent-mode tree --format tree
```

### JSON形式で構造を取得（プログラマブル）

```bash
sage --agent-mode tree --format json
```

### 特定のファイルを取得

```bash
sage --agent-mode files --files "cli.py,core.py,config.py"
```

### パターンマッチでファイルを取得

```bash
sage --agent-mode files --pattern "**/*.py" --exclude-pattern "**/test_*.py"
```

### 行数でフィルタ

```bash
sage --agent-mode files --min-lines 100 --max-lines 500
```

### コンテキスト制限付き全体出力

```bash
sage --agent-mode full \
  --max-total-lines 5000 \
  --max-file-lines 500 \
  --truncate-strategy middle \
  --exclude-large
```

詳細は [workflow.md](references/workflow.md) を参照。
