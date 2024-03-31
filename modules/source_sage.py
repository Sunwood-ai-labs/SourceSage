import os
from modules.file_utils import load_ignore_patterns, load_language_map
from modules.markdown_utils import generate_markdown_for_folder

class SourceSage:
    def __init__(self, folders, ignore_file='.SourceSageignore', output_file='output.md', language_map_file='language_map.json'):
        self.folders = folders
        print(ignore_file)
        print(folders)
        self.ignore_file = ignore_file
        self.output_file = output_file
        self.exclude_patterns = load_ignore_patterns(ignore_file)
        print(self.exclude_patterns)
        self.language_map = load_language_map(language_map_file)

    def generate_markdown(self):
        with open(self.output_file, 'w', encoding='utf-8') as md_file:
            project_name = os.path.basename(os.path.abspath(self.folders[0]))
            md_file.write(f"# Project: {project_name}\n\n")
            for folder in self.folders:
                markdown_content = generate_markdown_for_folder(folder, self.exclude_patterns, self.language_map)
                md_file.write(markdown_content + '\n\n')