import os

from loguru import logger

try:
    from ..DocuSum.git_info_collector import GitInfoCollector
except Exception:
    GitInfoCollector = None


class MarkdownReportGenerator:
    def __init__(
        self,
        diff,
        latest_tag,
        previous_tag,
        report_title,
        report_sections,
        output_path,
        repo_path=None,
    ):
        self.diff = diff
        self.latest_tag = latest_tag
        self.previous_tag = previous_tag
        self.report_title = report_title
        self.report_sections = report_sections
        self.output_path = output_path
        self.repo_path = repo_path or os.getcwd()

    def generate_markdown_report(self):
        """Generate a Markdown release report from git diff output."""
        logger.debug("Generating Markdown release report")
        repo_name = os.path.basename(os.path.abspath(self.repo_path)) if self.repo_path else ""
        title = f"{repo_name} {self.report_title}".strip()
        report_content = f"# {title}\n\n"

        for section in self.report_sections:
            if section == "version_comparison":
                report_content += self._generate_version_comparison_section()
            elif section == "diff_details":
                report_content += self._generate_diff_details_section()
            elif section == "repo_info":
                report_content += self._generate_repo_info_section()
            elif section == "readme":
                report_content += self._generate_readme_section()

        with open(self.output_path, "w", encoding="utf-8") as file:
            file.write(report_content)

        logger.debug("Markdown release report generated successfully")

    def _generate_version_comparison_section(self):
        return f"## Version Comparison\n\n**{self.previous_tag}** to **{self.latest_tag}**\n\n"

    def _generate_diff_details_section(self):
        section_content = "## Diff Details\n\n"
        file_diffs = self._organize_diff_by_file()
        section_content += self._generate_file_sections(file_diffs)
        return section_content

    def _generate_repo_info_section(self):
        section_content = "## Git Repository Information\n\n"

        if GitInfoCollector is None:
            return section_content + "Git information collector is not available.\n\n"

        git_path = os.path.join(self.repo_path, ".git")
        try:
            collector = GitInfoCollector(git_path)
            info = collector.collect_info()
        except Exception as exc:
            logger.warning(f"Failed to collect Git information: {exc}")
            info = None

        if not info:
            return section_content + "Failed to collect repository information.\n\n"

        section_content += "### Basic Information\n\n"
        section_content += f"- Remote URL: {info.get('remote_url', 'Not available')}\n"
        section_content += f"- Default branch: {info.get('default_branch', 'Not available')}\n"
        section_content += f"- Current branch: {info.get('current_branch', 'Not available')}\n"
        section_content += f"- Created: {info.get('creation_date', 'Not available')}\n"
        section_content += f"- Total commits: {info.get('total_commits', '0')}\n\n"

        last = info.get("last_commit")
        if last:
            section_content += "### Latest Commit\n\n"
            section_content += f"- Message: {last.get('message', '')}\n"
            section_content += f"- Hash: {last.get('hash', '')}\n"
            section_content += f"- Author: {last.get('author', '')} ({last.get('email', '')})\n"
            section_content += f"- Date: {last.get('date', '')}\n\n"

        tags = info.get("tags")
        if tags:
            section_content += "### Latest Tags\n\n"
            for tag in tags:
                section_content += f"- {tag}\n"
            section_content += "\n"

        contributors = info.get("contributors")
        if contributors:
            section_content += "### Top Contributors\n\n"
            section_content += "| Name | Commits |\n"
            section_content += "|------|---------|\n"
            for contributor in contributors:
                section_content += f"| {contributor.get('name', '')} | {contributor.get('commits', '')} |\n"
            section_content += "\n"

        return section_content

    def _generate_readme_section(self):
        section_content = "## README\n\n"
        readme_path = os.path.join(self.repo_path, "README.md")
        try:
            if os.path.exists(readme_path):
                with open(readme_path, "r", encoding="utf-8") as file:
                    section_content += file.read().strip() + "\n\n"
            else:
                section_content += "README.md was not found.\n\n"
        except Exception as exc:
            logger.warning(f"Failed to read README: {exc}")
            section_content += "Failed to read README content.\n\n"
        return section_content

    def _organize_diff_by_file(self):
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
        file_sections = ""
        for file_path, lines in file_diffs.items():
            file_sections += f"### {file_path}\n\n"
            file_sections += "```diff\n"
            file_sections += "\n".join(lines)
            file_sections += "\n```\n\n"
        return file_sections
