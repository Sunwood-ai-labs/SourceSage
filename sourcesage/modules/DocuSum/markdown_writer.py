import datetime
import os

from loguru import logger


class MarkdownWriter:
    """Class to generate Markdown documents"""

    def __init__(self, stats_collector, pattern_matcher):
        """
        Initialize MarkdownWriter

        Args:
            stats_collector: StatsCollector instance
            pattern_matcher: FilePatternMatcher instance
        """
        self.stats_collector = stats_collector
        self.pattern_matcher = pattern_matcher

    def write_git_info(self, md_file, git_info):
        """Write Git repository information"""
        if git_info:
            md_file.write("## 📂 Git Repository Information\n\n")

            # Basic information
            md_file.write("### 🌐 Basic Information\n\n")
            md_file.write(
                f"- 🔗 Remote URL: {git_info.get('remote_url', 'Not available')}\n"
            )
            md_file.write(
                f"- 🌿 Default branch: {git_info.get('default_branch', 'Not available')}\n"
            )
            md_file.write(
                f"- 🎯 Current branch: {git_info.get('current_branch', 'Not available')}\n"
            )
            md_file.write(
                f"- 📅 Created: {git_info.get('creation_date', 'Not available')}\n"
            )
            md_file.write(
                f"- 📈 Total commits: {git_info.get('total_commits', '0')}\n\n"
            )

            # Latest commit information
            last_commit = git_info.get("last_commit")
            if last_commit:
                md_file.write("### 🔄 Latest Commit\n\n")
                md_file.write(f"- 📝 Message: {last_commit['message']}\n")
                md_file.write(f"- 🔍 Hash: {last_commit['hash']}\n")
                md_file.write(
                    f"- 👤 Author: {last_commit['author']} ({last_commit['email']})\n"
                )
                md_file.write(f"- ⏰ Date: {last_commit['date']}\n\n")

            # Tag information
            tags = git_info.get("tags")
            if tags:
                md_file.write("### 🏷️ Latest Tags\n\n")
                for tag in tags:
                    md_file.write(f"- {tag}\n")
                md_file.write("\n")

            # Contributor information
            contributors = git_info.get("contributors")
            if contributors:
                md_file.write("### 👥 Top Contributors\n\n")
                md_file.write("| 👤 Name | 📊 Commits |\n")
                md_file.write("|---------|----------|\n")
                for contributor in contributors:
                    md_file.write(
                        f"| {contributor['name']} | {contributor['commits']} |\n"
                    )
                md_file.write("\n")

    def write_stats(self, md_file, stats):
        """Write statistics information"""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        md_file.write("## 📊 Project Statistics\n\n")
        md_file.write(f"- 📅 Created: {current_time}\n")
        md_file.write(f"- 📁 Total directories: {stats['total_dirs']}\n")
        md_file.write(f"- 📄 Total files: {stats['total_files']}\n")
        md_file.write(f"- 📏 Max depth: {stats['max_depth']}\n")
        if stats["largest_dir"][0]:
            largest_dir = os.path.basename(stats["largest_dir"][0])
            md_file.write(
                f"- 📦 Largest directory: {largest_dir} ({stats['largest_dir'][1]} entries)\n"
            )
        md_file.write("\n")

    def write_file_stats_table(self, md_file, file_stats):
        """Write file size and line count table"""
        md_file.write("### 📊 File Size and Line Count\n\n")
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
        md_file.write(f"| **Total** |  | **{total_lines}** |  |\n")  # Add total line count
        md_file.write("\n")

    def write_language_stats(self, md_file, language_stats):
        """Write language-specific statistics"""
        md_file.write("### 📈 Language Statistics\n\n")
        md_file.write("| Language | Files | Total Lines | Total Size |\n")
        md_file.write("|----------|-------|-------------|-----------|\n")

        # Sort by total lines
        sorted_stats = sorted(
            language_stats.items(), key=lambda x: x[1]["total_lines"], reverse=True
        )

        for lang, stats in sorted_stats:
            size_str = self.stats_collector.format_size(stats["total_size"])
            md_file.write(
                f"| {lang} | {stats['files']} | {stats['total_lines']} | {size_str} |\n"
            )
        md_file.write("\n")

    def write_file_contents(self, md_file, file_processor, folder):
        """Write file contents"""
        try:
            for root, _, files in os.walk(folder):
                for file in sorted(files):  # Sort by filename
                    file_path = os.path.join(root, file)
                    if not self.pattern_matcher.should_exclude(file_path):
                        try:
                            content = file_processor.process_file(file_path, folder)
                            if content:
                                md_file.write(content)
                        except Exception as e:
                            logger.warning(f"File processing error {file_path}: {e}")
        except Exception as e:
            logger.error(f"File content output error: {e}")
            raise
