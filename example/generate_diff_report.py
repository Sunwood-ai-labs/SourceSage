import subprocess
import os
from loguru import logger

def run_command(command):
    """
    指定されたコマンドを実行し、出力をキャプチャして表示します。
    """
    logger.info(f">>>>>> 実行コマンド: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
    if result.returncode != 0:
        raise Exception(f"コマンドが失敗しました: {result.stderr}")
    return result.stdout.strip()  # 出力の前後の空白を削除

def get_git_diff():
    """
    現在のリリースと前のリリースの間の git diff を取得します。
    """
    logger.info("最新の git タグを取得しています...")
    run_command(["git", "fetch", "--tags"])
    
    logger.info("最新と前のタグを取得しています...")
    tags_output = run_command(["git", "tag", "--sort=-creatordate"])
    tags = tags_output.split()
    
    if len(tags) < 2:
        raise Exception("比較するタグが十分にありません。")
    
    latest_tag, previous_tag = tags[:2]
    logger.success(f"最新タグ: {latest_tag}, 前のタグ: {previous_tag}")
    
    logger.info("git diff を生成しています...")
    diff = run_command(["git", "diff", previous_tag, latest_tag])
    
    return diff, latest_tag, previous_tag

def generate_markdown_report(diff, latest_tag, previous_tag):
    """
    git diff からマークダウンレポートを生成します。
    """
    logger.info("マークダウンレポートを生成しています...")
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

    with open(".SourceSageAssets/git_diff_report.md", "w", encoding='utf8') as file:
        file.write(report_content)

    logger.success("マークダウンレポートが正常に生成されました！")

def main():
    logger.info("git diff レポートの生成を開始します...")
    diff, latest_tag, previous_tag = get_git_diff()
    generate_markdown_report(diff, latest_tag, previous_tag)
    logger.success("プロセスが完了しました。")

if __name__ == "__main__":
    main()