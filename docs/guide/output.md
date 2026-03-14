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

## What the primary documentation artifact includes

- Project title and tree structure
- Git repository information when a `.git` directory is available
- File and language statistics
- File-by-file excerpts for non-excluded files

## `--lite` differences

When you run SourceSage with `--lite`, the same `Repository_summary.md` keeps:

- Project title and tree structure
- Git repository information when available
- File and language statistics
- Root README files only

It skips the full `## File Contents` section so the summary stays smaller during first-pass exploration.

## Example output

The repository ships an example documentation artifact at [`example/Repository_summary.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/example/Repository_summary.md).
