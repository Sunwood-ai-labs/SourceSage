# sourcesage\modules\IssueWize.py
import json
import os
import re
import time
from dotenv import load_dotenv
from litellm import completion
from loguru import logger

from art import *

try:
    from .GitCommander import run_command
except:
    from GitCommander import run_command
    
# .envファイルから環境変数を読み込む

# ロガーの設定
logger.add("issue_creator.log", rotation="1 MB", compression="zip", enqueue=True)

class IssueWize:
    def __init__(self, model="gemini/gemini-pro"):
        
        tprint("IssueWize")
        
        self.model = model

    def extract_json_from_response(self, response_text):
        """
        応答テキストからJSONのコードブロックを抽出する。
        コードブロックが見つからない場合は、応答テキスト全体をJSONとして扱う。

        Args:
            response_text (str): LiteLLMからの応答テキスト

        Returns:
            str: 抽出されたJSONの文字列
        """
        json_match = re.search(r'```json(.*?)```', response_text, re.DOTALL)
        if json_match:
            return json_match.group(1).strip()
        else:
            logger.warning("応答テキストにJSONのコードブロックが見つかりませんでした。そのままJSONとしてパースします。")
            return response_text

    def generate_issue_data(self, issue_summary, repo_overview):
        """
        issueの概要からタイトルと本文をJSONフォーマットで生成する。

        Args:
            issue_summary (str): issueの概要
            repo_overview (str): リポジトリの概要

        Returns:
            dict: 生成されたissueのデータ（タイトル、本文、ラベル）
        """
        issue_response = completion(
            model=self.model,
            messages=[{"role": "user", "content": f"""
以下のissueの概要からタイトルと本文とラベルをJSONフォーマットで生成してください:
下記のリポジトリの概要を参考にして生成して
タスクはなるべく分割して。
JSONのbodyはなるべく文章にして改行などは使用しないで句読点などで区切って。
ラベルは下記のラベルリストから参照して

{issue_summary}

## JSONフォーマットの例:
{{
  "title": "例：新機能の実装",
  "body": "例：新機能の詳細をマークダウン形式で記載します。",
  "labels": ["enhancement"]
}}

## ラベルリスト:

ラベルは以下から選択してください:
- bug: 何かが正常に動作していない 
- documentation: ドキュメントの改善や追加
- duplicate: 既に存在するIssueやPull Request 
- enhancement: 新機能やリクエスト
- good first issue: 初心者におすすめ
- help wanted: 特別な注意が必要
- invalid: 正しくないと思われるもの
- question: 詳細情報が求められている
- wontfix: 対応しないもの

## リポジトリの概要:
{repo_overview}

"""}]
        )
        issue_response_text = issue_response.get('choices', [{}])[0].get('message', {}).get('content')

        # 応答のテキストをファイルに保存
        with open("issue_response.txt", "w", encoding="utf-8") as f:
            f.write(issue_response_text)

        issue_json = self.extract_json_from_response(issue_response_text)

        try:
            # JSONをパースしてタイトルと本文を取得
            issue_data = json.loads(issue_json)
            issue_data['labels'] = issue_data.get('labels', [])
            return issue_data
        except json.JSONDecodeError as e:
            logger.error(f"JSONのデコードに失敗しました: {e}")
            logger.error("応答のテキストは'issue_response.txt'ファイルに保存されました。")
            raise

    def generate_detailed_markdown(self, issue_summary, issue_body):
        """
        issueの概要とBodyから詳細なマークダウンファイルを生成する。

        Args:
            issue_summary (str): issueの概要
            issue_body (str): LiteLLMから取得したissueのBody

        Returns:
            str: 生成された詳細なマークダウンファイルの内容
        """
        detailed_markdown_response = completion(
            model=self.model,
            messages=[{"role": "user", "content": f"""
以下のissueの概要とBodyから、詳細な要件定義やペルソナなどを記載したマークダウンファイルを生成してください。
マークダウンには章構成を多用して可読性を高めてください。

## Issueの概要:
{issue_summary}

## IssueのBody:
{issue_body}
"""}]
        )
        detailed_markdown = detailed_markdown_response.get('choices', [{}])[0].get('message', {}).get('content')
        return detailed_markdown

    def create_issue(self, issue_data, project, milestone):
        """
        ghコマンドを使用してissueを作成する。

        Args:
            issue_data (dict): issueのデータ（タイトル、本文、ラベル）
            project (str): プロジェクト名
            milestone (str): マイルストーン名
        """
        title = issue_data['title']
        body = issue_data['body']
        labels = issue_data['labels']

        # ghコマンドを使用してissueを作成
        command = [
            "gh", "issue", "create",
            "--title", title,
            "--body", body,
            "--project", project
        ]

        # コマンドにラベルを追加
        for label in labels:
            command.extend(["--label", label])

        # コマンドにマイルストーンを追加
        if milestone:
            command.extend(["--milestone", milestone])

        # run_command関数を使用してghコマンドを実行
        run_command(command)

    def create_optimized_issue(self, issue_summary, project, milestone, repo_overview_file, max_retries=3, retry_delay=5):
        """
        issueの概要から最適化されたissueを作成する。

        Args:
            issue_summary (str): issueの概要
            project (str): プロジェクト名
            milestone (str): マイルストーン名
            repo_overview_file (str): リポジトリ概要のマークダウンファイルパス
            max_retries (int): 最大リトライ回数（デフォルトは3）
            retry_delay (int): リトライ間の遅延時間（秒）（デフォルトは5秒）
        """
        retry_count = 0

        # リポジトリ概要のマークダウンファイルを読み込む
        with open(repo_overview_file, "r", encoding="utf-8") as f:
            repo_overview = f.read()

        while retry_count < max_retries:
            try:
                logger.info(f"Issueの作成を開始します。リトライ回数: {retry_count}")

                # LiteLLMを使用してissueの概要からタイトルと本文を生成
                issue_data = self.generate_issue_data(issue_summary, repo_overview)

                # 詳細なマークダウンファイルを生成
                detailed_markdown = self.generate_detailed_markdown(issue_summary, issue_data['body'])

                # 詳細なマークダウンファイルをissueのBodyとして設定
                issue_data['body'] = detailed_markdown

                # issueを作成
                self.create_issue(issue_data, project, milestone)

                logger.success("Issueの作成が完了しました。")
                break

            except Exception as e:
                logger.error(f"Issueの作成に失敗しました: {e}")
                retry_count += 1
                if retry_count < max_retries:
                    logger.warning(f"リトライします。リトライ回数: {retry_count}")
                    time.sleep(retry_delay)
                else:
                    logger.error("リトライ回数の上限に達しました。Issueの作成を中止します。")

if __name__ == '__main__':
    # 使用例
    issue_summary = r"""
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\makim\miniconda3\Scripts\sourcesage.exe\__main__.py", line 7, in <module>
  File "C:\Users\makim\miniconda3\Lib\site-packages\sourcesage\cli.py", line 128, in main
    sourcesage.run()
  File "C:\Users\makim\miniconda3\Lib\site-packages\sourcesage\core.py", line 51, in run
    changelog_generator.integrate_changelogs()
  File "C:\Users\makim\miniconda3\Lib\site-packages\sourcesage\modules\ChangelogGenerator.py", line 150, in integrate_changelogs
    changelog_files = [file for file in os.listdir(self.output_dir) if file.startswith("CHANGELOG_")]
FileNotFoundError: [WinError 3] 指定されたパスが見つかりません。: './.SourceSageAssets/Changelog'

(base) C:\Prj\jupytext>
    """
    project_name = "TaskSphere"
    milestone = "Sprint01"
    repo_overview_file = r".SourceSageAssets\DOCUMIND\Repository_summary.md"
    # repo_overview_file = r"README.md"
    # model = "gemini/gemini-1.5-pro"
    model = "gemini/gemini-1.5-flash"
    issue_creator = IssueWize(model=model)
    issue_creator.create_optimized_issue(issue_summary, project_name, milestone, repo_overview_file, max_retries=5, retry_delay=10)
