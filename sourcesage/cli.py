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
        "-o", "--output", help="Output directory for generated files", default="./"
    )
    parser.add_argument("--repo", help="Path to the repository", default="./")
    parser.add_argument(
        "-l", "--lang", "--language",
        choices=["en", "ja"],
        default="en",
        dest="language",
        help="Output language (default: en)",
    )
    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show version and exit"
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
    # By default, use both .gitignore and .SourceSageignore
    # If .SourceSageignore doesn't exist, it will be auto-generated
    sourcesageignore_file = os.path.join(os.getcwd(), ".SourceSageignore")
    parser.add_argument(
        "--ignore-file",
        help="Path to ignore file (default: .SourceSageignore, also uses .gitignore if present)",
        default=sourcesageignore_file
    )
    parser.add_argument(
        "--language-map",
        help="Path to language map file",
        default=default_language_map,
    )

    # ==============================================
    # レポート生成用の引数を追加
    #
    parser.add_argument(
        "--diff",
        action="store_true",
        help="Generate diff report for release notes (deprecated: This feature will be removed in the future due to improved LLM command execution capabilities)",
    )
    parser.add_argument(
        "--repo-path",
        type=str,
        default="",
        help="Path to git repository (default: current directory)",
    )
    parser.add_argument(
        "--git-fetch-tags",
        type=str,
        nargs="+",
        default=["git", "fetch", "--tags"],
        help="Command to fetch git tags",
    )
    parser.add_argument(
        "--git-tag-sort",
        type=str,
        nargs="+",
        default=["git", "tag", "--sort=-creatordate"],
        help="Command to sort git tags",
    )
    parser.add_argument(
        "--git-diff-command",
        type=str,
        nargs="+",
        default=["git", "diff"],
        help="Command to generate git diff",
    )
    parser.add_argument(
        "--report-title",
        type=str,
        default="Git Diff Report",
        help="Markdown report title",
    )
    parser.add_argument(
        "--report-sections",
        type=str,
        nargs="+",
        default=["repo_info", "version_comparison", "diff_details", "readme"],
        help="Sections to include in report (repo_info, version_comparison, diff_details, readme)",
    )
    parser.add_argument(
        "--diff-output",
        type=str,
        default=".SourceSageAssets/RELEASE_REPORT/",
        help="Directory to save diff report",
    )
    parser.add_argument(
        "--report-file-name",
        type=str,
        default="Report_{latest_tag}.md",
        help="Markdown report filename. {latest_tag} will be replaced with the latest tag.",
    )

    # ==============================================
    # Help (custom Rich renderer)
    #
    parser.add_argument(
        "-h", "--help", action="store_true", help="Show this help and exit"
    )


def render_rich_help(parser: argparse.ArgumentParser, language="en"):
    """Render a Rich-styled help screen."""
    console.print(Panel(Align.center("SourceSage CLI"), style="info", expand=True))

    # Messages dictionary
    messages = {
        "en": {
            "usage_title": "Usage",
            "usage_text": "Generates Repository Summary by default.",
            "diff_text": " flag to enable (deprecated)",
            "core_options": "Core Options",
            "output_desc": "Output directory for generated files",
            "repo_desc": "Path to repository to analyze",
            "ignore_file_desc": "Path to ignore patterns file (default: .SourceSageignore, also uses .gitignore if present)",
            "language_map_desc": "Path to language map JSON",
            "language_desc": "Output language (default: en)",
            "release_options": "Release Report Options (deprecated)",
            "diff_desc": "Enable diff report generation (deprecated)",
            "repo_path_desc": "Root path of git repository",
            "git_fetch_tags_desc": "Command to fetch git tags",
            "git_tag_sort_desc": "Command to sort git tags",
            "git_diff_command_desc": "Git diff command",
            "report_title_desc": "Report title",
            "report_sections_desc": "Sections to include",
            "diff_output_desc": "Diff report output folder",
            "report_file_name_desc": "Report filename",
            "examples_title": "Examples",
        },
        "ja": {
            "usage_title": "使用方法",
            "usage_text": "デフォルトでRepository Summaryを生成します。",
            "diff_text": " フラグで有効化（非推奨）",
            "core_options": "基本オプション",
            "output_desc": "生成ファイルの出力ディレクトリ",
            "repo_desc": "解析対象のリポジトリパス",
            "ignore_file_desc": "無視パターンファイルのパス（デフォルト: .SourceSageignore、.gitignoreも使用）",
            "language_map_desc": "言語マップJSONのパス",
            "language_desc": "出力言語（デフォルト: en）",
            "release_options": "リリースレポートオプション（非推奨）",
            "diff_desc": "差分レポート生成を有効化（非推奨）",
            "repo_path_desc": "gitリポジトリのルートパス",
            "git_fetch_tags_desc": "gitタグ取得コマンド",
            "git_tag_sort_desc": "gitタグソートコマンド",
            "git_diff_command_desc": "git diff コマンド",
            "report_title_desc": "レポートタイトル",
            "report_sections_desc": "含めるセクション",
            "diff_output_desc": "差分レポート出力先フォルダ",
            "report_file_name_desc": "レポートファイル名",
            "examples_title": "例",
        },
    }

    msg = messages.get(language, messages["en"])

    # Usage
    usage = Text()
    usage.append(f"{msg['usage_title']}:\n", style="bold")
    usage.append("  sage [options]\n")
    usage.append("  sourcesage [options]\n\n")
    usage.append(f"{msg['usage_text']}\n", style="dim")
    usage.append("--diff", style="yellow")
    usage.append(f"{msg['diff_text']}\n", style="dim")
    console.print(Panel(usage, title=msg["usage_title"], border_style="cyan", expand=True))

    # Core options
    core_tbl = Table(title=msg["core_options"], show_header=True, header_style="bold cyan")
    core_tbl.add_column("Option")
    core_tbl.add_column("Default", style="dim")
    core_tbl.add_column("Description")

    def _get_default(dest, fallback=""):
        for a in parser._actions:
            if a.dest == dest:
                return a.default
        return fallback

    core_tbl.add_row(
        "-o, --output", str(_get_default("output")), msg["output_desc"]
    )
    core_tbl.add_row("--repo", str(_get_default("repo")), msg["repo_desc"])
    core_tbl.add_row(
        "--ignore-file", str(_get_default("ignore_file")), msg["ignore_file_desc"]
    )
    core_tbl.add_row(
        "-l, --lang", "en", msg["language_desc"]
    )
    core_tbl.add_row(
        "--language-map", str(_get_default("language_map")), msg["language_map_desc"]
    )
    console.print(core_tbl)

    # Release report options (deprecated)
    rel_tbl = Table(
        title=msg["release_options"], show_header=True, header_style="bold yellow"
    )
    rel_tbl.add_column("Option")
    rel_tbl.add_column("Default", style="dim")
    rel_tbl.add_column("Description")
    rel_tbl.add_row(
        "--diff", "False", msg["diff_desc"]
    )
    rel_tbl.add_row(
        "--repo-path", str(_get_default("repo_path")), msg["repo_path_desc"]
    )
    rel_tbl.add_row(
        "--git-fetch-tags", str(_get_default("git_fetch_tags")), msg["git_fetch_tags_desc"]
    )
    rel_tbl.add_row(
        "--git-tag-sort", str(_get_default("git_tag_sort")), msg["git_tag_sort_desc"]
    )
    rel_tbl.add_row(
        "--git-diff-command", str(_get_default("git_diff_command")), msg["git_diff_command_desc"]
    )
    rel_tbl.add_row(
        "--report-title", str(_get_default("report_title")), msg["report_title_desc"]
    )
    rel_tbl.add_row(
        "--report-sections", str(_get_default("report_sections")), msg["report_sections_desc"]
    )
    rel_tbl.add_row(
        "--diff-output",
        str(_get_default("diff_output")),
        msg["diff_output_desc"],
    )
    rel_tbl.add_row(
        "--report-file-name",
        str(_get_default("report_file_name")),
        msg["report_file_name_desc"],
    )
    console.print(rel_tbl)

    # Examples
    examples = Text()
    examples.append(f"{msg['examples_title']}:\n", style="bold")
    examples.append("  sage\n")
    examples.append("  sage --diff --report-title 'My Report'\n")
    examples.append("  sage -o ./output --repo ./myproject\n")
    console.print(Panel(examples, title=msg["examples_title"], border_style="yellow", expand=True))


def parse_arguments():
    """コマンドライン引数を解析する"""
    parser = argparse.ArgumentParser(description="SourceSage CLI", add_help=False)
    # Title only: keep ASCII art
    tprint(" SourceSage", font="rnd-xlarge")
    add_arguments(parser)
    args = parser.parse_args()
    if getattr(args, "help", False):
        render_rich_help(parser, args.language)
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
    # Messages dictionary
    messages = {
        "en": {
            "ignore_generated": "Generated .SourceSageignore file:",
            "ignore_not_found": "Default .SourceSageignore not found",
            "repository_summary": "Repository Summary",
            "generating": "Generating...",
            "generation_complete": "Repository Summary generation completed",
            "release_report": "Release Report",
            "deprecated_warning": "⚠️  Diff report generation is deprecated. This feature will be removed in the future due to improved LLM command execution capabilities.",
            "generating_diff": "Generating git diff report...",
            "latest_tag": "Latest tag:",
            "previous_tag": "Previous tag:",
            "output": "Output:",
            "skipping_no_tags": "No tags found, skipping Release Report",
            "process_complete": "Process completed successfully.",
        },
        "ja": {
            "ignore_generated": ".SourceSageignoreファイルを生成しました:",
            "ignore_not_found": "デフォルトの.SourceSageignoreが見つかりません",
            "repository_summary": "リポジトリサマリー",
            "generating": "生成中...",
            "generation_complete": "リポジトリサマリーの生成が完了しました",
            "release_report": "リリースレポート",
            "deprecated_warning": "⚠️  差分レポート生成機能は非推奨です。LLMのコマンド実行能力の向上により、この機能は将来削除される予定です。",
            "generating_diff": "git diff レポートを生成中...",
            "latest_tag": "最新タグ:",
            "previous_tag": "前のタグ:",
            "output": "出力:",
            "skipping_no_tags": "タグが見つからないため、Release Report をスキップしました",
            "process_complete": "プロセスが完了しました。",
        },
    }

    msg = messages.get(args.language, messages["en"])

    # -----------------------------------------------
    # .SourceSageignore ファイルの生成
    # デフォルトで .SourceSageignore と .gitignore を使う
    # Use the repo path if specified, otherwise use current directory
    base_dir = args.repo if args.repo else os.getcwd()
    sourcesageignore_path = os.path.join(base_dir, ".SourceSageignore")
    if not os.path.exists(sourcesageignore_path):
        # パッケージのデフォルト.SourceSageignoreをコピー
        package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        default_ignore_file = os.path.join(
            package_root, "sourcesage", "config", ".SourceSageignore"
        )
        if os.path.exists(default_ignore_file):
            import shutil
            shutil.copy(default_ignore_file, sourcesageignore_path)
            console.print(f"[success]{msg['ignore_generated']} {sourcesageignore_path}[/]")
        else:
            console.print(f"[warn]{msg['ignore_not_found']}[/]")
    args.ignore_file = sourcesageignore_path

    # -----------------------------------------------
    # 出力ディレクトリの設定
    # --repo が指定されている場合は、出力先もそこにする
    # デフォルト値（"./"）の場合、--repo の値を使う
    if args.repo and args.output == "./":
        # シェルのPWD環境変数を使って、現在のシェルのカレントディレクトリを取得
        shell_cwd = os.environ.get('PWD', os.getcwd())
        # args.repo が相対パスの場合、シェルのカレントディレクトリからの相対パスとして解釈
        if not os.path.isabs(args.repo):
            args.repo = os.path.abspath(os.path.join(shell_cwd, args.repo))
            args.output = args.repo
        else:
            args.output = args.repo

    # -----------------------------------------------
    # SourceSageの実行（常に実行）
    console.print(
        Panel(Align.center(msg["repository_summary"]), style="info", expand=True)
    )
    with console.status(f"[info]{msg['generating']}[/]", spinner="dots"):
        sourcesage = SourceSage(
            args.output, args.repo, args.ignore_file, args.language_map, args.language
        )
        sourcesage.run()
    console.print(f"[success]{msg['generation_complete']}[/]")

    # -----------------------------------------------
    # レポートの生成（オプション機能、非推奨）
    #
    if args.diff:
        console.print(Panel(Align.center(msg["release_report"]), style="info", expand=True))

        # 非推奨警告の表示
        console.print(
            f"[warn]{msg['deprecated_warning']}[/]"
        )

        with console.status(f"[info]{msg['generating_diff']}[/]", spinner="dots"):
            git_diff_generator = GitDiffGenerator(
                args.repo_path,
                args.git_fetch_tags,
                args.git_tag_sort,
                args.git_diff_command,
            )
            diff, latest_tag, previous_tag = git_diff_generator.get_git_diff()

        if diff != None:
            console.print(
                f"[info]{msg['latest_tag']} [bold]{latest_tag}[/], {msg['previous_tag']} [bold]{previous_tag}[/]"
            )
            report_file_name = args.report_file_name.format(latest_tag=latest_tag)
            os.makedirs(args.diff_output, exist_ok=True)
            output_path = os.path.join(args.diff_output, report_file_name)

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
                f"[info]{msg['generating']}[/]", spinner="dots"
            ):
                markdown_report_generator.generate_markdown_report()
            console.print(f"[success]{msg['output']} [/][red]{output_path}[/]")
        else:
            console.print(
                f"[warn]{msg['skipping_no_tags']}[/]"
            )

    console.print(
        Panel(Align.center(msg["process_complete"]), style="success", expand=True)
    )


def main():

    from dotenv import load_dotenv

    # Load version from pyproject.toml
    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pyproject_path = os.path.join(package_root, "pyproject.toml")
    version = "unknown"
    try:
        import tomli
        with open(pyproject_path, "rb") as f:
            pyproject = tomli.load(f)
            version = pyproject.get("project", {}).get("version", "unknown")
    except Exception:
        # Fallback to reading the file manually
        try:
            with open(pyproject_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("version ="):
                        version = line.split("=")[1].strip().strip('"').strip("'")
                        break
        except Exception:
            version = "7.1.1"  # Fallback version

    dotenv_path = os.path.join(os.getcwd(), ".env")
    logger.debug(f"dotenv_path : {dotenv_path}")
    load_dotenv(dotenv_path=dotenv_path, verbose=True, override=True)

    args = parse_arguments()
    log_arguments(args)

    # Show version and exit if -v or --version is specified
    if args.version:
        console.print(f"SourceSage v{version}", style="bold green")
        sys.exit(0)

    run(args)


if __name__ == "__main__":
    main()
