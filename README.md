<p align="center">
  <img
    src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/public/hero.svg"
    alt="SourceSage hero"
    width="100%"
  >
</p>

<h1 align="center">SourceSage</h1>

<p align="center">
  <strong>Repository analysis CLI that turns source trees into AI-friendly Markdown documentation.</strong>
</p>

<p align="center">
  <a href="./README.ja.md">日本語</a> |
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
> Release notes, README text, and other repository-facing materials are often produced with SourceSage and other AI-assisted tools, then reviewed and refined by the maintainers.

## Why SourceSage

- Generate repository documentation that an assistant can read immediately.
- Combine project structure, Git context, file statistics, and file excerpts in one Markdown artifact.
- Work against the current checkout or any other local repository through `--repo`.

## Install And Run

### Try it once with `uvx`

```bash
uvx --refresh sourcesage --help
uvx --refresh sourcesage --repo /path/to/repository
```

### Install it as a tool

```bash
uv tool install sourcesage
sourcesage --help
sourcesage --repo /path/to/repository
```

### Install it with `pip`

```bash
pip install sourcesage
sourcesage --help
```

### Run from source

```bash
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync
uv run sage --help
uv run sage --repo .
```

## Common Commands

```bash
uv run sage --repo .
uv run sage --repo /path/to/repository -l ja
uv run sage --repo /path/to/repository -o ./out
uv run sage --repo . --ignore-file .SourceSageignore
```

`--diff` is still available for legacy compatibility, but it is intentionally deprecated and no longer the primary workflow.

## Output

Primary artifact:

```text
.SourceSageAssets/
  Repository_summary.md
```

SourceSage merges `.gitignore` and `.SourceSageignore`. If `.SourceSageignore` does not exist yet, it creates a default template automatically before analysis starts.

## Documentation

- Docs site: [sunwood-ai-labs.github.io/SourceSage](https://sunwood-ai-labs.github.io/SourceSage/)
- Getting started: [docs/guide/getting-started.md](./docs/guide/getting-started.md)
- CLI guide: [docs/guide/cli.md](./docs/guide/cli.md)
- Japanese guide: [docs/ja/guide/getting-started.md](./docs/ja/guide/getting-started.md)

## Project Standards

- [Changelog](./CHANGELOG.md)
- [Contributing Guide](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)

## Development

```bash
uv sync
uv run pytest -q
cd docs
npm ci
npm run docs:build
```

## Related Project

- [SourceSage MCP Server](https://github.com/Sunwood-ai-labs/source-sage-mcp-server)
