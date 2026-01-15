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

## Test Results

### Latest Test Run (2026-01-15)

```
============================= test session starts ==============================
platform linux -- Python 3.13.9, pytest-8.4.1, pluggy-1.6.0
collected 30 items

tests/test_cli.py::TestCLIArguments::test_short_output_option PASSED     [  3%]
tests/test_cli.py::TestCLIArguments::test_long_output_option PASSED      [  6%]
tests/test_cli.py::TestCLIArguments::test_diff_option PASSED             [ 10%]
tests/test_cli.py::TestCLIArguments::test_use_ignore_option PASSED       [ 13%]
tests/test_cli.py::TestCLIArguments::test_default_values PASSED          [ 16%]
tests/test_cli.py::TestCLIArguments::test_diff_output_option PASSED      [ 20%]
tests/test_cli.py::TestCLIArguments::test_combined_options PASSED        [ 23%]
tests/test_cli.py::TestSourceSageignoreGeneration::test_sourcesageignore_template_exists PASSED [ 26%]
tests/test_cli.py::TestSourceSageignoreGeneration::test_sourcesageignore_has_sections PASSED [ 30%]
tests/test_cli.py::TestSourceSageignoreGeneration::test_sourcesageignore_has_venv_patterns PASSED [ 33%]
tests/test_cli.py::TestSourceSageignoreGeneration::test_sourcesageignore_has_lock_files PASSED [ 36%]
tests/test_cli.py::TestCLIOptions::test_repo_path_option PASSED          [ 40%]
tests/test_cli.py::TestCLIOptions::test_report_title_option PASSED       [ 43%]
tests/test_cli.py::TestCLIOptions::test_ignore_file_option PASSED        [ 46%]
tests/test_cli.py::TestBackwardCompatibility::test_sourcesage_command_name_in_pyproject PASSED [ 50%]
tests/test_cli.py::TestBackwardCompatibility::test_old_options_removed PASSED [ 53%]
tests/test_language_and_ignore.py::TestLanguageOption::test_language_option_default PASSED [ 56%]
tests/test_language_and_ignore.py::TestLanguageOption::test_language_option_english PASSED [ 60%]
tests/test_language_and_ignore.py::TestLanguageOption::test_language_option_japanese PASSED [ 63%]
tests/test_language_and_ignore.py::TestLanguageOption::test_language_option_invalid PASSED [ 66%]
tests/test_language_and_ignore.py::TestIgnoreFileMerging::test_single_ignore_file PASSED [ 70%]
tests/test_language_and_ignore.py::TestIgnoreFileMerging::test_multiple_ignore_files PASSED [ 73%]
tests/test_language_and_ignore.py::TestIgnoreFileMerging::test_gitignore_and_sourcesageignore_merge PASSED [ 76%]
tests/test_language_and_ignore.py::TestIgnoreFileMerging::test_sourcesageignore_has_uv_lock PASSED [ 80%]
tests/test_language_and_ignore.py::TestIgnoreFileMerging::test_packaged_sourcesageignore_has_uv_lock PASSED [ 83%]
tests/test_language_and_ignore.py::TestFilePatternMatcherFunctionality::test_default_patterns PASSED [ 86%]
tests/test_language_and_ignore.py::TestFilePatternMatcherFunctionality::test_pattern_matching_wildcards PASSED [ 90%]
tests/test_language_and_ignore.py::TestFilePatternMatcherFunctionality::test_directory_patterns PASSED [ 93%]
tests/test_language_and_ignore.py::TestFilePatternMatcherFunctionality::test_include_patterns PASSED [ 96%]
tests/test_language_and_ignore.py::TestBackwardCompatibility::test_single_file_still_works PASSED [100%]

============================== 30 passed in 0.41s ==============================
```

**Summary:**
- **Total Tests:** 30
- **Passed:** 30
- **Failed:** 0
- **Skipped:** 0
- **Success Rate:** 100%

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
