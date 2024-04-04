import argparse
from .core import SourceSage

def main():
    parser = argparse.ArgumentParser(description='SourceSage CLI')
    parser.add_argument('--config', help='Path to the configuration file', default='sourcesage.yml')
    parser.add_argument('--output', help='Output directory for generated files', default='./')
    parser.add_argument('--repo', help='Path to the repository', default='./')
    parser.add_argument('--owner', help='Owner of the repository', default='Sunwood-ai-labs')  # デフォルト値を設定
    parser.add_argument('--repository', help='Name of the repository', default='SourceSage')  # デフォルト値を設定
    
    args = parser.parse_args()

    sourcesage = SourceSage(args.config, args.output, args.repo, args.owner, args.repository)
    sourcesage.run()

if __name__ == '__main__':
    main()