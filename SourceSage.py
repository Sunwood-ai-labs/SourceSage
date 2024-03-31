# SourceSage.py (リファクタリング後)

import os
import sys
from modules.source_sage import SourceSage
from modules.ChangelogGenerator import ChangelogGenerator
from modules.StageInfoGenerator import StageInfoGenerator
from modules.GitHubIssueRetrieve import GitHubIssueRetriever
from modules.StagedDiffGenerator import StagedDiffGenerator
from modules.IssuesToMarkdown import IssuesToMarkdown

if __name__ == "__main__":
    repo_path = "./"
    source_sage_assets_dir = "SourceSageAssets"
    config_dir = "config"
    docs_dir = "docs"

    folders = [repo_path]
    source_sage = SourceSage(folders, ignore_file='.SourceSageignore',
                             output_file=f"{source_sage_assets_dir}/SourceSage.md",
                             language_map_file=f"{config_dir}/language_map.json")
    source_sage.generate_markdown()

    changelog_output_dir = f"{source_sage_assets_dir}/Changelog"
    os.makedirs(changelog_output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    generator = ChangelogGenerator(repo_path, changelog_output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()

    owner = "Sunwood-ai-labs"
    repository = "SourceSage"
    issues_file_name = "open_issues_filtered.json"

    issue_retriever = GitHubIssueRetriever(owner, repository, source_sage_assets_dir, issues_file_name)
    issue_retriever.run()

    diff_generator = StagedDiffGenerator(
        repo_path=repo_path,
        output_dir=source_sage_assets_dir,
        language_map_file=f"{config_dir}/language_map.json"
    )
    diff_generator.run()

    stage_info_generator = StageInfoGenerator(
        issue_file_path=f"{source_sage_assets_dir}/{issues_file_name}",
        stage_diff_file_path=f"{source_sage_assets_dir}/STAGED_DIFF.md",
        template_file_path=f"{docs_dir}/STAGE_INFO/STAGE_INFO_AND_ISSUES_TEMPLATE.md",
        output_file_path=f"{source_sage_assets_dir}/STAGE_INFO_AND_ISSUES_AND_PROMT.md"
    )
    stage_info_generator.run()

    stage_info_generator = StageInfoGenerator(
        issue_file_path=f"{source_sage_assets_dir}/{issues_file_name}",
        stage_diff_file_path=f"{source_sage_assets_dir}/STAGED_DIFF.md",
        template_file_path=f"{docs_dir}/STAGE_INFO/STAGE_INFO_TEMPLATE.md",
        output_file_path=f"{source_sage_assets_dir}/STAGE_INFO_AND_PROMT.md"
    )
    stage_info_generator.run()

    issues_markdown_output_dir = f"{source_sage_assets_dir}/ISSUES_RESOLVE"
    converter = IssuesToMarkdown(
        issues_file=f"{source_sage_assets_dir}/{issues_file_name}",
        sourcesage_file=f"{source_sage_assets_dir}/SourceSage.md",
        template_file=f"{docs_dir}/ISSUES_RESOLVE/ISSUES_RESOLVE_TEMPLATE.md",
        output_folder=issues_markdown_output_dir
    )
    converter.load_data()
    converter.create_markdown_files()