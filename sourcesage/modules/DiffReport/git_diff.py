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
        logger.debug("最新の git タグを取得しています...")
        run_command(self.git_fetch_tags, cwd=self.repo_path if self.repo_path else None)

        logger.debug("最新と前のタグを取得しています...")
        tags_output = run_command(
            self.git_tag_sort, cwd=self.repo_path if self.repo_path else None
        )
        tags = tags_output.split()

        if len(tags) < 2:
            logger.error("比較するタグが十分にありません。タグを2以上追加してください")
            return None, None, None

        latest_tag, previous_tag = tags[:2]
        logger.debug(f"最新タグ: {latest_tag}, 前のタグ: {previous_tag}")

        logger.debug("git diff を生成しています...")
        diff_command = self.git_diff_command + [previous_tag, latest_tag]
        diff = run_command(diff_command, cwd=self.repo_path if self.repo_path else None)

        return diff, latest_tag, previous_tag
