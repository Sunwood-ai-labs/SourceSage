from setuptools import setup, find_packages

setup(
    name='sourcesage',
    version='4.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sourcesage=sourcesage.cli:main',
        ],
    },
    install_requires=[
        'loguru',
        'GitPython',
        'requests',
    ],
)