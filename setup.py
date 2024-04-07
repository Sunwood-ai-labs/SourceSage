from setuptools import setup, find_packages


# READMEファイルの内容を読み込む
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='sourcesage',
    version='4.0.9',
    packages=find_packages(),
    package_data={
        'sourcesage': ['config/**/**', ],
    },
    entry_points={
        'console_scripts': [
            'sourcesage=sourcesage.cli:main',
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sunwood-ai-labs/SourceSage",
    install_requires=[
        'loguru',
        'GitPython',
        'requests',
        'art',
    ],
)