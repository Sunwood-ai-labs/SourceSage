---
name: sourcesage-cli
description: Generate AI-friendly repository documentation with the SourceSage CLI. Use when Codex needs to run `sage` or `sourcesage` to create `.SourceSageAssets/Repository_summary.md`, analyze the current repository or another local repository, switch the output language between English and Japanese, change the output directory, or optionally create a deprecated tag-diff release report with `--diff`.
---

# SourceSage CLI

## Overview

Use the SourceSage CLI from this repository checkout to generate repository summaries for the current repo or another local repo.

Prefer the local checkout over assuming `sourcesage` is globally installed. In this repository layout, the SourceSage tool root is the directory that contains this `SKILL.md`.

## Workflow

1. Resolve the SourceSage tool root and the target repository.
   - If the user did not specify another repo, analyze the current workspace.
   - If the current workspace is not the SourceSage repo, run SourceSage from its own checkout with `uv run --directory <sourcesage-root> sage ...`.

2. Pick the smallest command that satisfies the request.
   - Current repo summary: `uv run sage`
   - Current repo summary in Japanese: `uv run sage -l ja`
   - Another repo with default output inside that repo: `uv run --directory <sourcesage-root> sage --repo "<target-repo>"`
   - Another repo with explicit output directory: `uv run --directory <sourcesage-root> sage --repo "<target-repo>" -o "<output-dir>"`
   - Deprecated diff report: `uv run --directory <sourcesage-root> sage --repo "<target-repo>" --diff`

3. Verify the generated artifacts after every run.
   - Repository summary: `<output-dir>/.SourceSageAssets/Repository_summary.md`
   - Deprecated diff report: `<output-dir>/.SourceSageAssets/RELEASE_REPORT/Report_<latest-tag>.md`
   - Open the generated markdown and summarize the important results instead of only reporting that the command ran.

4. Report side effects and command mismatches.
   - Expect SourceSage to create `<repo>/.SourceSageignore` if it does not exist.
   - Treat `--ignore-file` as the supported ignore override.
   - Do not rely on `--use-ignore` unless the CLI is updated and re-verified, because the current CLI does not expose that flag.

## Command Notes

- Prefer `uv run sage` inside the SourceSage repo because `pyproject.toml` defines both `sage` and `sourcesage` entry points.
- Prefer `uv run --directory <sourcesage-root> sage ...` outside the SourceSage repo so the command uses this checkout without requiring a global install.
- Fall back to `sourcesage` or `sage` directly only when the package is already installed and `uv` is unavailable.
- Use `-l ja` or `-l en` for output language.
- Use `-o` when the user wants artifacts outside the repo root.
- Use `--repo` to analyze another repository from this checkout.

## Validation

- Run the chosen command instead of only describing it.
- Confirm that the expected markdown file exists.
- Read the generated output and report the path plus a short summary of what was produced.
- Re-run the exact command after changing any execution instructions or docs that mention it.

## Avoid

- Do not assume README examples are authoritative when they differ from `sourcesage/cli.py`.
- Do not overwrite existing artifacts silently when the user asked for a specific destination and it already contains results.
- Do not describe SourceSage usage from memory when you can inspect `pyproject.toml` and `sourcesage/cli.py` in this repo.
