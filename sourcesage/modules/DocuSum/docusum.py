import os
from pathlib import Path

from loguru import logger
from rich.console import Console

try:
    from .file_pattern_matcher import FilePatternMatcher
    from .file_processor import FileProcessor
    from .git_info_collector import GitInfoCollector
    from .language_detector import LanguageDetector
    from .markdown_writer import MarkdownWriter
    from .stats_collector import StatsCollector
    from .tree_generator import TreeGenerator
except ImportError:
    from file_pattern_matcher import FilePatternMatcher
    from file_processor import FileProcessor
    from git_info_collector import GitInfoCollector
    from language_detector import LanguageDetector
    from markdown_writer import MarkdownWriter
    from stats_collector import StatsCollector
    from tree_generator import TreeGenerator


class DocuSum:
    """
    リポジトリの構造とファイル内容をマークダウンドキュメントに変換するクラス。
    gitignoreスタイルのパターンマッチングをサポートし、柔軟な除外設定が可能。
    """

    def __init__(
        self,
        folders=None,
        ignore_file=".SourceSageignore",
        language_map_file="language_map.json",
        output_file="repository_summary.md",
        git_path=None,
    ):
        """
        DocuSumの初期化。

        Args:
            folders (list): 処理対象のフォルダパスのリスト
            ignore_file (str): 除外パターンを記述したファイルのパス
            language_map_file (str): 言語マッピング定義ファイルのパス
            output_file (str): 出力マークダウンファイルのパス
            git_path (str): .gitディレクトリのパス（デフォルトはfolders[0]/.git）
        """
        self.folders = folders if folders is not None else [os.getcwd()]
        self.ignore_file = ignore_file
        self.output_file = output_file
        self.git_path = git_path if git_path else os.path.join(self.folders[0], ".git")

        # .SourceSageIgnoreファイルの初期化
        self._init_ignore_file()

        # language_map_file が存在しない場合、パッケージ同梱の設定を使用
        if not os.path.exists(language_map_file):
            # this file: sourcesage/modules/DocuSum/docusum.py
            # package config: sourcesage/config/language_map.json
            pkg_sourcesage_dir = os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            )
            language_map_file = os.path.join(
                pkg_sourcesage_dir, "config", "language_map.json"
            )

        # 各種ユーティリティクラスの初期化
        self.pattern_matcher = FilePatternMatcher(ignore_file)
        self.language_detector = LanguageDetector(language_map_file)
        self.tree_generator = TreeGenerator(self.pattern_matcher)
        self.file_processor = FileProcessor(self.language_detector)
        self.git_info_collector = GitInfoCollector(self.git_path)
        self.stats_collector = StatsCollector(
            self.pattern_matcher, self.language_detector, self.file_processor
        )
        self.markdown_writer = MarkdownWriter(
            self.stats_collector, self.pattern_matcher
        )

    def generate_markdown(self):
        """マークダウンドキュメントを生成する"""
        output_dir = os.path.dirname(self.output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        console = Console()

        try:
            with open(self.output_file, "w", encoding="utf-8") as md_file:
                for folder in self.folders:
                    project_name = os.path.basename(os.path.abspath(folder))
                    md_file.write(f"# Project: {project_name}\n\n")
                    console.log(f"[bold]プロジェクト:[/] {project_name}")

                    with console.status(
                        "[cyan]ディレクトリツリー生成...[/]", spinner="dots"
                    ) as status:
                        tree = self.tree_generator.generate_tree(folder)
                        stats = self.tree_generator.get_tree_stats(folder)
                        md_file.write(f"{tree}\n")

                    with console.status("[cyan]Git情報収集...[/]", spinner="dots"):
                        git_info = self.git_info_collector.collect_info()
                        self.markdown_writer.write_git_info(md_file, git_info)

                    with console.status("[cyan]統計情報生成...[/]", spinner="dots"):
                        self.markdown_writer.write_stats(md_file, stats)

                    with console.status("[cyan]ファイル統計収集...[/]", spinner="dots"):
                        file_stats = self.stats_collector.collect_file_stats(folder)
                        self.markdown_writer.write_file_stats_table(md_file, file_stats)

                    with console.status("[cyan]言語統計生成...[/]", spinner="dots"):
                        language_stats = self.stats_collector.collect_language_stats(
                            file_stats
                        )
                        self.markdown_writer.write_language_stats(
                            md_file, language_stats
                        )

                    with console.status("[cyan]ファイル内容処理...[/]", spinner="dots"):
                        self.markdown_writer.write_file_contents(
                            md_file, self.file_processor, folder
                        )

            console.log(
                f"[green]マークダウンドキュメントが生成されました:[/] [red]{self.output_file}[/]"
            )
            return self.output_file

        except Exception as e:
            logger.error(f"マークダウン生成エラー: {e}")
            raise

    def _init_ignore_file(self):
        """
        .SourceSageignore の初期化。
        指定パスに存在しない場合は、パッケージ同梱のデフォルトをコピーする。
        """
        if os.path.exists(self.ignore_file):
            return

        try:
            # locate packaged default at: sourcesage/config/.SourceSageignore
            pkg_sourcesage_dir = os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            )
            packaged_ignore = os.path.join(
                pkg_sourcesage_dir, "config", ".SourceSageignore"
            )

            if os.path.exists(packaged_ignore):
                with open(packaged_ignore, "r", encoding="utf-8") as src, open(
                    self.ignore_file, "w", encoding="utf-8"
                ) as dst:
                    dst.write(src.read())
                logger.success(f"{self.ignore_file} をデフォルトから作成しました")
            else:
                # Fallback minimal template
                content = """__pycache__/\n*.pyc\n.git/\n.SourceSageAssets/\n"""
                with open(self.ignore_file, "w", encoding="utf-8") as dst:
                    dst.write(content)
                logger.warning(
                    f"パッケージ内にデフォルトが見つかりませんでした。最小テンプレートで {self.ignore_file} を作成しました"
                )
        except Exception as e:
            logger.error(f"{self.ignore_file} の作成に失敗しました: {e}")
            raise

    def analyze_repository(self):
        """リポジトリの分析結果を生成する"""
        analysis_results = []

        for folder in self.folders:
            stats = self.tree_generator.get_tree_stats(folder)
            analysis_results.append({"folder": folder, "stats": stats})

        return analysis_results


if __name__ == "__main__":
    import argparse
    import sys

    # コマンドライン引数のパース
    parser = argparse.ArgumentParser(
        description="リポジトリの構造とファイル内容をマークダウンドキュメントに変換します。"
    )
    parser.add_argument(
        "folders",
        nargs="*",
        default=["."],
        help="処理対象のフォルダパス（指定しない場合は現在のディレクトリ）",
    )
    parser.add_argument(
        "--ignore-file",
        default=".SourceSageignore",
        help="除外パターンを記述したファイルのパス",
    )
    parser.add_argument(
        "--language-map",
        default="language_map.json",
        help="言語マッピング定義ファイルのパス",
    )
    parser.add_argument(
        "--output",
        default="repository_summary.md",
        help="出力マークダウンファイルのパス",
    )
    parser.add_argument(
        "--git-path", help=".gitディレクトリのパス（デフォルトはfolders[0]/.git）"
    )

    args = parser.parse_args()

    try:
        # DocuSumの初期化と実行
        docusum = DocuSum(
            folders=args.folders,
            ignore_file=args.ignore_file,
            language_map_file=args.language_map,
            output_file=args.output,
            git_path=args.git_path,
        )
        output_file = docusum.generate_markdown()

    except Exception as e:
        logger.error(f"エラーが発生しました: {e}")
        sys.exit(1)
