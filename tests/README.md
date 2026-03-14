# SourceSage Tests

## Test Overview

This directory contains tests for SourceSage functionality.

## Test Files

### 1. `test_cli.py`
Tests for CLI argument parsing and basic functionality.

**Test Classes:**
- `TestCLIArguments` - Tests for CLI argument parsing
- `TestSourceSageignoreGeneration` - Tests for .SourceSageignore file generation
- `TestCLIOptions` - Tests for various CLI options
- `TestBackwardCompatibility` - Tests for backward compatibility

**Total Tests:** 16

### 2. `test_language_and_ignore.py`
Tests for language options and ignore file merging functionality.

**Test Classes:**
- `TestLanguageOption` - Tests for `--language` option (en/ja)
- `TestIgnoreFileMerging` - Tests for .gitignore and .SourceSageignore merging
- `TestFilePatternMatcherFunctionality` - Tests for FilePatternMatcher functionality
- `TestBackwardCompatibility` - Tests for backward compatibility with single file input

**Total Tests:** 14

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

## Key Features Tested

### 1. Language Options
- Default language is `en` (English)
- `--language ja` option switches to Japanese
- Invalid language options are rejected

### 2. Ignore File Merging
- `.gitignore` and `.SourceSageignore` are properly merged
- Patterns from both files are respected
- `uv.lock` is correctly excluded via `.SourceSageignore`

### 3. File Pattern Matching
- Default patterns work correctly
- Wildcard patterns (`*.pyc`, `*.log`) function as expected
- Directory patterns (`__pycache__/`, `node_modules/`) work properly
- Include patterns (negation) are supported

### 4. Backward Compatibility
- Single file path still works for `FilePatternMatcher`
- Existing CLI options continue to function
- Old removed options properly error out

## Recent Improvements

1. **Language Support**: Added `--language` option to support English and Japanese output
2. **Ignore File Merging**: Improved ignore file handling to merge `.gitignore` and `.SourceSageignore`
3. **Better Testing**: Added comprehensive tests for new features

## Future Improvements

- Add integration tests for end-to-end functionality
- Add performance tests for large repositories
- Add tests for markdown generation quality
- Add tests for Git information collection
- Add tests for language detection
