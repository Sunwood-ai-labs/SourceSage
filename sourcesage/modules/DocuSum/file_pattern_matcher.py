import os
from pathlib import Path
import fnmatch
from loguru import logger

class FilePatternMatcher:
    """ファイルパターンマッチングを処理するクラス"""
    
    def __init__(self, ignore_file):
        self.ignore_file = ignore_file
        # デフォルトの除外パターン
        self.default_patterns = [
            '.git',
            'node_modules',
            '__pycache__',
            '*.pyc',
            '.DS_Store',
            '.SourceSageAssets',
            'package-lock.json',
            '*.log'
        ]
        self.patterns = self._load_patterns()

    def _load_patterns(self):
        """gitignoreスタイルのパターンをロードする"""
        include_patterns = []
        exclude_patterns = self.default_patterns.copy()
        
        if os.path.exists(self.ignore_file):
            with open(self.ignore_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if line.startswith('!'):
                            include_patterns.append(line[1:])
                        else:
                            exclude_patterns.append(line)
        
        return {'include': include_patterns, 'exclude': exclude_patterns}

    def should_exclude(self, path):
        """パスが除外パターンにマッチするかチェックする"""
        path = str(Path(path)).replace('\\', '/')
        
        # ディレクトリの場合、そのディレクトリ全体を除外するかチェック
        if os.path.isdir(path):
            dir_path = path if path.endswith('/') else f"{path}/"
            for pattern in self.patterns['exclude']:
                # パターンが.git/のような形式の場合、配下全て除外
                if pattern.endswith('/'):
                    if self._match_directory_pattern(dir_path, pattern):
                        return True
        
        # 通常のパターンマッチング
        excluded = any(self._match_pattern(path, pattern)
                      for pattern in self.patterns['exclude'])
        if not excluded:
            return False
        
        if self.patterns['include']:
            return not any(self._match_pattern(path, pattern)
                         for pattern in self.patterns['include'])
        
        return excluded

    def _match_pattern(self, path, pattern):
        """パターンとパスのマッチングを行う"""
        # ディレクトリパターンの処理
        if pattern.endswith('/'):
            return self._match_directory_pattern(path, pattern)
        
        # 再帰的パターンの処理
        if '**' in pattern:
            return self._match_recursive_pattern(path, pattern)
        
        # 通常のパターンマッチング
        return self._match_glob_pattern(path, pattern)

    def _match_directory_pattern(self, path, pattern):
        """ディレクトリパターンのマッチングを行う"""
        if not pattern.endswith('/'):
            pattern = f"{pattern}/"
        
        path = path if path.endswith('/') else f"{path}/"
        normalized_pattern = pattern.rstrip('/')
        
        # 完全一致
        if fnmatch.fnmatch(path.rstrip('/'), normalized_pattern):
            return True
        
        # パスの一部として含まれる場合
        path_parts = path.split('/')
        pattern_parts = normalized_pattern.split('/')
        
        for i in range(len(path_parts) - len(pattern_parts) + 1):
            if all(fnmatch.fnmatch(path_parts[i + j], pattern_parts[j])
                   for j in range(len(pattern_parts))):
                return True
        
        return False

    def _match_recursive_pattern(self, path, pattern):
        """再帰的パターンのマッチングを行う"""
        pattern_parts = pattern.split('**')
        if len(pattern_parts) == 2:
            start, end = pattern_parts
            path_normalized = path.replace('\\', '/')
            
            # startパターンのマッチング
            if start:
                if not path_normalized.startswith(start.rstrip('/')):
                    return False
                path_normalized = path_normalized[len(start.rstrip('/')):]
            
            # endパターンのマッチング
            if end:
                return path_normalized.endswith(end.lstrip('/'))
            
            return True
        
        return False

    def _match_glob_pattern(self, path, pattern):
        """基本的なグロブパターンマッチングを行う"""
        normalized_path = str(Path(path)).replace('\\', '/')
        basename = os.path.basename(normalized_path)
        
        # パスとベースネームの両方でマッチをチェック
        return fnmatch.fnmatch(normalized_path, pattern) or \
               fnmatch.fnmatch(basename, pattern) or \
               (pattern in normalized_path.split('/'))  # パスの一部としてマッチ
