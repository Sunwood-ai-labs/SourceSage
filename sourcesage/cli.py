# sourcesage\cli.py
import argparse
from .core import SourceSage
from .modules.ReleaseDiffReportGenerator import GitDiffGenerator, MarkdownReportGenerator
import os
from loguru import logger
import sys
from art import *

from .config.constants import Constants
from .modules.CommitCraft import CommitCraft
from .modules.DocuMind import DocuMind

logger.configure(
    handlers=[
        {
            "sink": sys.stderr,
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level:<10}</level> | <cyan>{name:<45}:{line:<5}</cyan> | <level>{message}</level>",
            "colorize": True,
        }
    ]
)

def main():
    parser = argparse.ArgumentParser(description='SourceSage CLI')
    tprint("   SourceSage", font="rnd-xlarge")
    
    # ==============================================
    # 基本設定
    #
    parser.add_argument('--config', help='設定ファイルへのパス', default='sourcesage.yml')
    parser.add_argument('--output', help='生成されたファイルの出力ディレクトリ', default='./')
    parser.add_argument('--repo', help='リポジトリへのパス', default='./')
    parser.add_argument('--owner', help='リポジトリのオーナー', default='Sunwood-ai-labs')  
    parser.add_argument('--repository', help='リポジトリの名前', default='SourceSage')  
    parser.add_argument('--mode', nargs='+', help='実行するモード: Sage, GenerateReport, CommitCraft, DocuMind, または all', default='all')

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
    parser.add_argument('--output-path', type=str, default=".SourceSageAssets/RELEASE_REPORT/", help='Markdownレポートの保存先フォルダ')
    parser.add_argument('--report-file-name', type=str, default="Report_{latest_tag}.md", help='Markdownレポートのファイル名。{latest_tag}は最新のタグに置換されます。')
    
    # ==============================================
    # CommitCraft用の引数を追加
    #
    parser.add_argument('--llm-output', type=str, default="llm_output.md", help='LLMレスポンスの出力ファイル')
    parser.add_argument('--model-name', type=str, default=None, help='LLMのモデル名（デフォルト: None）')
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
        
    args = parser.parse_args()

    # -----------------------------------------------
    # SourceSageの実行
    #
    if 'all' in args.mode or 'Sage' in args.mode:
        logger.info("SourceSageを起動します...")
        sourcesage = SourceSage(args.config, args.output, args.repo, args.owner, args.repository, args.ignore_file, args.language_map)
        sourcesage.run()

    # -----------------------------------------------
    # レポートの生成
    #
    if 'all' in args.mode or 'GenerateReport' in args.mode:
        logger.info("git diff レポートの生成を開始します...")
        git_diff_generator = GitDiffGenerator(args.repo_path, args.git_fetch_tags, args.git_tag_sort, args.git_diff_command)
        diff, latest_tag, previous_tag = git_diff_generator.get_git_diff()

        if(diff != None):
            report_file_name = args.report_file_name.format(latest_tag=latest_tag)
            os.makedirs(args.output_path, exist_ok=True)
            output_path = os.path.join(args.output_path, report_file_name)

            markdown_report_generator = MarkdownReportGenerator(diff, latest_tag, previous_tag, args.report_title, args.report_sections, output_path)
            markdown_report_generator.generate_markdown_report()

    # -----------------------------------------------
    # CommitCraftを使用してLLMにステージ情報を送信し、コミットメッセージを生成
    #
    if 'all' in args.mode or 'CommitCraft' in args.mode:
        stage_info_file = args.stage_info_file
        llm_output_file = os.path.join(args.commit_craft_output, args.llm_output)
        os.makedirs(args.commit_craft_output, exist_ok=True)
        commit_craft = CommitCraft(args.model_name, stage_info_file, llm_output_file)
        commit_craft.generate_commit_messages()
    
    # -----------------------------------------------
    # DocuMindを使用してリリースノートを生成
    #
    if 'all' in args.mode or 'DocuMind' in args.mode:
        docuMind = DocuMind(args.docuMind_model, args.docuMind_db, args.docuMind_release_report, args.docuMind_changelog, args.repo_name, args.repo_version, args.docuMind_prompt_output)
        release_notes = docuMind.generate_release_notes()
        docuMind.save_release_notes(args.docuMind_output, release_notes)

    logger.success("プロセスが完了しました。")
    tprint("!! successfully !!", font="rnd-medium")

if __name__ == '__main__':
    main()