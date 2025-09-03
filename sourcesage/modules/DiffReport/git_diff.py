from loguru import logger

from ..GitCommander import run_command


class GitDiffGenerator:
    def __init__(self, repo_path, git_fetch_tags, git_tag_sort, git_diff_command):
        self.repo_path = repo_path
        self.git_fetch_tags = git_fetch_tags
        self.git_tag_sort = git_tag_sort
        self.git_diff_command = git_diff_command

    def get_git_diff(self):
        """
        現在のリリースと前のリリースの間の git diff を取得します。
        """
        try:
            logger.debug("最新の git タグを取得しています...")
            run_command(
                self.git_fetch_tags, cwd=self.repo_path if self.repo_path else None
            )

            logger.debug("最新と前のタグを取得しています...")
            tags_output = run_command(
                self.git_tag_sort, cwd=self.repo_path if self.repo_path else None
            )
        except Exception as e:
            logger.warning(f"タグ情報の取得に失敗しました: {e}. レポート生成をスキップします。")
            return None, None, None

        tags = tags_output.split() if tags_output else []

        if len(tags) < 2:
            logger.warning("比較するタグが不足しています（最低2つ必要）。レポート生成をスキップします。")
            return None, None, None

        latest_tag, previous_tag = tags[:2]
        logger.debug(f"最新タグ: {latest_tag}, 前のタグ: {previous_tag}")

        logger.debug("git diff を生成しています...")
        diff_command = self.git_diff_command + [previous_tag, latest_tag]
        try:
            diff = run_command(
                diff_command, cwd=self.repo_path if self.repo_path else None
            )
        except Exception as e:
            logger.warning(f"git diff の生成に失敗しました: {e}. レポート生成をスキップします。")
            return None, None, None

        return diff, latest_tag, previous_tag
