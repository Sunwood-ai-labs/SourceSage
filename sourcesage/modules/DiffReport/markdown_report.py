from loguru import logger


class MarkdownReportGenerator:
    def __init__(self, diff, latest_tag, previous_tag, report_title, report_sections, output_path):
        self.diff = diff
        self.latest_tag = latest_tag
        self.previous_tag = previous_tag
        self.report_title = report_title
        self.report_sections = report_sections
        self.output_path = output_path

    def generate_markdown_report(self):
        """
        git diff からマークダウンレポートを生成します。
        """
        logger.debug("マークダウンレポートを生成しています...")
        report_content = f"# {self.report_title}\n\n"

        for section in self.report_sections:
            if section == "version_comparison":
                report_content += self._generate_version_comparison_section()
            elif section == "diff_details":
                report_content += self._generate_diff_details_section()

        with open(self.output_path, "w", encoding='utf8') as file:
            file.write(report_content)

        logger.debug("マークダウンドキュメントが正常に生成されました！")

    def _generate_version_comparison_section(self):
        """
        バージョン比較セクションを生成します。
        """
        section_content = "## バージョン比較\n\n"
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

