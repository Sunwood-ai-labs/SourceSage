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
from .modules.AgentMode import AgentOutput
from .modules.AgentMode.agent_output import AgentModeType, OutputFormat
from .modules.DocuSum.file_pattern_matcher import FilePatternMatcher
from .modules.DocuSum.language_detector import LanguageDetector
from .modules.DocuSum.file_processor import FileProcessor

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
    # Use .SourceSageignore by default
    sourcesageignore_file = os.path.join(os.getcwd(), ".SourceSageignore")
    parser.add_argument(
        "--ignore-file",
        help="Path to ignore file (default: .SourceSageignore)",
        default=sourcesageignore_file
    )
    parser.add_argument(
        "--use-ignore",
        action="store_true",
        help="Enable ignore flag (use/generate .SourceSageignore)",
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
    # Agent Mode Options (for AI agents like Claude Code)
    #
    parser.add_argument(
        "--agent-mode",
        type=str,
        choices=["tree", "files", "full"],
        default=None,
        help="Agent mode: tree (structure only), files (selective), full (with limits)",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["tree", "json"],
        default="tree",
        help="Output format for agent mode (default: tree)",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Maximum tree depth for agent mode",
    )
    parser.add_argument(
        "--show-lines",
        action="store_true",
        default=True,
        help="Show line counts in tree output (default: True)",
    )
    parser.add_argument(
        "--show-size",
        action="store_true",
        default=True,
        help="Show file sizes in tree output (default: True)",
    )
    parser.add_argument(
        "--sort-by",
        type=str,
        choices=["name", "lines", "size", "modified"],
        default="name",
        help="Sort criterion for tree output (default: name)",
    )
    parser.add_argument(
        "--large-threshold",
        type=int,
        default=200,
        help="Lines threshold for marking files as 'large' (default: 200)",
    )
    parser.add_argument(
        "--files",
        type=str,
        default=None,
        help="Comma-separated list of files to include (for --agent-mode files)",
    )
    parser.add_argument(
        "--pattern",
        type=str,
        default=None,
        help="Glob pattern to include files (for --agent-mode files)",
    )
    parser.add_argument(
        "--exclude-pattern",
        type=str,
        default=None,
        help="Glob pattern to exclude files (for --agent-mode files)",
    )
    parser.add_argument(
        "--min-lines",
        type=int,
        default=None,
        help="Minimum line count filter (for --agent-mode files)",
    )
    parser.add_argument(
        "--max-lines",
        type=int,
        default=None,
        help="Maximum line count filter (for --agent-mode files)",
    )
    parser.add_argument(
        "--max-total-lines",
        type=int,
        default=10000,
        help="Maximum total lines in output (for --agent-mode full, default: 10000)",
    )
    parser.add_argument(
        "--max-file-lines",
        type=int,
        default=1000,
        help="Maximum lines per file (for --agent-mode full, default: 1000)",
    )
    parser.add_argument(
        "--truncate-strategy",
        type=str,
        choices=["head", "tail", "middle"],
        default="middle",
        help="How to truncate long files (default: middle)",
    )
    parser.add_argument(
        "--priority-files",
        type=str,
        default=None,
        help="Comma-separated glob patterns for priority files",
    )
    parser.add_argument(
        "--exclude-large",
        action="store_true",
        help="Automatically exclude large files",
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
            "ignore_file_desc": "Path to ignore patterns file (default: .gitignore)",
            "use_ignore_desc": "Use/generate .SourceSageignore",
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
            "ignore_file_desc": "無視パターンファイルのパス（デフォルト: .gitignore）",
            "use_ignore_desc": ".SourceSageignoreを使用/生成する",
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
        "--use-ignore", "False", msg["use_ignore_desc"]
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

    # Agent Mode options
    agent_msg = {
        "en": {
            "agent_options": "Agent Mode Options (for AI agents)",
            "agent_mode_desc": "Agent mode: tree, files, or full",
            "format_desc": "Output format (tree or json)",
            "max_depth_desc": "Maximum tree depth",
            "large_threshold_desc": "Lines threshold for 'large' files",
            "files_desc": "Comma-separated file paths",
            "pattern_desc": "Glob pattern to include",
            "max_total_lines_desc": "Maximum total lines",
            "max_file_lines_desc": "Maximum lines per file",
            "truncate_strategy_desc": "How to truncate (head/tail/middle)",
        },
        "ja": {
            "agent_options": "エージェントモードオプション（AIエージェント向け）",
            "agent_mode_desc": "エージェントモード: tree, files, full",
            "format_desc": "出力形式（tree または json）",
            "max_depth_desc": "ツリーの最大深度",
            "large_threshold_desc": "'large'判定の行数閾値",
            "files_desc": "カンマ区切りのファイルパス",
            "pattern_desc": "含めるglobパターン",
            "max_total_lines_desc": "出力の最大総行数",
            "max_file_lines_desc": "ファイルごとの最大行数",
            "truncate_strategy_desc": "切り詰め方法（head/tail/middle）",
        },
    }
    agent_m = agent_msg.get(language, agent_msg["en"])

    agent_tbl = Table(
        title=agent_m["agent_options"], show_header=True, header_style="bold green"
    )
    agent_tbl.add_column("Option")
    agent_tbl.add_column("Default", style="dim")
    agent_tbl.add_column("Description")
    agent_tbl.add_row("--agent-mode", "None", agent_m["agent_mode_desc"])
    agent_tbl.add_row("--format", "tree", agent_m["format_desc"])
    agent_tbl.add_row("--max-depth", "None", agent_m["max_depth_desc"])
    agent_tbl.add_row("--large-threshold", "200", agent_m["large_threshold_desc"])
    agent_tbl.add_row("--files", "None", agent_m["files_desc"])
    agent_tbl.add_row("--pattern", "None", agent_m["pattern_desc"])
    agent_tbl.add_row("--max-total-lines", "10000", agent_m["max_total_lines_desc"])
    agent_tbl.add_row("--max-file-lines", "1000", agent_m["max_file_lines_desc"])
    agent_tbl.add_row("--truncate-strategy", "middle", agent_m["truncate_strategy_desc"])
    console.print(agent_tbl)

    # Examples
    examples = Text()
    examples.append(f"{msg['examples_title']}:\n", style="bold")
    examples.append("  sage\n")
    examples.append("  sage --use-ignore\n")
    examples.append("  sage --diff --report-title 'My Report'\n")
    examples.append("  sage -o ./output --repo ./myproject\n")
    examples.append("\n")
    examples.append("Agent Mode Examples:\n", style="bold green")
    examples.append("  sage --agent-mode tree --show-lines\n")
    examples.append("  sage --agent-mode tree --format json\n")
    examples.append("  sage --agent-mode files --files 'cli.py,core.py'\n")
    examples.append("  sage --agent-mode files --pattern '**/*.py'\n")
    examples.append("  sage --agent-mode full --max-total-lines 5000\n")
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


def run_agent_mode(args, console):
    """Run agent mode processing."""
    messages = {
        "en": {
            "agent_mode": "Agent Mode",
            "generating_tree": "Generating tree structure...",
            "generating_files": "Generating file contents...",
            "generating_full": "Generating full output with limits...",
            "complete": "Agent mode output complete",
        },
        "ja": {
            "agent_mode": "エージェントモード",
            "generating_tree": "ツリー構造を生成中...",
            "generating_files": "ファイル内容を生成中...",
            "generating_full": "制限付き完全出力を生成中...",
            "complete": "エージェントモード出力完了",
        },
    }
    msg = messages.get(args.language, messages["en"])

    console.print(Panel(Align.center(msg["agent_mode"]), style="info", expand=True))

    # Initialize components
    ignore_files = [args.ignore_file] if args.ignore_file and os.path.exists(args.ignore_file) else []
    pattern_matcher = FilePatternMatcher(ignore_files)
    language_detector = LanguageDetector(args.language_map)
    file_processor = FileProcessor(language_detector)

    agent_output = AgentOutput(pattern_matcher, language_detector, file_processor)

    # Determine output format
    output_format = OutputFormat.JSON if args.format == "json" else OutputFormat.TREE

    output = ""

    if args.agent_mode == "tree":
        with console.status(f"[info]{msg['generating_tree']}[/]", spinner="dots"):
            output = agent_output.generate_tree(
                dir_path=args.repo,
                output_format=output_format,
                max_depth=args.max_depth,
                show_lines=args.show_lines,
                show_size=args.show_size,
                sort_by=args.sort_by,
                large_threshold=args.large_threshold,
            )

    elif args.agent_mode == "files":
        with console.status(f"[info]{msg['generating_files']}[/]", spinner="dots"):
            file_paths = args.files.split(",") if args.files else None
            include_patterns = [args.pattern] if args.pattern else None
            exclude_patterns = [args.exclude_pattern] if args.exclude_pattern else None

            output = agent_output.generate_files(
                dir_path=args.repo,
                file_paths=file_paths,
                include_patterns=include_patterns,
                exclude_patterns=exclude_patterns,
                min_lines=args.min_lines,
                max_lines=args.max_lines,
                max_file_lines=args.max_file_lines,
                output_format=output_format,
            )

    elif args.agent_mode == "full":
        with console.status(f"[info]{msg['generating_full']}[/]", spinner="dots"):
            priority_files = args.priority_files.split(",") if args.priority_files else None

            output = agent_output.generate_full(
                dir_path=args.repo,
                max_total_lines=args.max_total_lines,
                max_file_lines=args.max_file_lines,
                truncate_strategy=args.truncate_strategy,
                priority_files=priority_files,
                exclude_large=args.exclude_large,
                large_threshold=args.large_threshold,
                output_format=output_format,
            )

    # Print output directly to stdout for agent consumption
    print(output)

    console.print(f"[success]{msg['complete']}[/]")


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

    # ==============================================
    # Agent Mode - Handle separately and exit early
    #
    if args.agent_mode:
        run_agent_mode(args, console)
        return

    # -----------------------------------------------
    # .SourceSageignore ファイルの生成
    if args.use_ignore:
        sourcesageignore_path = os.path.join(os.getcwd(), ".SourceSageignore")
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

    dotenv_path = os.path.join(os.getcwd(), ".env")
    logger.debug(f"dotenv_path : {dotenv_path}")
    load_dotenv(dotenv_path=dotenv_path, verbose=True, override=True)

    args = parse_arguments()
    log_arguments(args)
    run(args)


if __name__ == "__main__":
    main()
