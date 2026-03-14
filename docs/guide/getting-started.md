# Getting Started

## Overview

SourceSage scans a repository and writes an AI-friendly Markdown brief to `.SourceSageAssets/Repository_summary.md`.

## Verified local setup

```bash
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync
```

## Try the published package

```bash
uvx --refresh sourcesage --help
```

## Generate a summary for the current repository

```bash
uv run sage --repo .
```

This command creates `.SourceSageignore` when missing and writes the summary under `.SourceSageAssets/`.

## Generate a Japanese summary into a custom directory

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
