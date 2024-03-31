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
    source_sage_assets_dir = os.path.join(repo_path, os.getenv("SOURCE_SAGE_ASSETS_DIR"))
    config_dir = os.path.join(repo_path, os.getenv("CONFIG_DIR"))
    docs_dir = os.path.join(repo_path, os.getenv("DOCS_DIR"))
    issue_log_dir = os.path.join(source_sage_assets_dir, os.getenv("ISSUE_LOG_DIR"))
    issues_resolve_dir = os.path.join(source_sage_assets_dir, os.getenv("ISSUES_RESOLVE_DIR"))
    stage_info_dir = os.path.join(source_sage_assets_dir, os.getenv("STAGE_INFO_DIR"))

    os.makedirs(issue_log_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する
    os.makedirs(issues_resolve_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する
    os.makedirs(stage_info_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    folders = [os.path.join(repo_path, folder) for folder in os.getenv("FOLDERS").split(",")]  # カンマ区切りの文字列をリストに変換
    source_sage = SourceSage(folders, ignore_file=os.path.join(config_dir, os.getenv("IGNORE_FILE")),
                             output_file=os.path.join(source_sage_assets_dir, os.getenv("OUTPUT_FILE")),
                             language_map_file=os.path.join(config_dir, os.getenv("LANGUAGE_MAP_FILE")))
    source_sage.generate_markdown()

    changelog_output_dir = os.path.join(source_sage_assets_dir, "Changelog")
    os.makedirs(changelog_output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    generator = ChangelogGenerator(repo_path, changelog_output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()

    owner = os.getenv("OWNER")
    repository = os.getenv("REPOSITORY")
    issues_file_name = os.getenv("ISSUES_FILE_NAME")

    issue_retriever = GitHubIssueRetriever(owner, repository, issue_log_dir, issues_file_name)
    issue_retriever.run()

    diff_generator = StagedDiffGenerator(
        repo_path=repo_path,
        output_dir=source_sage_assets_dir,
        language_map_file=os.path.join(config_dir, "language_map.json")
    )
    diff_generator.run()

    stage_info_generator = StageInfoGenerator(
        issue_file_path=os.path.join(issue_log_dir, issues_file_name),
        stage_diff_file_path=os.path.join(source_sage_assets_dir, "STAGED_DIFF.md"),
        template_file_path=os.path.join(docs_dir, os.getenv("STAGE_INFO_DIR"), "STAGE_INFO_AND_ISSUES_TEMPLATE.md"),
        output_file_path=os.path.join(stage_info_dir, "STAGE_INFO_AND_ISSUES_AND_PROMT.md")
    )
    stage_info_generator.run()

    stage_info_generator = StageInfoGenerator(
        issue_file_path=os.path.join(issue_log_dir, issues_file_name),
        stage_diff_file_path=os.path.join(source_sage_assets_dir, "STAGED_DIFF.md"),
        template_file_path=os.path.join(docs_dir, os.getenv("STAGE_INFO_DIR"), "STAGE_INFO_TEMPLATE.md"),
        output_file_path=os.path.join(stage_info_dir, "STAGE_INFO_AND_PROMT.md")
    )
    stage_info_generator.run()

    converter = IssuesToMarkdown(
        issues_file=os.path.join(issue_log_dir, issues_file_name),
        sourcesage_file=os.path.join(source_sage_assets_dir, "SourceSage.md"),
        template_file=os.path.join(docs_dir, os.getenv("ISSUES_RESOLVE_DIR"), "ISSUES_RESOLVE_TEMPLATE.md"),
        output_folder=issues_resolve_dir
    )
    converter.load_data()
    converter.create_markdown_files()