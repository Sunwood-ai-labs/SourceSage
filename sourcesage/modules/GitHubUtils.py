# modules/GitHubUtils.py (新規作成)

import requests
import json
import os
from git import Repo
from loguru import logger

class GitHubUtils:
    @staticmethod
    def retrieve_issues(owner, repository):
        api_url = f'https://api.github.com/repos/{owner}/{repository}/issues?state=open'
        response = requests.get(api_url)
        issues = response.json()
        return issues

    @staticmethod
    def filter_issues(issues):
        filtered_issues = [
            {"number": issue["number"], "title": issue["title"], "body": issue["body"]}
            for issue in issues
            if "pull_request" not in issue
        ]
        return filtered_issues

    @staticmethod
    def save_issues(issues, save_path, file_name):
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        with open(os.path.join(save_path, file_name), 'w', encoding='utf-8') as f:
            json.dump(issues, f, ensure_ascii=False, indent=4)

        logger.info(f'Filtered open issues saved to {os.path.join(save_path, file_name)}')

    @staticmethod
    def get_staged_diff(repo_path):
        repo = Repo(repo_path)
        previous_commit = repo.head.commit
        staged_diff = previous_commit.diff(None, create_patch=True)
        return staged_diff