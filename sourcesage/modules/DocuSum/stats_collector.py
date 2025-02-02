import os
from loguru import logger

class StatsCollector:
    """プロジェクトの統計情報を収集するクラス"""

    def __init__(self, pattern_matcher, language_detector, file_processor):
        """
        StatsCollectorの初期化

        Args:
            pattern_matcher: FilePatternMatcherのインスタンス
            language_detector: LanguageDetectorのインスタンス
            file_processor: FileProcessorのインスタンス
        """
        self.pattern_matcher = pattern_matcher
        self.language_detector = language_detector
        self.file_processor = file_processor

    def collect_file_stats(self, folder):
        """ファイルの統計情報を収集する"""
        file_stats = []
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                if not self.pattern_matcher.should_exclude(file_path):
                    relative_path = os.path.relpath(file_path, folder)
                    try:
                        size = os.path.getsize(file_path)
                        line_count = self.file_processor._count_lines(file_path)
                        language = self.language_detector.detect_language(file_path)
                        file_stats.append({
                            'path': relative_path,
                            'size': size,
                            'lines': line_count if line_count is not None else 0,
                            'language': language
                        })
                    except Exception as e:
                        logger.warning(f"ファイル統計収集エラー {relative_path}: {e}")
        return sorted(file_stats, key=lambda x: x['size'], reverse=True)

    def collect_language_stats(self, file_stats):
        """言語別の統計情報を収集する"""
        language_stats = {}
        for stat in file_stats:
            lang = stat['language']
            if lang not in language_stats:
                language_stats[lang] = {
                    'files': 0,
                    'total_lines': 0,
                    'total_size': 0
                }
            language_stats[lang]['files'] += 1
            language_stats[lang]['total_lines'] += stat['lines']
            language_stats[lang]['total_size'] += stat['size']
        return language_stats

    @staticmethod
    def format_size(size):
        """ファイルサイズを適切な単位に変換する"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"
