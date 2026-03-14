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

## `--lite` の違い

`--lite` を付けて実行した場合も、同じ `Repository_summary.md` に次は残ります。

- プロジェクト名とツリー構造
- 利用可能なら Git 情報
- ファイル統計と言語統計
- ルート README のみ

その代わり、全文抜粋を並べる `## File Contents` セクションは生成しません。初回探索でサマリーが大きくなりすぎるのを避けるための軽量モードです。

## 生成例

サンプルのドキュメント成果物は [`example/Repository_summary.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/example/Repository_summary.md) にあります。
