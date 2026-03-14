# CLI Reference

## Primary command

```bash
uv run sage --help
```

SourceSage exposes both `sage` and `sourcesage` entry points from this repository.

## Core options

| Option | Purpose |
| --- | --- |
| `--repo <path>` | Analyze a target repository. |
| `-o, --output <dir>` | Write generated files under `<dir>/.SourceSageAssets/`. |
| `-l, --lang {en,ja}` | Switch documentation headings between English and Japanese. |
| `--ignore-file <path>` | Override the ignore template path used by SourceSage. |
| `--language-map <path>` | Use a custom language map JSON file. |
| `-v, --version` | Print the package version. |

## Deprecated diff report

```bash
uv run sage --repo . --diff
```

`--diff` still works, but it is intentionally deprecated and only produces a release report when the repository has at least two tags.

## Ignore behavior

SourceSage merges:

- `.gitignore`
- `.SourceSageignore`

When `.SourceSageignore` is missing, SourceSage writes a default template automatically before analysis starts.
