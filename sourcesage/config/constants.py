import os


class Constants:
    """Minimal constants needed by current features.

    Focused on DocuMind (Repository_summary.md) output paths only.
    """

    def __init__(self, output_dir):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.CONFIG_DIR = os.path.join(self.BASE_DIR, "config")

        # Output settings for Repository summary
        self.SOURCE_SAGE_MD = "Repository_summary.md"
        self.DOCUMIND_DIR = "DOCUMIND"

        self.set_output_dir(output_dir)

    def set_output_dir(self, output_dir):
        self.SOURCE_SAGE_ASSETS_DIR = os.path.join(output_dir, ".SourceSageAssets")
