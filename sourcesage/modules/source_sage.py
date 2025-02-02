import os
from .DocuSum.docusum import DocuSum
from loguru import logger

class SourceSage:
    def __init__(self, folders, ignore_file='.SourceSageignore', output_file='output.md', language_map_file='language_map.json'):
        """
        SourceSageの初期化

        Args:
            folders (list): 処理対象のフォルダパスのリスト
            ignore_file (str): 除外パターンを記述したファイルのパス
            output_file (str): 出力マークダウンファイルのパス
            language_map_file (str): 言語マッピング定義ファイルのパス
        """
        self.docusum = DocuSum(
            folders=folders,
            ignore_file=ignore_file,
            language_map_file=language_map_file,
            output_file=output_file
        )
        logger.info(f"SourceSageを初期化: ignore_file={ignore_file}, folders={folders}")

    def generate_markdown(self):
        """
        リポジトリのマークダウンドキュメントを生成する
        """
        try:
            logger.info("マークダウンドキュメントの生成を開始")
            self.docusum.generate_markdown()
            logger.success("マークダウンドキュメントの生成が完了しました")
        except Exception as e:
            logger.error(f"マークダウンドキュメントの生成中にエラーが発生: {e}")
            raise
