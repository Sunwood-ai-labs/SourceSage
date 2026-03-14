# はじめに

## 概要

SourceSage はリポジトリを走査し、`.SourceSageAssets/Repository_summary.md` に AI 向けの Markdown 要約を書き出します。

## 検証済みのローカルセットアップ

```bash
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync
```

## 現在のリポジトリを要約する

```bash
uv run sage --repo .
```

`.SourceSageignore` が無ければ自動生成し、要約は `.SourceSageAssets/` 配下に出力されます。

## 日本語の要約を別ディレクトリへ出力する

```bash
uv run sage --repo . -l ja -o ./out
```

## ローカル検証

```bash
uv run pytest -q
```

## 次の一歩

- 対応フラグは [CLI リファレンス](/ja/guide/cli)
- 生成物の構成は [出力ガイド](/ja/guide/output)
- 問題があれば [トラブルシューティング](/ja/guide/troubleshooting)
