import os
import sys
from modules.EnvFileHandler import create_or_append_env_file
from modules.source_sage import SourceSage
from modules.ChangelogGenerator import ChangelogGenerator
from modules.StageInfoGenerator import StageInfoGenerator
from modules.GitHubIssueRetrieve import GitHubIssueRetriever
from modules.StagedDiffGenerator import StagedDiffGenerator
from modules.IssuesToMarkdown import IssuesToMarkdown

try:
    from dotenv import load_dotenv
    # .envファイルから環境変数を読み込む
    load_dotenv()
except ImportError:
    pass

if __name__ == "__main__":
    # 現在のスクリプトの絶対パス
    current_file_path = os.path.abspath(__file__)
    # SourceSage ディレクトリの絶対パス
    base_dir = os.path.dirname(current_file_path)
    # config ディレクトリの絶対パス
    config_dir = os.path.join(base_dir, 'config')

    # 以下、環境変数の利用を置き換えるためのパス設定
    repo_path = base_dir
    source_sage_assets_dir = os.path.join(repo_path, "SourceSageAssets")
    docs_dir = os.path.join(repo_path, "docs")
    issue_log_dir = os.path.join(source_sage_assets_dir, "ISSUE_LOG")
    issues_resolve_dir = os.path.join(source_sage_assets_dir, "ISSUES_RESOLVE")
    stage_info_dir = os.path.join(source_sage_assets_dir, "STAGE_INFO")

    os.makedirs(issue_log_dir, exist_ok=True)
    os.makedirs(issues_resolve_dir, exist_ok=True)
    os.makedirs(stage_info_dir, exist_ok=True)

    # カンマ区切りの文字列をリストに変換し、各フォルダパスを絶対パスに変換
    # folders = "./" # [repo_path]  # FOLDERS 環境変数を直接リストとして扱い、適宜修正してください
    # 現在の作業ディレクトリを取得
    working_dir = os.getcwd()
    # 探索するフォルダを現在の作業ディレクトリに設定
    folders = [working_dir]

    # language_map.json と .SourceSageignore ファイルの絶対パスを指定
    language_map_file = os.path.join(config_dir, 'language_map.json')
    ignore_file = os.path.join(config_dir, '.SourceSageignore')

    source_sage = SourceSage(folders, ignore_file=ignore_file,
                             output_file=os.path.join(source_sage_assets_dir, "SourceSage.md"),
                             language_map_file=language_map_file)
    source_sage.generate_markdown()

    changelog_output_dir = os.path.join(source_sage_assets_dir, "Changelog")
    os.makedirs(changelog_output_dir, exist_ok=True)

    generator = ChangelogGenerator(working_dir, changelog_output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()

    owner = "Sunwood-ai-labs"
    repository = "PythonDiagrammatic"
    issues_file_name = "open_issues_filtered.json"

    issue_retriever = GitHubIssueRetriever(owner, repository, issue_log_dir, issues_file_name)
    issue_retriever.run()

    diff_generator = StagedDiffGenerator(repo_path=repo_path, output_dir=source_sage_assets_dir,
                                         language_map_file=language_map_file)
    diff_generator.run()

    # StageInfoGenerator の template_file_path と output_file_path を適宜修正
    stage_info_template_path = os.path.join(docs_dir, "STAGE_INFO", "STAGE_INFO_AND_ISSUES_TEMPLATE.md")
    stage_info_output_path = os.path.join(stage_info_dir, "STAGE_INFO_AND_ISSUES_AND_PROMT.md")
    stage_info_generator = StageInfoGenerator(issue_file_path=os.path.join(issue_log_dir, issues_file_name),
                                              stage_diff_file_path=os.path.join(source_sage_assets_dir, "STAGED_DIFF.md"),
                                              template_file_path=stage_info_template_path,
                                              output_file_path=stage_info_output_path)
    stage_info_generator.run()

    # IssuesToMarkdown の template_file_path を適宜修正
    issues_resolve_template_path = os.path.join(docs_dir, "ISSUES_RESOLVE", "ISSUES_RESOLVE_TEMPLATE.md")
    converter = IssuesToMarkdown(issues_file=os.path.join(issue_log_dir, issues_file_name),
                                 sourcesage_file=os.path.join(source_sage_assets_dir, "SourceSage.md"),
                                 template_file=issues_resolve_template_path,
                                 output_folder=issues_resolve_dir)
    converter.load_data()
    converter.create_markdown_files()