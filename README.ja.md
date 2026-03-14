<p align="center">
  <img
    src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/public/hero.svg"
    alt="SourceSage hero"
    width="100%"
  >
</p>

<h1 align="center">SourceSage</h1>

<p align="center">
  <strong>ソースツリーを AI が読みやすい Markdown ドキュメントへ変換するリポジトリ解析 CLI です。</strong>
</p>

<p align="center">
  <a href="./README.md">English</a> |
  <a href="https://sunwood-ai-labs.github.io/SourceSage/">Docs</a> |
  <a href="https://pypi.org/project/sourcesage/">PyPI</a> |
  <a href="https://github.com/Sunwood-ai-labs/SourceSage/releases">Releases</a>
</p>

<p align="center">
  <a href="https://github.com/Sunwood-ai-labs/SourceSage/actions/workflows/ci.yml">
    <img alt="CI" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/SourceSage/ci.yml?branch=main&label=CI">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/SourceSage/actions/workflows/deploy-docs.yml">
    <img alt="Docs" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/SourceSage/deploy-docs.yml?branch=main&label=Docs">
  </a>
  <a href="https://pypi.org/project/sourcesage/">
    <img alt="PyPI version" src="https://img.shields.io/pypi/v/sourcesage">
  </a>
  <a href="./LICENSE">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-0f766e">
  </a>
</p>

> [!IMPORTANT]
> リリースノートや README などの公開文面には、SourceSage を含む AI 支援ツールを使って下書きし、メンテナがレビューして仕上げているものがあります。

## SourceSage でできること

- AI アシスタントがすぐ読めるリポジトリ要約を生成できます。
- ツリー構造、Git 情報、ファイル統計、抜粋を 1 つの Markdown にまとめられます。
- 現在のリポジトリだけでなく、`--repo` で別のローカルリポジトリも解析できます。

## インストールと実行

### `uvx` で一度だけ試す

```bash
uvx --refresh sourcesage --help
uvx --refresh sourcesage --repo /path/to/repository
```

### ツールとしてインストールする

```bash
uv tool install sourcesage
sourcesage --help
sourcesage --repo /path/to/repository
```

### `pip` でインストールする

```bash
pip install sourcesage
sourcesage --help
```

### ソースから実行する

```bash
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync
uv run sage --help
uv run sage --repo .
```

## よく使うコマンド

```bash
uv run sage --repo .
uv run sage --repo /path/to/repository -l ja
uv run sage --repo /path/to/repository -o ./out
uv run sage --repo . --ignore-file .SourceSageignore
```

`--diff` は互換性のため残していますが、現在の主導線ではなく非推奨扱いです。

## 出力

標準の出力先:

```text
.SourceSageAssets/
  Repository_summary.md
```

SourceSage は `.gitignore` と `.SourceSageignore` を統合して使います。`.SourceSageignore` が無い場合は、解析前にデフォルトテンプレートを自動生成します。

## ドキュメント

- Docs サイト: [sunwood-ai-labs.github.io/SourceSage](https://sunwood-ai-labs.github.io/SourceSage/)
- はじめに: [docs/ja/guide/getting-started.md](./docs/ja/guide/getting-started.md)
- CLI ガイド: [docs/ja/guide/cli.md](./docs/ja/guide/cli.md)
- 英語版ガイド: [docs/guide/getting-started.md](./docs/guide/getting-started.md)

## プロジェクト規約

- [変更履歴](./CHANGELOG.md)
- [コントリビューションガイド](./CONTRIBUTING.md)
- [行動規範](./CODE_OF_CONDUCT.md)
- [セキュリティポリシー](./SECURITY.md)

## 開発

```bash
uv sync
uv run pytest -q
cd docs
npm ci
npm run docs:build
```

## 関連プロジェクト

- [SourceSage MCP Server](https://github.com/Sunwood-ai-labs/source-sage-mcp-server)
