<p align="center">
  <img
    src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/SourceSage_icon4.png"
    alt="SourceSage hero"
    width="100%"
  >
</p>

<h1 align="center">SourceSage</h1>

<p align="center">
  <strong>任意のローカルリポジトリを、AI が読みやすいドキュメントに変換します。</strong>
</p>

<p align="center">
  SourceSage はリポジトリのツリー、Git 情報、ファイル統計、ファイル内容を解析し、
  LLM と人の両方がすばやく読める Markdown サマリを生成します。
</p>

<p align="center">
  <a href="https://github.com/Sunwood-ai-labs/SourceSage/actions/workflows/ci.yml">
    <img alt="CI" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/SourceSage/ci.yml?branch=main&label=ci">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/SourceSage/actions/workflows/deploy-docs.yml">
    <img alt="Docs" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/SourceSage/deploy-docs.yml?branch=main&label=docs">
  </a>
  <a href="https://pypi.org/project/sourcesage/">
    <img alt="PyPI version" src="https://img.shields.io/pypi/v/sourcesage">
  </a>
  <a href="LICENSE">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-0f766e">
  </a>
</p>

<p align="center">
  <a href="README.md">English</a>
  ·
  <strong>日本語</strong>
  ·
  <a href="https://sunwood-ai-labs.github.io/SourceSage/">Docs</a>
  ·
  <a href="https://github.com/Sunwood-ai-labs/SourceSage/releases">Releases</a>
</p>

>[!IMPORTANT]
>このリポジトリのリリースノート、README、コミットメッセージの多くは、[AIRA](https://github.com/Sunwood-ai-labs/AIRA)、[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage)、[Gaiah](https://github.com/Sunwood-ai-labs/Gaiah)、[HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II) と Claude / ChatGPT を組み合わせて作成しています。

## 🌿 SourceSage でできること

- リポジトリを、AI エージェントがすぐ読める Markdown 1 枚に要約できます。
- ツリー構造だけでなく、Git 情報、統計、ファイル抜粋までまとめて取得できます。
- 今いるリポジトリだけでなく、`--repo` で別のローカルリポジトリも解析できます。
- `-l en` と `-l ja` で出力言語を切り替えられます。

## ✨ 主な機能

### 📘 Repository Summary

`.SourceSageAssets/Repository_summary.md` を生成し、以下を含めます。

- ディレクトリツリー
- Git リポジトリ情報
- ファイルサイズ / 行数テーブル
- 言語統計
- ファイル内容の抜粋

### 🧾 Release Report（非推奨）

CLI には互換性のため `--diff` が残っていますが、この機能は旧来のリリースノート運用向けの非推奨機能です。
新規の導線としては、差分レポート前提の自動化より GitHub Releases を主導線にするのがおすすめです。

## 🚀 クイックスタート

### 🔧 このリポジトリから実行する

```bash
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync
uv run sage --help
uv run sage --repo .
```

### ⚡ クローンせずに試す

```bash
uvx --refresh sourcesage --help
```

### 📦 別のリポジトリを解析する

```bash
uv run --directory D:\Prj\SourceSage sage --repo D:\Prj\SourceSage\example -o D:\Prj\SourceSage\.tmp-docs-check\example
uv run sage --repo . -l ja
```

1 行目は検証済みの具体例です。通常は SourceSage のチェックアウト先と解析対象リポジトリのパスに置き換えてください。

### 🧰 独自の ignore ルールを使う

SourceSage は対象リポジトリの `.gitignore` と `.SourceSageignore` を自動でマージします。
別の ignore ファイルを使いたい場合は `--ignore-file` を使ってください。

```bash
uv run sage --repo . --ignore-file .SourceSageignore -o .\.tmp-docs-check\ignore
```

## 🗺️ CLI リファレンス

### ✅ よく使うコマンド

```bash
uv run sage --repo .                    # 現在のリポジトリを解析
uv run sage --repo . -l ja              # 日本語出力
uv run sage --repo . -o ./out           # 出力先を変更
uv run sage --help                      # Rich 形式のヘルプを表示
```

### 🧩 主なオプション

| オプション | 役割 |
| --- | --- |
| `--repo` | 解析対象のリポジトリ |
| `-o`, `--output` | 生成ファイルの出力先 |
| `-l`, `--lang`, `--language` | 出力言語 (`en` / `ja`) |
| `--ignore-file` | ignore ファイルの上書き指定 |
| `--language-map` | 言語マップ JSON の上書き指定 |
| `--diff` | 互換性のため残っている旧来の diff レポートフロー |

## 📂 出力ファイル

- Repository Summary: `.SourceSageAssets/Repository_summary.md`
- Release Report: `.SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md`

`--repo` を指定して `-o` を省略した場合、生成物は対象リポジトリ側に書き込まれます。

## 📚 ドキュメント

詳しい英日ガイドは [`docs/`](docs/) にあり、GitHub Pages でも公開します。

- English: [Getting Started](docs/guide/getting-started.md)
- 日本語: [はじめに](docs/ja/guide/getting-started.md)
- 公開サイト: [sunwood-ai-labs.github.io/SourceSage](https://sunwood-ai-labs.github.io/SourceSage/)

## 🤝 プロジェクト運用

- [変更履歴](CHANGELOG.md)
- [コントリビューションガイド](CONTRIBUTING.md)
- [行動規範](CODE_OF_CONDUCT.md)
- [セキュリティポリシー](SECURITY.md)

## 🧪 開発

```bash
uv sync
uv run pytest -q
```

### docs をローカルでビルドする

```bash
cd docs
npm ci
npm run docs:build
```

## 🛠️ トラブルシューティング

### `uvx` や `uv` のキャッシュが古い

```bash
uv cache clean sourcesage
uv cache prune
```

### 出力が期待と違う

- `--repo` がリポジトリのルートを指しているか確認する
- `.gitignore` や `.SourceSageignore` が必要なファイルを除外していないか確認する
- 別ルールを使いたい場合は `--ignore-file` を明示する

## 🌐 関連プロジェクト

### SourceSage MCP Server

[SourceSage MCP Server](https://github.com/Sunwood-ai-labs/source-sage-mcp-server)
は SourceSage の解析機能を MCP 対応アシスタントから直接使えるようにした派生プロジェクトです。

## 📄 ライセンス

SourceSage は [MIT License](LICENSE) で公開されています。
