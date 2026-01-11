<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/head_icon4.png" width="100%">
</p>

# IssueWize：AIを活用した効率的なIssue作成

IssueWizeは、開発者が提供するIssueの概要から、AIを活用して詳細なIssueを自動的に作成するツールです。これにより、開発者はIssueの作成にかかる時間を大幅に削減し、プロジェクトの課題を効率的に管理することができます。

## 使用方法

1. SourceSageのCLIコマンドから、以下のようにパラメータを指定してIssueWizeを実行します。

```bash
sourcesage --mode IssueWize --issue-summary "Issueの概要" --project-name "プロジェクト名" --milestone-name "マイルストーン名" --repo-overview-file "リポジトリ概要のマークダウンファイルパス" --issuewize-model "使用するAIモデル名"
```

2. IssueWizeは指定されたIssueの概要とリポジトリ概要を元に、AIを使用して詳細なIssueを自動的に作成します。

3. 作成されたIssueには、タイトル、本文、ラベル、プロジェクト、マイルストーンが設定されます。

4. Issueの本文には、AIが生成した詳細な要件定義やペルソナなどが記載されたマークダウンが含まれます。

## パラメータ

- `--issue-summary`: Issueの概要を指定します。
- `--project-name`: プロジェクト名を指定します。
- `--milestone-name`: マイルストーン名を指定します。
- `--repo-overview-file`: リポジトリ概要のマークダウンファイルのパスを指定します。
- `--issuewize-model`: 使用するAIモデル名を指定します（デフォルトは`gemini/gemini-1.5-flash`）。

## サンプル

以下はSourceSageのCLIコマンドを使用してIssueWizeを実行するサンプルです。

```bash
sourcesage --mode IssueWize --issue-summary "IssueWize.pyをSourceSageのCLIコマンドから実行できるようにコマンドを追加する。SourceSageのCLIコマンドからパラメータを指定できるようにしたい（repo_overview_fileやモデル名などのパラメータ）" --project-name "TaskSphere" --milestone-name "Sprint01" --repo-overview-file ".SourceSageAssets\Repository_summary.md" --issuewize-model "gemini/gemini-1.5-flash"
```

このコマンドでは、以下のパラメータを指定しています。

- `--mode IssueWize`: IssueWizeモードを実行することを指定します。
- `--issue-summary "..."`: Issueの概要を指定します。ここでは、IssueWize.pyをSourceSageのCLIコマンドから実行できるようにするための要件が記載されています。
- `--project-name "TaskSphere"`: プロジェクト名を"TaskSphere"に指定します。
- `--milestone-name "Sprint01"`: マイルストーン名を"Sprint01"に指定します。
- `--repo-overview-file ".SourceSageAssets\Repository_summary.md"`: リポジトリ概要のマークダウンファイルのパスを指定します。
- `--issuewize-model "gemini/gemini-1.5-flash"`: 使用するAIモデル名を"gemini/gemini-1.5-flash"に指定します。

このコマンドを実行すると、IssueWizeは指定されたパラメータを使用して、AIによる詳細なIssueの自動生成を行います。生成されたIssueには、タイトル、本文、ラベル、プロジェクト、マイルストーンが設定されます。

開発者は、このようにSourceSageのCLIコマンドからIssueWizeを実行することで、Issueの作成にかかる時間を大幅に削減し、効率的なプロジェクト管理を実現できます。
