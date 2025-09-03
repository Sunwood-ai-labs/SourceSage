# sourcesage\cli.py
import argparse
import os
import sys

from art import *
from loguru import logger
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.theme import Theme

from .core import SourceSage
from .logging_utils import setup_rich_logging
from .modules.DiffReport import GitDiffGenerator, MarkdownReportGenerator

# Configure loguru to use Rich styling globally
console = setup_rich_logging()
console = Console(
    theme=Theme(
        {"info": "cyan", "success": "green", "warn": "yellow", "error": "bold red"}
    )
)

# logger is now styled via Rich; no explicit loguru formatter here


def add_arguments(parser):
    """SourceSage用の引数をパーサーに追加する"""

    # ==============================================
    # 基本設定
    #
    parser.add_argument(
        "--ss-output", help="生成されたファイルの出力ディレクトリ", default="./"
    )
    parser.add_argument("--repo", help="リポジトリへのパス", default="./")
    parser.add_argument(
        "--ss-mode",
        nargs="+",
        help="実行するモード: Sage, GenerateReport, またはall",
        default=["all"],
    )

    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_ignore_file_pkg = os.path.join(
        package_root, "sourcesage", "config", ".SourceSageignore"
    )
    default_language_map = os.path.join(
        package_root, "sourcesage", "config", "language_map.json"
    )

    # ==============================================
    # 無視ファイルと言語マップ設定
    #
    # Create/use .SourceSageignore in the current working directory by default
    ignore_file_cwd = os.path.join(os.getcwd(), ".SourceSageignore")
    parser.add_argument(
        "--ignore-file", help="無視ファイルへのパス", default=ignore_file_cwd
    )
    parser.add_argument(
        "--language-map",
        help="言語マップファイルへのパス",
        default=default_language_map,
    )

    # ==============================================
    # レポート生成用の引数を追加
    #
    parser.add_argument(
        "--repo-path",
        type=str,
        default="",
        help="gitリポジトリへのパス（省略時はカレントディレクトリ）",
    )
    parser.add_argument(
        "--git-fetch-tags",
        type=str,
        nargs="+",
        default=["git", "fetch", "--tags"],
        help="gitタグを取得するコマンド",
    )
    parser.add_argument(
        "--git-tag-sort",
        type=str,
        nargs="+",
        default=["git", "tag", "--sort=-creatordate"],
        help="gitタグをソートするコマンド",
    )
    parser.add_argument(
        "--git-diff-command",
        type=str,
        nargs="+",
        default=["git", "diff"],
        help="git diffを生成するコマンド",
    )
    parser.add_argument(
        "--report-title",
        type=str,
        default="Git Diff レポート",
        help="Markdownレポートのタイトル",
    )
    parser.add_argument(
        "--report-sections",
        type=str,
        nargs="+",
        default=["repo_info", "version_comparison", "diff_details", "readme"],
        help="レポートに含めるセクション (repo_info, version_comparison, diff_details, readme)",
    )
    parser.add_argument(
        "--ss-output-path",
        type=str,
        default=".SourceSageAssets/RELEASE_REPORT/",
        help="Markdownレポートの保存先フォルダ",
    )
    parser.add_argument(
        "--report-file-name",
        type=str,
        default="Report_{latest_tag}.md",
        help="Markdownレポートのファイル名。{latest_tag}は最新のタグに置換されます。",
    )

    # ==============================================
    # Help (custom Rich renderer)
    #
    parser.add_argument(
        "-h", "--help", action="store_true", help="このヘルプを表示して終了"
    )


def render_rich_help(parser: argparse.ArgumentParser):
    """Render a Rich-styled help screen."""
    console.print(Panel(Align.center("SourceSage CLI"), style="info", expand=True))

    # Usage
    usage = Text()
    usage.append("Usage:\n", style="bold")
    usage.append("  ss [options]\n")
    usage.append("  sourcesage [options]\n")
    console.print(Panel(usage, title="Usage", border_style="cyan", expand=True))

    # Modes
    modes = Text()
    modes.append("--ss-mode all ", style="green")
    modes.append("(デフォルト)\n")
    modes.append("--ss-mode Sage ", style="green")
    modes.append("(Repository Summaryのみ)\n")
    modes.append("--ss-mode GenerateReport ", style="green")
    modes.append("(Release Reportのみ)\n")
    console.print(Panel(modes, title="Modes", border_style="green", expand=True))

    # Core options
    core_tbl = Table(title="Core Options", show_header=True, header_style="bold cyan")
    core_tbl.add_column("Option")
    core_tbl.add_column("Default", style="dim")
    core_tbl.add_column("Description")

    def _get_default(dest, fallback=""):
        for a in parser._actions:
            if a.dest == dest:
                return a.default
        return fallback

    core_tbl.add_row(
        "--ss-output", str(_get_default("ss_output")), "生成ファイルの出力ディレクトリ"
    )
    core_tbl.add_row("--repo", str(_get_default("repo")), "解析対象のリポジトリパス")
    core_tbl.add_row(
        "--ignore-file", str(_get_default("ignore_file")), "無視パターンファイルのパス"
    )
    core_tbl.add_row(
        "--language-map", str(_get_default("language_map")), "言語マップJSONのパス"
    )
    core_tbl.add_row("--ss-mode", "[all|Sage|GenerateReport]", "実行モード")
    console.print(core_tbl)

    # Release report options
    rel_tbl = Table(
        title="Release Report Options", show_header=True, header_style="bold magenta"
    )
    rel_tbl.add_column("Option")
    rel_tbl.add_column("Default", style="dim")
    rel_tbl.add_column("Description")
    rel_tbl.add_row(
        "--repo-path", str(_get_default("repo_path")), "gitリポジトリのルートパス"
    )
    rel_tbl.add_row(
        "--git-fetch-tags", str(_get_default("git_fetch_tags")), "gitタグ取得コマンド"
    )
    rel_tbl.add_row(
        "--git-tag-sort", str(_get_default("git_tag_sort")), "gitタグソートコマンド"
    )
    rel_tbl.add_row(
        "--git-diff-command", str(_get_default("git_diff_command")), "git diff コマンド"
    )
    rel_tbl.add_row(
        "--report-title", str(_get_default("report_title")), "レポートタイトル"
    )
    rel_tbl.add_row(
        "--report-sections", str(_get_default("report_sections")), "含めるセクション"
    )
    rel_tbl.add_row(
        "--ss-output-path",
        str(_get_default("ss_output_path")),
        "レポート出力先フォルダ",
    )
    rel_tbl.add_row(
        "--report-file-name",
        str(_get_default("report_file_name")),
        "レポートファイル名",
    )
    console.print(rel_tbl)

    # Examples
    examples = Text()
    examples.append("Examples:\n", style="bold")
    examples.append("  ss\n")
    examples.append("  ss --ss-mode Sage\n")
    examples.append("  ss --ss-mode GenerateReport --report-title 'My Report'\n")
    console.print(Panel(examples, title="Examples", border_style="yellow", expand=True))


def parse_arguments():
    """コマンドライン引数を解析する"""
    parser = argparse.ArgumentParser(description="SourceSage CLI", add_help=False)
    # Title only: keep ASCII art
    tprint(" SourceSage", font="rnd-xlarge")
    add_arguments(parser)
    args = parser.parse_args()
    if getattr(args, "help", False):
        render_rich_help(parser)
        sys.exit(0)
    return args


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
    if "all" in args.ss_mode or "Sage" in args.ss_mode:
        console.print(
            Panel(Align.center("Repository Summary"), style="info", expand=True)
        )
        with console.status("[info]生成中...[/]", spinner="dots"):
            sourcesage = SourceSage(
                args.ss_output, args.repo, args.ignore_file, args.language_map
            )
            sourcesage.run()
        console.print("[success]Repository Summary 生成 完了[/]")

    # -----------------------------------------------
    # レポートの生成
    #
    if "all" in args.ss_mode or "GenerateReport" in args.ss_mode:
        console.print(Panel(Align.center("Release Report"), style="info", expand=True))
        with console.status("[info]git diff レポートを生成中...[/]", spinner="dots"):
            git_diff_generator = GitDiffGenerator(
                args.repo_path,
                args.git_fetch_tags,
                args.git_tag_sort,
                args.git_diff_command,
            )
            diff, latest_tag, previous_tag = git_diff_generator.get_git_diff()

        if diff != None:
            console.print(
                f"[info]最新タグ: [bold]{latest_tag}[/], 前のタグ: [bold]{previous_tag}[/]"
            )
            report_file_name = args.report_file_name.format(latest_tag=latest_tag)
            os.makedirs(args.ss_output_path, exist_ok=True)
            output_path = os.path.join(args.ss_output_path, report_file_name)

            repo_root = args.repo_path if args.repo_path else os.getcwd()
            markdown_report_generator = MarkdownReportGenerator(
                diff,
                latest_tag,
                previous_tag,
                args.report_title,
                args.report_sections,
                output_path,
                repo_path=repo_root,
            )
            with console.status(
                "[info]Markdown レポートを出力中...[/]", spinner="dots"
            ):
                markdown_report_generator.generate_markdown_report()
            console.print(f"[success]出力: [/][red]{output_path}[/]")
        else:
            console.print(
                "[warn]タグが見つからないため、Release Report をスキップしました[/]"
            )

    console.print(
        Panel(Align.center("プロセスが完了しました。"), style="success", expand=True)
    )


def main():

    from dotenv import load_dotenv

    dotenv_path = os.path.join(os.getcwd(), ".env")
    logger.debug(f"dotenv_path : {dotenv_path}")
    load_dotenv(dotenv_path=dotenv_path, verbose=True, override=True)

    args = parse_arguments()
    log_arguments(args)
    run(args)


if __name__ == "__main__":
    main()
