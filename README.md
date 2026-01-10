<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/SourceSage_icon4.png" width="100%">
<br>
<h1 align="center">SourceSage</h1>
<h2 align="center">
  ～Transforming code for AI～

  <br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/sourcesage">
  <img alt="PyPI - Format" src="https://img.shields.io/pypi/format/sourcesage">
  <img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/sourcesage">
  <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/sourcesage">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/sourcesage">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/sourcesage">
  <a href="https://app.codacy.com/gh/Sunwood-ai-labs/SourceSage/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/77ab7715dd23499d82caca4e7ea3b093"/></a>

  [![SourceSage - Sunwood-ai-labs](https://img.shields.io/static/v1?label=SourceSage&message=Sunwood-ai-labs&color=blue&logo=github)](https://github.com/Sunwood-ai-labs/SourceSage "Go to GitHub repo")
![GitHub Repo stars](https://img.shields.io/github/stars/Sunwood-ai-labs/SourceSage)
[![forks - Sunwood-ai-labs](https://img.shields.io/github/forks/SourceSage/Sunwood-ai-labs?style=social)](https://github.com/Sunwood-ai-labs/SourceSage)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Sunwood-ai-labs/SourceSage)](https://github.com/Sunwood-ai-labs/SourceSage)
[![GitHub Top Language](https://img.shields.io/github/languages/top/Sunwood-ai-labs/SourceSage)](https://github.com/Sunwood-ai-labs/SourceSage)
![GitHub Release](https://img.shields.io/github/v/release/Sunwood-ai-labs/SourceSage?color=red)
![GitHub Tag](https://img.shields.io/github/v/tag/Sunwood-ai-labs/SourceSage?sort=semver&color=orange)
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/SourceSage/publish-to-pypi.yml">
  <br>

<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/tag/sourcesage/"><b>[🍀 Official Blog]</b></a>
</p>

</h2>


</p>

[日本語](README.ja.md) | English

SourceSage is a tool that comprehensively analyzes repository structure and content to generate AI-friendly documentation. It primarily provides Repository_summary.md generation and RELEASE_REPORT creation features.

>[!IMPORTANT]
>Nearly 90% of the release notes, README, and commit messages in this repository are generated using [AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), and [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II) with [claude.ai](https://claude.ai/) and [ChatGPT4](https://chatgpt.com/).

## 🌟 Related Projects

### SourceSage MCP Server
[SourceSage MCP Server](https://github.com/Sunwood-ai-labs/source-sage-mcp-server) is a derived version of SourceSage that integrates with the Model Context Protocol (MCP). It enables AI assistants like Claude Desktop to directly access repository analysis capabilities.

## Release Notes

For the latest updates, please visit our GitHub releases page.

https://github.com/Sunwood-ai-labs/SourceSage/releases


## 🎯 Key Features

SourceSage is a simple and lightweight repository analysis tool that provides two main features:

### 1. 📋 Repository Summary Generation

Comprehensively analyzes repository structure, commit information, and file statistics to generate AI-friendly markdown documentation.

**Output File**: `.SourceSageAssets/DOCUMIND/Repository_summary.md`

**Included Information**:
- 🌳 Project tree structure
- 📋 Git repository information
- 📈 File size and line count statistics
- 📝 Detailed file contents

### 2. 📄 Release Report Generation (Optional Feature - Deprecated)

> ⚠️ **Deprecated Feature**: This feature will be removed in a future release. With improvements in LLM command execution capabilities, automatic diff report generation is becoming unnecessary.

Analyzes differences between Git tags to automatically generate release reports (enabled with `--generate-diff-report` flag).

**Output File**: `.SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md`

**Included Information**:
- 🏷️ Version comparison
- 🔄 Detailed change differences
- 📋 Commit history
  - 📂 Repository basic information (remote URL, branch, latest commit, etc.)
  - 📖 README content (optional)


## 🚀 Quick Start

### 📦 Installation (Fastest)

```bash
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync
uv run ss
```

Note: When using as a package, run `pip install sourcesage` then execute `ss` (or `sourcesage`).

### 🗺️ Basic Usage (Minimum Required)

```bash
# Generate repository summary (default: uses .gitignore)
uv run ss

# Use/generate .SourceSageignore file
uv run ss --use-sourcesage-ignore

# Generate release report (optional - deprecated)
uv run ss --generate-diff-report
```

Output locations:
- Repository Summary: `.SourceSageAssets/DOCUMIND/Repository_summary.md`
- Release Report: `.SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md` (only with `--generate-diff-report`)

Frequently used options (excerpt):

```bash
uv run ss --ss-output ./out              # Change output destination
uv run ss --ignore-file .gitignore       # Specify ignore rules (default)
uv run ss --use-sourcesage-ignore        # Use/generate .SourceSageignore
uv run ss --generate-diff-report         # Generate diff report (deprecated)
```

Notes:
- From v7.2.0, `.gitignore` is used by default. Use `--use-sourcesage-ignore` if you need a custom ignore file.
- When `--language-map` is omitted, the included defaults (`sourcesage/config/`) are automatically used.
- Release Report is generated when there are 2 or more tags (only with `--generate-diff-report`).

### 📊 Example Generated Content

#### Repository Summary

```markdown
    # Project: SourceSage

    ```plaintext
    OS: posix
    Directory: /path/to/project

    ├── .SourceSageignore
    ├── pyproject.toml
    ├── sourcesage/
    │   ├── __init__.py
    │   ├── cli.py
    │   └── modules/
    │       ├── DocuSum/
    │       └── DiffReport/
    │           ├── __init__.py
    │           ├── git_diff.py
    │           └── markdown_report.py
    └── README.md
    ```

    ## 📊 Project Statistics

    - 📅 Created: 2025-02-02 16:22:31
    - 📁 Total Directories: 5
    - 📄 Total Files: 15
    - 📏 Maximum Depth: 3
```

## 🛠️ Development Environment

SourceSage supports modern Python development environments:

- **Python**: 3.8 or later
- **Package Management**: uv / pip
- **Build System**: hatchling
- **Configuration File**: pyproject.toml

### Development Setup

```bash
# Development environment setup using uv
git clone https://github.com/Sunwood-ai-labs/SourceSage.git
cd SourceSage
uv sync

# Run tests
uv run pytest

# Code formatting
uv run black sourcesage/
uv run isort sourcesage/

# Build package
uv build
```


## 💡 Usage Examples

```bash
# 1) Output repository summary (default: uses .gitignore)
uv run ss

# 2) Output summary using .SourceSageignore
uv run ss --use-sourcesage-ignore

# 3) Generate diff report (deprecated feature)
uv run ss --generate-diff-report

# 4) Change output destination
uv run ss --ss-output ./analysis
```

## Contributing

Help us improve SourceSage! If you have bug reports or feature suggestions, please open an issue or submit a pull request at our [GitHub repository](https://github.com/Sunwood-ai-labs/SourceSage).

## License

This project is released under the [MIT License](LICENSE).
