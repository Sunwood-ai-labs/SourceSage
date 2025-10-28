from pathlib import Path
import sys

import pytest

ROOT_DIR = Path(__file__).resolve().parents[3]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from sourcesage.modules.DocuSum.file_pattern_matcher import FilePatternMatcher


@pytest.fixture
def ignore_file(tmp_path):
    ignore_path = tmp_path / ".SourceSageignore"
    ignore_path.write_text(".github/\n!.github/workflows/\n", encoding="utf-8")
    return ignore_path


def test_should_exclude_github_directory(tmp_path, ignore_file):
    matcher = FilePatternMatcher(str(ignore_file))

    github_dir = tmp_path / ".github"
    github_dir.mkdir()
    (github_dir / "config.yml").write_text("name: test\n", encoding="utf-8")

    assert matcher.should_exclude(str(github_dir)) is True
    assert matcher.should_exclude(str(github_dir / "config.yml")) is True


def test_should_include_negated_subdirectory(tmp_path, ignore_file):
    matcher = FilePatternMatcher(str(ignore_file))

    workflows_dir = tmp_path / ".github" / "workflows"
    workflows_dir.mkdir(parents=True)
    workflow_file = workflows_dir / "ci.yml"
    workflow_file.write_text("name: CI\n", encoding="utf-8")

    assert matcher.should_exclude(str(workflows_dir)) is False
    assert matcher.should_exclude(str(workflow_file)) is False
