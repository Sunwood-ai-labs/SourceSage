# Getting Started

## Overview

SourceSage scans a repository and writes an AI-friendly Markdown documentation artifact to `.SourceSageAssets/Repository_summary.md`.

## Try it once with `uvx`

```bash
uvx --refresh sourcesage --help
uvx --refresh sourcesage --repo /path/to/repository
```

## Run from source

```bash
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync
uv run sage --help
uv run sage --repo .
```

This creates `.SourceSageignore` when missing and writes the primary documentation artifact under `.SourceSageAssets/`.

## Analyze another repository from this checkout

```bash
uv run --directory D:\Prj\SourceSage sage --repo D:\Prj\SourceSage\example -o D:\Prj\SourceSage\.tmp-docs-check\example
```

Replace those paths with your own SourceSage checkout and target repository.

## Generate Japanese documentation into a custom directory

```bash
uv run sage --repo . -l ja -o ./out
```

## Verify the repository locally

```bash
uv run pytest -q
```

## Next steps

- Review flags in the [CLI Reference](/guide/cli).
- Inspect the generated files in the [Output Guide](/guide/output).
- If something looks wrong, start with [Troubleshooting](/guide/troubleshooting).
