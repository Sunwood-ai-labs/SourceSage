# CLI Reference

## Common commands

```bash
uv run sage --repo .
uv run sage --repo . -l ja
uv run sage --repo . -o ./out
uv run sage --help
```

## Options

| Option | Description |
| --- | --- |
| `--repo` | Path to the repository to analyze |
| `-o`, `--output` | Output directory for generated files |
| `-l`, `--lang`, `--language` | Output language: `en` or `ja` |
| `--ignore-file` | Ignore-file override |
| `--language-map` | Language-map JSON override |
| `--diff` | Legacy-only release diff report flow |
| `--repo-path` | Git repository path used by the legacy diff flow |

## Notes

- `--ignore-file` is the supported way to provide a custom ignore file.
- `--diff` remains visible for compatibility, but it is not recommended for new release pipelines.
- When `--repo` is provided and `-o` is omitted, SourceSage writes the artifacts into the target repository.
