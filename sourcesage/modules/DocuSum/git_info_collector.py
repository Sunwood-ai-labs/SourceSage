import os
import datetime
import configparser
import subprocess
from pathlib import Path
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
        self.repo_root = str(Path(git_path).parent)

    def _run_git_command(self, command):
        """
        Gitコマンドを実行する

        Args:
            command (list): 実行するGitコマンドとその引数のリスト
        """
        try:
            result = subprocess.run(
                ['git'] + command,
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            return None
        except Exception as e:
            logger.error(f"Gitコマンド実行エラー {' '.join(command)}: {e}")
            return None

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
                    
                    # リモートURL情報の取得
                    if config.has_section('remote "origin"'):
                        git_info['remote_url'] = config.get('remote "origin"', 'url')
                    else:
                        git_info['remote_url'] = 'Not configured'
                
                # 現在のブランチを取得
                current_branch = self._run_git_command(['rev-parse', '--abbrev-ref', 'HEAD'])
                git_info['current_branch'] = current_branch if current_branch else 'Unknown'
                
                # デフォルトブランチの取得
                if config.has_section('branch "main"'):
                    git_info['default_branch'] = 'main'
                elif config.has_section('branch "master"'):
                    git_info['default_branch'] = 'master'
                else:
                    git_info['default_branch'] = 'Not configured'
                
                # コミット情報の取得
                last_commit = self._run_git_command(['log', '-1', '--format=%H|%an|%ae|%at|%s'])
                if last_commit:
                    commit_hash, author, email, timestamp, message = last_commit.split('|')
                    commit_date = datetime.datetime.fromtimestamp(int(timestamp))
                    git_info['last_commit'] = {
                        'hash': commit_hash[:8],
                        'author': author,
                        'email': email,
                        'date': commit_date.strftime('%Y-%m-%d %H:%M:%S'),
                        'message': message
                    }
                
                # タグ情報の取得
                tags = self._run_git_command(['tag', '-l', '--sort=-creatordate'])
                if tags:
                    git_info['tags'] = tags.split('\n')[:5]  # 最新の5つのタグを保持
                
                # リポジトリ作成日時の取得（HEADが作成された日時）
                head_path = os.path.join(self.git_path, 'HEAD')
                if os.path.exists(head_path):
                    creation_time = datetime.datetime.fromtimestamp(os.path.getctime(head_path))
                    git_info['creation_date'] = creation_time.strftime('%Y-%m-%d %H:%M:%S')
                
                # リポジトリの統計情報
                total_commits = self._run_git_command(['rev-list', '--count', 'HEAD'])
                git_info['total_commits'] = total_commits if total_commits else '0'
                
                contributors = self._run_git_command(['shortlog', '-sn', 'HEAD'])
                if contributors:
                    git_info['contributors'] = [
                        {'commits': line.split()[0], 'name': ' '.join(line.split()[1:])}
                        for line in contributors.split('\n')[:5]  # 上位5人のコントリビューターを保持
                    ]
                
                return git_info

        except Exception as e:
            logger.error(f"Gitリポジトリ情報の取得エラー: {e}")
        
        return None
