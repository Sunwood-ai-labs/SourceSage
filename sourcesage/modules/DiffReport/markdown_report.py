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
        """
        git diff からマークダウンレポートを生成します。
        """
        logger.debug("マークダウンレポートを生成しています...")
        repo_name = (
            os.path.basename(os.path.abspath(self.repo_path)) if self.repo_path else ""
        )
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

        with open(self.output_path, "w", encoding="utf8") as file:
            file.write(report_content)

        logger.debug("マークダウンドキュメントが正常に生成されました！")

    def _generate_version_comparison_section(self):
        """
        バージョン比較セクションを生成します。
        """
        section_content = "## バージョン比較\n\n"
        section_content += (
            f"**{self.previous_tag}** と **{self.latest_tag}** の比較\n\n"
        )
        return section_content

    def _generate_diff_details_section(self):
        """
        差分の詳細セクションを生成します。
        """
        section_content = "## 差分の詳細\n\n"
        file_diffs = self._organize_diff_by_file()
        section_content += self._generate_file_sections(file_diffs)
        return section_content

    def _generate_repo_info_section(self):
        """
        リポジトリ情報セクションを生成します。
        """
        section_content = "## \U0001f4c2 Gitリポジトリ情報\n\n"

        if GitInfoCollector is None:
            section_content += "Git情報コレクターが利用できません。\n\n"
            return section_content

        git_path = os.path.join(self.repo_path, ".git")
        try:
            collector = GitInfoCollector(git_path)
            info = collector.collect_info()
        except Exception as e:
            logger.warning(f"Git情報の取得に失敗: {e}")
            info = None

        if not info:
            section_content += "情報を取得できませんでした。\n\n"
            return section_content

        # 基本情報
        section_content += "### \U0001f310 基本情報\n\n"
        section_content += (
            f"- \U0001f517 リモートURL: {info.get('remote_url', 'Not available')}\n"
        )
        section_content += f"- \U0001f33f デフォルトブランチ: {info.get('default_branch', 'Not available')}\n"
        section_content += f"- \U0001f3af 現在のブランチ: {info.get('current_branch', 'Not available')}\n"
        section_content += (
            f"- \U0001f4c5 作成日時: {info.get('creation_date', 'Not available')}\n"
        )
        section_content += (
            f"- \U0001f4c8 総コミット数: {info.get('total_commits', '0')}\n\n"
        )

        # 最新コミット
        last = info.get("last_commit")
        if last:
            section_content += "### \U0001f501 最新のコミット\n\n"
            section_content += f"- \U0001f4dd メッセージ: {last.get('message','')}\n"
            section_content += f"- \U0001f50d ハッシュ: {last.get('hash','')}\n"
            section_content += (
                f"- \U0001f464 作者: {last.get('author','')} ({last.get('email','')})\n"
            )
            section_content += f"- \u23f0 日時: {last.get('date','')}\n\n"

        # タグ
        tags = info.get("tags")
        if tags:
            section_content += "### \U0001f3f7\ufe0f 最新のタグ\n\n"
            for t in tags:
                section_content += f"- {t}\n"
            section_content += "\n"

        # コントリビューター
        contributors = info.get("contributors")
        if contributors:
            section_content += "### \U0001f465 主要コントリビューター\n\n"
            section_content += "| \U0001f464 名前 | \U0001f4ca コミット数 |\n"
            section_content += "|---------|-------------|\n"
            for c in contributors:
                section_content += f"| {c.get('name','')} | {c.get('commits','')} |\n"
            section_content += "\n"

        return section_content

    def _generate_readme_section(self):
        """
        READMEの内容を末尾に追加します。
        """
        section_content = "## \U0001f4d6 README\n\n"
        readme_path = os.path.join(self.repo_path, "README.md")
        try:
            if os.path.exists(readme_path):
                with open(readme_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                section_content += content + "\n\n"
            else:
                section_content += "README.md が見つかりません。\n\n"
        except Exception as e:
            logger.warning(f"README読み込みエラー: {e}")
            section_content += "READMEの読み込みに失敗しました。\n\n"

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
