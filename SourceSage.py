import os
import sys
from modules.EnvFileHandler import create_or_append_env_file
from modules.source_sage import SourceSage
from modules.ChangelogGenerator import ChangelogGenerator
from modules.StageInfoGenerator import StageInfoGenerator
from modules.GitHubIssueRetrieve import GitHubIssueRetriever
from modules.StagedDiffGenerator import StagedDiffGenerator
from modules.IssuesToMarkdown import IssuesToMarkdown
import config.constants as const

def main():
    print("----------------------------")
    print("| Constants:")
    for name, value in vars(const).items():
        if not name.startswith("__"):
            print(f"| {name} : {value}")
    print()
    print("----------------------------")

    os.makedirs(const.ISSUE_LOG_DIR, exist_ok=True)
    os.makedirs(const.ISSUES_RESOLVE_DIR, exist_ok=True)
    os.makedirs(const.STAGE_INFO_DIR, exist_ok=True)

    # 探索するフォルダを現在の作業ディレクトリに設定
    folders = [os.getcwd()]

    source_sage = SourceSage(folders, ignore_file=const.IGNORE_FILE,
                             output_file=os.path.join(const.SOURCE_SAGE_ASSETS_DIR, const.SOURCE_SAGE_MD),
                             language_map_file=const.LANGUAGE_MAP_FILE)
    source_sage.generate_markdown()

    changelog_output_dir = os.path.join(const.SOURCE_SAGE_ASSETS_DIR, const.CHANGELOG_DIR)
    os.makedirs(changelog_output_dir, exist_ok=True)

    generator = ChangelogGenerator(os.getcwd(), changelog_output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()

    issue_retriever = GitHubIssueRetriever(const.OWNER, const.REPOSITORY, const.ISSUE_LOG_DIR, const.ISSUES_FILE_NAME)
    issue_retriever.run()

    diff_generator = StagedDiffGenerator(repo_path=const.REPO_PATH, output_dir=const.SOURCE_SAGE_ASSETS_DIR,
                                         language_map_file=const.LANGUAGE_MAP_FILE)
    diff_generator.run()

    stage_info_template_path = os.path.join(const.DOCS_DIR, const.TEMPLATE_STAGE_INFO_DIR, const.STAGE_INFO_TEMPLATE_MD)
    stage_info_output_path = os.path.join(const.STAGE_INFO_DIR, const.STAGE_INFO_OUTPUT_MD)
    stage_info_generator = StageInfoGenerator(issue_file_path=os.path.join(const.ISSUE_LOG_DIR, const.ISSUES_FILE_NAME),
                                              stage_diff_file_path=os.path.join(const.SOURCE_SAGE_ASSETS_DIR, const.STAGED_DIFF_MD),
                                              template_file_path=stage_info_template_path,
                                              output_file_path=stage_info_output_path)
    stage_info_generator.run()

    stage_info_template_path = os.path.join(const.DOCS_DIR, const.TEMPLATE_STAGE_INFO_DIR, const.STAGE_INFO_SIMPLE_TEMPLATE_MD)
    stage_info_output_path = os.path.join(const.STAGE_INFO_DIR, const.STAGE_INFO_SIMPLE_OUTPUT_MD)
    stage_info_generator = StageInfoGenerator(issue_file_path=os.path.join(const.ISSUE_LOG_DIR, const.ISSUES_FILE_NAME),
                                              stage_diff_file_path=os.path.join(const.SOURCE_SAGE_ASSETS_DIR, const.STAGED_DIFF_MD),
                                              template_file_path=stage_info_template_path,
                                              output_file_path=stage_info_output_path)
    stage_info_generator.run()

    issues_resolve_template_path = os.path.join(const.DOCS_DIR, const.TEMPLATE_ISSUES_RESOLVE_DIR, const.ISSUES_RESOLVE_TEMPLATE_MD)
    converter = IssuesToMarkdown(issues_file=os.path.join(const.ISSUE_LOG_DIR, const.ISSUES_FILE_NAME),
                                 sourcesage_file=os.path.join(const.SOURCE_SAGE_ASSETS_DIR, const.SOURCE_SAGE_MD),
                                 template_file=issues_resolve_template_path,
                                 output_folder=const.ISSUES_RESOLVE_DIR)
    converter.load_data()
    converter.create_markdown_files()

if __name__ == "__main__":
    main()