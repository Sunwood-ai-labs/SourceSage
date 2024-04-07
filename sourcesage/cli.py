import argparse
from .core import SourceSage
import os

def main():
    parser = argparse.ArgumentParser(description='SourceSage CLI')
    parser.add_argument('--config', help='Path to the configuration file', default='sourcesage.yml')
    parser.add_argument('--output', help='Output directory for generated files', default='./')
    parser.add_argument('--repo', help='Path to the repository', default='./')
    parser.add_argument('--owner', help='Owner of the repository', default='Sunwood-ai-labs')  # デフォルト値を設定
    parser.add_argument('--repository', help='Name of the repository', default='SourceSage')  # デフォルト値を設定

    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_ignore_file = os.path.join(package_root, 'sourcesage', 'config', '.SourceSageignore')  # 修正
    default_language_map = os.path.join(package_root, 'sourcesage', 'config', 'language_map.json')  # 修正

    parser.add_argument('--ignore-file', help='Path to the ignore file', default=default_ignore_file)  # 修正
    parser.add_argument('--language-map', help='Path to the language map file', default=default_language_map)  # 修正
    
    args = parser.parse_args()

    sourcesage = SourceSage(args.config, args.output, args.repo, args.owner, args.repository, args.ignore_file, args.language_map)
    sourcesage.run()

if __name__ == '__main__':
    main()