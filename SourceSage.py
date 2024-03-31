import os
import sys
from modules.EnvFileHandler import create_or_append_env_file
from modules.source_sage import SourceSage
from modules.ChangelogGenerator import ChangelogGenerator
from modules.StageInfoGenerator import StageInfoGenerator
from modules.GitHubIssueRetrieve import GitHubIssueRetriever
from modules.StagedDiffGenerator import StagedDiffGenerator
from modules.IssuesToMarkdown import IssuesToMarkdown

create_or_append_env_file()  # .envファイルがない場合は作成、ある場合は追記

try:
    from dotenv import load_dotenv
    # .envファイルから環境変数を読み込む
    load_dotenv()
except ImportError:
    pass


if __name__ == "__main__":
    repo_path = os.getenv("REPO_PATH")
    source_sage_assets_dir = os.getenv("SOURCE_SAGE_ASSETS_DIR")
    config_dir = os.getenv("CONFIG_DIR")
    docs_dir = os.getenv("DOCS_DIR")
    issue_log_dir = os.getenv("ISSUE_LOG_DIR")


    folders = os.getenv("FOLDERS").split(",")  # カンマ区切りの文字列をリストに変換
    source_sage = SourceSage(folders, ignore_file=os.getenv("IGNORE_FILE"),
                             output_file=os.getenv("OUTPUT_FILE"),
                             language_map_file=os.getenv("LANGUAGE_MAP_FILE"))
    source_sage.generate_markdown()

    changelog_output_dir = f"{source_sage_assets_dir}/Changelog"
    os.makedirs(changelog_output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    generator = ChangelogGenerator(repo_path, changelog_output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()

    owner = os.getenv("OWNER")
    repository = os.getenv("REPOSITORY")
    issues_file_name = os.getenv("ISSUES_FILE_NAME")

    issue_retriever = GitHubIssueRetriever(owner, repository, source_sage_assets_dir + "/" + issue_log_dir, issues_file_name)
    issue_retriever.run()


    diff_generator = StagedDiffGenerator(
        repo_path=repo_path,
        output_dir=source_sage_assets_dir,
        language_map_file=f"{config_dir}/language_map.json"
    )
    diff_generator.run()

    stage_info_generator = StageInfoGenerator(
        issue_file_path=f"{source_sage_assets_dir}/{issue_log_dir}/{issues_file_name}",
        stage_diff_file_path=f"{source_sage_assets_dir}/STAGED_DIFF.md",
        template_file_path=f"{docs_dir}/STAGE_INFO/STAGE_INFO_AND_ISSUES_TEMPLATE.md",
        output_file_path=f"{source_sage_assets_dir}/STAGE_INFO/STAGE_INFO_AND_ISSUES_AND_PROMT.md"
    )
    stage_info_generator.run()

    stage_info_generator = StageInfoGenerator(
        issue_file_path=f"{source_sage_assets_dir}/{issue_log_dir}/{issues_file_name}",
        stage_diff_file_path=f"{source_sage_assets_dir}/STAGED_DIFF.md",
        template_file_path=f"{docs_dir}/STAGE_INFO/STAGE_INFO_TEMPLATE.md",
        output_file_path=f"{source_sage_assets_dir}/STAGE_INFO/STAGE_INFO_AND_PROMT.md"
    )
    stage_info_generator.run()

    issues_markdown_output_dir = f"{source_sage_assets_dir}/ISSUES_RESOLVE"
    converter = IssuesToMarkdown(
        issues_file=f"{source_sage_assets_dir}/{issue_log_dir}/{issues_file_name}",
        sourcesage_file=f"{source_sage_assets_dir}/SourceSage.md",
        template_file=f"{docs_dir}/ISSUES_RESOLVE/ISSUES_RESOLVE_TEMPLATE.md",
        output_folder=issues_markdown_output_dir
    )
    converter.load_data()
    converter.create_markdown_files()