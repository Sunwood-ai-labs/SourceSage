import os
from litellm import completion
from loguru import logger
from dotenv import load_dotenv
from art import *

class CommitCraft:
    def __init__(self, model_name, stage_info_file, llm_output_file):
        self.model_name = model_name
        self.stage_info_file = stage_info_file
        self.llm_output_file = llm_output_file
        
        tprint("CommitCraft")

    def generate_commit_messages(self):
        if self.model_name is None:
            logger.info("モデル名が指定されていません。CommitCraftをスキップします。")
            return

        load_dotenv()

        with open(self.stage_info_file, "r", encoding="utf-8") as f:
            stage_info_content = f.read()
            
        logger.info(f"ステージ情報ファイル :  '{self.stage_info_file}'")
        logger.info(f"モデル'{self.model_name}'を使用してLLMにステージ情報を送信しています...")
        response = completion(
            model=self.model_name, 
            messages=[{"role": "user", "content": stage_info_content}]
        )

        # レスポンスからコンテンツを抽出
        content = response.get('choices', [{}])[0].get('message', {}).get('content')

        # レスポンスのコンテンツを指定されたファイルに書き込む
        with open(self.llm_output_file, "w", encoding="utf-8") as f:
            f.write(content)

        logger.success(f"LLMレスポンスが{self.llm_output_file}に保存されました。")