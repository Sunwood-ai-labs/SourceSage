

import os
import sys
import pprint

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
pprint.pprint(sys.path)

from modules.source_sage import SourceSage
from modules.ChangelogGenerator import ChangelogGenerator

if __name__ == "__main__":
    folders = ['./']
    source_sage = SourceSage(folders, ignore_file='.SourceSageignore',
                             output_file='docs/SourceSage.md',
                             language_map_file='config/language_map.json')
    source_sage.generate_markdown()


    repo_path = "./"
    output_dir = "docs/Changelog"
    os.makedirs(output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    generator = ChangelogGenerator(repo_path, output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()