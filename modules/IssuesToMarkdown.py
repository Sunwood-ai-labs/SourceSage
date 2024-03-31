import json
import os

class IssuesToMarkdown:
    def __init__(self, issues_file, sourcesage_file, template_file, output_folder):
        self.issues_file = issues_file
        self.sourcesage_file = sourcesage_file
        self.template_file = template_file
        self.output_folder = output_folder

    def load_data(self):
        with open(self.issues_file, "r", encoding="utf-8") as f:
            self.issues = json.load(f)

        with open(self.sourcesage_file, "r", encoding="utf-8") as f:
            self.sourcesage_md = f.read()

        with open(self.template_file, "r", encoding="utf-8") as f:
            self.template = f.read()

    def create_markdown_files(self):
        for issue in self.issues:
            number = issue["number"]
            title = issue["title"]
            body = issue["body"]

            content = self.template.replace("{{number}}", str(number))
            content = content.replace("{{title}}", title)
            content = content.replace("{{body}}", body or "")
            content = content.replace("{{sourcesage_md}}", self.sourcesage_md)

            filename = os.path.join(self.output_folder, f"ISSUE_{number}.md")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"Issue {number}のマークダウンファイルを作成しました。")

        print("全てのissueのマークダウンファイルを作成しました。")

if __name__ == "__main__":
    issues_file = "SourceSageAssets\\open_issues_filtered.json"
    sourcesage_file = "SourceSageAssets\\SourceSage.md"
    template_file = "docs\\ISSUES_RESOLVE\\ISSUES_RESOLVE_TEMPLATE.md"
    output_folder = "docs\\ISSUES_RESOLVE"

    converter = IssuesToMarkdown(issues_file, sourcesage_file, template_file, output_folder)
    converter.load_data()
    converter.create_markdown_files()