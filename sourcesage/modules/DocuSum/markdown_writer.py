import os
from loguru import logger

class MarkdownWriter:
    """マークダウンドキュメントを生成するクラス"""

    def __init__(self, stats_collector, pattern_matcher):
        """
        MarkdownWriterの初期化

        Args:
            stats_collector: StatsCollectorのインスタンス
            pattern_matcher: FilePatternMatcherのインスタンス
        """
        self.stats_collector = stats_collector
        self.pattern_matcher = pattern_matcher

    def write_git_info(self, md_file, git_info):
        """Gitリポジトリ情報を書き込む"""
        if git_info:
            md_file.write("## 📂 Gitリポジトリ情報\n\n")
            md_file.write(f"- 🔗 リモートURL: {git_info.get('remote_url', 'Not available')}\n")
            md_file.write(f"- 🌿 デフォルトブランチ: {git_info.get('default_branch', 'Not available')}\n")
            md_file.write(f"- 📅 作成日時: {git_info.get('creation_date', 'Not available')}\n\n")

    def write_stats(self, md_file, stats):
        """統計情報を出力する"""
        md_file.write("## 📊 プロジェクト統計\n\n")
        md_file.write(f"- 📁 総ディレクトリ数: {stats['total_dirs']}\n")
        md_file.write(f"- 📄 総ファイル数: {stats['total_files']}\n")
        md_file.write(f"- 📏 最大深度: {stats['max_depth']}\n")
        if stats['largest_dir'][0]:
            largest_dir = os.path.basename(stats['largest_dir'][0])
            md_file.write(f"- 📦 最大ディレクトリ: {largest_dir} ({stats['largest_dir'][1]} エントリ)\n")
        md_file.write("\n")

    def write_file_stats_table(self, md_file, file_stats):
        """ファイルサイズと行数の表を出力する"""
        md_file.write("### 📊 ファイルサイズと行数\n\n")
        md_file.write("| ファイル | サイズ | 行数 | 言語 |\n")
        md_file.write("|----------|--------|------|------|\n")
        
        for stat in file_stats:
            size_str = self.stats_collector.format_size(stat['size'])
            line_count = stat['lines'] if stat['lines'] is not None else 'N/A'
            md_file.write(f"| {stat['path']} | {size_str} | {line_count} | {stat['language']} |\n")
        md_file.write("\n")

    def write_language_stats(self, md_file, language_stats):
        """言語別の統計情報を出力する"""
        md_file.write("### 📈 言語別統計\n\n")
        md_file.write("| 言語 | ファイル数 | 総行数 | 合計サイズ |\n")
        md_file.write("|------|------------|--------|------------|\n")
        
        # 総行数でソート
        sorted_stats = sorted(
            language_stats.items(),
            key=lambda x: x[1]['total_lines'],
            reverse=True
        )
        
        for lang, stats in sorted_stats:
            size_str = self.stats_collector.format_size(stats['total_size'])
            md_file.write(
                f"| {lang} | {stats['files']} | {stats['total_lines']} | {size_str} |\n"
            )
        md_file.write("\n")

    def write_file_contents(self, md_file, file_processor, folder):
        """ファイル内容を出力する"""
        try:
            for root, _, files in os.walk(folder):
                for file in sorted(files):  # ファイル名でソート
                    file_path = os.path.join(root, file)
                    if not self.pattern_matcher.should_exclude(file_path):
                        try:
                            content = file_processor.process_file(file_path, folder)
                            if content:
                                md_file.write(content)
                        except Exception as e:
                            logger.warning(f"ファイル処理エラー {file_path}: {e}")
        except Exception as e:
            logger.error(f"ファイル内容の出力エラー: {e}")
            raise
