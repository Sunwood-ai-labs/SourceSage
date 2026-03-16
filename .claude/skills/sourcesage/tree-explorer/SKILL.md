---
name: sourcesage-tree
description: |
  Quick repository tree with file statistics.
  Use for initial codebase exploration or when you need
  to see project structure at a glance.
allowed-tools: Bash(sage:*)
---

# SourceSage Tree Explorer

リポジトリのツリー構造と統計を素早く取得します。

## 使用方法

### 従来のツリー形式（人間が読みやすい）

```bash
sage --agent-mode tree --show-lines --format tree
```

出力例:
```
================================================================================
Repository: my-project
================================================================================

Summary: 45 files | 12 directories | 3,842 total lines

--------------------------------------------------------------------------------
Directory Tree
--------------------------------------------------------------------------------

src/                                     [dir]     8 items
├── __init__.py                          [py]     12 lines |    245 B
├── cli.py                               [py]    449 lines | 15.2 KB  * large
├── core.py                              [py]     41 lines |  1.1 KB
└── modules/                             [dir]    10 items
    ├── source_sage.py                   [py]     89 lines |  2.8 KB
    └── DocuSum/                         [dir]     8 items
        └── docusum.py                   [py]    286 lines |  9.4 KB  * large
```

### JSON形式（プログラマブル）

```bash
sage --agent-mode tree --show-lines --format json
```

出力例:
```json
{
  "repository": "my-project",
  "summary": {
    "total_files": 45,
    "total_directories": 12,
    "total_lines": 3842,
    "total_size_bytes": 125840
  },
  "tree": [
    {
      "path": "src/cli.py",
      "type": "file",
      "language": "python",
      "lines": 449,
      "size_bytes": 15234,
      "is_large": true
    }
  ],
  "statistics": {
    "by_language": {
      "python": {"files": 15, "lines": 2100, "size_bytes": 68000}
    },
    "large_files": [
      {"path": "src/cli.py", "lines": 449}
    ]
  }
}
```

## オプション

| オプション | デフォルト | 説明 |
|-----------|-----------|------|
| `--format` | tree | 出力形式: tree, json |
| `--max-depth` | なし | ツリーの最大深度 |
| `--sort-by` | name | ソート基準: name, lines, size, modified |
| `--large-threshold` | 200 | "large"警告の行数閾値 |

## Tips

- まずツリーを見て、重要そうなファイル（行数が多い、エントリーポイント等）を特定
- その後 `/sourcesage` でファイル内容を取得
- JSON形式はフィルタリングや後続処理に最適
