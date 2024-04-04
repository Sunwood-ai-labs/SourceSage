from .modules.EnvFileHandler import create_or_append_env_file
from .modules.source_sage import SourceSage as SourceSageModule
from .modules.ChangelogGenerator import ChangelogGenerator
from .modules.StageInfoGenerator import StageInfoGenerator
from .modules.GitHubIssueRetrieve import GitHubIssueRetriever
from .modules.StagedDiffGenerator import StagedDiffGenerator
from .modules.IssuesToMarkdown import IssuesToMarkdown
from .config import constants

class SourceSage:
    def __init__(self, config_path, output_dir, repo_path):
        self.config_path = config_path
        self.output_dir = output_dir
        self.repo_path = repo_path

    def run(self):
        print("Running SourceSage...")
        
        # Load configuration
        config = self.load_config()

        # Create necessary directories
        os.makedirs(constants.ISSUE_LOG_DIR, exist_ok=True)
        os.makedirs(constants.ISSUES_RESOLVE_DIR, exist_ok=True)
        os.makedirs(constants.STAGE_INFO_DIR, exist_ok=True)

        # Generate SourceSage markdown
        sourcesage_module = SourceSageModule(folders=[self.repo_path], ignore_file=constants.IGNORE_FILE,
                                             output_file=os.path.join(constants.SOURCE_SAGE_ASSETS_DIR, constants.SOURCE_SAGE_MD),
                                             language_map_file=constants.LANGUAGE_MAP_FILE)
        sourcesage_module.generate_markdown()

        # Generate changelog
        changelog_generator = ChangelogGenerator(self.repo_path, os.path.join(constants.SOURCE_SAGE_ASSETS_DIR, constants.CHANGELOG_DIR))
        changelog_generator.generate_changelog_for_all_branches()
        changelog_generator.integrate_changelogs()

        # Retrieve GitHub issues
        issue_retriever = GitHubIssueRetriever(constants.OWNER, constants.REPOSITORY, constants.ISSUE_LOG_DIR, constants.ISSUES_FILE_NAME)
        issue_retriever.run()

        # Generate staged diff
        diff_generator = StagedDiffGenerator(repo_path=self.repo_path, output_dir=constants.SOURCE_SAGE_ASSETS_DIR,
                                             language_map_file=constants.LANGUAGE_MAP_FILE)
        diff_generator.run()

        # Generate stage info and issues
        stage_info_generator = StageInfoGenerator(issue_file_path=os.path.join(constants.ISSUE_LOG_DIR, constants.ISSUES_FILE_NAME),
                                                  stage_diff_file_path=os.path.join(constants.SOURCE_SAGE_ASSETS_DIR, constants.STAGED_DIFF_MD),
                                                  template_file_path=os.path.join(constants.DOCS_DIR, constants.TEMPLATE_STAGE_INFO_DIR, constants.STAGE_INFO_TEMPLATE_MD),
                                                  output_file_path=os.path.join(constants.STAGE_INFO_DIR, constants.STAGE_INFO_OUTPUT_MD))
        stage_info_generator.run()

        # Convert issues to markdown
        issues_to_markdown = IssuesToMarkdown(issues_file=os.path.join(constants.ISSUE_LOG_DIR, constants.ISSUES_FILE_NAME),
                                              sourcesage_file=os.path.join(constants.SOURCE_SAGE_ASSETS_DIR, constants.SOURCE_SAGE_MD),
                                              template_file=os.path.join(constants.DOCS_DIR, constants.TEMPLATE_ISSUES_RESOLVE_DIR, constants.ISSUES_RESOLVE_TEMPLATE_MD),
                                              output_folder=constants.ISSUES_RESOLVE_DIR)
        issues_to_markdown.load_data()
        issues_to_markdown.create_markdown_files()

        print("SourceSage completed successfully.")

    def load_config(self):
        # Load configuration from YAML file
        # Implement this method based on your configuration file structure
        pass