import os
from loguru import logger

class TreeGenerator:
    """ディレクトリツリーを生成するクラス"""
    
    def __init__(self, pattern_matcher):
        self.pattern_matcher = pattern_matcher

    def generate_tree(self, dir_path, max_depth=None):
        """ディレクトリツリーを生成する"""
        tree = ["```plaintext"]
        tree.append(f"OS: {os.name}")
        tree.append(f"Directory: {os.path.abspath(dir_path)}\n")
        
        def _build_tree(path, prefix="", depth=0):
            if max_depth is not None and depth > max_depth:
                return
            
            try:
                # ディレクトリエントリをソート（ディレクトリ優先）
                entries = sorted(os.scandir(path), 
                               key=lambda e: (not e.is_dir(), e.name.lower()))
                
                for i, entry in enumerate(entries):
                    if self.pattern_matcher.should_exclude(entry.path):
                        continue
                    
                    is_last = (i == len(entries) - 1)
                    current_prefix = "└── " if is_last else "├── "
                    
                    # エントリ名の装飾（ディレクトリの場合は/を付加）
                    entry_name = f"{entry.name}{'/' if entry.is_dir() else ''}"
                    tree.append(f"{prefix}{current_prefix}{entry_name}")
                    
                    if entry.is_dir():
                        next_prefix = prefix + ("    " if is_last else "│   ")
                        _build_tree(entry.path, next_prefix, depth + 1)
            
            except PermissionError as e:
                logger.warning(f"アクセス権限エラー {path}: {e}")
            except Exception as e:
                logger.error(f"ディレクトリ処理エラー {path}: {e}")
        
        try:
            _build_tree(dir_path)
        except Exception as e:
            logger.error(f"ツリー生成エラー {dir_path}: {e}")
            tree.append(f"Error: {str(e)}")
        
        tree.append("```\n")
        return "\n".join(tree)

    def get_tree_stats(self, dir_path):
        """ツリーの統計情報を取得する"""
        stats = {
            'total_dirs': 0,
            'total_files': 0,
            'max_depth': 0,
            'largest_dir': ('', 0)
        }

        def _count_entries(path, depth=0):
            try:
                dir_count = 0
                file_count = 0
                
                with os.scandir(path) as entries:
                    for entry in entries:
                        if self.pattern_matcher.should_exclude(entry.path):
                            continue
                            
                        if entry.is_dir():
                            dir_count += 1
                            sub_dir_count, sub_file_count = _count_entries(entry.path, depth + 1)
                            dir_count += sub_dir_count
                            file_count += sub_file_count
                        else:
                            file_count += 1
                
                stats['max_depth'] = max(stats['max_depth'], depth)
                if dir_count + file_count > stats['largest_dir'][1]:
                    stats['largest_dir'] = (path, dir_count + file_count)
                
                return dir_count, file_count
                
            except Exception as e:
                logger.error(f"統計情報収集エラー {path}: {e}")
                return 0, 0

        total_dirs, total_files = _count_entries(dir_path)
        stats['total_dirs'] = total_dirs
        stats['total_files'] = total_files
        
        return stats
