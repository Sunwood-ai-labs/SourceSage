import os

from loguru import logger

from .DocuSum.docusum import DocuSum


class SourceSage:
    def __init__(
        self,
        folders,
        ignore_file=".SourceSageignore",
        output_file="output.md",
        language_map_file="language_map.json",
        language="en",
    ):
        """
        SourceSageの初期化

        Args:
            folders (list): 処理対象のフォルダパスのリスト
            ignore_file (str): 除外パターンを記述したファイルのパス
            output_file (str): 出力マークダウンファイルのパス
            language_map_file (str): 言語マッピング定義ファイルのパス
            language (str): 出力言語 (en または ja、デフォルト: en)
        """
        self.docusum = DocuSum(
            folders=folders,
            ignore_file=ignore_file,
            language_map_file=language_map_file,
            output_file=output_file,
            language=language,
        )
        logger.info(f"SourceSage initialized: ignore_file={ignore_file}, folders={folders}, language={language}")

    def generate_markdown(self):
        """
        リポジトリのマークダウンドキュメントを生成する
        """
        try:
            logger.info("Starting markdown document generation")
            self.docusum.generate_markdown()
            logger.success("Markdown document generation completed")
        except Exception as e:
            logger.error(f"Error during markdown document generation: {e}")
            raise
