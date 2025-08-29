# sourcesage\core.py
import os
from rich.console import Console
from .modules.source_sage import SourceSage as SourceSageModule
from .config.constants import Constants
from loguru import logger

console = Console()

class SourceSage:
    def __init__(self, output_dir, repo_path, owner, repository, ignore_file, language_map_file):
        self.output_dir = output_dir
        self.repo_path = repo_path
        self.ignore_file = ignore_file
        self.language_map_file = language_map_file

        self.constants = Constants(output_dir, owner, repository) 

    def run(self):
        # Progress is primarily handled by CLI; keep this lean.
        logger.debug("Running SourceSage core...")

        # Generate SourceSage markdown (Repository_summary.md)
        sourcesage_module = SourceSageModule(folders=[self.repo_path], ignore_file=self.ignore_file,
                                             output_file=os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.DOCUMIND_DIR, self.constants.SOURCE_SAGE_MD),
                                             language_map_file=self.language_map_file)
        sourcesage_module.generate_markdown()
        logger.debug("SourceSage core completed successfully.")
    
