<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/SourceSage_icon4.png" width="100%">
<br>
<h1 align="center">SourceSage</h1>
<h2 align="center">
  ～Transforming code for AI～

  <br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/sourcesage">
  <img alt="PyPI - Format" src="https://img.shields.io/pypi/format/sourcesage">
  <img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/sourcesage">
  <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/sourcesage">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/sourcesage">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/sourcesage">
  <a href="https://app.codacy.com/gh/Sunwood-ai-labs/SourceSage/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/77ab7715dd23499d82caca4e7ea3b093"/></a>

  [![SourceSage - Sunwood-ai-labs](https://img.shields.io/static/v1?label=SourceSage&message=Sunwood-ai-labs&color=blue&logo=github)](https://github.com/Sunwood-ai-labs/SourceSage "Go to GitHub repo")
![GitHub Repo stars](https://img.shields.io/github/stars/Sunwood-ai-labs/SourceSage)
[![forks - Sunwood-ai-labs](https://img.shields.io/github/forks/SourceSage/Sunwood-ai-labs?style=social)](https://github.com/Sunwood-ai-labs/SourceSage)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Sunwood-ai-labs/SourceSage)](https://github.com/Sunwood-ai-labs/SourceSage)
[![GitHub Top Language](https://img.shields.io/github/languages/top/Sunwood-ai-labs/SourceSage)](https://github.com/Sunwood-ai-labs/SourceSage)
![GitHub Release](https://img.shields.io/github/v/release/Sunwood-ai-labs/SourceSage?color=red)
![GitHub Tag](https://img.shields.io/github/v/tag/Sunwood-ai-labs/SourceSage?sort=semver&color=orange)
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/SourceSage/publish-to-pypi.yml">
  <br>

<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/tag/sourcesage/"><b>[🍀 Official Blog]</b></a>
</p>

</h2>


</p>


SourceSageは、プロジェクトのソースコードとファイル構成を単一のマークダウンファイルに統合し、AIによる自動修正やドキュメント化を実現するPythonスクリプトです。開発のライフサイクル全体を通して、コードの品質向上と生産性の向上を支援します。


>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。

## 更新内容

- [【2024/06/10】 SourceSage 5.0.2](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/v5.0.2)
  - AIRA と Harmon.AI の設定を追加し、コード生成機能を追加(`DocuMind`、`CommitCraft`)
- [【2024/05/12】 SourceSage 4.2.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/v4.2.0)
  - ステージング情報のテンプレートに絵文字と[GAIAH](https://github.com/Sunwood-ai-labs/Gaiah)に対応
- [【2024/04/30】 SourceSage 4.1.2](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/vv4.1.2)
  - GitHub ActionsによるPyPIへの自動パブリッシュ設定を追加し、リリースプロセスを自動化
- [【2024/04/07】 SourceSage 4.1.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/undefined4.1.1)
  - CLI引数の追加とコアモジュールの修正、プロジェクトの構成とファイルの変更によるシンプル化
  - セットアップ手順、実行方法、クイックスタートセクション、テストドキュメントの更新
- [【2024/04/05】 SourceSage 4.0.3](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/undefined4.0.3)
  - README.mdのセットアップ手順と実行手順を簡素化
  - リポジトリのオーナーと名前をコマンドライン引数で指定可能に
  - テスト実行方法のドキュメントを更新
- [【2024/03/31】 SourceSage 3.0.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/tag3.0.0)
  - 下記3つの機能の構成を提案
    - [IssueWise](https://github.com/Sunwood-ai-labs/SourceSage/#1-issuewise開発前の課題解決)機能を追加し、GitHubのオープンIssueを取得してAIによる自動修正をサポート
    - [CommitCraft](https://github.com/Sunwood-ai-labs/SourceSage/#2-commitcraft開発中のコミット管理)機能を追加し、変更差分を追跡してAIが適切なコミットメッセージを生成
    - [DocuMind](https://github.com/Sunwood-ai-labs/SourceSage/#3-documindリリース後のドキュメント化)機能を追加し、プロジェクトの概要とGitの変更履歴を組み合わせてドキュメント化
- [【2024/03/30】 SourceSage 2.0.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/tag2.0.0)
  - ChangelogGenerator classを導入し、コードの可読性と保守性を向上
  - 言語ごとのシンタックスハイライト機能を追加
  - .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外
- 【2024/03/29】 初期リリース


## 主な機能

### [IssueWise（開発前の課題解決）](https://github.com/Sunwood-ai-labs/SourceSage/#1-issuewise開発前の課題解決)

- GitHubのオープンIssueを自動取得し、AIによる課題の自動修正をサポート
- 課題を効率的に特定し、迅速に解決策を見つけられます

### [CommitCraft（開発中のコミット管理）](https://github.com/Sunwood-ai-labs/SourceSage/#2-commitcraft開発中のコミット管理)
- 変更差分を追跡し、AIが適切なコミットメッセージを自動生成
- コミットの内容を正確に記述でき、変更履歴を明確に管理できます

### [DocuMind（リリース後のドキュメント化）](https://github.com/Sunwood-ai-labs/SourceSage/#3-documindリリース後のドキュメント化)
- プロジェクトの概要とGitの変更履歴を組み合わせてドキュメント化 
- プロジェクトの全体像を把握しやすく、メンテナンス性が向上します

## 使用方法

### セットアップ

SourceSageを使用するには、まずPythonのパッケージマネージャーであるpipを使ってインストールします。以下のコマンドをターミナルまたはコマンドプロンプトで実行してください：

```bash
pip install sourcesage
```

これにより、SourceSageがシステムにインストールされ、コマンドラインから実行できるようになります。

### クイックスタート

SourceSageをプロジェクトで使用するには、以下の手順に従ってください：

1. ターミナルまたはコマンドプロンプトを開きます。

2. `cd`コマンドを使って、解析対象のプロジェクトのルートディレクトリに移動します。例えば、プロジェクトが`~/my_project`ディレクトリにある場合は、以下のコマンドを実行します：
   ```bash 
   cd ~/my_project
   ```
   
   Note: `cd`コマンドは "change directory" の略で、現在のディレクトリを指定したディレクトリに変更するために使用します。

3. 次に、以下のコマンドを実行してSourceSageを起動します：
   ```bash
   sourcesage
   ```

4. SourceSageが実行されると、以下のファイルが`SourceSageAssets`ディレクトリに生成されます：
   - `DocuMind.md`：AIがプロジェクトの構造と内容を理解しやすい形式のマークダウンファイルです。
   - `Changelog`：Gitの変更履歴を保存するディレクトリです。
   - `ISSUES_RESOLVE` : Issuesとプロジェクト全体がマージされたファイルを保存するディレクトリです。これらのファイルは、AIがIssueを解決するための重要な情報源となります。
   - `COMMIT_CRAFT` : 開発中のステージされたコードのファイルを保存するディレクトリです。これらのファイルは、AIが適切なコミットメッセージを生成するために使用されます。
   - `open_issues_filtered.json`：GitHubからフェッチしたオープンなIssueのJSONファイルです。
   - `STAGED_DIFF.md`：ステージされた変更の差分情報を含むマークダウンファイルです。

これらのファイルを使って、AIによるプロジェクトの解析や自動修正、ドキュメント化などを行うことができます。

```bash
sourcesage 
```


#### リポジトリ情報の収集と差分情報のレポート作成

```bash
sourcesage --mode Sage GenerateReport
```

#### コミットメッセージの生成

```bash
sourcesage --mode Sage GenerateReport CommitCraft --model-name "gemini/gemini-1.5-pro-latest"
```

#### リリースノートの生成

```bash
sourcesage --mode DocuMind --docuMind-model "gemini/gemini-1.5-pro-latest" --docuMind-db ".SourceSageAssets\DOCUMIND\Repository_summary.md" --docuMind-release-report ".SourceSageAssets\RELEASE_REPORT\Report_v5.0.2.md"  --docuMind-changelog ".SourceSageAssets\Changelog\CHANGELOG_release_5.0.2.md"  --docuMind-output ".SourceSageAssets/DOCUMIND/RELEASE_NOTES_v5.0.2.md"  --docuMind-prompt-output ".SourceSageAssets/DOCUMIND/_PROMPT_v5.0.2.md"  --repo-name "SourceSage" --repo-version "v0.5.0"

```


### リポジトリのIssueも取得する方法

デフォルトでは、SourceSageは現在のディレクトリをプロジェクトのルートとして解析します。ただし、GitHub上のリポジトリのIssueも取得したい場合は、以下のようにリポジトリのオーナー名とリポジトリ名をコマンドライン引数で指定します：

```bash 
sourcesage --owner Sunwood-ai-labs --repository SourceSage
```

上記の例では、`Sunwood-ai-labs`がリポジトリのオーナー名、`SourceSage`がリポジトリ名です。これらの引数を指定することで、SourceSageはGitHub APIを使ってリポジトリのオープンなIssueを取得し、`open_issues_filtered.json`ファイルに保存します。

>[!Note] GitHub APIを使用するには、インターネット接続が必要です。また、リポジトリがプライベートの場合は、適切なアクセストークンを設定する必要があります。

以上が、SourceSageの基本的な使用方法です。ぜひ自分のプロジェクトでSourceSageを活用して、開発効率の向上を体験してみてください！

### 除外ファイルの指定

作業ディレクトリに`.SourceSageignore`ファイルを作成することで、任意のファイルやディレクトリを処理から除外できます。このファイルには、除外したいファイルやディレクトリのパターンを1行ずつ記述します。例えば、以下のように指定します：

```plaintext
# .SourceSageignoreの例
node_modules/
*.log
*.tmp
```

上記の例では、`node_modules`ディレクトリと、拡張子が`.log`または`.tmp`のファイルが除外されます。

`.SourceSageignore`ファイルを使用する場合は、以下のようにコマンドライン引数で指定します：

```bash 
sourcesage --owner Sunwood-ai-labs --repository SourceSage --ignore-file .SourceSageignore
```

この機能を使用することで、不要なファイルやディレクトリを処理から除外し、より効率的にSourceSageを実行できます。

## 1. IssueWise：開発前の課題解決

<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/head_icon4.png" width="50%">
</p>

IssueWiseは、GitHubのオープンなIssue(課題)を自動的に取得し、SourceSageが生成したプロジェクトの概要と組み合わせることで、AIによる課題の自動修正を可能にするツールです。これにより、開発者はプロジェクトの課題を効率的に特定し、解決策を迅速に見つけることができます。

`SourceSageAssets/ISSUE_WISE/ISSUES_RESOLVE`に生成されるマークダウンファイルを使用します。

例：[`docs/SAMPLE/SAMPLE_ISSUE_11.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/docs/SAMPLE/SAMPLE_ISSUE_11.md)

このマークダウンファイルをそのままAIに入力することで、AIが課題を解決するためのコードを生成します。AIは、Issueの内容とプロジェクトの概要を組み合わせて分析し、適切な修正を提案します。

このマークダウンファイルは、下記のファイルのフォーマットで出力されます。
[`docs/ISSUES_RESOLVE/ISSUES_RESOLVE_TEMPLATE.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/docs/ISSUES_RESOLVE/ISSUES_RESOLVE_TEMPLATE.md)

IssueWiseを使用することで、開発者は手作業でIssueを確認する負担を軽減し、AIによる自動修正の恩恵を受けることができます。

## 2. CommitCraft：開発中のコミット管理

<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/head_icon5.png" width="50%">
</p>

CommitCraftは、開発中のステージされた変更を追跡し、AIを活用して適切なコミットメッセージを自動生成するツールです。これにより、開発者はコミットの内容を正確に記述することができ、プロジェクトの変更履歴をより明確に管理できます。

`SourceSageAssets/COMMIT_CRAFT/STAGED_DIFF.md`に生成されるマークダウンファイルを使用します。

例：[`docs/SAMPLE/SAMPLE_STAGE_INFO_AND_PROMT.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/docs/SAMPLE/SAMPLE_STAGE_INFO_AND_PROMT.md)

このマークダウンファイルをそのままAIに入力することで、AIがコミットメッセージを生成します。AIは、ステージされた変更の差分を分析し、その内容を要約したコミットメッセージを提案します。

絵文字を活用した視覚的に分かりやすいコミットメッセージの例はこちらです。

例：[`docs/SAMPLE/SAMPLE_STAGE_INFO_AND_PROMT_EMOJI.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/docs/SAMPLE/SAMPLE_STAGE_INFO_AND_PROMT_EMOJI.md)

このファイルでは、コミットメッセージのフォーマットに絵文字を取り入れ、変更内容をより直感的に表現しています。

また、Gaiah用のコミットメッセージ生成を支援するテンプレートの例はこちらです。

例：[`docs/SAMPLE/SAMPLE_STAGE_INFO_AND_PROMT_GAIAH.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/docs/SAMPLE/SAMPLE_STAGE_INFO_AND_PROMT_GAIAH.md)

このテンプレートでは、効果的で意味のあるコミットメッセージを作成するためのベストプラクティスに従ったガイドラインを提供しています。主要な変更とその目的に焦点を当て、コミットで行われた変更を明確かつ簡潔に説明するように促します。

Issueとマージされたファイルの例はこちらです。

例：[`docs/SAMPLE/SAMPLE_STAGE_INFO_AND_ISSUES_AND_PROMT.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/docs/SAMPLE/SAMPLE_STAGE_INFO_AND_ISSUES_AND_PROMT.md)

このファイルには、ステージされた変更の差分とオープンなIssueの情報が含まれています。AIはこれらの情報を組み合わせて分析し、より包括的なコミットメッセージを生成します。

CommitCraftを使用することで、開発者はコミットメッセージを考える負担を軽減し、一貫性のある適切なコミットメッセージを自動的に生成できます。絵文字の活用やGaiahのテンプレートを利用することで、よりわかりやすく効果的なコミットメッセージの作成が可能になります。



## 3. DocuMind：リリース後のドキュメント化

<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/main/docs/icon/head_icon7.png" width="100%">  
</p>

DocuMindは、リリース後のプロジェクトの統合とドキュメント化を支援するツールです。SourceSageが生成するプロジェクトの概要と、自動生成されたGitの変更履歴を組み合わせることで、プロジェクトの全体像を明確に把握できます。これにより、開発者はプロジェクトのドキュメントを効率的に作成し、メンテナンス性を向上させることができます。

`SourceSageAssets/DocuMind.md`に生成されるマークダウンファイルを使用します。 

例：[`docs/SAMPLE/SAMPLE_DocuMind.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/docs/SAMPLE/SAMPLE_DocuMind.md)

また、`SourceSageAssets/Changelog`に生成されるコミットメッセージのマークダウンファイルを使用します。

例：[`docs/SAMPLE/SAMPLE_CHANGELOG_release_4.1.0.md`](https://github.com/Sunwood-ai-labs/SourceSage/blob/main/docs/SAMPLE/SAMPLE_CHANGELOG_release_4.1.0.md)

この2つのマークダウンファイルをそのままAIに入力することで、AIがプロジェクトの構造と変更内容を理解し、リリースノートやドキュメントを生成することができます。AIは、プロジェクトの概要とGitの変更履歴を分析し、プロジェクトの主要な機能や変更点を要約します。

DocuMindを使用することで、開発者はドキュメント作成の負担を軽減し、常に最新の状態を反映したドキュメントを自動的に生成できます。

## 開発者向け


### 単体テスト

<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/develop/docs/icon/test_icon.jpeg" width="50%">  
</p>


このドキュメントでは、テストを実行するためのコマンドラインについて説明します。

[tests/README.md](https://github.com/Sunwood-ai-labs/SourceSage/blob/develop/tests/README.md)

#### テストの実行

ユニットテストを実行するには、以下のコマンドを使用します。

```bash
pytest tests/test_sourcesage.py
```

このコマンドにより、`tests/test_sourcesage.py`ファイルに定義されたテストケースが実行されます。


### パッケージリリースガイド

<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/develop/docs/icon/package_icon.png" width="50%">  
</p>

このドキュメントでは、GitHub Actions CI/CDを使用してPythonパッケージをPyPIに自動的に公開する方法について説明します。

[docs/package_release/README.md](https://github.com/Sunwood-ai-labs/SourceSage/tree/develop/docs/package_release)

#### 前提条件

- PyPIのアカウントを作成済みであること
- プロジェクトのGitHubリポジトリが存在すること


## 貢献

SourceSageの改善にご協力ください！バグの報告や機能追加の提案がある場合は、[GitHubリポジトリ](https://github.com/Sunwood-ai-labs/SourceSage)でIssueを開くかプルリクエストを送信してください。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。