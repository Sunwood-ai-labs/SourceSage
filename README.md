<p align="center">
  <img
    src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/SourceSage_icon4.png"
    alt="SourceSage hero"
    width="100%"
  >
</p>

<h1 align="center">SourceSage</h1>

<p align="center">
  <strong>Generate AI-friendly repository documentation from any local codebase.</strong>
</p>

<p align="center">
  SourceSage analyzes a repository's tree, Git context, file statistics, and file contents,
  then writes a shareable Markdown summary that LLMs and humans can scan quickly.
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
  <strong>English</strong>
  ·
  <a href="README.ja.md">日本語</a>
  ·
  <a href="https://sunwood-ai-labs.github.io/SourceSage/">Docs</a>
  ·
  <a href="https://github.com/Sunwood-ai-labs/SourceSage/releases">Releases</a>
</p>

>[!IMPORTANT]
>Nearly 90% of the release notes, README text, and commit messages in this repository are produced with [AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), and [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II) alongside Claude and ChatGPT.

## 🌿 Why SourceSage

- Turn a repository into a single Markdown artifact that an AI agent can ingest immediately.
- Capture both structure and context: tree, Git metadata, statistics, and file excerpts.
- Work from the current checkout or point SourceSage at another local repository with `--repo`.
- Generate output in English or Japanese with `-l en` or `-l ja`.

## ✨ Core Features

### 📘 Repository Summary

SourceSage creates `.SourceSageAssets/Repository_summary.md` with:

- a directory tree
- Git repository information
- file size and line-count tables
- language statistics
- selected file contents

### 🧾 Release Report (Deprecated)

The CLI still exposes `--diff` for legacy release-note pipelines, but the feature is deprecated.
For new workflows, prefer GitHub Releases instead of building automation around diff reports.

## 🚀 Quick Start

### 🔧 Run From This Repository

```bash
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync
uv run sage --help
uv run sage --repo .
```

### ⚡ Run Without Cloning

```bash
uvx --refresh sourcesage --help
```

### 📦 Analyze Another Repository

```bash
uv run --directory D:\Prj\SourceSage sage --repo D:\Prj\SourceSage\example -o D:\Prj\SourceSage\.tmp-docs-check\example
uv run sage --repo . -l ja
```

Replace the paths in the first command with your own SourceSage checkout and target repository.

### 🧰 Use a Custom Ignore File

SourceSage automatically merges the target repository's `.gitignore` and `.SourceSageignore`.
If you need a different ignore file, use `--ignore-file`.

```bash
uv run sage --repo . --ignore-file .SourceSageignore -o .\.tmp-docs-check\ignore
```

## 🗺️ CLI Reference

### ✅ Common Commands

```bash
uv run sage --repo .                    # analyze the current repository
uv run sage --repo . -l ja              # generate Japanese output
uv run sage --repo . -o ./out           # write results to a custom directory
uv run sage --help                      # show the Rich help screen
```

### 🧩 Important Options

| Option | Purpose |
| --- | --- |
| `--repo` | Repository to analyze |
| `-o`, `--output` | Output directory for generated files |
| `-l`, `--lang`, `--language` | Output language: `en` or `ja` |
| `--ignore-file` | Override the ignore file path |
| `--language-map` | Override the language map JSON |
| `--diff` | Legacy-only diff report flow retained for compatibility |

## 📂 Output Files

- Repository summary: `.SourceSageAssets/Repository_summary.md`
- Release report: `.SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md`

When `--repo` is set and `-o` is omitted, SourceSage writes the artifacts into the target repository.

## 📚 Documentation

The full bilingual guide lives in [`docs/`](docs/) and is published through GitHub Pages:

- English: [Getting Started](docs/guide/getting-started.md)
- Japanese: [はじめに](docs/ja/guide/getting-started.md)
- Live site: [sunwood-ai-labs.github.io/SourceSage](https://sunwood-ai-labs.github.io/SourceSage/)

## 🤝 Project Standards

- [Changelog](CHANGELOG.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)

## 🧪 Development

```bash
uv sync
uv run pytest -q
```

### Build the docs locally

```bash
cd docs
npm ci
npm run docs:build
```

## 🛠️ Troubleshooting

### `uvx` or `uv` cache looks stale

```bash
uv cache clean sourcesage
uv cache prune
```

### Output does not match your repository layout

- confirm you pointed `--repo` at the repository root
- check whether `.gitignore` or `.SourceSageignore` is excluding the files you expected
- run again with an explicit `--ignore-file` if you need a different rule set

## 🌐 Related Projects

### SourceSage MCP Server

[SourceSage MCP Server](https://github.com/Sunwood-ai-labs/source-sage-mcp-server)
brings SourceSage analysis into MCP-compatible assistants such as Claude Desktop.

## 📄 License

SourceSage is released under the [MIT License](LICENSE).
