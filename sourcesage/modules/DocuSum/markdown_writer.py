import datetime
import os

from loguru import logger


class MarkdownWriter:
    """Generate the primary documentation artifact markdown."""

    MESSAGES = {
        "en": {
            "git_info": "## Git Repository Information",
            "basic_info": "### Basic Information",
            "remote_url": "Remote URL",
            "default_branch": "Default branch",
            "current_branch": "Current branch",
            "created": "Created",
            "total_commits": "Total commits",
            "latest_commit": "### Latest Commit",
            "message": "Message",
            "hash": "Hash",
            "author": "Author",
            "date": "Date",
            "latest_tags": "### Latest Tags",
            "top_contributors": "### Top Contributors",
            "project_stats": "## Project Statistics",
            "total_directories": "Total directories",
            "total_files": "Total files",
            "max_depth": "Max depth",
            "largest_directory": "Largest directory",
            "entries": "entries",
            "file_size_and_line_count": "### File Size and Line Count",
            "language_stats": "### Language Statistics",
            "file_contents": "## File Contents",
            "name": "Name",
            "commits": "Commits",
        },
        "ja": {
            "git_info": "## Git リポジトリ情報",
            "basic_info": "### 基本情報",
            "remote_url": "リモート URL",
            "default_branch": "デフォルトブランチ",
            "current_branch": "現在のブランチ",
            "created": "作成日時",
            "total_commits": "総コミット数",
            "latest_commit": "### 最新コミット",
            "message": "メッセージ",
            "hash": "ハッシュ",
            "author": "作成者",
            "date": "日時",
            "latest_tags": "### 最新タグ",
            "top_contributors": "### 主なコントリビューター",
            "project_stats": "## プロジェクト統計",
            "total_directories": "総ディレクトリ数",
            "total_files": "総ファイル数",
            "max_depth": "最大深さ",
            "largest_directory": "最大ディレクトリ",
            "entries": "件",
            "file_size_and_line_count": "### ファイルサイズと行数",
            "language_stats": "### 言語別統計",
            "file_contents": "## ファイル内容",
            "name": "名前",
            "commits": "コミット数",
        },
    }

    def __init__(self, stats_collector, pattern_matcher, language="en"):
        self.stats_collector = stats_collector
        self.pattern_matcher = pattern_matcher
        self.messages = self.MESSAGES.get(language, self.MESSAGES["en"])

    def write_git_info(self, md_file, git_info):
        """Write Git repository information."""
        if not git_info:
            return

        md_file.write(f"{self.messages['git_info']}\n\n")
        md_file.write(f"{self.messages['basic_info']}\n\n")
        md_file.write(
            f"- {self.messages['remote_url']}: {git_info.get('remote_url', 'Not available')}\n"
        )
        md_file.write(
            f"- {self.messages['default_branch']}: {git_info.get('default_branch', 'Not available')}\n"
        )
        md_file.write(
            f"- {self.messages['current_branch']}: {git_info.get('current_branch', 'Not available')}\n"
        )
        md_file.write(
            f"- {self.messages['created']}: {git_info.get('creation_date', 'Not available')}\n"
        )
        md_file.write(
            f"- {self.messages['total_commits']}: {git_info.get('total_commits', '0')}\n\n"
        )

        last_commit = git_info.get("last_commit")
        if last_commit:
            md_file.write(f"{self.messages['latest_commit']}\n\n")
            md_file.write(
                f"- {self.messages['message']}: {last_commit['message']}\n"
            )
            md_file.write(f"- {self.messages['hash']}: {last_commit['hash']}\n")
            md_file.write(
                f"- {self.messages['author']}: {last_commit['author']} ({last_commit['email']})\n"
            )
            md_file.write(f"- {self.messages['date']}: {last_commit['date']}\n\n")

        tags = git_info.get("tags")
        if tags:
            md_file.write(f"{self.messages['latest_tags']}\n\n")
            for tag in tags:
                md_file.write(f"- {tag}\n")
            md_file.write("\n")

        contributors = git_info.get("contributors")
        if contributors:
            md_file.write(f"{self.messages['top_contributors']}\n\n")
            md_file.write(
                f"| {self.messages['name']} | {self.messages['commits']} |\n"
            )
            md_file.write("|------|---------|\n")
            for contributor in contributors:
                md_file.write(
                    f"| {contributor['name']} | {contributor['commits']} |\n"
                )
            md_file.write("\n")

    def write_stats(self, md_file, stats):
        """Write statistics information."""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        md_file.write(f"{self.messages['project_stats']}\n\n")
        md_file.write(f"- {self.messages['created']}: {current_time}\n")
        md_file.write(
            f"- {self.messages['total_directories']}: {stats['total_dirs']}\n"
        )
        md_file.write(f"- {self.messages['total_files']}: {stats['total_files']}\n")
        md_file.write(f"- {self.messages['max_depth']}: {stats['max_depth']}\n")
        if stats["largest_dir"][0]:
            largest_dir = os.path.basename(stats["largest_dir"][0])
            md_file.write(
                f"- {self.messages['largest_directory']}: {largest_dir} ({stats['largest_dir'][1]} {self.messages['entries']})\n"
            )
        md_file.write("\n")

    def write_file_stats_table(self, md_file, file_stats):
        """Write the file size and line count table."""
        md_file.write(f"{self.messages['file_size_and_line_count']}\n\n")
        md_file.write("| File | Size | Lines | Language |\n")
        md_file.write("|------|------|-------|----------|\n")

        total_lines = 0
        for stat in file_stats:
            size_str = self.stats_collector.format_size(stat["size"])
            line_count = stat["lines"] if stat["lines"] is not None else "N/A"
            md_file.write(
                f"| {stat['path']} | {size_str} | {line_count} | {stat['language']} |\n"
            )
            if isinstance(stat["lines"], int):
                total_lines += stat["lines"]
        md_file.write(f"| **Total** |  | **{total_lines}** |  |\n")
        md_file.write("\n")

    def write_language_stats(self, md_file, language_stats):
        """Write language-specific statistics."""
        md_file.write(f"{self.messages['language_stats']}\n\n")
        md_file.write("| Language | Files | Total Lines | Total Size |\n")
        md_file.write("|----------|-------|-------------|-----------|\n")

        sorted_stats = sorted(
            language_stats.items(), key=lambda item: item[1]["total_lines"], reverse=True
        )

        for language, stats in sorted_stats:
            size_str = self.stats_collector.format_size(stats["total_size"])
            md_file.write(
                f"| {language} | {stats['files']} | {stats['total_lines']} | {size_str} |\n"
            )
        md_file.write("\n")

    def write_file_contents(self, md_file, file_processor, folder):
        """Write file contents."""
        try:
            md_file.write(f"{self.messages['file_contents']}\n\n")
            for root, _, files in os.walk(folder):
                for file_name in sorted(files):
                    file_path = os.path.join(root, file_name)
                    if self.pattern_matcher.should_exclude(file_path):
                        continue

                    try:
                        content = file_processor.process_file(file_path, folder)
                    except Exception as exc:
                        logger.warning(f"File processing error {file_path}: {exc}")
                        continue

                    if content:
                        md_file.write(content)
        except Exception as exc:
            logger.error(f"File content output error: {exc}")
            raise
