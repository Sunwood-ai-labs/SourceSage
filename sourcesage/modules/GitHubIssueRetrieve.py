# modules/GitHubIssueRetrieve.py (変更後)

from .GitHubUtils import GitHubUtils

class GitHubIssueRetriever:
    def __init__(self, owner, repository, save_path, file_name):
        self.owner = owner
        self.repository = repository
        self.save_path = save_path
        self.file_name = file_name

    def run(self):
        issues = GitHubUtils.retrieve_issues(self.owner, self.repository)
        filtered_issues = GitHubUtils.filter_issues(issues)
        GitHubUtils.save_issues(filtered_issues, self.save_path, self.file_name)


if __name__ == "__main__":
    owner = "Sunwood-ai-labs"
    repository = "SourceSage"
    save_path = "SourceSageAssets"
    file_name = "open_issues_filtered.json"

    retriever = GitHubIssueRetriever(owner, repository, save_path, file_name)
    retriever.run()