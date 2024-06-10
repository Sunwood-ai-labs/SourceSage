import os
from .file_utils import load_ignore_patterns, load_language_map  # 相対インポートを修正
from .markdown_utils import generate_markdown_for_folder
from loguru import logger
import sys

# logger.level("CMD", no=25, color="<green>", icon="✓")
# "subprocess"レベルを追加
logger.level("SUBPROCESS", no=15, color="<cyan>", icon="🔍")

class SourceSage:
    def __init__(self, folders, ignore_file='.SourceSageignore', output_file='output.md', language_map_file='language_map.json'):
        self.folders = folders
        logger.info(f"ignore_file is ... {ignore_file}")        
        logger.info(folders)
        self.ignore_file = ignore_file
        self.output_file = output_file
        self.exclude_patterns = load_ignore_patterns(ignore_file)
        logger.info(self.exclude_patterns)
        self.language_map = load_language_map(language_map_file)

    def generate_markdown(self):
        # output_fileのディレクトリを取得
        output_dir = os.path.dirname(self.output_file)
        
        # ディレクトリが存在しない場合は作成
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        with open(self.output_file, 'w', encoding='utf-8') as md_file:
            project_name = os.path.basename(os.path.abspath(self.folders[0]))
            md_file.write(f"# Project: {project_name}\n\n")
            for folder in self.folders:
                markdown_content = generate_markdown_for_folder(folder, self.exclude_patterns, self.language_map)
                md_file.write(markdown_content + '\n\n')