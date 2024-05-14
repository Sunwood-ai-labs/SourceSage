import argparse
from .core import SourceSage
from .modules.ReleaseDiffReportGenerator import GitDiffGenerator, MarkdownReportGenerator
import os
from loguru import logger
import sys
from art import *

logger.configure(
    handlers=[
        {
            "sink": sys.stderr,
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level:<8}</level> | <cyan>{name:<45}:{line:<5}</cyan> | <level>{message}</level>",
            "colorize": True,
        }
    ]
)

def main():
    parser = argparse.ArgumentParser(description='SourceSage CLI')
    parser.add_argument('--config', help='設定ファイルへのパス', default='sourcesage.yml')
    parser.add_argument('--output', help='生成されたファイルの出力ディレクトリ', default='./')
    parser.add_argument('--repo', help='リポジトリへのパス', default='./')
    parser.add_argument('--owner', help='リポジトリのオーナー', default='Sunwood-ai-labs')  
    parser.add_argument('--repository', help='リポジトリの名前', default='SourceSage')  

    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_ignore_file = os.path.join(package_root, 'sourcesage', 'config', '.SourceSageignore')
    default_language_map = os.path.join(package_root, 'sourcesage', 'config', 'language_map.json')

    current_dir_ignore_file = os.path.join(os.getcwd(), '.SourceSageignore')
    if os.path.exists(current_dir_ignore_file):
        ignore_file = current_dir_ignore_file
        logger.info(f"カレントディレクトリの無視ファイルを使用: {ignore_file}")
    else:
        ignore_file = default_ignore_file
        logger.info(f"デフォルトの無視ファイルを使用: {ignore_file}")

    parser.add_argument('--ignore-file', help='無視ファイルへのパス', default=ignore_file)
    parser.add_argument('--language-map', help='言語マップファイルへのパス', default=default_language_map)
    
    # レポート生成用の引数を追加
    parser.add_argument('--repo-path', type=str, default="", help='gitリポジトリへのパス')
    parser.add_argument('--git-fetch-tags', type=str, nargs='+', default=["git", "fetch", "--tags"], help='gitタグを取得するコマンド')
    parser.add_argument('--git-tag-sort', type=str, nargs='+', default=["git", "tag", "--sort=-creatordate"], help='gitタグをソートするコマンド')
    parser.add_argument('--git-diff-command', type=str, nargs='+', default=["git", "diff"], help='git diffを生成するコマンド')
    parser.add_argument('--report-title', type=str, default="Git Diff レポート", help='Markdownレポートのタイトル')
    parser.add_argument('--report-sections', type=str, nargs='+', default=["version_comparison", "diff_details"], help='レポートに含めるセクション')
    parser.add_argument('--output-path', type=str, default=".SourceSageAssets/RELEASE_REPORT/", help='Markdownレポートの保存先フォルダ')
    parser.add_argument('--report-file-name', type=str, default="Report_{latest_tag}.md", help='Markdownレポートのファイル名。{latest_tag}は最新のタグに置換されます。')
    
    args = parser.parse_args()

    # SourceSageの実行
    sourcesage = SourceSage(args.config, args.output, args.repo, args.owner, args.repository, args.ignore_file, args.language_map)
    sourcesage.run()

    # レポートの生成
    logger.info("git diff レポートの生成を開始します...")
    git_diff_generator = GitDiffGenerator(args.repo_path, args.git_fetch_tags, args.git_tag_sort, args.git_diff_command)
    diff, latest_tag, previous_tag = git_diff_generator.get_git_diff()

    report_file_name = args.report_file_name.format(latest_tag=latest_tag)
    os.makedirs(args.output_path, exist_ok=True)
    output_path = os.path.join(args.output_path, report_file_name)

    markdown_report_generator = MarkdownReportGenerator(diff, latest_tag, previous_tag, args.report_title, args.report_sections, output_path)
    markdown_report_generator.generate_markdown_report()

    logger.success("プロセスが完了しました。")
    tprint("!! successfully !!", font="rnd-medium")

if __name__ == '__main__':
    main()