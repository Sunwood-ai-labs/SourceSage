import os
from pathlib import Path
from loguru import logger
from art import *
import requests

try:
    from .file_pattern_matcher import FilePatternMatcher
    from .language_detector import LanguageDetector
    from .tree_generator import TreeGenerator
    from .file_processor import FileProcessor
    from .git_info_collector import GitInfoCollector
    from .stats_collector import StatsCollector
    from .markdown_writer import MarkdownWriter
except ImportError:
    from file_pattern_matcher import FilePatternMatcher
    from language_detector import LanguageDetector
    from tree_generator import TreeGenerator
    from file_processor import FileProcessor
    from git_info_collector import GitInfoCollector
    from stats_collector import StatsCollector
    from markdown_writer import MarkdownWriter

class DocuSum:
    """
    リポジトリの構造とファイル内容をマークダウンドキュメントに変換するクラス。
    gitignoreスタイルのパターンマッチングをサポートし、柔軟な除外設定が可能。
    """

    def __init__(self, folders=None, ignore_file='.SourceSageignore', language_map_file='language_map.json', output_file='repository_summary.md', git_path=None):
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
        self.git_path = git_path if git_path else os.path.join(self.folders[0], '.git')

        # .SourceSageIgnoreファイルの初期化
        self._init_ignore_file()
        
        # language_map_fileが指定されていない場合、モジュールのディレクトリ内のファイルを使用
        if not os.path.exists(language_map_file):
            module_dir = os.path.dirname(os.path.abspath(__file__))
            language_map_file = os.path.join(module_dir, 'language_map.json')
        
        # 各種ユーティリティクラスの初期化
        self.pattern_matcher = FilePatternMatcher(ignore_file)
        self.language_detector = LanguageDetector(language_map_file)
        self.tree_generator = TreeGenerator(self.pattern_matcher)
        self.file_processor = FileProcessor(self.language_detector)
        self.git_info_collector = GitInfoCollector(self.git_path)
        self.stats_collector = StatsCollector(
            self.pattern_matcher,
            self.language_detector,
            self.file_processor
        )
        self.markdown_writer = MarkdownWriter(
            self.stats_collector,
            self.pattern_matcher
        )

    def generate_markdown(self):
        
        tprint("DocuSum")
        
        """マークダウンドキュメントを生成する"""
        output_dir = os.path.dirname(self.output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        try:
            with open(self.output_file, 'w', encoding='utf-8') as md_file:
                for folder in self.folders:
                    project_name = os.path.basename(os.path.abspath(folder))
                    md_file.write(f"# Project: {project_name}\n\n")
                    logger.info(f"プロジェクト: {project_name}") # 進捗表示
                                        
                    # ディレクトリツリーの生成と統計情報の取得
                    logger.info("ディレクトリツリー生成...") # 進捗表示
                    tree = self.tree_generator.generate_tree(folder)
                    stats = self.tree_generator.get_tree_stats(folder)
                    
                    # ツリー構造の出力
                    md_file.write(f"{tree}\n")
                    
                    # Gitリポジトリ情報の出力
                    logger.info("Git情報収集...") # 進捗表示
                    git_info = self.git_info_collector.collect_info()
                    self.markdown_writer.write_git_info(md_file, git_info)
                    
                    # 統計情報の出力
                    logger.info("統計情報生成...") # 進捗表示
                    self.markdown_writer.write_stats(md_file, stats)
                    
                    # ファイルサイズと行数の統計
                    logger.info("ファイル統計収集...") # 進捗表示
                    file_stats = self.stats_collector.collect_file_stats(folder)
                    self.markdown_writer.write_file_stats_table(md_file, file_stats)
                    
                    # 言語別統計
                    logger.info("言語統計生成...") # 進捗表示
                    language_stats = self.stats_collector.collect_language_stats(file_stats)
                    self.markdown_writer.write_language_stats(md_file, language_stats)
                    
                    # ファイル内容の処理
                    logger.info("ファイル内容処理...") # 進捗表示
                    self.markdown_writer.write_file_contents(md_file, self.file_processor, folder)
            
            logger.success(f"マークダウンドキュメントが生成されました: {self.output_file}")
            return self.output_file
        
        except Exception as e:
            logger.error(f"マークダウン生成エラー: {e}")
            raise

    def _init_ignore_file(self):
        """
        .SourceSageIgnoreファイルの初期化を行う。
        ファイルが存在しない場合、GitHubからデフォルトの設定をダウンロードして作成する。
        """
        if not os.path.exists(self.ignore_file):
            try:
                url = "https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/refs/heads/develop/sourcesage/modules/DocuSum/.SourceSageignore"
                response = requests.get(url)
                response.raise_for_status()  # エラーチェック
                
                with open(self.ignore_file, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                    
                logger.success(f"{self.ignore_file}を作成しました")
            except Exception as e:
                logger.error(f"{self.ignore_file}の作成に失敗しました: {e}")
                raise

    def analyze_repository(self):
        """リポジトリの分析結果を生成する"""
        analysis_results = []
        
        for folder in self.folders:
            stats = self.tree_generator.get_tree_stats(folder)
            analysis_results.append({
                'folder': folder,
                'stats': stats
            })
        
        return analysis_results

if __name__ == '__main__':
    import argparse
    import sys
        
    # コマンドライン引数のパース
    parser = argparse.ArgumentParser(description='リポジトリの構造とファイル内容をマークダウンドキュメントに変換します。')
    parser.add_argument('folders', nargs='*', default=['.'], help='処理対象のフォルダパス（指定しない場合は現在のディレクトリ）')
    parser.add_argument('--ignore-file', default='.SourceSageignore', help='除外パターンを記述したファイルのパス')
    parser.add_argument('--language-map', default='language_map.json', help='言語マッピング定義ファイルのパス')
    parser.add_argument('--output', default='repository_summary.md', help='出力マークダウンファイルのパス')
    parser.add_argument('--git-path', help='.gitディレクトリのパス（デフォルトはfolders[0]/.git）')
    
    args = parser.parse_args()
    
    try:
        # DocuSumの初期化と実行
        docusum = DocuSum(
            folders=args.folders,
            ignore_file=args.ignore_file,
            language_map_file=args.language_map,
            output_file=args.output,
            git_path=args.git_path
        )
        output_file = docusum.generate_markdown()

    except Exception as e:
        logger.error(f"エラーが発生しました: {e}")
        sys.exit(1)
