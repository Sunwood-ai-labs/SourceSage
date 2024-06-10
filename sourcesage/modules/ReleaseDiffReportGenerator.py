# sourcesage\modules\ReleaseDiffReportGenerator.py
import subprocess
import os
from loguru import logger
import argparse
from art import *
from .GitCommander import run_command

class GitDiffGenerator:
    def __init__(self, repo_path, git_fetch_tags, git_tag_sort, git_diff_command):
        self.repo_path = repo_path
        self.git_fetch_tags = git_fetch_tags
        self.git_tag_sort = git_tag_sort
        self.git_diff_command = git_diff_command
        tprint("GitDiffGenerator")

    def get_git_diff(self):
        """
        現在のリリースと前のリリースの間の git diff を取得します。
        """
        logger.info("最新の git タグを取得しています...")
        run_command(self.git_fetch_tags)

        logger.info("最新と前のタグを取得しています...")
        tags_output = run_command(self.git_tag_sort)
        tags = tags_output.split()

        if len(tags) < 2:
            logger.error("比較するタグが十分にありません。タグを2以上追加してください")
            return None, None, None

        latest_tag, previous_tag = tags[:2]
        logger.success(f"最新タグ: {latest_tag}, 前のタグ: {previous_tag}")

        logger.info("git diff を生成しています...")
        diff_command = self.git_diff_command + [previous_tag, latest_tag]
        diff = run_command(diff_command)

        return diff, latest_tag, previous_tag

class MarkdownReportGenerator:
    def __init__(self, diff, latest_tag, previous_tag, report_title, report_sections, output_path):
        self.diff = diff
        self.latest_tag = latest_tag
        self.previous_tag = previous_tag
        self.report_title = report_title
        self.report_sections = report_sections
        self.output_path = output_path
        tprint("MarkdownReportGenerator")

    def generate_markdown_report(self):
        """
        git diff からマークダウンレポートを生成します。
        """
        logger.info("マークダウンレポートを生成しています...")
        report_content = f"# {self.report_title}\n\n"

        for section in self.report_sections:
            if section == "version_comparison":
                report_content += self._generate_version_comparison_section()
            elif section == "diff_details":
                report_content += self._generate_diff_details_section()

        with open(self.output_path, "w", encoding='utf8') as file:
            file.write(report_content)

        logger.success("マークダウンレポートが正常に生成されました！")

    def _generate_version_comparison_section(self):
        """
        バージョン比較セクションを生成します。
        """
        section_content = f"## バージョン比較\n\n"
        section_content += f"**{self.previous_tag}** と **{self.latest_tag}** の比較\n\n"
        return section_content

    def _generate_diff_details_section(self):
        """
        差分の詳細セクションを生成します。
        """
        section_content = "## 差分の詳細\n\n"
        file_diffs = self._organize_diff_by_file()
        section_content += self._generate_file_sections(file_diffs)
        return section_content

    def _organize_diff_by_file(self):
        """
        ファイル名ごとに差分を整理します。
        """
        file_diffs = {}
        current_file = None
        for line in self.diff.split("\n"):
            if line.startswith("diff --git"):
                current_file = line.split(" ")[-1][2:]
                file_diffs[current_file] = []
            elif current_file:
                file_diffs[current_file].append(line)
        return file_diffs

    def _generate_file_sections(self, file_diffs):
        """
        ファイル名ごとに見出しとコードブロックを生成します。
        """
        file_sections = ""
        for file, lines in file_diffs.items():
            file_sections += f"### {file}\n\n"
            file_sections += "```diff\n"
            file_sections += "\n".join(lines)
            file_sections += "\n```\n\n"
        return file_sections

def parse_arguments():
    """
    コマンドライン引数をパースします。
    """
    parser = argparse.ArgumentParser(description='Generate a git diff report in Markdown format.')
    parser.add_argument('--repo-path', type=str, default="", help='Path to the git repository')
    parser.add_argument('--git-fetch-tags', type=str, nargs='+', default=["git", "fetch", "--tags"], help='Command to fetch git tags')
    parser.add_argument('--git-tag-sort', type=str, nargs='+', default=["git", "tag", "--sort=-creatordate"], help='Command to sort git tags')
    parser.add_argument('--git-diff-command', type=str, nargs='+', default=["git", "diff"], help='Command to generate git diff')
    parser.add_argument('--report-title', type=str, default="Git Diff レポート", help='Title of the Markdown report')
    parser.add_argument('--report-sections', type=str, nargs='+', default=["version_comparison", "diff_details"], help='Sections to include in the report')
    parser.add_argument('--output-path', type=str, default=".SourceSageAssets/git_diff_report.md", help='Path to save the Markdown report')
    return parser.parse_args()

def main():
    logger.info("git diff レポートの生成を開始します...")

    args = parse_arguments()
    git_diff_generator = GitDiffGenerator(args.repo_path, args.git_fetch_tags, args.git_tag_sort, args.git_diff_command)
    diff, latest_tag, previous_tag = git_diff_generator.get_git_diff()

    markdown_report_generator = MarkdownReportGenerator(diff, latest_tag, previous_tag, args.report_title, args.report_sections, args.output_path)
    markdown_report_generator.generate_markdown_report()

    logger.success("プロセスが完了しました。")

if __name__ == "__main__":
    main()