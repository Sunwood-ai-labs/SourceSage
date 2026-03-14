# 出力ファイル

## Repository Summary

標準の出力先:

```text
.SourceSageAssets/Repository_summary.md
```

このサマリには次の内容が含まれます。

- リポジトリツリー
- Git リポジトリ情報
- プロジェクト統計
- ファイル一覧テーブル
- 言語統計
- ファイル内容の抜粋

## Release Report

非推奨の diff 出力:

```text
.SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md
```

旧来のタグ間レポートがまだ必要な場合にだけ利用してください。

## 出力先のルール

- `uv run sage --repo .` は現在のリポジトリに出力します
- `uv run sage --repo <path>` は指定した対象リポジトリに出力します
- `uv run sage --repo <path> -o <output>` は明示した出力先に出力します
