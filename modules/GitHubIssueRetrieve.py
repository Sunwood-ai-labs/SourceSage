import requests
import json
import os

class GitHubIssueRetriever:
    def __init__(self, owner, repository, save_path, file_name):
        self.owner = owner
        self.repository = repository
        self.save_path = save_path
        self.file_name = file_name

    def retrieve_issues(self):
        api_url = f'https://api.github.com/repos/{self.owner}/{self.repository}/issues?state=open'
        response = requests.get(api_url)
        issues = response.json()
        return issues

    def filter_issues(self, issues):
        filtered_issues = [
            {"number": issue["number"], "title": issue["title"], "body": issue["body"]}
            for issue in issues
            if "pull_request" not in issue
        ]
        return filtered_issues

    def save_issues(self, issues):
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        with open(os.path.join(self.save_path, self.file_name), 'w', encoding='utf-8') as f:
            json.dump(issues, f, ensure_ascii=False, indent=4)

        print(f'Filtered open issues saved to {os.path.join(self.save_path, self.file_name)}')

    def run(self):
        issues = self.retrieve_issues()
        filtered_issues = self.filter_issues(issues)
        self.save_issues(filtered_issues)


if __name__ == "__main__":
    owner = "Sunwood-ai-labs"
    repository = "SourceSage"
    save_path = "SourceSageAssets"
    file_name = "open_issues_filtered.json"

    retriever = GitHubIssueRetriever(owner, repository, save_path, file_name)
    retriever.run()