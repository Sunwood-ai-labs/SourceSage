import os
import datetime
import configparser
from loguru import logger

class GitInfoCollector:
    """Gitリポジトリの情報を収集するクラス"""

    def __init__(self, git_path):
        """
        GitInfoCollectorの初期化

        Args:
            git_path (str): .gitディレクトリのパス
        """
        self.git_path = git_path

    def collect_info(self):
        """Gitリポジトリの情報を収集する"""
        git_info = {}
        
        try:
            if os.path.exists(self.git_path):
                # configファイルの読み込み
                config_path = os.path.join(self.git_path, 'config')
                if os.path.exists(config_path):
                    config = configparser.ConfigParser()
                    config.read(config_path)
                    
                    # リモートURLの取得
                    if config.has_section('remote "origin"'):
                        git_info['remote_url'] = config.get('remote "origin"', 'url')
                    else:
                        git_info['remote_url'] = 'Not configured'
                    
                    # ブランチ情報の取得
                    if config.has_section('branch "main"'):
                        git_info['default_branch'] = config.get('branch "main"', 'remote')
                    elif config.has_section('branch "master"'):
                        git_info['default_branch'] = config.get('branch "master"', 'remote')
                    else:
                        git_info['default_branch'] = 'Not configured'
                
                # リポジトリ作成日時の取得（HEADが作成された日時）
                head_path = os.path.join(self.git_path, 'HEAD')
                if os.path.exists(head_path):
                    creation_time = datetime.datetime.fromtimestamp(os.path.getctime(head_path))
                    git_info['creation_date'] = creation_time.strftime('%Y-%m-%d %H:%M:%S')
                
                return git_info

        except Exception as e:
            logger.error(f"Gitリポジトリ情報の取得エラー: {e}")
        
        return None
