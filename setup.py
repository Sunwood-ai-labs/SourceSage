from setuptools import setup, find_packages


# READMEファイルの内容を読み込む
with open("README.md", "r", encoding="utf-8") as fh:
   long_description = fh.read()

# requirements.txtファイルの内容を読み込む
# with open('requirements.txt') as f:
#    required = f.read().splitlines()

setup(
    # パッケージの名前
    name='sourcesage',
    
    # パッケージのバージョン
    version='5.0.2',
    
    # パッケージに含めるモジュールを自動的に探す
    packages=find_packages(),
    
    # パッケージの分類情報
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    
    # パッケージに含めるデータファイル
    package_data={
        'sourcesage': ['config/**/**', 
                        'config/.SourceSageignore'],
    },
    
    # コマンドラインからの実行用エントリーポイント
    entry_points={
        'console_scripts': [
            'sourcesage=sourcesage.cli:main',
        ],
    },
    
    # PyPIに表示される長い説明文
    long_description=long_description,
    
    # 長い説明文のフォーマット
    long_description_content_type="text/markdown",
    
    # プロジェクトのURL
    url="https://github.com/Sunwood-ai-labs/SourceSage",
    
    # パッケージのインストールに必要な依存関係
    # install_requires=required,
    install_requires=[
            'loguru',
            'GitPython',
            'requests',
            'art',
            'termcolor',
            'google-generativeai',
            'litellm'
    ],
)