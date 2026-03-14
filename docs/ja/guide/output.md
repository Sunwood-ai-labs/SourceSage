# 出力ガイド

## 標準の出力構成

通常実行では次の構成で出力されます。

```text
.SourceSageAssets/
└── Repository_summary.md
```

`--diff` を有効にし、十分なタグがある場合は次も生成できます。

```text
.SourceSageAssets/
└── RELEASE_REPORT/
    └── Report_<latest_tag>.md
```

## Repository summary に含まれる内容

- プロジェクト名とツリー構造
- `.git` がある場合の Git 情報
- ファイル統計と言語統計
- 除外対象ではないファイルの抜粋

## 出力サンプル

サンプルは [`example/Repository_summary.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/example/Repository_summary.md) にあります。
