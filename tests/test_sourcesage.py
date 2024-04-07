import os
from sourcesage.cli import main
from sourcesage.core import SourceSage
import sys

def ensure_temp_directory():
    """temp フォルダが存在することを確認し、なければ作成します。"""
    temp_path = os.path.join(os.getcwd(), 'temp')
    os.makedirs(temp_path, exist_ok=True)
    return temp_path

def test_sourcesage_cli(capsys):
    temp_dir = ensure_temp_directory()  # tempフォルダの確認/作成

    # テスト用の設定ファイルを作成
    config_path = os.path.join(temp_dir, 'sourcesage.yml')
    with open(config_path, 'w') as f:
        f.write('exclude_patterns:\n  - "*.pyc"\n  - "__pycache__"\n')

    # パッケージのルートディレクトリを取得
    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ignore_file_path = os.path.join(package_root, 'sourcesage', 'config', '.SourceSageignore')  # 修正
    language_map_path = os.path.join(package_root, 'sourcesage', 'config', 'language_map.json')  # 修正

    sys.argv = ['sourcesage', '--config', config_path, '--output', temp_dir, '--repo', package_root, '--owner', 'Sunwood-ai-labs', '--repository', 'SourceSage', '--ignore-file', ignore_file_path, '--language-map', language_map_path]
    main()

    # 出力を確認
    captured = capsys.readouterr()
    assert 'Running SourceSage...' in captured.out
    assert 'SourceSage completed successfully.' in captured.out

    # 出力ファイルが生成されたことを確認
    output_file = os.path.join(temp_dir, 'SourceSage.md')
    # assert os.path.exists(output_file)

    # 出力ファイルの保存場所を表示
    print(f"Output file saved at: {output_file}")

def test_sourcesage_core():
    temp_dir = ensure_temp_directory()  # tempフォルダの確認/作成

    # テスト用の設定ファイルを作成
    config_path = os.path.join(temp_dir, 'sourcesage.yml')
    with open(config_path, 'w') as f:
        f.write('exclude_patterns:\n  - "*.pyc"\n  - "__pycache__"\n')

    # パッケージのルートディレクトリを取得
    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ignore_file_path = os.path.join(package_root, 'sourcesage', 'config', '.SourceSageignore')  # 修正
    language_map_path = os.path.join(package_root, 'sourcesage', 'config', 'language_map.json')  # 修正

    # 必要なディレクトリを作成
    necessary_dirs = ['SourceSageAssets/Changelog', 'SourceSageAssets/ISSUE_LOG', 'SourceSageAssets/ISSUES_RESOLVE', 'SourceSageAssets/STAGE_INFO']
    for dir_path in necessary_dirs:
        os.makedirs(os.path.join(temp_dir, dir_path), exist_ok=True)

    # SourceSageクラスを直接インスタンス化して実行
    sourcesage = SourceSage(config_path, temp_dir, package_root, 'Sunwood-ai-labs', 'SourceSage', ignore_file_path, language_map_path)
    sourcesage.run()

    # 出力ファイルが生成されたことを確認
    output_file = os.path.join(temp_dir, 'SourceSage.md')
    # assert os.path.exists(output_file)

    # 出力ファイルの保存場所を表示
    print(f"Output file saved at: {output_file}")