# はじめに

## 概要

SourceSage はリポジトリを走査し、AI が読みやすい Markdown ドキュメントを `.SourceSageAssets/Repository_summary.md` に生成します。

## `uvx` で一度だけ試す

```bash
uvx --refresh sourcesage --help
uvx --refresh sourcesage --repo /path/to/repository
```

## ソースから実行する

```bash
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync
uv run sage --help
uv run sage --repo .
```

このコマンドは `.SourceSageignore` が無い場合に自動生成し、主要なドキュメント成果物を `.SourceSageAssets/` 配下に書き込みます。

## まずは軽量モードで確認する

```bash
uv run sage --repo . --lite
```

ignore ルールをまだ詰めていない段階では、`--lite` から始めると安全です。ツリー、Git 情報、統計、ルート README を残しつつ、全ファイル抜粋でサマリーが膨らむのを避けられます。

## このチェックアウトから別のリポジトリを解析する

```bash
uv run --directory D:\Prj\SourceSage sage --repo D:\Prj\SourceSage\example -o D:\Prj\SourceSage\.tmp-docs-check\example
```

通常は自分の SourceSage チェックアウト先と対象リポジトリのパスに置き換えてください。

## 日本語ドキュメントを別ディレクトリへ出力する

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
