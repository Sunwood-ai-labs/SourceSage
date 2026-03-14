# SourceSage Tests

## Test Overview

This directory contains tests for SourceSage functionality.

## Test Files

### 1. `test_cli.py`
CLI parsing, default behaviors, ignore-file generation, and version display.

**Total Tests:** 21

### 2. `test_language_and_ignore.py`
Language selection and ignore-rule merging across `.gitignore` and `.SourceSageignore`.

**Total Tests:** 18

### 3. `test_git_info.py`
Git command execution, repository inspection, tag handling, and diff-report prerequisites.

**Total Tests:** 12

### 4. `test_e2e.py`
End-to-end CLI execution against real temporary repositories.

**Total Tests:** 5

### 5. `test_docusum_markdown_structure.py`
Repository summary structure, tables, UTF-8 output, and exclusion behavior.

**Total Tests:** 12

## Verification Snapshot

Current local verification for this polish pass:

```bash
uv run pytest -q
```

Result:

- 68 tests passed
- 0 tests failed

## Running Tests

### Run all tests:
```bash
uv run pytest tests/ -v
```

### Run specific test file:
```bash
uv run pytest tests/test_cli.py -v
uv run pytest tests/test_language_and_ignore.py -v
```

### Run specific test class:
```bash
uv run pytest tests/test_language_and_ignore.py::TestLanguageOption -v
```

### Run with coverage:
```bash
uv run pytest tests/ --cov=sourcesage --cov-report=html
```

## Coverage Highlights

### 1. CLI behavior
- argument parsing, output paths, report flags, and version commands
- backward compatibility of the `sage` and `sourcesage` entrypoints

### 2. Language and ignore handling
- default and explicit language selection for English and Japanese
- merged ignore behavior across `.gitignore` and `.SourceSageignore`
- wildcard, directory, and include-pattern matching

### 3. Git and diff-report prerequisites
- command execution success and failure paths
- repository branch, commit, and tag inspection
- graceful handling when diff prerequisites are missing

### 4. End-to-end output
- repository summary generation in temporary repositories
- custom output directories and language-specific output
- automatic `.SourceSageignore` creation and reuse

### 5. Markdown quality
- required headings and statistics tables
- UTF-8 output and project naming
- exclusion of ignored files and `.git`
