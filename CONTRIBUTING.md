# Contributing

Thanks for contributing to SourceSage.

## Development Setup

```bash
uv sync
uv run pytest -q
```

For documentation changes:

```bash
cd docs
npm ci
npm run docs:build
```

## Pull Request Checklist

- keep changes focused and easy to review
- update English and Japanese docs together when both surfaces are affected
- run the relevant verification commands before opening a PR
- include user-facing screenshots or output snippets only when they add clarity

## Repository Conventions

- Python entrypoints should continue to work through both `sage` and `sourcesage`
- prefer `uv run ...` when documenting Python commands in this repository
- keep generated artifacts such as `.SourceSageAssets/` out of commits unless a change explicitly needs them

## Reporting Issues

- use GitHub Issues for bugs, regressions, and feature requests
- include your OS, Python version, SourceSage version, and the command you ran
- if the issue is security-sensitive, follow [SECURITY.md](SECURITY.md) instead of opening a public issue
