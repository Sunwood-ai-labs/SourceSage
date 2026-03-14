# Output Guide

## Default artifact layout

After a standard run, SourceSage writes:

```text
.SourceSageAssets/
  Repository_summary.md
```

When `--diff` is enabled and enough tags exist, SourceSage can also write:

```text
.SourceSageAssets/
  RELEASE_REPORT/
    Report_<latest_tag>.md
```

## What the repository summary includes

- Project title and tree structure
- Git repository information when a `.git` directory is available
- File and language statistics
- File-by-file excerpts for non-excluded files

## Example output

The repository ships an example summary at [`example/Repository_summary.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/example/Repository_summary.md).
