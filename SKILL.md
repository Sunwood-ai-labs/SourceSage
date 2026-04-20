---
name: sourcesage-cli
description: "Generate AI-friendly repository documentation with the SourceSage CLI. Use when Codex needs to run `sage` or `sourcesage` to create `.SourceSageAssets/Repository_summary.md`, analyze the current repository or another local repository, switch the output language between English and Japanese, use `--lite` to keep the summary small, change the output directory, or optionally create a deprecated tag-diff release report with `--diff`."
---

# SourceSage CLI

Use the SourceSage CLI from this repository checkout to generate repository summaries for the current repo or another local repo. Prefer the local checkout over assuming `sourcesage` is globally installed; the tool root is the directory containing this `SKILL.md`.

## Workflow

1. **Resolve tool root and target.** Analyze the current workspace by default. Outside this repo, prefix commands with `uv run --directory <sourcesage-root>`. Fall back to bare `sage` only when `uv` is unavailable and the package is already installed.

2. **Pick the smallest command that satisfies the request.** Prefer `uv run sage` (both `sage` and `sourcesage` entry points are in `pyproject.toml`).

   | Scenario | Command |
   |----------|---------|
   | Current repo | `uv run sage` |
   | Lite mode | `uv run sage --lite` |
   | Japanese output | `uv run sage -l ja` |
   | Another repo | `uv run --directory <sourcesage-root> sage --repo "<target>"` |
   | Another repo, lite | `uv run --directory <sourcesage-root> sage --repo "<target>" --lite` |
   | Custom output dir | `uv run --directory <sourcesage-root> sage --repo "<target>" -o "<dir>"` |
   | Diff report (deprecated) | `uv run --directory <sourcesage-root> sage --repo "<target>" --diff` |

   Use `--lite` for first-pass exploration when ignore rules are not tuned or full excerpts would be too large.

3. **Verify the generated artifacts after every run.**
   - Repository summary: `<output-dir>/.SourceSageAssets/Repository_summary.md`
   - Deprecated diff report: `<output-dir>/.SourceSageAssets/RELEASE_REPORT/Report_<latest-tag>.md`
   - Open the generated markdown and summarize the important results instead of only reporting that the command ran.
   - In `--lite` mode, confirm the summary keeps the tree, Git info, statistics, and root README files while omitting the `## File Contents` section.

4. **Report side effects.** SourceSage creates `<repo>/.SourceSageignore` if missing. Use `--ignore-file` for custom ignore patterns (`--use-ignore` is not exposed by the current CLI).

## Validation

- Run the chosen command instead of only describing it.
- Confirm that the expected markdown file exists.
- Read the generated output and report the path plus a short summary of what was produced.
- Re-run the exact command after changing any execution instructions or docs that mention it.

## Avoid

- Do not assume README examples are authoritative when they differ from `sourcesage/cli.py`; check the source.
- Do not overwrite existing artifacts silently when the user asked for a specific destination and it already contains results.

## References

- `sourcesage/cli.py` — canonical CLI flags, argument defaults, and help text
- `pyproject.toml` — entry points (`sage`, `sourcesage`), version, and dependencies
