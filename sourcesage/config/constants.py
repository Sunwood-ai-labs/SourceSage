import os


class Constants:
    """Minimal constants needed by current features.

    Focused on the primary documentation artifact output paths.
    """

    def __init__(self, output_dir):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.CONFIG_DIR = os.path.join(self.BASE_DIR, "config")

        # Output settings for the primary documentation artifact
        self.SOURCE_SAGE_MD = "Repository_summary.md"

        self.set_output_dir(output_dir)

    def set_output_dir(self, output_dir):
        self.SOURCE_SAGE_ASSETS_DIR = os.path.join(output_dir, ".SourceSageAssets")
