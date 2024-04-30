
![](https://github.com/Sunwood-ai-labs/SourceSage/blob/develop/docs/icon/package_icon.png?raw=true)

# パッケージリリースガイド

このドキュメントでは、GitHub Actions CI/CDを使用してPythonパッケージをPyPIに自動的に公開する方法について説明します。

## 前提条件

- PyPIのアカウントを作成済みであること
- プロジェクトのGitHubリポジトリが存在すること

## PyPIでの信頼できる公開の設定

1. PyPIのアカウント設定ページで、新しいプロジェクトを登録します。
2. 信頼できる公開者（トラステッドパブリッシャー）を設定します。
   - GitHubリポジトリのオーナー名、リポジトリ名、ワークフロー名を指定します。
   - GitHub環境名（例: `pypi`）を指定します。

## GitHub Actionsワークフローの設定

1. リポジトリのルートディレクトリに`.github/workflows`ディレクトリを作成します。

2. `.github/workflows`ディレクトリ内に`publish-to-pypi.yml`ファイルを作成し、以下の内容を記述します:

```yaml
name: Publish Python Package

on:
  push:
    branches:
      - main
    tags:
      - '*'

jobs:
  publish:
    runs-on: ubuntu-latest
    environment: 
      name: pypi
      url: https://pypi.org/p/sourcesage
    permissions:
      id-token: write
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build
      - name: Build package
        run: python -m build
      - name: Publish package
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          skip-existing: true
```

このワークフローは、以下の条件が満たされたときに実行されます：

- プッシュイベントがmainブランチで発生する
- プッシュされたコミットにタグが付けられている

## 手動でのパッケージのビルドとテスト

パッケージのビルドとテストは、以下のコマンドで行うことができます。

### ビルド

```bash
python setup.py sdist bdist_wheel
```

### テスト（TestPyPIへの公開）

```bash
twine upload --repository pypitest dist/*
```

### 本番（PyPIへの公開）

```bash
twine upload --repository pypi dist/*
```

ただし、GitHub Actionsを用いた自動化により、これらの手動でのビルドや公開は不要になります。タグ付きのコミットをmainブランチにプッシュするだけで、自動的にビルド・テスト・公開が行われます。

## 自動リリースの実行

1. リリース用のコミットをmainブランチにプッシュします。
2. そのコミットにタグを付与します。

GitHub Actionsによって自動的にパッケージがビルドされ、PyPIに公開されます。

以上の手順により、SourceSageパッケージのリリースを自動化することができます。