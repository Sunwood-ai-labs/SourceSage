import os
from loguru import logger

class FileProcessor:
    """ファイル処理を行うクラス"""
    
    def __init__(self, language_detector):
        self.language_detector = language_detector
        self.binary_extensions = {'.pyc', '.pyo', '.pyd', '.so', '.dll', '.exe', 
                                '.jpg', '.jpeg', '.png', '.gif', '.ico', '.pdf'}

    def process_file(self, file_path, base_path):
        """ファイルの内容をマークダウン形式に変換する"""
        try:
            relative_path = os.path.relpath(file_path, base_path)
            
            # バイナリファイルのチェック
            if self._is_binary_file(file_path):
                logger.debug(f"バイナリファイルをスキップ: {relative_path}")
                return f"`{relative_path}` - Binary file\n\n"
            
            # 言語検出とファイル読み込み
            language = self.language_detector.detect_language(file_path)
            content = self._read_file_content(file_path)
            
            if content is None:
                return f"`{relative_path}` - Error: Failed to read file\n\n"
            
            # ファイル情報の追加
            file_info = self._get_file_info(file_path)
            
            # マークダウン形式で出力
            return (
                f"`{relative_path}`\n\n"
                f"{file_info}\n"
                f"```{language}\n"
                f"{content}\n"
                f"```\n\n"
            )
        
        except Exception as e:
            logger.error(f"ファイル処理エラー {relative_path}: {e}")
            return f"`{relative_path}` - Error: {e}\n\n"

    def _is_binary_file(self, file_path):
        """ファイルがバイナリかどうかを判定する"""
        # 拡張子によるチェック
        ext = os.path.splitext(file_path)[1].lower()
        if ext in self.binary_extensions:
            return True
            
        # ファイルの内容によるチェック
        try:
            with open(file_path, 'rb') as f:
                chunk = f.read(1024)
                return b'\x00' in chunk  # NULL文字が含まれていればバイナリと判定
        except Exception:
            return True

    def _read_file_content(self, file_path, max_size=1024*1024):
        """ファイルの内容を読み込む"""
        try:
            # ファイルサイズチェック
            if os.path.getsize(file_path) > max_size:
                logger.warning(f"ファイルサイズ超過: {file_path}")
                return "File too large to display"
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                
                # 空ファイルの場合
                if not content:
                    return "(Empty file)"
                    
                return content
                
        except UnicodeDecodeError:
            logger.warning(f"エンコーディングエラー: {file_path}")
            return None
        except Exception as e:
            logger.error(f"ファイル読み込みエラー {file_path}: {e}")
            return None

    def _get_file_info(self, file_path):
        """ファイルの追加情報を取得する"""
        try:
            stats = os.stat(file_path)
            size = self._format_size(stats.st_size)
            lines = self._count_lines(file_path)
            
            info = [
                f"**サイズ**: {size}",
                f"**行数**: {lines if lines is not None else 'N/A'} 行"
            ]
            
            return " | ".join(info)
            
        except Exception as e:
            logger.error(f"ファイル情報取得エラー {file_path}: {e}")
            return ""

    def _format_size(self, size):
        """ファイルサイズを適切な単位に変換する"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"

    def _count_lines(self, file_path):
        """ファイルの行数をカウントする"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return sum(1 for _ in f)
        except Exception:
            return None
