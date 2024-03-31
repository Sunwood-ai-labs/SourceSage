# modules/ChangelogUtils.py (新規作成)

from datetime import datetime

class ChangelogUtils:
    @staticmethod
    def format_commit(commit):
        message = commit.message.strip()
        sha = commit.hexsha[:7]
        author = commit.author.name
        date = datetime.fromtimestamp(commit.committed_date).strftime("%Y-%m-%d")
        return f"- [{sha}] - {message} ({author}, {date})"

    @staticmethod
    def generate_git_tree(repo, branch, num_commits):
        tree_text = "```\n"
        tree_text += "Git Commit Log Tree:\n"
        commits = list(repo.iter_commits(branch, max_count=num_commits))
        for i, commit in enumerate(commits, start=1):
            if i == len(commits):  # 最後のコミット
                prefix = "└──"
            else:
                prefix = "├──"
            tree_text += f"{prefix} {commit.hexsha[:7]} - {commit.summary}\n"
        tree_text += "```\n"
        return tree_text

    @staticmethod
    def write_commit_details(file, commits, index):
        commit = commits[index]
        formatted_message = commit.message.replace('\n', '\n    ')
        file.write(f"### コミットハッシュ: {commit.hexsha[:5]}...\n\n")
        file.write(f"- **作者**: {commit.author.name}\n")
        file.write(f"- **日時**: {commit.authored_datetime}\n")
        file.write(f"- **メッセージ**: \n\n    {formatted_message}\n\n")