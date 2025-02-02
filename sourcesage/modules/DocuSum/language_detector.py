import os
import json
from loguru import logger

class LanguageDetector:
    """ファイルの言語を検出するクラス"""
    
    def __init__(self, language_map_file):
        self.language_map = self._load_language_map(language_map_file)

    def _load_language_map(self, language_map_file):
        """言語マッピング定義をロードする"""
        if os.path.exists(language_map_file):
            try:
                with open(language_map_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError as e:
                logger.error(f"言語マッピングファイルの解析エラー: {e}")
            except Exception as e:
                logger.error(f"言語マッピングファイルの読み込みエラー: {e}")
        return self._get_default_language_map()

    def _get_default_language_map(self):
        """デフォルトの言語マッピングを返す"""
        return {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.html': 'html',
            '.css': 'css',
            '.md': 'markdown',
            '.json': 'json',
            '.yml': 'yaml',
            '.yaml': 'yaml',
            '.sh': 'bash',
            '.bash': 'bash',
            '.sql': 'sql',
            '.xml': 'xml',
            '.java': 'java',
            '.cpp': 'cpp',
            '.c': 'c',
            '.h': 'c',
            '.hpp': 'cpp',
            '.cs': 'csharp',
            '.go': 'go',
            '.rs': 'rust',
            '.rb': 'ruby',
            '.php': 'php',
            '.scala': 'scala',
            '.kt': 'kotlin',
            '.swift': 'swift',
            '.r': 'r',
            '.dockerfile': 'dockerfile',
            '.tex': 'tex'
        }

    def detect_language(self, file_path):
        """ファイルの言語を検出する"""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        
        # 特殊なファイル名の処理
        if os.path.basename(file_path).lower() == 'dockerfile':
            return 'dockerfile'
        
        return self.language_map.get(ext, 'plaintext')
