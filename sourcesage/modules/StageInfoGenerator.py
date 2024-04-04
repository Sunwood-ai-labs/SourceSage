# modules/StageInfoGenerator.py (変更後)

import json
import os
from .GitHubIssueRetrieve import GitHubIssueRetriever
from .StagedDiffGenerator import StagedDiffGenerator

class StageInfoGenerator:
    def __init__(self, issue_file_path, stage_diff_file_path, template_file_path, output_file_path):
        self.issue_file_path = issue_file_path
        self.stage_diff_file_path = stage_diff_file_path
        self.template_file_path = template_file_path
        self.output_file_path = output_file_path

    def load_issues(self):
        with open(self.issue_file_path, "r", encoding="utf-8") as issue_file:
            return json.load(issue_file)

    def load_stage_diff(self):
        with open(self.stage_diff_file_path, "r", encoding="utf-8") as diff_file:
            return diff_file.read()

    def load_template(self):
        with open(self.template_file_path, "r", encoding="utf-8") as template_file:
            return template_file.read()

    def generate_stage_info(self):
        issues = self.load_issues()
        stage_diff = self.load_stage_diff()
        template = self.load_template()

        output_dir = os.path.dirname(self.output_file_path)
        os.makedirs(output_dir, exist_ok=True)

        # テンプレートの [open_issues_filtered.json] の位置に issues を挿入
        template = template.replace("[open_issues_filtered.json]", json.dumps(issues, indent=2, ensure_ascii=False))

        # テンプレートの [STAGED_DIFF.md] の位置に stage_diff を挿入
        template = template.replace("[STAGED_DIFF.md]", stage_diff)

        with open(self.output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(template)

    def run(self):
        self.generate_stage_info()

if __name__ == "__main__":
    owner = "Sunwood-ai-labs"
    repository = "SourceSage"
    save_path = "SourceSageAssets"
    file_name = "open_issues_filtered.json"

    issue_retriever = GitHubIssueRetriever(owner, repository, save_path, file_name)
    issue_retriever.run()

    diff_generator = StagedDiffGenerator(
        repo_path="./",
        output_dir="SourceSageAssets",
        language_map_file="config/language_map.json"
    )
    diff_generator.run()

    stage_info_generator = StageInfoGenerator(
        issue_file_path="SourceSageAssets/open_issues_filtered.json",
        stage_diff_file_path="SourceSageAssets/STAGED_DIFF.md",
        template_file_path="docs/STAGE_INFO/STAGE_INFO_AND_ISSUES_TEMPLATE.md",
        output_file_path="SourceSageAssets/STAGE_INFO_AND_ISSUES_AND_PROMT.md"
    )
    stage_info_generator.run()

    stage_info_generator = StageInfoGenerator(
        issue_file_path="SourceSageAssets/open_issues_filtered.json",
        stage_diff_file_path="SourceSageAssets/STAGED_DIFF.md",
        template_file_path="docs/STAGE_INFO/STAGE_INFO_TEMPLATE.md",
        output_file_path="SourceSageAssets/STAGE_INFO_AND_PROMT.md"
    )
    stage_info_generator.run()