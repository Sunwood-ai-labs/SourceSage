import argparse
from .core import SourceSage

def main():
    parser = argparse.ArgumentParser(description='SourceSage CLI')
    # 各引数にデフォルト値を設定
    parser.add_argument('--config', help='Path to the configuration file', default='sourcesage.yml')
    parser.add_argument('--output', help='Output directory for generated files', default='./')
    parser.add_argument('--repo', help='Path to the repository', default='./')
    
    args = parser.parse_args()

    # 引数の値を直接使用
    sourcesage = SourceSage(args.config, args.output, args.repo)
    sourcesage.run()

if __name__ == '__main__':
    main()
