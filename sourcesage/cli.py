import argparse
from .core import SourceSage

def main():
    parser = argparse.ArgumentParser(description='SourceSage CLI')
    parser.add_argument('--config', help='Path to the configuration file')
    parser.add_argument('--output', help='Output directory for generated files')
    parser.add_argument('--repo', help='Path to the repository')
    
    args = parser.parse_args()

    config_path = args.config or 'sourcesage.yml'
    output_dir = args.output or 'output'
    repo_path = args.repo or '.'

    sourcesage = SourceSage(config_path, output_dir, repo_path)
    sourcesage.run()

if __name__ == '__main__':
    main()