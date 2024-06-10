import os
from .modules.EnvFileHandler import create_or_append_env_file
from .modules.source_sage import SourceSage as SourceSageModule
from .modules.ChangelogGenerator import ChangelogGenerator
from .modules.StageInfoGenerator import StageInfoGenerator
from .modules.GitHubIssueRetrieve import GitHubIssueRetriever
from .modules.StagedDiffGenerator import StagedDiffGenerator
from .modules.IssuesToMarkdown import IssuesToMarkdown

from .config.constants import Constants

from art import *

from loguru import logger

class SourceSage:
    def __init__(self, config_path, output_dir, repo_path, owner, repository, ignore_file, language_map_file):
        self.config_path = config_path
        self.output_dir = output_dir
        self.repo_path = repo_path
        self.ignore_file = ignore_file
        self.language_map_file = language_map_file

        self.constants = Constants(output_dir, owner, repository) 

    def run(self):
        logger.info("Running SourceSage...")
        
        # Load configuration
        config = self.load_config()

        # Create necessary directories
        os.makedirs(self.constants.ISSUE_LOG_DIR, exist_ok=True)
        os.makedirs(self.constants.ISSUES_RESOLVE_DIR, exist_ok=True)
        os.makedirs(self.constants.STAGE_INFO_DIR, exist_ok=True)
        
        # Generate SourceSage markdown
        sourcesage_module = SourceSageModule(folders=[self.repo_path], ignore_file=self.ignore_file,
                                             output_file=os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.DOCUMIND_DIR, self.constants.SOURCE_SAGE_MD),
                                             language_map_file=self.language_map_file)
        sourcesage_module.generate_markdown()

        # Generate changelog
        changelog_generator = ChangelogGenerator(self.repo_path, os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.CHANGELOG_DIR))
        changelog_generator.generate_changelog_for_all_branches()
        changelog_generator.integrate_changelogs()

        # Retrieve GitHub issues
        issue_retriever = GitHubIssueRetriever(self.constants.OWNER, self.constants.REPOSITORY, self.constants.ISSUE_LOG_DIR, self.constants.ISSUES_FILE_NAME)
        issue_retriever.run()

        # Generate staged diff
        diff_generator = StagedDiffGenerator(repo_path=self.repo_path, output_dir=self.constants.SOURCE_SAGE_ASSETS_DIR,
                                             language_map_file=self.language_map_file)
        diff_generator.run()

        # Generate stage info and issues
        stage_info_generator = StageInfoGenerator(issue_file_path=os.path.join(self.constants.ISSUE_LOG_DIR, self.constants.ISSUES_FILE_NAME),
                                                  stage_diff_file_path=os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.STAGED_DIFF_MD),
                                                  template_file_path=os.path.join(self.constants.DOCS_DIR, self.constants.TEMPLATE_STAGE_INFO_DIR, self.constants.STAGE_INFO_TEMPLATE_MD),
                                                  output_file_path=os.path.join(self.constants.STAGE_INFO_DIR, self.constants.STAGE_INFO_OUTPUT_MD))
        stage_info_generator.run()

        # Generate stage info
        stage_info_generator = StageInfoGenerator(issue_file_path=os.path.join(self.constants.ISSUE_LOG_DIR, self.constants.ISSUES_FILE_NAME),
                                                  stage_diff_file_path=os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.STAGED_DIFF_MD),
                                                  template_file_path=os.path.join(self.constants.DOCS_DIR, self.constants.TEMPLATE_STAGE_INFO_DIR, self.constants.STAGE_INFO_SIMPLE_TEMPLATE_MD),
                                                  output_file_path=os.path.join(self.constants.STAGE_INFO_DIR, self.constants.STAGE_INFO_SIMPLE_OUTPUT_MD))
        stage_info_generator.run()
        stage_info_generator = StageInfoGenerator(issue_file_path=os.path.join(self.constants.ISSUE_LOG_DIR, self.constants.ISSUES_FILE_NAME),
                                                  stage_diff_file_path=os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.STAGED_DIFF_MD),
                                                  template_file_path=os.path.join(self.constants.DOCS_DIR, self.constants.TEMPLATE_STAGE_INFO_DIR, self.constants.STAGE_INFO_SIMPLE_TEMPLATE_MD_EMOJI),
                                                  output_file_path=os.path.join(self.constants.STAGE_INFO_DIR, self.constants.STAGE_INFO_SIMPLE_OUTPUT_MD_EMOJI))
        stage_info_generator.run()
        stage_info_generator = StageInfoGenerator(issue_file_path=os.path.join(self.constants.ISSUE_LOG_DIR, self.constants.ISSUES_FILE_NAME),
                                                  stage_diff_file_path=os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.STAGED_DIFF_MD),
                                                  template_file_path=os.path.join(self.constants.DOCS_DIR, self.constants.TEMPLATE_STAGE_INFO_DIR, self.constants.STAGE_INFO_SIMPLE_TEMPLATE_MD_GAIAH),
                                                  output_file_path=os.path.join(self.constants.STAGE_INFO_DIR, self.constants.STAGE_INFO_SIMPLE_OUTPUT_MD_GAIAH))
        stage_info_generator.run()

        stage_info_generator = StageInfoGenerator(issue_file_path=os.path.join(self.constants.ISSUE_LOG_DIR, self.constants.ISSUES_FILE_NAME),
                                                  stage_diff_file_path=os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.STAGED_DIFF_MD),
                                                  template_file_path=os.path.join(self.constants.DOCS_DIR, self.constants.TEMPLATE_STAGE_INFO_DIR, self.constants.STAGE_INFO_SIMPLE_TEMPLATE_MD_GAIAH_B),
                                                  output_file_path=os.path.join(self.constants.STAGE_INFO_DIR, self.constants.STAGE_INFO_SIMPLE_OUTPUT_MD_GAIAH_B))
        stage_info_generator.run()

        # Convert issues to markdown
        issues_to_markdown = IssuesToMarkdown(issues_file=os.path.join(self.constants.ISSUE_LOG_DIR, self.constants.ISSUES_FILE_NAME),
                                              sourcesage_file=os.path.join(self.constants.SOURCE_SAGE_ASSETS_DIR, self.constants.DOCUMIND_DIR, self.constants.SOURCE_SAGE_MD),
                                              template_file=os.path.join(self.constants.DOCS_DIR, self.constants.TEMPLATE_ISSUES_RESOLVE_DIR, self.constants.ISSUES_RESOLVE_TEMPLATE_MD),
                                              output_folder=self.constants.ISSUES_RESOLVE_DIR)
        issues_to_markdown.load_data()
        issues_to_markdown.create_markdown_files()

        # logger.info("SourceSage completed successfully.")
        # tprint("!! successfully !!", font="rnd-medium")
    def load_config(self):
        # Load configuration from YAML file
        # Implement this method based on your configuration file structure
        pass