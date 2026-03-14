# 出力ガイド

## 標準の出力構成

通常実行では次のファイルを生成します。

```text
.SourceSageAssets/
  Repository_summary.md
```

`--diff` を有効にし、必要なタグが揃っている場合は次も生成されます。

```text
.SourceSageAssets/
  RELEASE_REPORT/
    Report_<latest_tag>.md
```

## 主要ドキュメント成果物に含まれる内容

- プロジェクト名とツリー構造
- `.git` ディレクトリがある場合の Git 情報
- ファイル統計と言語統計
- 除外されていないファイルの抜粋

## 生成例

サンプルのドキュメント成果物は [`example/Repository_summary.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/example/Repository_summary.md) にあります。
