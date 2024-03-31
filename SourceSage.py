

import os
import sys
import pprint

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
pprint.pprint(sys.path)

from modules.source_sage import SourceSage
from modules.ChangelogGenerator import ChangelogGenerator
from modules.StageInfoGenerator import StageInfoGenerator
from modules.GitHubIssueRetrieve import GitHubIssueRetriever
from modules.StagedDiffGenerator import StagedDiffGenerator

if __name__ == "__main__":
    folders = ['./']
    source_sage = SourceSage(folders, ignore_file='.SourceSageignore',
                             output_file='SourceSageAssets/SourceSage.md',
                             language_map_file='config/language_map.json')
    source_sage.generate_markdown()

    repo_path = "./"
    output_dir = "SourceSageAssets/Changelog"
    os.makedirs(output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    generator = ChangelogGenerator(repo_path, output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()

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