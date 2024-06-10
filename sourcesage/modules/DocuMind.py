# sourcesage\modules\DocuMind.py
import os
from litellm import completion
from loguru import logger
from dotenv import load_dotenv
from art import *

class DocuMind:
    def __init__(self, model_name, documen_db_path, release_report_path, changelog_path, repo_name, repo_version, prompt_output_path):
        
        tprint("DocuMind")
        
        self.model_name = model_name
        self.documen_db_path = documen_db_path
        self.release_report_path = release_report_path.format(latest_tag=repo_version)
        self.changelog_path = changelog_path.format(version=repo_version)
        self.repo_name = repo_name
        self.repo_version = repo_version
        self.prompt_output_path = prompt_output_path
        self.documen_db = self.load_documen_db()
        self.release_report = self.load_release_report()
        self.changelog = self.load_changelog()
        

    def load_documen_db(self):
        """DocuMindファイルを読み込む"""
        with open(self.documen_db_path, "r", encoding="utf-8") as file:
            return file.read()

    def load_release_report(self):
        """リリースレポートファイルを読み込む"""
        if os.path.exists(self.release_report_path):
            with open(self.release_report_path, "r", encoding="utf-8") as file:
                return file.read()
        else:
            logger.warning(f"リリースレポートファイル'{self.release_report_path}'が見つかりませんでした。スキップします。")
            return ""

    def load_changelog(self):
        """変更履歴ファイルを読み込む"""
        if os.path.exists(self.changelog_path):
            with open(self.changelog_path, "r", encoding="utf-8") as file:
                return file.read()
        else:
            logger.warning(f"変更履歴ファイル'{self.changelog_path}'が見つかりませんでした。スキップします。")
            return ""

    def generate_release_notes(self):
        """リリースノートを生成する"""
        load_dotenv()

        prompt = f"以下の情報を元に、{self.repo_name}の新バージョン{self.repo_version}の日本語のリリースノートを生成してください。記載されているissueがあれば番号(#00みたいに)と共に記載して\n\n"
        prompt += f"# DocuMind\n\n{self.documen_db}\n\n"
        prompt += f"# リリースレポート\n\n{self.release_report}\n\n"
        prompt += f"# 変更履歴\n\n{self.changelog}\n\n"

        self.save_prompt(prompt)

        if self.model_name is None:
            logger.warning("モデル名が指定されていないため、リリースノートの生成をスキップします。")
            return ""

        logger.info(f"モデル'{self.model_name}'を使用してLLMにリリースノート生成を依頼しています...")
        try:
            response = completion(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            release_notes = response.get('choices', [{}])[0].get('message', {}).get('content', '')
            return release_notes
        except Exception as e:
            logger.error(f"リリースノートの生成中にエラーが発生しました: {str(e)}")
            return ""

    def save_prompt(self, prompt):
        """プロンプトを保存する"""
        with open(self.prompt_output_path, "w", encoding="utf-8") as file:
            file.write(prompt)
        logger.success(f"プロンプトが{self.prompt_output_path}に保存されました。")

    def save_release_notes(self, output_path, release_notes):
        """リリースノートを保存する"""
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(release_notes)
        logger.success(f"リリースノートが{output_path}に保存されました。")