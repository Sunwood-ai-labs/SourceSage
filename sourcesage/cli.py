import argparse
from .core import SourceSage
import os
from loguru import logger
import sys
# logger.add(sink=sys.stderr, format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level:<8} | {name}:{line} | {message}")

# ログ出力のフォーマットを指定
logger.configure(
    handlers=[
        {
            "sink": sys.stderr,
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level:<6}</level> | <cyan>{name:<45}:{line:<5}</cyan> | <level>{message}</level>",
            "colorize": True,
        }
    ]
)

def main():
    parser = argparse.ArgumentParser(description='SourceSage CLI')
    parser.add_argument('--config', help='Path to the configuration file', default='sourcesage.yml')
    parser.add_argument('--output', help='Output directory for generated files', default='./')
    parser.add_argument('--repo', help='Path to the repository', default='./')
    parser.add_argument('--owner', help='Owner of the repository', default='Sunwood-ai-labs')  # デフォルト値を設定
    parser.add_argument('--repository', help='Name of the repository', default='SourceSage')  # デフォルト値を設定

    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_ignore_file = os.path.join(package_root, 'sourcesage', 'config', '.SourceSageignore')
    default_language_map = os.path.join(package_root, 'sourcesage', 'config', 'language_map.json')

    current_dir_ignore_file = os.path.join(os.getcwd(), '.SourceSageignore')
    if os.path.exists(current_dir_ignore_file):
        ignore_file = current_dir_ignore_file
        logger.info(f"Using ignore file from current directory: {ignore_file}")
    else:
        ignore_file = default_ignore_file
        logger.info(f"Using default ignore file: {ignore_file}")

    parser.add_argument('--ignore-file', help='Path to the ignore file', default=ignore_file)
    parser.add_argument('--language-map', help='Path to the language map file', default=default_language_map)
    
    args = parser.parse_args()

    sourcesage = SourceSage(args.config, args.output, args.repo, args.owner, args.repository, args.ignore_file, args.language_map)
    sourcesage.run()

if __name__ == '__main__':
    main()