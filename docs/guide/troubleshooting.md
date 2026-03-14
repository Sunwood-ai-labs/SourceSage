# Troubleshooting

## The summary includes `.git` files

SourceSage should exclude `.git/` by default. If you still see Git internals, check whether you passed a custom ignore file that overrides the defaults.

## Old `uvx` cache is still being used

```bash
uv cache clean
uv cache prune
```

## You need a custom ignore policy

Create or edit `.SourceSageignore` in the target repository, then rerun:

```bash
uv run sage --repo .
```

## The diff report was skipped

`--diff` needs at least two Git tags. If tags are missing, SourceSage skips the report instead of failing the whole command.
