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
    parser.add_argument('--config', help='Path to the configuration file', default='sourcesage.yml')
    parser.add_argument('--output', help='Output directory for generated files', default='./')
    parser.add_argument('--repo', help='Path to the repository', default='./')
    parser.add_argument('--owner', help='Owner of the repository', default='Sunwood-ai-labs')  
    parser.add_argument('--repository', help='Name of the repository', default='SourceSage')  

    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_ignore_file = os.path.join(package_root, 'sourcesage', 'config', '.SourceSageignore')
    default_language_map = os.path.join(package_root, 'sourcesage', 'config', 'language_map.json')

    current_dir_ignore_file = os.path.join(os.getcwd(), '.SourceSageignore')
    if os.path.exists(current_dir_ignore_file):
        ignore_file = current_dir_ignore_file
        logger.info(f"Using ignore file from current directory: {ignore_file}")
    else:
        ignore_file = default_ignore_file
        logger.info(f"Using default ignore file: {ignore_file}")

    parser.add_argument('--ignore-file', help='Path to the ignore file', default=ignore_file)
    parser.add_argument('--language-map', help='Path to the language map file', default=default_language_map)
    
    # レポート生成用の引数を追加
    parser.add_argument('--repo-path', type=str, default="", help='Path to the git repository')
    parser.add_argument('--git-fetch-tags', type=str, nargs='+', default=["git", "fetch", "--tags"], help='Command to fetch git tags')
    parser.add_argument('--git-tag-sort', type=str, nargs='+', default=["git", "tag", "--sort=-creatordate"], help='Command to sort git tags')
    parser.add_argument('--git-diff-command', type=str, nargs='+', default=["git", "diff"], help='Command to generate git diff')
    parser.add_argument('--report-title', type=str, default="Git Diff レポート", help='Title of the Markdown report')
    parser.add_argument('--report-sections', type=str, nargs='+', default=["version_comparison", "diff_details"], help='Sections to include in the report')
    parser.add_argument('--output-path', type=str, default=".SourceSageAssets/git_diff_report.md", help='Path to save the Markdown report')
    
    args = parser.parse_args()

    # SourceSageの実行
    sourcesage = SourceSage(args.config, args.output, args.repo, args.owner, args.repository, args.ignore_file, args.language_map)
    sourcesage.run()

    # レポートの生成
    logger.info("git diff レポートの生成を開始します...")
    git_diff_generator = GitDiffGenerator(args.repo_path, args.git_fetch_tags, args.git_tag_sort, args.git_diff_command)
    diff, latest_tag, previous_tag = git_diff_generator.get_git_diff()

    markdown_report_generator = MarkdownReportGenerator(diff, latest_tag, previous_tag, args.report_title, args.report_sections, args.output_path)
    markdown_report_generator.generate_markdown_report()

    logger.success("プロセスが完了しました。")
    tprint("!! successfully !!", font="rnd-medium")

if __name__ == '__main__':
    main()