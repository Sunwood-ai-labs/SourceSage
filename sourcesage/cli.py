# sourcesage\cli.py
import argparse
from .core import SourceSage
from .modules.ReleaseDiffReportGenerator import GitDiffGenerator, MarkdownReportGenerator
import os
from loguru import logger
import sys
from art import *
import yaml

from .config.constants import Constants
from .modules.CommitCraft import CommitCraft
from .modules.DocuMind import DocuMind
from .modules.IssueWize import IssueWize

logger.configure(
    handlers=[
        {
            "sink": sys.stderr,
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level:<10}</level> | <cyan>{name:<45}:{line:<5}</cyan> | <level>{message}</level>",
            "colorize": True,
        }
    ]
)

def add_arguments(parser):
    """SourceSage用の引数をパーサーに追加する"""
    
    # ==============================================
    # 基本設定
    #
    parser.add_argument('--ss-config', help='設定ファイルへのパス', default='sourcesage.yml')
    parser.add_argument('--ss-output', help='生成されたファイルの出力ディレクトリ', default='./')
    parser.add_argument('--repo', help='リポジトリへのパス', default='./')
    parser.add_argument('--owner', help='リポジトリのオーナー', default='Sunwood-ai-labs')  
    parser.add_argument('--repository', help='リポジトリの名前', default='SourceSage')  
    parser.add_argument('--ss-mode', nargs='+', help='実行するモード: Sage, GenerateReport, CommitCraft, DocuMind, IssueWize, またはall', default='all')
    # ==============================================
    # 変更履歴の設定
    #
    parser.add_argument('--changelog-start-tag', type=str, default=None, help='変更履歴の開始タグ')
    parser.add_argument('--changelog-end-tag', type=str, default=None, help='変更履歴の終了タグ')


    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_ignore_file = os.path.join(package_root, 'sourcesage', 'config', '.SourceSageignore')
    default_language_map = os.path.join(package_root, 'sourcesage', 'config', 'language_map.json')
    
    # ==============================================
    # 無視ファイルと言語マップ設定
    #
    current_dir_ignore_file = os.path.join(os.getcwd(), '.SourceSageignore')
    if os.path.exists(current_dir_ignore_file):
        ignore_file = current_dir_ignore_file
        logger.info(f"カレントディレクトリの無視ファイルを使用: {ignore_file}")
    else:
        ignore_file = default_ignore_file
        logger.info(f"デフォルトの無視ファイルを使用: {ignore_file}")

    parser.add_argument('--ignore-file', help='無視ファイルへのパス', default=ignore_file)
    parser.add_argument('--language-map', help='言語マップファイルへのパス', default=default_language_map)
    
    # ==============================================
    # レポート生成用の引数を追加
    #
    parser.add_argument('--repo-path', type=str, default="", help='gitリポジトリへのパス')
    parser.add_argument('--git-fetch-tags', type=str, nargs='+', default=["git", "fetch", "--tags"], help='gitタグを取得するコマンド')
    parser.add_argument('--git-tag-sort', type=str, nargs='+', default=["git", "tag", "--sort=-creatordate"], help='gitタグをソートするコマンド')
    parser.add_argument('--git-diff-command', type=str, nargs='+', default=["git", "diff"], help='git diffを生成するコマンド')
    parser.add_argument('--report-title', type=str, default="Git Diff レポート", help='Markdownレポートのタイトル')
    parser.add_argument('--report-sections', type=str, nargs='+', default=["version_comparison", "diff_details"], help='レポートに含めるセクション')
    parser.add_argument('--ss-output-path', type=str, default=".SourceSageAssets/RELEASE_REPORT/", help='Markdownレポートの保存先フォルダ')
    parser.add_argument('--report-file-name', type=str, default="Report_{latest_tag}.md", help='Markdownレポートのファイル名。{latest_tag}は最新のタグに置換されます。')
    
    # ==============================================
    # IssueWize用の引数を追加
    #
    parser.add_argument('--issue-summary', type=str, default=None, help='Issueの概要')
    parser.add_argument('--project-name', type=str, default=None, help='IssueWizeのプロジェクト名')
    parser.add_argument('--milestone-name', type=str, default=None, help='IssueWizeのマイルストーン名')
    parser.add_argument('--repo-overview-file', type=str, default=None, help='リポジトリ概要のマークダウンファイルパス')
    parser.add_argument('--issuewize-model', type=str, default=None, help='IssueWizeで使用するモデル名')
    
    # ==============================================
    # CommitCraft用の引数を追加
    #
    parser.add_argument('--llm-output', type=str, default="llm_output.md", help='LLMレスポンスの出力ファイル')
    parser.add_argument('--ss-model-name', type=str, default=None, help='LLMのモデル名（デフォルト: None）')
    parser.add_argument('--stage-info-file', type=str, default=".SourceSageAssets\COMMIT_CRAFT/STAGE_INFO\STAGE_INFO_AND_PROMT_GAIAH_B.md", help='ステージファイルパス')
    parser.add_argument('--commit-craft-output', type=str, default=".SourceSageAssets/COMMIT_CRAFT/", help='CommitCraftの出力フォルダ')
    
    # ==============================================
    # DocuMind用の引数を追加
    #
    parser.add_argument('--docuMind-model', type=str, default=None, help='DocuMindで使用するLLMのモデル名')
    parser.add_argument('--docuMind-db', type=str, default=".SourceSageAssets/DOCUMIND/Repository_summary.md", help='DocuMindのデータベースファイルのパス')
    parser.add_argument('--docuMind-release-report', type=str, default=".SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md", help='リリースレポートのパス。{latest_tag}は最新のタグに置換されます。')
    parser.add_argument('--docuMind-changelog', type=str, default=".SourceSageAssets/Changelog/CHANGELOG_release_{version}.md", help='変更履歴のパス。{version}はバージョンに置換されます。')
    parser.add_argument('--docuMind-output', type=str, default=".SourceSageAssets/DOCUMIND/RELEASE_NOTES.md", help='リリースノートの出力パス')
    parser.add_argument('--docuMind-prompt-output', type=str, default=".SourceSageAssets/DOCUMIND/_PROMPT.md", help='リリースノート作成のプロンプト')
    parser.add_argument('--repo-name', type=str, default="SourceSage", help='リポジトリの名前')
    parser.add_argument('--repo-version', type=str, default="v0.2.0", help='リポジトリのバージョン')
    
    # ==============================================
    # Configファイル
    #
    parser.add_argument('-f', '--yaml-file', help='設定をyamlファイルから読み込む', default=None)

def parse_arguments():
    """コマンドライン引数を解析する"""
    parser = argparse.ArgumentParser(description='SourceSage CLI')
    tprint(" SourceSage", font="rnd-xlarge")
    add_arguments(parser)
    return parser.parse_args()

def load_config_from_yaml(yaml_file=None):
    """YAMLファイルから設定を読み込み、argparse.Namespaceオブジェクトを返す"""
    default_config_file = 'sourcesage_config.yml'

    if yaml_file:
        config_file = yaml_file
    elif os.path.exists(default_config_file):
        config_file = default_config_file
    else:
        return None  # 設定ファイルが見つからない場合は None を返す

    logger.info(f"{config_file}を読み込みます...")
    with open(config_file, 'r') as f:
        yaml_args = yaml.safe_load(f)
        args_dict = {}  # args_dict を初期化
        for key, value in yaml_args.items():
            key = key.replace("-", "_")
            logger.debug(">> {: >30} : {: <20}".format(str(key), str(value)))
            args_dict[key] = value
        return argparse.Namespace(**args_dict)

def log_arguments(args):
    """引数の内容をログ出力する"""
    logger.info(f"---------------------------- パラメータ ----------------------------")
    args_dict = vars(args)
    for key, value in args_dict.items():
        key = key.replace("-", "_")
        logger.debug(">> {: >30} : {: <20}".format(str(key), str(value)))

def run(args=None):
      
    # -----------------------------------------------
    # SourceSageの実行
    if 'all' in args.ss_mode or 'Sage' in args.ss_mode:
        logger.info("SourceSageを起動します...")
        sourcesage = SourceSage(args.ss_config, args.ss_output, args.repo, args.owner, args.repository, args.ignore_file, args.language_map,
                                args.changelog_start_tag, args.changelog_end_tag)
        sourcesage.run()

    # -----------------------------------------------  
    # IssueWizeを使用してIssueを作成
    #
    if 'all' in args.ss_mode or 'IssueWize' in args.ss_mode:
        issuewize = IssueWize(model=args.issuewize_model)
        if args.issue_summary and args.project_name and args.repo_overview_file:
            logger.info("IssueWizeを使用してIssueを作成します...")
            issuewize.create_optimized_issue(args.issue_summary, args.project_name, args.milestone_name, args.repo_overview_file)
        else:
            logger.warning("IssueWizeの実行に必要なパラメータが指定されていません。--issue-summary, --project-name, --repo-overview-fileを指定してください。")
        

    # -----------------------------------------------
    # レポートの生成
    #
    if 'all' in args.ss_mode or 'GenerateReport' in args.ss_mode:
        logger.info("git diff レポートの生成を開始します...")
        git_diff_generator = GitDiffGenerator(args.repo_path, args.git_fetch_tags, args.git_tag_sort, args.git_diff_command)
        diff, latest_tag, previous_tag = git_diff_generator.get_git_diff()

        if(diff != None):
            report_file_name = args.report_file_name.format(latest_tag=latest_tag)
            os.makedirs(args.ss_output_path, exist_ok=True)
            output_path = os.path.join(args.ss_output_path, report_file_name)

            markdown_report_generator = MarkdownReportGenerator(diff, latest_tag, previous_tag, args.report_title, args.report_sections, output_path)
            markdown_report_generator.generate_markdown_report()

    # -----------------------------------------------
    # CommitCraftを使用してLLMにステージ情報を送信し、コミットメッセージを生成
    #
    if 'all' in args.ss_mode or 'CommitCraft' in args.ss_mode:
        stage_info_file = args.stage_info_file
        llm_output_file = os.path.join(args.commit_craft_output, args.llm_output)
        os.makedirs(args.commit_craft_output, exist_ok=True)
        commit_craft = CommitCraft(args.ss_model_name, stage_info_file, llm_output_file)
        commit_craft.generate_commit_messages()
    
    # -----------------------------------------------
    # DocuMindを使用してリリースノートを生成
    #
    if 'all' in args.ss_mode or 'DocuMind' in args.ss_mode:
        docuMind = DocuMind(args.docuMind_model, args.docuMind_db, args.docuMind_release_report, args.docuMind_changelog, args.repo_name, args.repo_version, args.docuMind_prompt_output)
        release_notes = docuMind.generate_release_notes()
        docuMind.save_release_notes(args.docuMind_output, release_notes)

    logger.success("プロセスが完了しました。")
    tprint("!! successfully !!", font="rnd-medium")

def main():
    
    from dotenv import load_dotenv
    dotenv_path=os.path.join(os.getcwd(), '.env')
    logger.debug(f"dotenv_path : {dotenv_path}")
    load_dotenv(dotenv_path=dotenv_path, verbose=True, override=True)
    
    _args = parse_arguments() 
    args = load_config_from_yaml(_args.yaml_file) or _args 
    log_arguments(args) 
    run(args)

if __name__ == '__main__':
    main()
