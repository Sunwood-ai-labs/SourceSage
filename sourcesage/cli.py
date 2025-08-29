# sourcesage\cli.py
import argparse
from .core import SourceSage
from .modules.ReleaseDiffReportGenerator import GitDiffGenerator, MarkdownReportGenerator
import os
from loguru import logger
import sys
from art import *
from rich.console import Console
from rich.panel import Panel
from rich.theme import Theme
from .logging_utils import setup_rich_logging

# Configure loguru to use Rich styling globally
console = setup_rich_logging()
console = Console(theme=Theme({
    "info": "cyan",
    "success": "green",
    "warn": "yellow",
    "error": "bold red"
}))

# logger is now styled via Rich; no explicit loguru formatter here

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
    parser.add_argument('--ss-mode', nargs='+', help='実行するモード: Sage, GenerateReport, またはall', default=['all'])


    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_ignore_file_pkg = os.path.join(package_root, 'sourcesage', 'config', '.SourceSageignore')
    default_language_map = os.path.join(package_root, 'sourcesage', 'config', 'language_map.json')
    
    # ==============================================
    # 無視ファイルと言語マップ設定
    #
    # Prefer project-local .SourceSageignore; fallback to packaged default
    ignore_file_cwd = os.path.join(os.getcwd(), '.SourceSageignore')
    ignore_default = ignore_file_cwd if os.path.exists(ignore_file_cwd) else default_ignore_file_pkg

    parser.add_argument('--ignore-file', help='無視ファイルへのパス', default=ignore_default)
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
    # Configファイル
    #
    parser.add_argument('-f', '--yaml-file', help='設定をyamlファイルから読み込む', default=None)

def parse_arguments():
    """コマンドライン引数を解析する"""
    parser = argparse.ArgumentParser(description='SourceSage CLI')
    # Title only: keep ASCII art
    tprint(" SourceSage", font="rnd-xlarge")
    add_arguments(parser)
    return parser.parse_args()


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
        console.print(Panel.fit("Repository Summary", style="info"))
        with console.status("[info]生成中...[/]", spinner="dots"):
            sourcesage = SourceSage(args.ss_output, args.repo, args.owner, args.repository, args.ignore_file, args.language_map)
            sourcesage.run()
        console.print("[success]Repository Summary 生成 完了[/]")

    # -----------------------------------------------
    # レポートの生成
    #
    if 'all' in args.ss_mode or 'GenerateReport' in args.ss_mode:
        console.print(Panel.fit("Release Report", style="info"))
        with console.status("[info]git diff レポートを生成中...[/]", spinner="dots"):
            git_diff_generator = GitDiffGenerator(args.repo_path, args.git_fetch_tags, args.git_tag_sort, args.git_diff_command)
            diff, latest_tag, previous_tag = git_diff_generator.get_git_diff()

        if(diff != None):
            console.print(f"[info]最新タグ: [bold]{latest_tag}[/], 前のタグ: [bold]{previous_tag}[/]")
            report_file_name = args.report_file_name.format(latest_tag=latest_tag)
            os.makedirs(args.ss_output_path, exist_ok=True)
            output_path = os.path.join(args.ss_output_path, report_file_name)

            markdown_report_generator = MarkdownReportGenerator(diff, latest_tag, previous_tag, args.report_title, args.report_sections, output_path)
            with console.status("[info]Markdown レポートを出力中...[/]", spinner="dots"):
                markdown_report_generator.generate_markdown_report()
            console.print(f"[success]出力: {output_path}[/]")

    console.print(Panel.fit("プロセスが完了しました。", style="success"))

def main():
    
    from dotenv import load_dotenv
    dotenv_path=os.path.join(os.getcwd(), '.env')
    logger.debug(f"dotenv_path : {dotenv_path}")
    load_dotenv(dotenv_path=dotenv_path, verbose=True, override=True)
    
    
    args = parse_arguments()
    log_arguments(args)
    run(args)
if __name__ == '__main__':
    main()
