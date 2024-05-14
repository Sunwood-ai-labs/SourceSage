import subprocess
from termcolor import colored
import os

def run_command(command):
    """
    指定されたコマンドを実行し、出力をキャプチャして表示します。
    """
    print(colored(f">>>>>> 実行コマンド: {' '.join(command)}", "cyan"))
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
    if result.returncode != 0:
        raise Exception(f"コマンドが失敗しました: {result.stderr}")
    return result.stdout.strip()  # 出力の前後の空白を削除

def get_git_diff():
    """
    現在のリリースと前のリリースの間の git diff を取得します。
    """
    print(colored("最新の git タグを取得しています...", "blue"))
    run_command(["git", "fetch", "--tags"])
    
    print(colored("最新と前のタグを取得しています...", "blue"))
    tags_output = run_command(["git", "tag", "--sort=-creatordate"])
    tags = tags_output.split()
    
    if len(tags) < 2:
        raise Exception("比較するタグが十分にありません。")
    
    latest_tag, previous_tag = tags[:2]
    print(colored(f"最新タグ: {latest_tag}, 前のタグ: {previous_tag}", "green"))
    
    print(colored("git diff を生成しています...", "blue"))
    diff = run_command(["git", "diff", previous_tag, latest_tag])
    
    return diff, latest_tag, previous_tag

def generate_markdown_report(diff, latest_tag, previous_tag):
    """
    git diff からマークダウンレポートを生成します。
    """
    print(colored("マークダウンレポートを生成しています...", "blue"))
    report_content = f"# Git Diff レポート\n\n"
    report_content += f"## バージョン比較\n\n"
    report_content += f"**{previous_tag}** と **{latest_tag}** の比較\n\n"
    report_content += "## 差分の詳細\n\n"

    # ファイル名ごとに差分を整理
    file_diffs = {}
    current_file = None
    for line in diff.split("\n"):
        if line.startswith("diff --git"):
            current_file = line.split(" ")[-1][2:]  # ファイル名を抽出
            file_diffs[current_file] = []
        elif current_file:
            file_diffs[current_file].append(line)

    # ファイル名ごとに見出しとコードブロックを生成
    for file, lines in file_diffs.items():
        report_content += f"### {file}\n\n"
        report_content += "```diff\n"
        report_content += "\n".join(lines)
        report_content += "\n```\n\n"

    with open("SourceSageAssets/git_diff_report.md", "w", encoding='utf8') as file:
        file.write(report_content)

    print(colored("マークダウンレポートが正常に生成されました！", "green"))

def main():
    print(colored("git diff レポートの生成を開始します...", "yellow"))
    diff, latest_tag, previous_tag = get_git_diff()
    generate_markdown_report(diff, latest_tag, previous_tag)
    print(colored("プロセスが完了しました。", "green"))

if __name__ == "__main__":
    main()
