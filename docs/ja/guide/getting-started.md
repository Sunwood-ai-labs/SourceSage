# はじめに

## 概要

SourceSage はリポジトリを走査し、AI が読みやすい Markdown サマリを `.SourceSageAssets/Repository_summary.md` に生成します。

## 検証済みのローカルセットアップ

```bash
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync
```

## 配布版を試す

```bash
uvx --refresh sourcesage --help
```

## 現在のリポジトリを要約する

```bash
uv run sage --repo .
```

このコマンドは `.SourceSageignore` が無い場合に自動生成し、出力を `.SourceSageAssets/` 配下に書き込みます。

## 日本語の要約を別ディレクトリへ出力する

```bash
uv run sage --repo . -l ja -o ./out
```

## リポジトリをローカルで検証する

```bash
uv run pytest -q
```

## 次の一歩

- 利用可能なフラグは [CLI リファレンス](/ja/guide/cli) で確認できます。
- 生成物の構成は [出力ガイド](/ja/guide/output) にまとまっています。
- 想定どおりに出力されない場合は [トラブルシューティング](/ja/guide/troubleshooting) から確認してください。
