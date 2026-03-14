# 出力ファイル

## Repository Summary

デフォルト出力先:

```text
.SourceSageAssets/Repository_summary.md
```

このサマリには次が含まれます。

- リポジトリツリー
- Git 情報
- プロジェクト統計
- ファイル一覧テーブル
- 言語統計
- ファイル内容の抜粋

## Release Report

非推奨の diff 出力先:

```text
.SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md
```

必要な場合のみ、従来のタグ差分レポートとして使ってください。

## 出力先ルール

- `uv run sage --repo .` は現在のリポジトリへ出力
- `uv run sage --repo <path>` は対象リポジトリへ出力
- `uv run sage --repo <path> -o <output>` は明示した出力ディレクトリへ出力
