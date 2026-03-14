# Output Files

## Repository Summary

Default path:

```text
.SourceSageAssets/Repository_summary.md
```

The summary includes:

- the repository tree
- Git repository information
- project statistics
- file tables
- language statistics
- selected file contents

## Release Report

Deprecated diff output:

```text
.SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md
```

Use it only when you still need the legacy tag-to-tag report.

## Output location rules

- `uv run sage --repo .` writes into the current repository
- `uv run sage --repo <path>` writes into the target repository
- `uv run sage --repo <path> -o <output>` writes into the explicit output directory
