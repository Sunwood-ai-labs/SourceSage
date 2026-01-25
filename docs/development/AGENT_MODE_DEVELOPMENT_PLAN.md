# SourceSage Agent Mode 開発計画書

## 概要

本計画書は、SourceSageをAIエージェント（Claude Code等）が効率的に使用できるようにするための機能拡張について定義します。主な目的は**コンテキストウィンドウの爆発を防ぎつつ、必要な情報を段階的に取得できる仕組み**を提供することです。

---

## 背景と課題

### 現状の課題

| 課題 | 詳細 |
|------|------|
| コンテキスト爆発 | 大規模リポジトリでは`Repository_summary.md`が数万行になり、LLMのコンテキストを圧迫 |
| 全か無か | 現在は全ファイル内容を出力するか、しないかの二択 |
| エージェント非対応 | CLIは人間向けで、プログラマブルな出力形式がない |
| 段階的探索不可 | ツリー構造を見てから必要なファイルだけ取得、という操作ができない |

### 目標

```
エージェントが「最小限のコンテキストで最大限の理解」を得られる仕組みを構築
```

---

## アーキテクチャ設計

### 新規モジュール構成

```
sourcesage/
├── modules/
│   ├── DocuSum/                    # 既存
│   └── AgentMode/                  # 🆕 新規モジュール
│       ├── __init__.py
│       ├── agent_output.py         # エージェント向け出力制御
│       ├── tree_with_stats.py      # ツリー＋行数統計
│       ├── file_selector.py        # ファイル選択的取得
│       ├── context_limiter.py      # コンテキスト制限管理
│       └── formats/
│           ├── markdown.py         # マークダウン形式
│           ├── json.py             # JSON形式（プログラマブル）
│           └── compact.py          # 圧縮形式
```

---

## Phase 1: コア機能 - ツリー＋行数出力

### 1.1 機能概要

ファイル内容を出力せず、**ツリー構造と各ファイルのメタ情報（行数、サイズ）のみ**を出力するモード。

### 1.2 CLIオプション

```bash
# 基本使用法
sage --agent-mode tree

# オプション
sage --agent-mode tree \
  --max-depth 3 \              # ツリーの最大深度
  --show-lines \               # 行数を表示
  --show-size \                # ファイルサイズを表示
  --sort-by lines \            # ソート基準: lines|size|name|modified
  --format markdown            # 出力形式: markdown|json|compact
```

### 1.3 出力例（Markdown形式）

```markdown
# Repository Tree: SourceSage

📊 **Summary**: 45 files, 12 directories, 3,842 total lines

```
sourcesage/                          [dir]  8 items
├── __init__.py                      [py]   12 lines
├── cli.py                           [py]   449 lines
├── core.py                          [py]   41 lines
├── config/                          [dir]  3 items
│   ├── constants.py                 [py]   15 lines
│   └── language_map.json            [json] 45 lines
└── modules/                         [dir]  10 items
    ├── source_sage.py               [py]   89 lines
    └── DocuSum/                     [dir]  8 items
        ├── docusum.py               [py]   286 lines  ⚠️ large
        ├── tree_generator.py        [py]   101 lines
        └── ...
```
```

### 1.4 出力例（JSON形式）

```json
{
  "repository": "SourceSage",
  "summary": {
    "total_files": 45,
    "total_directories": 12,
    "total_lines": 3842
  },
  "tree": [
    {
      "path": "sourcesage/__init__.py",
      "type": "file",
      "language": "python",
      "lines": 12,
      "size": 245
    },
    {
      "path": "sourcesage/cli.py",
      "type": "file",
      "language": "python",
      "lines": 449,
      "size": 15234
    }
  ]
}
```

### 1.5 実装タスク

- [ ] `AgentMode/tree_with_stats.py` - ツリー＋統計生成クラス
- [ ] `AgentMode/formats/markdown.py` - Markdown形式出力
- [ ] `AgentMode/formats/json.py` - JSON形式出力
- [ ] `cli.py` に `--agent-mode` 引数追加
- [ ] テスト作成

---

## Phase 2: コンテキスト制限機能

### 2.1 機能概要

出力の**総行数**と**1ファイルあたりの最大行数**を制限するオプション。

### 2.2 CLIオプション

```bash
sage --agent-mode full \
  --max-total-lines 5000 \     # 全体の最大行数
  --max-file-lines 500 \       # 1ファイルの最大行数
  --truncate-strategy tail \   # 切り詰め方法: head|tail|middle|summary
  --priority-files "*.py" \    # 優先的に含めるファイル
  --exclude-large              # 大きいファイルを自動除外
```

### 2.3 制限戦略

| 戦略 | 説明 |
|------|------|
| `head` | ファイルの先頭N行を表示 |
| `tail` | ファイルの末尾N行を表示 |
| `middle` | 先頭と末尾を表示、中間を省略 |
| `summary` | AIが要約（将来実装） |

### 2.4 出力例（制限適用時）

```markdown
## `sourcesage/cli.py`
**Size**: 15.2 KB | **Lines**: 449 (showing first 100)

```python
#!/usr/bin/env python3
"""SourceSage CLI - Command Line Interface"""

import argparse
import os
from pathlib import Path
...

# ⚠️ TRUNCATED: 349 more lines (use --max-file-lines to adjust)
```
```

### 2.5 実装タスク

- [ ] `AgentMode/context_limiter.py` - 制限ロジック
- [ ] 切り詰め戦略の実装（head/tail/middle）
- [ ] 優先度ベースのファイル選択
- [ ] 警告メッセージの生成
- [ ] テスト作成

---

## Phase 3: 選択的ファイル取得

### 3.1 機能概要

特定のファイルやパターンにマッチするファイルのみを取得するモード。

### 3.2 CLIオプション

```bash
# 特定ファイルを取得
sage --agent-mode files \
  --files "sourcesage/cli.py,sourcesage/core.py"

# パターンマッチ
sage --agent-mode files \
  --pattern "**/*.py" \
  --exclude-pattern "**/test_*.py"

# 行数フィルタ
sage --agent-mode files \
  --min-lines 100 \            # 100行以上のファイルのみ
  --max-lines 500              # 500行以下のファイルのみ
```

### 3.3 エージェント向けワークフロー

```
Step 1: ツリー取得
  $ sage --agent-mode tree --show-lines --format json
  → ファイル一覧と行数を確認

Step 2: 重要ファイルを選択的取得
  $ sage --agent-mode files --files "cli.py,core.py"
  → 必要なファイルのみ取得

Step 3: 追加で必要なファイルを取得
  $ sage --agent-mode files --pattern "**/test_*.py"
  → テストファイルを追加取得
```

### 3.4 実装タスク

- [ ] `AgentMode/file_selector.py` - ファイル選択ロジック
- [ ] パターンマッチング機能
- [ ] 行数フィルタリング
- [ ] 複数パターンの組み合わせ
- [ ] テスト作成

---

## Phase 4: Claude Code Skills 統合

### 4.1 Skills形式での提供

```yaml
# .claude/skills/sourcesage.yaml
name: sourcesage
description: Repository structure analyzer for AI agents
version: 1.0.0

commands:
  - name: tree
    description: Get repository tree with file statistics
    usage: sage --agent-mode tree [options]

  - name: files
    description: Get specific files content
    usage: sage --agent-mode files --files <paths>

  - name: summary
    description: Get repository summary within context limits
    usage: sage --agent-mode full --max-total-lines <n>
```

### 4.2 推奨ワークフロー（Skills説明用）

```markdown
## SourceSage - Repository Explorer

### コードベース探索の手順

1. **まずツリーを取得**
   ```bash
   sage --agent-mode tree --show-lines --format markdown
   ```
   → 全体構造と各ファイルの行数を把握

2. **重要そうなファイルを特定**
   - エントリーポイント（cli.py, main.py, index.ts など）
   - 行数が多いファイル（コア機能の可能性大）
   - 設定ファイル

3. **選択的にファイル内容を取得**
   ```bash
   sage --agent-mode files --files "src/cli.py,src/core.py"
   ```

4. **必要に応じて追加取得**
   ```bash
   sage --agent-mode files --pattern "src/modules/*.py"
   ```

### コンテキスト管理のベストプラクティス

- 全体で5000行以下を目安に
- 1ファイル500行以下を推奨
- 大きいファイルは `--truncate-strategy middle` で中間省略
```

### 4.3 実装タスク

- [ ] Skills YAML定義ファイル作成
- [ ] ドキュメント整備
- [ ] サンプルワークフロー作成
- [ ] Claude Code との統合テスト

---

## Phase 5: 高度な機能（将来）

### 5.1 インテリジェント要約

```bash
sage --agent-mode smart \
  --context-budget 4000 \      # 使用可能なトークン数
  --focus "authentication"     # 注目するトピック
```

→ 指定トークン数内で最も関連性の高い情報を自動選択

### 5.2 差分モード

```bash
sage --agent-mode diff \
  --since "HEAD~5" \           # 最近5コミットの変更
  --max-lines 2000
```

→ 最近の変更のみを効率的に取得

### 5.3 依存関係グラフ

```bash
sage --agent-mode deps \
  --entry "src/cli.py" \       # エントリーポイント
  --depth 2                    # 依存の深さ
```

→ 指定ファイルからの依存関係を可視化

---

## 実装優先度マトリクス

| Phase | 機能 | 重要度 | 難易度 | 優先度 |
|-------|------|--------|--------|--------|
| 1 | ツリー＋行数出力 | ⭐⭐⭐ | ⭐⭐ | **P0** |
| 2 | コンテキスト制限 | ⭐⭐⭐ | ⭐⭐ | **P0** |
| 3 | 選択的ファイル取得 | ⭐⭐⭐ | ⭐⭐ | **P1** |
| 4 | Skills統合 | ⭐⭐ | ⭐ | **P1** |
| 5 | 高度な機能 | ⭐ | ⭐⭐⭐ | **P2** |

---

## 技術仕様

### 出力形式

| 形式 | 用途 | ファイル |
|------|------|----------|
| `markdown` | 人間＆LLM両方が読みやすい | `*.md` |
| `json` | プログラマブルな処理 | `*.json` |
| `compact` | 最小コンテキスト | テキスト |

### デフォルト制限値

```python
DEFAULT_LIMITS = {
    "max_total_lines": 10000,      # 全体の最大行数
    "max_file_lines": 1000,        # 1ファイルの最大行数
    "max_depth": None,             # ツリー深度（無制限）
    "truncate_strategy": "middle", # 切り詰め方法
    "large_file_threshold": 500,   # "large"警告の閾値
}
```

### エラーハンドリング

```python
class AgentModeError(Exception):
    """Agent mode specific errors"""
    pass

class ContextLimitExceeded(AgentModeError):
    """Raised when context limit would be exceeded"""
    pass

class FileNotFoundError(AgentModeError):
    """Raised when specified file doesn't exist"""
    pass
```

---

## テスト計画

### ユニットテスト

```
tests/
└── agent_mode/
    ├── test_tree_with_stats.py
    ├── test_context_limiter.py
    ├── test_file_selector.py
    └── test_formats/
        ├── test_markdown.py
        └── test_json.py
```

### 統合テスト

- 小規模リポジトリ（<100ファイル）
- 中規模リポジトリ（100-1000ファイル）
- 大規模リポジトリ（>1000ファイル）

### E2Eテスト

- Claude Code からの実際の使用シナリオ
- コンテキスト制限の効果測定

---

## マイルストーン

### MVP (Minimum Viable Product)

- [x] ~~調査・設計~~
- [ ] Phase 1: ツリー＋行数出力
- [ ] Phase 2: コンテキスト制限

### v1.0

- [ ] Phase 3: 選択的ファイル取得
- [ ] Phase 4: Skills統合
- [ ] ドキュメント整備

### v2.0

- [ ] Phase 5: 高度な機能
- [ ] パフォーマンス最適化
- [ ] 追加フォーマット対応

---

## 関連ファイル

| ファイル | 行数 | 役割 |
|---------|------|------|
| `sourcesage/cli.py` | 449 | CLIエントリーポイント（修正必要） |
| `sourcesage/modules/DocuSum/tree_generator.py` | 101 | 既存ツリー生成（参考） |
| `sourcesage/modules/DocuSum/file_processor.py` | 131 | 既存ファイル処理（参考） |
| `sourcesage/modules/DocuSum/stats_collector.py` | 67 | 既存統計収集（参考） |

---

## 次のステップ

1. この計画書のレビュー・承認
2. Phase 1 の実装開始
3. テスト環境の準備
4. 段階的リリース

---

*作成日: 2026-01-25*
*対象バージョン: v7.3.0 (予定)*
