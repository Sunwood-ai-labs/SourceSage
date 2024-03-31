# Changelog - Features

## feature/git-log-filter

- [e4bc9db] - 主要な変更点を簡潔にまとめました:

- コミット表示数を5から30に増やし、メインブランチ('main')で確認するように変更
- ファイルパスを更新して、CHANGELOG_Diff.mdへの出力先を変更

この変更により、より包括的な変更履歴を確認できるようになりました。開発チームにとって有益な情報が得られるはずです。 (Maki, 2024-03-30)
- [bd84a1a] - Merge branch 'feature/git-diff' into develop (Maki, 2024-03-30)
- [a3f0970] - リポジトリの言語マッピングを更新し、コミットログの表示を改善しました。

- ファイル拡張子またはファイル名から適切な言語を自動判定するように変更しました。これにより、コード差分の表示が読みやすくなります。
- 新規追加ファイルや削除ファイルの内容を表示する際に、言語の構文によってコード表示を適切に整形するようにしました。
- ファイルパスが見つからない場合の処理を改善し、ユーザーにより分かりやすいメッセージを表示します。
- コミットログの表示が簡潔で分かりやすくなり、変更内容の理解がしやすくなりました。 (Maki, 2024-03-30)
- [c9b9f9e] - 日本語での簡潔なコミットメッセージは以下の通りです:

`CHANGELOG ファイルの場所を変更`

この変更は、既存の CHANGELOG ファイルの保存場所を "Changelog" ディレクトリから "SourceSageAseets" ディレクトリに変更するものです。この変更により、CHANGELOG ファイルがソースコードに関連したディレクトリ構造に含まれるようになり、プロジェクト全体の管理がより一貫性を持つようになります。 (Maki, 2024-03-30)
- [8bcd15b] - コミットメッセージ:

ファイルディフを自動でMD形式の変更履歴に生成するスクリプトを追加

開発ブランチ上の最新5件のコミットを要約し、変更されたファイルとその変更内容を Changelog/CHANGELOG_Diff.md に記録するツールを追加しました。これにより、プロジェクトの変更履歴を簡単に把握できるようになります。コミットハッシュ、作者、日時、コミットメッセージ、変更ファイル一覧と差分を自動で生成することで、ドキュメンテーションの手間を大幅に削減できます。 (Maki, 2024-03-30)
- [3269ed1] - リポジトリ構造の変更とドキュメントのための出力パスの更新

- ソースコード出力ファイルのパスを'docs/SourceSage.md'から'SourceSageAseets/SourceSage.md'に変更
- 変更履歴ファイルの出力パスを'docs/Changelog'から'SourceSageAseets/Changelog'に変更
- これらの変更により、ソースコードとドキュメントファイルの一元管理が容易になり、リポジトリの構造が明確になりました (Maki, 2024-03-30)
- [9f25863] - Delete DIFF_CHANGELOG_main.md (Maki, 2024-03-30)
- [2c47802] - Delete DIFF_CHANGELOG_integrated.md (Maki, 2024-03-30)
- [5267304] - Delete DIFF_CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [a9af521] - Delete DIFF_CHANGELOG_develop.md (Maki, 2024-03-30)
- [3b77e50] - Create DIFF_CHANGELOG_main.md (Maki, 2024-03-30)
- [94e0be2] - Create DIFF_CHANGELOG_integrated.md (Maki, 2024-03-30)
- [084b538] - Create DIFF_CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [a70e351] - Create DIFF_CHANGELOG_develop.md (Maki, 2024-03-30)
- [077ced5] - Update .gitignore (Maki, 2024-03-30)
- [58662d9] - SourceSage 2.0.0 リリース
- ChangelogGeneratorクラスを導入し、コードの可読性と保守性を向上
- 言語ごとのシンタックスハイライト機能を追加
- 対象フォルダやファイルの除外設定を複数行に対応
- コード生成時のエラー処理を改善
- 設定ファイルの場所を外部化し、柔軟性を高化
- .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動除外 (Maki, 2024-03-30)
- [3bb857a] - Update CHANGELOG_develop.md (Maki, 2024-03-30)
- [c210513] - Update CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [e43afbe] - Update CHANGELOG_integrated.md (Maki, 2024-03-30)
- [53a0682] - Update CHANGELOG_main.md (Maki, 2024-03-30)
- [6e36d50] - Update SourceSage.md (Maki, 2024-03-30)
- [327a4ce] - Update README.md (Maki, 2024-03-30)
- [664664e] - コミットメッセージ:

ChangelogGeneratorクラスを導入し、コードの可読性と保守性を向上しました。
シンタックスハイライトの機能を追加し、複数の言語に対応しました。
ファイル/フォルダの除外設定を改善し、柔軟性を向上させました。
設定ファイルの場所を外部化することで、全体的な設定の管理が容易になりました。
.SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外できるようにしました。
Gitの変更履歴を自動生成し、ドキュメント化する機能を追加しました。 (Maki, 2024-03-30)
- [2129f83] - Update SourceSage.md (Maki, 2024-03-30)
- [d8d53bf] - Update CHANGELOG_integrated.md (Maki, 2024-03-30)
- [4a079c6] - Update CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [f93f470] - Update CHANGELOG_develop.md (Maki, 2024-03-30)
- [c980f40] - Merge branch 'feature/add-git-logs' into develop (Maki, 2024-03-30)
- [c67b909] - ソースコードの忽視対象ファイルリストを更新し、変更履歴生成機能を追加

- .SourceSageignoreファイルに"Changelog"ディレクトリを除外対象に追加
- ソースコード解析結果の出力ディレクトリを"docs/SourceSage.md"に変更
- 変更履歴生成機能を追加し、"docs/Changelog"ディレクトリへの出力を実装

これにより、ソースコード解析結果と変更履歴をドキュメント化して管理できるようになり、開発プロセスの透明性と可視性が向上します。 (Maki, 2024-03-30)
- [5813fc7] - Create SourceSage.md (Maki, 2024-03-30)
- [f58eeaa] - Delete CHANGELOG.md (Maki, 2024-03-30)
- [67d8074] - Delete SourceSage.md (Maki, 2024-03-30)
- [c7489ce] - Delete get_git_log.py (Maki, 2024-03-30)
- [83f7c55] - Create CHANGELOG_main.md (Maki, 2024-03-30)
- [67c1538] - Create CHANGELOG_integrated.md (Maki, 2024-03-30)
- [0e1a13a] - Create CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [17127ed] - Create CHANGELOG_features.md (Maki, 2024-03-30)
- [9a7739b] - Create CHANGELOG_develop.md (Maki, 2024-03-30)
- [c346a22] - 変更の目的を明確にし、ファイル名や具体的な変更箇所の記述は最小限に抑えた簡潔なコミットメッセージを以下のように作成しました:

"ChangelogGeneratorクラスの導入によりコードの可読性と保守性を向上"

このコミットでは、以下の主な変更が行われています:

- `get_repo()`, `get_commits()`, `format_commit()` の各機能をChangelogGeneratorクラスにまとめ、インスタンス化して使用するように変更
- クラス化することで、関数の再利用性や拡張性が向上し、コードの可読性と保守性が改善されました
- 使用方法も簡潔になり、main関数の呼び出しが明確になりました (Maki, 2024-03-30)
- [0344765] - Update CHANGELOG.md (Maki, 2024-03-30)
- [5c5e6ac] - Create get_git_log.py (Maki, 2024-03-30)
- [8d4a253] - Create CHANGELOG.md (Maki, 2024-03-30)
- [f26fca5] - Merge branch 'feature/modules' into develop (Maki, 2024-03-30)
- [36d6a4a] - 簡潔にまとめると、このコミットでは以下の変更が行われています:

- `SourceSage.py` ファイルの内容を大幅に変更
- `sys.path.append()` を使ってモジュールのパスを追加
- `pprint.pprint()` を使ってシステムパスをデバッグ出力
- `SourceSage` クラスのインスタンス化と `generate_markdown()` 呼び出しの際に、設定ファイルのパスを変更

これらの変更は、ソースコードの構造を改善し、モジュールの読み込みを正しく行うことを目的としています。これにより、ソースコードの可読性と保守性が向上します。 (Maki, 2024-03-30)
- [60ccecb] - Update SourceSage.md (Maki, 2024-03-30)
- [6796a56] - Create language_map.json (Maki, 2024-03-30)
- [d6e1af6] - Delete language_map.json (Maki, 2024-03-30)
- [01a3876] - Merge branch 'feature/code-block' into develop (Maki, 2024-03-30)
- [b42c67d] - ソースコード生成ツールの改善

- 言語ごとのシンタックスハイライト機能を追加しました
- 対象フォルダの指定やファイルの除外設定を複数行対応しました
- コード生成時のエラー処理を改善しました
- 設定ファイルの場所を外部化し、柔軟性を高めました

これらの変更により、ソースコード抽出時の表示が改善され、ツールの使い勝手が向上しました。 (Maki, 2024-03-30)
- [c5cbeff] - Update SourceSage.md (Maki, 2024-03-30)
- [0229075] - Update README.md (Maki, 2024-03-30)
- [a7e2de5] - Merge branch 'feature/ignore-file' into develop (Maki, 2024-03-30)
- [7c2fcc8] - Create SourceSage.md (Maki, 2024-03-30)
- [d900f91] - Configured GitLens AI settings to use Anthropic's Claude-3 model and generate commit messages in Japanese. (Maki, 2024-03-30)
- [067e1b2] - ソースコードをより効率的に組織化するために、次の変更を行いました:

1. 無視するファイルやフォルダをリスト化した `.SourceSageignore` ファイルを追加しました。これにより、不要なファイルやフォルダを自動的に除外できるようになりました。
2. `SourceSage.py` の `_is_excluded()` メソッドを改善し、 `.SourceSageignore` ファイルに記載された除外パターンに従って、ファイルとフォルダの除外処理を行うようにしました。
3. 不要なコメントを削除し、コードの可読性と保守性を向上させました。

これらの変更により、SourceSageツールの使いやすさが向上し、プロジェクトの管理がスムーズになるはずです。 (Maki, 2024-03-30)
- [79705b5] - Refactor README for SourceSage project

Consolidated project structure and content into a single markdown file, enabling easier understanding and analysis for AI language models. Excluded unnecessary files and directories, enhancing clarity. Updated usage instructions and examples to reflect changes. Also localized link to GitHub repository.

No references. (Maki, 2024-03-30)
- [1c6ebb6] - Refactor exclude patterns for SourceSage

Update exclude patterns to better reflect current project structure and exclude unnecessary files and folders. This change ensures accurate and efficient markdown generation. No associated issues addressed. (Maki, 2024-03-30)
- [a7c5a82] - Refactor output file name for clarity

Change the output file name to 'SourceSage.md' for improved clarity and consistency with the class name. This enhances code readability and maintainability. No associated issues. (Maki, 2024-03-30)
- [d656a61] - Update README.md (Maki, 2024-03-29)
- [bc31164] - Create SourceSage.py (Maki, 2024-03-29)
- [c749d9a] - Create SourceSage_icon6.png (Maki, 2024-03-29)
- [407ddbe] - Update README.md (Maki, 2024-03-29)
- [330b107] - Create SourceSage_icon5.png (Maki, 2024-03-29)
- [77eafaf] - Update README.md (Maki, 2024-03-29)
- [167e71e] - Create SourceSage_icon4.png (Maki, 2024-03-29)
- [3d69364] - Update README.md (Maki, 2024-03-29)
- [4828ab0] - Create SourceSage_icon3.png (Maki, 2024-03-29)
- [7ed0982] - Update README.md (Maki, 2024-03-29)
- [3f2bb6d] - Update README.md (Maki, 2024-03-29)
- [7b2c70f] - Create SourceSage_icon.png (Maki, 2024-03-29)
- [8a96c27] - Initial commit (Maki, 2024-03-29)

## feature/git-refactor

- [51e3612] - [refactor] SourceSage.pyのリファクタリング

## 変更内容

- 環境変数の読み込みと.envファイルの作成処理を`modules.EnvFileHandler`モジュールに移動
 - `create_env_file()`関数を`create_or_append_env_file()`関数に変更し、.envファイルがない場合は作成、ある場合は追記するように修正
- 不要なコメントを削除
- importの順序を調整
 - 標準ライブラリ、外部ライブラリ、自作モジュールの順にimport
- `if __name__ == "__main__":`の条件を追加

## リファクタリングの目的

- コードの可読性と保守性の向上
- 環境変数の読み込みと.envファイルの作成処理の責務を分離
- PEP8に準拠したコードスタイルの適用

これらの変更により、SourceSage.pyの構造が改善され、より理解しやすく保守しやすいコードになりました。 (Maki, 2024-03-31)
- [5538d65] - 「環境ファイルの自動生成機能を追加」

このコミットでは、SourceSage.pyにenv_file関数を追加し、.envファイルが存在しない場合に自動で作成するようにしました。これにより、SourceSageプロジェクトを新しく始める際に、手動でenv_fileを作成する必要がなくなりました。開発者の生産性が向上し、プロジェクト開始がスムーズになることが期待されます。 (Maki, 2024-03-31)
- [e769b1e] - ソース管理用の環境変数ファイルを追加  #2

この変更は、ソースコード管理を容易にするためのプロジェクト設定ファイルを追加するものです。環境変数ファイルには、リポジトリのパス、ソースファイルの場所、出力ファイル名などの重要な構成情報が含まれています。これにより、プロジェクト全体のファイル構造が明確になり、コードの移植性と再現性が向上します。 (Maki, 2024-03-31)
- [91e0f37] - dotenvモジュールのインポートエラーをキャッチし、エラーが発生してもデフォルト値を使用するように変更 (Maki, 2024-03-31)
- [06b64fe] - [feat] issue#2 SourceSage.pyのパラメータを環境変数(.env)から設定できるようにする

SourceSage.pyで使用しているパラメータを環境変数(.env)から設定できるように変更しました。

## 変更内容

- python-dotenvパッケージをインストールし、.envファイルから環境変数を読み込めるようにしました
- .envファイルをプロジェクトルートに作成し、以下のパラメータを定義しました
  - REPO_PATH
  - SOURCE_SAGE_ASSETS_DIR
  - CONFIG_DIR
  - DOCS_DIR
  - FOLDERS
  - IGNORE_FILE
  - OUTPUT_FILE
  - LANGUAGE_MAP_FILE
  - OWNER
  - REPOSITORY
  - ISSUES_FILE_NAME
- SourceSage.pyを変更し、上記のパラメータを環境変数から読み込むようにしました
  - os.getenv()を使用して環境変数の値を取得
  - FOLDERSはカンマ区切りの文字列をリストに変換

## 利点

- .envファイルを変更するだけで、簡単にパラメータを変更できるようになりました
- コードを変更することなくパラメータを設定できるため、メンテナンス性が向上しました
- 複数のフォルダを指定する場合も、.envファイルのFOLDERSをカンマ区切りで指定するだけで対応可能です

以上の変更により、issue#2の要件を満たすことができました。 (Maki, 2024-03-31)
- [277db10] - 開いているIssueのデータを保存し、フィルタリングした結果を別ファイルとして保存する機能を追加しました。これにより、開発者がIssueの状況を詳細に把握しやすくなり、プロジェクト管理が効率化されます。 (Maki, 2024-03-31)
- [0b4a102] - demo md (Maki, 2024-03-31)
- [56e5def] - リファクタリング: SourceSage.pyの変数名とフォルダ名を統一

- ソースコード内の重複するフォルダ名や変数を統一し、コードの可読性を向上
  - source_sage_assets_dirを"SourceSageAssets"とし、関連するパスで使用するように修正
  - config_dirを"config"とし、設定ファイルのパスで使用するように修正
  - docs_dirを"docs"とし、テンプレートファイルのパスで使用するように修正
- 変数名を一部変更し、より分かりやすい名前に修正
  - save_pathをsource_sage_assets_dirに変更
  - file_nameをissues_file_nameに変更
  - output_dirをchangelog_output_dirとissues_markdown_output_dirに分けて使用するように修正
- IssuesToMarkdownのインスタンス化時の引数を、他の部分と同様にf-stringを使用して指定するように修正
- これらの変更により、コードの一貫性と可読性が向上し、保守性が改善された (Maki, 2024-03-31)
- [784acce] - 機能: IssuesToMarkdownクラスにloguruを使用したログ出力を追加

- loguruをインポートして使用できるようにした
- load_data()メソッド内で、データのロード状況をログ出力するようにした
- create_markdown_files()メソッド内で、マークダウンファイルの作成状況をログ出力するようにした
- これにより、処理の進行状況や重要な情報がログに記録されるようになり、デバッグやモニタリングがしやすくなった (Maki, 2024-03-31)
- [248d49b] - 機能: IssuesToMarkdownクラスをSourceSage.pyに統合

- modules/IssuesToMarkdown.pyからIssuesToMarkdownクラスをインポート
- if __name__ == "__main__":ブロックの最後に、IssuesToMarkdownクラスのインスタンス化と実行のコードを追加
- これにより、SourceSage.pyを実行することで、他の処理と一緒にIssuesToMarkdownクラスの処理も実行されるようになった (Maki, 2024-03-31)
- [b0e6da7] - 機能: 出力フォルダを指定できるオプションを追加

- IssuesToMarkdownクラスの初期化時に出力フォルダを指定できるようにした
- create_markdown_filesメソッド内で、os.path.joinを使用して出力フォルダとファイル名を結合
- main部分で出力フォルダを指定できるようにした
- これにより、出力先を柔軟に設定できるようになった (Maki, 2024-03-31)
- [6a33080] - [refactor] Git関係のモジュールのリファクタリング

- GitHubIssueRetrieve.pyとStagedDiffGenerator.pyの重複部分を削除し、GitHubUtils.pyというモジュールにまとめました。
- ChangelogGenerator.pyとDiffChangelogGenerator.pyの共通部分をChangelogUtils.pyモジュールに抽出しました。
- StageInfoGenerator.py内の不要なimport文を削除し、モジュールのインポート方法を修正しました。
- SourceSage.py内のモジュールのインポート方法を修正し、不要なimport文を削除しました。
- モジュール間の依存関係を整理し、コードの可読性と保守性を向上させました。 (Maki, 2024-03-31)
- [7f0765c] - Merge branch 'feature/issues-to-resolve' into develop (Maki, 2024-03-31)
- [c773352] - [refactor] Git関連モジュールのリファクタリング

## 概要

- `DiffChangelogGenerator.py`と`ChangelogGenerator.py`に重複があったため、`ChangelogGenerator.py`に統合
- `ChangelogGenerator.py`の不要なメソッドを削除し、コードを整理
- `SourceSage.py`から不要なimportを削除

## 詳細

### `DiffChangelogGenerator.py`の統合

- `ChangelogGenerator.py`に`DiffChangelogGenerator.py`の機能を統合し、`DiffChangelogGenerator.py`を削除
- `ChangelogGenerator`クラスに以下のメソッドを追加
  - `generate_diff_changelog(self, branch='main', num_commits=2)`
  - `generate_git_tree(self, branch, num_commits)`
  - `write_commit_details(self, file, commits, index)`
  - `write_changed_files(self, file, commits, index)`
  - `write_file_diff(self, file, diff_item, commit, previous_commit)`
  - `write_diff_content(self, file, diff_item, commit, previous_commit, language, file_path)`
  - `escape_code_block(self, content, language)`

### `ChangelogGenerator.py`の整理

- 不要なメソッド`ensure_directory_exists(self, path)`を削除
- `generate_changelog_for_all_branches(self)`メソッド内の不要な出力を削除

### `SourceSage.py`の整理

- 不要なimport文を削除
  - `from modules.DiffChangelogGenerator import RepositoryChangelogGenerator`

## まとめ

Git関連モジュールのリファクタリングにより、コードの重複を解消し、可読性と保守性を向上させました。`ChangelogGenerator`クラスに機能を集約することで、モジュール構造がシンプルになりました。 (Maki, 2024-03-31)
- [ccec5c2] - [feat] SourceSage.pyの機能追加と改善

## 概要

SourceSage.pyに以下の機能を追加し、既存の機能を改善しました。

## 詳細

### 新機能

- GitHubのIssue情報を取得する`GitHubIssueRetriever`クラスを追加
- ステージングされた変更点の差分を生成する`StagedDiffGenerator`クラスを追加
- ステージング情報とIssue情報を統合してMarkdownファイルに出力する`StageInfoGenerator`クラスを追加

### 改善点

- 出力ファイルのパスを`SourceSageAseets`から`SourceSageAssets`に修正
- `ChangelogGenerator`クラスの出力ディレクトリを`SourceSageAseets/Changelog`から`SourceSageAssets/Changelog`に変更

### 処理の流れ

1. `SourceSage`クラスを使用してMarkdownファイルを生成
2. `ChangelogGenerator`クラスを使用してすべてのブランチのChangelogを生成し、統合
3. `GitHubIssueRetriever`クラスを使用してGitHubのIssue情報を取得し、JSONファイルに保存
4. `StagedDiffGenerator`クラスを使用してステージングされた変更点の差分を生成
5. `StageInfoGenerator`クラスを使用して、ステージング情報とIssue情報を統合し、テンプレートに基づいてMarkdownファイルに出力
  - Issue情報を含むMarkdownファイルを生成
  - Issue情報を含まないMarkdownファイルを生成

これらの機能追加と改善により、SourceSage.pyはより多くの情報を生成し、ユーザーにとって有用なものになりました。 (Maki, 2024-03-31)
- [3626c75] - Merge branch 'feature/get-issue' into develop (Maki, 2024-03-31)
- [42d6009] - [feat] コミットメッセージのフォーマットとタイプの説明を追加

## 変更内容

- コミットメッセージのフォーマットを追加
  - タイトルに種類と概要を記載
  - 本文に詳細な説明を記載（必要に応じて）
- コミットメッセージの種類の説明を追加
  - feat: 新機能
  - fix: バグ修正
  - docs: ドキュメントのみの変更
  - style: コードの動作に影響しない変更（空白、フォーマット、セミコロンの欠落など）
  - refactor: バグの修正も機能の追加も行わないコードの変更
  - perf: パフォーマンスを向上させるコードの変更
  - test: 欠けているテストの追加や既存のテストの修正
  - chore: ビルドプロセスやドキュメント生成などの補助ツールやライブラリの変更

## 変更ファイル

- docs/STAGE_INFO/STAGE_INFO_AND_ISSUES_TEMPLATE.md
- docs/STAGE_INFO/STAGE_INFO_TEMPLATE.md

上記のファイルにコミットメッセージのフォーマットとタイプの説明を追加しました。これにより、コミットメッセージの書き方がわかりやすくなり、統一性が保たれます。 (Maki, 2024-03-31)
- [cd44f62] - ソースコードの自動修正とコミットメッセージ生成の機能を追加

## 概要

- GitHubのオープンなissueを取得し、AIによる自動修正機能を追加
- ステージされた変更からAIが適切なコミットメッセージを生成する機能を実装
- プロジェクトの統合とドキュメント化のためのツールを提供

## 詳細

### 1. 課題の確認とAIによる自動修正

- `get_issues.py`を使用してGitHubのオープンなissueを取得し、JSONファイルに保存
- issueの内容と現在のソースコードの情報をClaude AIに入力し、自動でissueの修正を行う
  - `SourceSage.py`を使用して現在のプロジェクトのソースコードとファイル構成を1つのマークダウンファイルに統合
  - `get_issues.py`で取得したissueデータと`SourceSage.py`で生成したマークダウンをClaude AIに入力
  - AIがissueの内容を理解し、現在のソースコードを分析して自動的にissueの修正を提案
  - 提案された修正内容を確認し、必要に応じて手動で調整を行う

### 2. ステージされた変更の確認とコミットメッセージの自動生成

- `StagedDiffGenerator`クラスを使用してステージされた差分を取得し、マークダウンファイルに出力
- ステージされた変更とissueの情報をAIに入力し、適切なコミットメッセージを生成
  - `get_issues.py`で取得したissueデータと`StagedDiffGenerator`で生成したマークダウンをClaude AIに入力
  - AIが既存のissueを考慮してコミットメッセージを自動生成

### 3. プロジェクトの統合とドキュメント化

- `SourceSage.py`を使用してプロジェクト全体のソースコードとファイル構成をAIが理解しやすい形式で統合
  - プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイルにまとめる
  - 不要なファイルやディレクトリを除外するための設定が可能
  - 複数のプログラミング言語に対応し、シンタックスハイライト機能を提供
- Gitの変更履歴を自動生成し、ドキュメント化
  - ブランチごとに変更履歴をマークダウンファイルに出力
  - すべてのブランチの変更履歴を1つのファイルに統合

## その他の変更

- README.mdのアイコン画像のパスを修正
- タイムラインのサンプルを追加し、CSSでスタイリング
- 各種アイコン画像を追加
- `GitHubIssueRetrieve.py`、`StageInfoGenerator.py`、`StagedDiffGenerator.py`のモジュールを追加し、機能を実装

以上の変更により、ソースコードの自動修正とコミットメッセージ生成の機能が追加されました。また、プロジェクトの統合とドキュメント化のためのツールも提供されています。 (Maki, 2024-03-31)
- [2e5517e] - feat: タイムライン機能の追加とissueの解決

このコミットには以下の変更が含まれています:

- マークダウンにかっこいいタイムラインの図を追加 (resolves #5)
  - 魅力的なタイムラインを作成するためのCSSスタイルを実装
  - タイムライン機能を紹介するサンプルマークダウンファイルを提供

また、このコミットにはドキュメントの更新も含まれています:
- 新しいタイムライン機能を紹介するタイムラインサンプルマークダウンファイルを追加
- タイムラインの図をサポートするためにCSSスタイルを更新 (Maki, 2024-03-31)
- [0c0296b] - feat: ステージの差分生成と課題の取得を実装

Resolves #1, #3

このコミットには以下の変更が含まれています:

1. `demo/get_issues.py` を追加しました。これは、GitHub API を使用してリポジトリのオープンな課題を取得するPythonスクリプトです。スクリプトはプルリクエストを除外し、関連する課題データ（番号、タイトル、本文）をJSONファイルに保存します。

2. `modules/StagedDiffGenerator.py` に `StagedDiffGenerator` クラスを実装しました。このクラスは、リポジトリのステージされた変更を含むマークダウンファイル `STAGED_DIFF.md` を生成します。このクラスは `gitpython` ライブラリを使用してステージされた差分を取得し、ファイルパス、差分の内容、ファイル拡張子に基づいたコードブロックのエスケープを使用して出力をフォーマットします。

3. `.gitignore` ファイルを更新し、`SourceSageAssets` ディレクトリを含めるようにしました。

4. `gitpython` ライブラリを使用してステージされた差分を取得するデモスクリプト `demo/get_diff.py` を追加しました。

`StagedDiffGenerator` クラスは、ステージされた変更の読みやすい差分を生成する便利な方法を提供し、コミット前の変更内容の確認と理解を容易にします。`get_issues.py` スクリプトを使用すると、リポジトリのオープンな課題を簡単に取得できます。これはプロジェクトのタスクの追跡と管理に役立ちます。

これらの変更は、課題 #1 と #3 で概説されている要件に対応し、プロジェクトの機能性とユーザビリティを向上させます。 (Maki, 2024-03-31)
- [6ee000e] - Merge branch 'feature/git-log-filter' into develop (Maki, 2024-03-30)
- [eb47be6] - add demo md (Maki, 2024-03-30)
- [7d71c6c] - ファイル構造の改善とコードの可読性向上

- ファイル構造の整理と命名規則の適用により、コードのメンテナンス性と可読性が向上しました。
- ランゲージマッピング機能を拡張し、さまざまな言語のハイライトに対応しました。
- コミットログの表示機能を追加し、変更内容の把握が容易になりました。

これらの変更により、ソースコードの効率的な管理と理解が促進されます。開発プロセスの改善と開発者の生産性向上につながることが期待されます。 (Maki, 2024-03-30)
- [cb246b4] - Create README.md (Maki, 2024-03-30)
- [5e103c4] - Update .gitignore (Maki, 2024-03-30)
- [e4bc9db] - 主要な変更点を簡潔にまとめました:

- コミット表示数を5から30に増やし、メインブランチ('main')で確認するように変更
- ファイルパスを更新して、CHANGELOG_Diff.mdへの出力先を変更

この変更により、より包括的な変更履歴を確認できるようになりました。開発チームにとって有益な情報が得られるはずです。 (Maki, 2024-03-30)
- [bd84a1a] - Merge branch 'feature/git-diff' into develop (Maki, 2024-03-30)
- [a3f0970] - リポジトリの言語マッピングを更新し、コミットログの表示を改善しました。

- ファイル拡張子またはファイル名から適切な言語を自動判定するように変更しました。これにより、コード差分の表示が読みやすくなります。
- 新規追加ファイルや削除ファイルの内容を表示する際に、言語の構文によってコード表示を適切に整形するようにしました。
- ファイルパスが見つからない場合の処理を改善し、ユーザーにより分かりやすいメッセージを表示します。
- コミットログの表示が簡潔で分かりやすくなり、変更内容の理解がしやすくなりました。 (Maki, 2024-03-30)
- [c9b9f9e] - 日本語での簡潔なコミットメッセージは以下の通りです:

`CHANGELOG ファイルの場所を変更`

この変更は、既存の CHANGELOG ファイルの保存場所を "Changelog" ディレクトリから "SourceSageAseets" ディレクトリに変更するものです。この変更により、CHANGELOG ファイルがソースコードに関連したディレクトリ構造に含まれるようになり、プロジェクト全体の管理がより一貫性を持つようになります。 (Maki, 2024-03-30)
- [8bcd15b] - コミットメッセージ:

ファイルディフを自動でMD形式の変更履歴に生成するスクリプトを追加

開発ブランチ上の最新5件のコミットを要約し、変更されたファイルとその変更内容を Changelog/CHANGELOG_Diff.md に記録するツールを追加しました。これにより、プロジェクトの変更履歴を簡単に把握できるようになります。コミットハッシュ、作者、日時、コミットメッセージ、変更ファイル一覧と差分を自動で生成することで、ドキュメンテーションの手間を大幅に削減できます。 (Maki, 2024-03-30)
- [3269ed1] - リポジトリ構造の変更とドキュメントのための出力パスの更新

- ソースコード出力ファイルのパスを'docs/SourceSage.md'から'SourceSageAseets/SourceSage.md'に変更
- 変更履歴ファイルの出力パスを'docs/Changelog'から'SourceSageAseets/Changelog'に変更
- これらの変更により、ソースコードとドキュメントファイルの一元管理が容易になり、リポジトリの構造が明確になりました (Maki, 2024-03-30)
- [9f25863] - Delete DIFF_CHANGELOG_main.md (Maki, 2024-03-30)
- [2c47802] - Delete DIFF_CHANGELOG_integrated.md (Maki, 2024-03-30)
- [5267304] - Delete DIFF_CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [a9af521] - Delete DIFF_CHANGELOG_develop.md (Maki, 2024-03-30)
- [3b77e50] - Create DIFF_CHANGELOG_main.md (Maki, 2024-03-30)
- [94e0be2] - Create DIFF_CHANGELOG_integrated.md (Maki, 2024-03-30)
- [084b538] - Create DIFF_CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [a70e351] - Create DIFF_CHANGELOG_develop.md (Maki, 2024-03-30)
- [077ced5] - Update .gitignore (Maki, 2024-03-30)
- [58662d9] - SourceSage 2.0.0 リリース
- ChangelogGeneratorクラスを導入し、コードの可読性と保守性を向上
- 言語ごとのシンタックスハイライト機能を追加
- 対象フォルダやファイルの除外設定を複数行に対応
- コード生成時のエラー処理を改善
- 設定ファイルの場所を外部化し、柔軟性を高化
- .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動除外 (Maki, 2024-03-30)
- [3bb857a] - Update CHANGELOG_develop.md (Maki, 2024-03-30)
- [c210513] - Update CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [e43afbe] - Update CHANGELOG_integrated.md (Maki, 2024-03-30)
- [53a0682] - Update CHANGELOG_main.md (Maki, 2024-03-30)
- [6e36d50] - Update SourceSage.md (Maki, 2024-03-30)
- [327a4ce] - Update README.md (Maki, 2024-03-30)
- [664664e] - コミットメッセージ:

ChangelogGeneratorクラスを導入し、コードの可読性と保守性を向上しました。
シンタックスハイライトの機能を追加し、複数の言語に対応しました。
ファイル/フォルダの除外設定を改善し、柔軟性を向上させました。
設定ファイルの場所を外部化することで、全体的な設定の管理が容易になりました。
.SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外できるようにしました。
Gitの変更履歴を自動生成し、ドキュメント化する機能を追加しました。 (Maki, 2024-03-30)
- [2129f83] - Update SourceSage.md (Maki, 2024-03-30)
- [d8d53bf] - Update CHANGELOG_integrated.md (Maki, 2024-03-30)
- [4a079c6] - Update CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [f93f470] - Update CHANGELOG_develop.md (Maki, 2024-03-30)
- [c980f40] - Merge branch 'feature/add-git-logs' into develop (Maki, 2024-03-30)
- [c67b909] - ソースコードの忽視対象ファイルリストを更新し、変更履歴生成機能を追加

- .SourceSageignoreファイルに"Changelog"ディレクトリを除外対象に追加
- ソースコード解析結果の出力ディレクトリを"docs/SourceSage.md"に変更
- 変更履歴生成機能を追加し、"docs/Changelog"ディレクトリへの出力を実装

これにより、ソースコード解析結果と変更履歴をドキュメント化して管理できるようになり、開発プロセスの透明性と可視性が向上します。 (Maki, 2024-03-30)
- [5813fc7] - Create SourceSage.md (Maki, 2024-03-30)
- [f58eeaa] - Delete CHANGELOG.md (Maki, 2024-03-30)
- [67d8074] - Delete SourceSage.md (Maki, 2024-03-30)
- [c7489ce] - Delete get_git_log.py (Maki, 2024-03-30)
- [83f7c55] - Create CHANGELOG_main.md (Maki, 2024-03-30)
- [67c1538] - Create CHANGELOG_integrated.md (Maki, 2024-03-30)
- [0e1a13a] - Create CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [17127ed] - Create CHANGELOG_features.md (Maki, 2024-03-30)
- [9a7739b] - Create CHANGELOG_develop.md (Maki, 2024-03-30)
- [c346a22] - 変更の目的を明確にし、ファイル名や具体的な変更箇所の記述は最小限に抑えた簡潔なコミットメッセージを以下のように作成しました:

"ChangelogGeneratorクラスの導入によりコードの可読性と保守性を向上"

このコミットでは、以下の主な変更が行われています:

- `get_repo()`, `get_commits()`, `format_commit()` の各機能をChangelogGeneratorクラスにまとめ、インスタンス化して使用するように変更
- クラス化することで、関数の再利用性や拡張性が向上し、コードの可読性と保守性が改善されました
- 使用方法も簡潔になり、main関数の呼び出しが明確になりました (Maki, 2024-03-30)
- [0344765] - Update CHANGELOG.md (Maki, 2024-03-30)
- [5c5e6ac] - Create get_git_log.py (Maki, 2024-03-30)
- [8d4a253] - Create CHANGELOG.md (Maki, 2024-03-30)
- [f26fca5] - Merge branch 'feature/modules' into develop (Maki, 2024-03-30)
- [36d6a4a] - 簡潔にまとめると、このコミットでは以下の変更が行われています:

- `SourceSage.py` ファイルの内容を大幅に変更
- `sys.path.append()` を使ってモジュールのパスを追加
- `pprint.pprint()` を使ってシステムパスをデバッグ出力
- `SourceSage` クラスのインスタンス化と `generate_markdown()` 呼び出しの際に、設定ファイルのパスを変更

これらの変更は、ソースコードの構造を改善し、モジュールの読み込みを正しく行うことを目的としています。これにより、ソースコードの可読性と保守性が向上します。 (Maki, 2024-03-30)
- [60ccecb] - Update SourceSage.md (Maki, 2024-03-30)
- [6796a56] - Create language_map.json (Maki, 2024-03-30)
- [d6e1af6] - Delete language_map.json (Maki, 2024-03-30)
- [01a3876] - Merge branch 'feature/code-block' into develop (Maki, 2024-03-30)
- [b42c67d] - ソースコード生成ツールの改善

- 言語ごとのシンタックスハイライト機能を追加しました
- 対象フォルダの指定やファイルの除外設定を複数行対応しました
- コード生成時のエラー処理を改善しました
- 設定ファイルの場所を外部化し、柔軟性を高めました

これらの変更により、ソースコード抽出時の表示が改善され、ツールの使い勝手が向上しました。 (Maki, 2024-03-30)
- [c5cbeff] - Update SourceSage.md (Maki, 2024-03-30)
- [0229075] - Update README.md (Maki, 2024-03-30)
- [a7e2de5] - Merge branch 'feature/ignore-file' into develop (Maki, 2024-03-30)
- [7c2fcc8] - Create SourceSage.md (Maki, 2024-03-30)
- [d900f91] - Configured GitLens AI settings to use Anthropic's Claude-3 model and generate commit messages in Japanese. (Maki, 2024-03-30)
- [067e1b2] - ソースコードをより効率的に組織化するために、次の変更を行いました:

1. 無視するファイルやフォルダをリスト化した `.SourceSageignore` ファイルを追加しました。これにより、不要なファイルやフォルダを自動的に除外できるようになりました。
2. `SourceSage.py` の `_is_excluded()` メソッドを改善し、 `.SourceSageignore` ファイルに記載された除外パターンに従って、ファイルとフォルダの除外処理を行うようにしました。
3. 不要なコメントを削除し、コードの可読性と保守性を向上させました。

これらの変更により、SourceSageツールの使いやすさが向上し、プロジェクトの管理がスムーズになるはずです。 (Maki, 2024-03-30)
- [79705b5] - Refactor README for SourceSage project

Consolidated project structure and content into a single markdown file, enabling easier understanding and analysis for AI language models. Excluded unnecessary files and directories, enhancing clarity. Updated usage instructions and examples to reflect changes. Also localized link to GitHub repository.

No references. (Maki, 2024-03-30)
- [1c6ebb6] - Refactor exclude patterns for SourceSage

Update exclude patterns to better reflect current project structure and exclude unnecessary files and folders. This change ensures accurate and efficient markdown generation. No associated issues addressed. (Maki, 2024-03-30)
- [a7c5a82] - Refactor output file name for clarity

Change the output file name to 'SourceSage.md' for improved clarity and consistency with the class name. This enhances code readability and maintainability. No associated issues. (Maki, 2024-03-30)
- [d656a61] - Update README.md (Maki, 2024-03-29)
- [bc31164] - Create SourceSage.py (Maki, 2024-03-29)
- [c749d9a] - Create SourceSage_icon6.png (Maki, 2024-03-29)
- [407ddbe] - Update README.md (Maki, 2024-03-29)
- [330b107] - Create SourceSage_icon5.png (Maki, 2024-03-29)
- [77eafaf] - Update README.md (Maki, 2024-03-29)
- [167e71e] - Create SourceSage_icon4.png (Maki, 2024-03-29)
- [3d69364] - Update README.md (Maki, 2024-03-29)
- [4828ab0] - Create SourceSage_icon3.png (Maki, 2024-03-29)
- [7ed0982] - Update README.md (Maki, 2024-03-29)
- [3f2bb6d] - Update README.md (Maki, 2024-03-29)
- [7b2c70f] - Create SourceSage_icon.png (Maki, 2024-03-29)
- [8a96c27] - Initial commit (Maki, 2024-03-29)

## feature/add-git-logs

- [c346a22] - 変更の目的を明確にし、ファイル名や具体的な変更箇所の記述は最小限に抑えた簡潔なコミットメッセージを以下のように作成しました:

"ChangelogGeneratorクラスの導入によりコードの可読性と保守性を向上"

このコミットでは、以下の主な変更が行われています:

- `get_repo()`, `get_commits()`, `format_commit()` の各機能をChangelogGeneratorクラスにまとめ、インスタンス化して使用するように変更
- クラス化することで、関数の再利用性や拡張性が向上し、コードの可読性と保守性が改善されました
- 使用方法も簡潔になり、main関数の呼び出しが明確になりました (Maki, 2024-03-30)
- [0344765] - Update CHANGELOG.md (Maki, 2024-03-30)
- [5c5e6ac] - Create get_git_log.py (Maki, 2024-03-30)
- [8d4a253] - Create CHANGELOG.md (Maki, 2024-03-30)
- [f26fca5] - Merge branch 'feature/modules' into develop (Maki, 2024-03-30)
- [36d6a4a] - 簡潔にまとめると、このコミットでは以下の変更が行われています:

- `SourceSage.py` ファイルの内容を大幅に変更
- `sys.path.append()` を使ってモジュールのパスを追加
- `pprint.pprint()` を使ってシステムパスをデバッグ出力
- `SourceSage` クラスのインスタンス化と `generate_markdown()` 呼び出しの際に、設定ファイルのパスを変更

これらの変更は、ソースコードの構造を改善し、モジュールの読み込みを正しく行うことを目的としています。これにより、ソースコードの可読性と保守性が向上します。 (Maki, 2024-03-30)
- [60ccecb] - Update SourceSage.md (Maki, 2024-03-30)
- [6796a56] - Create language_map.json (Maki, 2024-03-30)
- [d6e1af6] - Delete language_map.json (Maki, 2024-03-30)
- [01a3876] - Merge branch 'feature/code-block' into develop (Maki, 2024-03-30)
- [b42c67d] - ソースコード生成ツールの改善

- 言語ごとのシンタックスハイライト機能を追加しました
- 対象フォルダの指定やファイルの除外設定を複数行対応しました
- コード生成時のエラー処理を改善しました
- 設定ファイルの場所を外部化し、柔軟性を高めました

これらの変更により、ソースコード抽出時の表示が改善され、ツールの使い勝手が向上しました。 (Maki, 2024-03-30)
- [c5cbeff] - Update SourceSage.md (Maki, 2024-03-30)
- [0229075] - Update README.md (Maki, 2024-03-30)
- [a7e2de5] - Merge branch 'feature/ignore-file' into develop (Maki, 2024-03-30)
- [7c2fcc8] - Create SourceSage.md (Maki, 2024-03-30)
- [d900f91] - Configured GitLens AI settings to use Anthropic's Claude-3 model and generate commit messages in Japanese. (Maki, 2024-03-30)
- [067e1b2] - ソースコードをより効率的に組織化するために、次の変更を行いました:

1. 無視するファイルやフォルダをリスト化した `.SourceSageignore` ファイルを追加しました。これにより、不要なファイルやフォルダを自動的に除外できるようになりました。
2. `SourceSage.py` の `_is_excluded()` メソッドを改善し、 `.SourceSageignore` ファイルに記載された除外パターンに従って、ファイルとフォルダの除外処理を行うようにしました。
3. 不要なコメントを削除し、コードの可読性と保守性を向上させました。

これらの変更により、SourceSageツールの使いやすさが向上し、プロジェクトの管理がスムーズになるはずです。 (Maki, 2024-03-30)
- [79705b5] - Refactor README for SourceSage project

Consolidated project structure and content into a single markdown file, enabling easier understanding and analysis for AI language models. Excluded unnecessary files and directories, enhancing clarity. Updated usage instructions and examples to reflect changes. Also localized link to GitHub repository.

No references. (Maki, 2024-03-30)
- [1c6ebb6] - Refactor exclude patterns for SourceSage

Update exclude patterns to better reflect current project structure and exclude unnecessary files and folders. This change ensures accurate and efficient markdown generation. No associated issues addressed. (Maki, 2024-03-30)
- [a7c5a82] - Refactor output file name for clarity

Change the output file name to 'SourceSage.md' for improved clarity and consistency with the class name. This enhances code readability and maintainability. No associated issues. (Maki, 2024-03-30)
- [d656a61] - Update README.md (Maki, 2024-03-29)
- [bc31164] - Create SourceSage.py (Maki, 2024-03-29)
- [c749d9a] - Create SourceSage_icon6.png (Maki, 2024-03-29)
- [407ddbe] - Update README.md (Maki, 2024-03-29)
- [330b107] - Create SourceSage_icon5.png (Maki, 2024-03-29)
- [77eafaf] - Update README.md (Maki, 2024-03-29)
- [167e71e] - Create SourceSage_icon4.png (Maki, 2024-03-29)
- [3d69364] - Update README.md (Maki, 2024-03-29)
- [4828ab0] - Create SourceSage_icon3.png (Maki, 2024-03-29)
- [7ed0982] - Update README.md (Maki, 2024-03-29)
- [3f2bb6d] - Update README.md (Maki, 2024-03-29)
- [7b2c70f] - Create SourceSage_icon.png (Maki, 2024-03-29)
- [8a96c27] - Initial commit (Maki, 2024-03-29)

## feature/git-log-filter

- [e4bc9db] - 主要な変更点を簡潔にまとめました:

- コミット表示数を5から30に増やし、メインブランチ('main')で確認するように変更
- ファイルパスを更新して、CHANGELOG_Diff.mdへの出力先を変更

この変更により、より包括的な変更履歴を確認できるようになりました。開発チームにとって有益な情報が得られるはずです。 (Maki, 2024-03-30)
- [bd84a1a] - Merge branch 'feature/git-diff' into develop (Maki, 2024-03-30)
- [a3f0970] - リポジトリの言語マッピングを更新し、コミットログの表示を改善しました。

- ファイル拡張子またはファイル名から適切な言語を自動判定するように変更しました。これにより、コード差分の表示が読みやすくなります。
- 新規追加ファイルや削除ファイルの内容を表示する際に、言語の構文によってコード表示を適切に整形するようにしました。
- ファイルパスが見つからない場合の処理を改善し、ユーザーにより分かりやすいメッセージを表示します。
- コミットログの表示が簡潔で分かりやすくなり、変更内容の理解がしやすくなりました。 (Maki, 2024-03-30)
- [c9b9f9e] - 日本語での簡潔なコミットメッセージは以下の通りです:

`CHANGELOG ファイルの場所を変更`

この変更は、既存の CHANGELOG ファイルの保存場所を "Changelog" ディレクトリから "SourceSageAseets" ディレクトリに変更するものです。この変更により、CHANGELOG ファイルがソースコードに関連したディレクトリ構造に含まれるようになり、プロジェクト全体の管理がより一貫性を持つようになります。 (Maki, 2024-03-30)
- [8bcd15b] - コミットメッセージ:

ファイルディフを自動でMD形式の変更履歴に生成するスクリプトを追加

開発ブランチ上の最新5件のコミットを要約し、変更されたファイルとその変更内容を Changelog/CHANGELOG_Diff.md に記録するツールを追加しました。これにより、プロジェクトの変更履歴を簡単に把握できるようになります。コミットハッシュ、作者、日時、コミットメッセージ、変更ファイル一覧と差分を自動で生成することで、ドキュメンテーションの手間を大幅に削減できます。 (Maki, 2024-03-30)
- [3269ed1] - リポジトリ構造の変更とドキュメントのための出力パスの更新

- ソースコード出力ファイルのパスを'docs/SourceSage.md'から'SourceSageAseets/SourceSage.md'に変更
- 変更履歴ファイルの出力パスを'docs/Changelog'から'SourceSageAseets/Changelog'に変更
- これらの変更により、ソースコードとドキュメントファイルの一元管理が容易になり、リポジトリの構造が明確になりました (Maki, 2024-03-30)
- [9f25863] - Delete DIFF_CHANGELOG_main.md (Maki, 2024-03-30)
- [2c47802] - Delete DIFF_CHANGELOG_integrated.md (Maki, 2024-03-30)
- [5267304] - Delete DIFF_CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [a9af521] - Delete DIFF_CHANGELOG_develop.md (Maki, 2024-03-30)
- [3b77e50] - Create DIFF_CHANGELOG_main.md (Maki, 2024-03-30)
- [94e0be2] - Create DIFF_CHANGELOG_integrated.md (Maki, 2024-03-30)
- [084b538] - Create DIFF_CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [a70e351] - Create DIFF_CHANGELOG_develop.md (Maki, 2024-03-30)
- [077ced5] - Update .gitignore (Maki, 2024-03-30)
- [58662d9] - SourceSage 2.0.0 リリース
- ChangelogGeneratorクラスを導入し、コードの可読性と保守性を向上
- 言語ごとのシンタックスハイライト機能を追加
- 対象フォルダやファイルの除外設定を複数行に対応
- コード生成時のエラー処理を改善
- 設定ファイルの場所を外部化し、柔軟性を高化
- .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動除外 (Maki, 2024-03-30)
- [3bb857a] - Update CHANGELOG_develop.md (Maki, 2024-03-30)
- [c210513] - Update CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [e43afbe] - Update CHANGELOG_integrated.md (Maki, 2024-03-30)
- [53a0682] - Update CHANGELOG_main.md (Maki, 2024-03-30)
- [6e36d50] - Update SourceSage.md (Maki, 2024-03-30)
- [327a4ce] - Update README.md (Maki, 2024-03-30)
- [664664e] - コミットメッセージ:

ChangelogGeneratorクラスを導入し、コードの可読性と保守性を向上しました。
シンタックスハイライトの機能を追加し、複数の言語に対応しました。
ファイル/フォルダの除外設定を改善し、柔軟性を向上させました。
設定ファイルの場所を外部化することで、全体的な設定の管理が容易になりました。
.SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外できるようにしました。
Gitの変更履歴を自動生成し、ドキュメント化する機能を追加しました。 (Maki, 2024-03-30)
- [2129f83] - Update SourceSage.md (Maki, 2024-03-30)
- [d8d53bf] - Update CHANGELOG_integrated.md (Maki, 2024-03-30)
- [4a079c6] - Update CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [f93f470] - Update CHANGELOG_develop.md (Maki, 2024-03-30)
- [c980f40] - Merge branch 'feature/add-git-logs' into develop (Maki, 2024-03-30)
- [c67b909] - ソースコードの忽視対象ファイルリストを更新し、変更履歴生成機能を追加

- .SourceSageignoreファイルに"Changelog"ディレクトリを除外対象に追加
- ソースコード解析結果の出力ディレクトリを"docs/SourceSage.md"に変更
- 変更履歴生成機能を追加し、"docs/Changelog"ディレクトリへの出力を実装

これにより、ソースコード解析結果と変更履歴をドキュメント化して管理できるようになり、開発プロセスの透明性と可視性が向上します。 (Maki, 2024-03-30)
- [5813fc7] - Create SourceSage.md (Maki, 2024-03-30)
- [f58eeaa] - Delete CHANGELOG.md (Maki, 2024-03-30)
- [67d8074] - Delete SourceSage.md (Maki, 2024-03-30)
- [c7489ce] - Delete get_git_log.py (Maki, 2024-03-30)
- [83f7c55] - Create CHANGELOG_main.md (Maki, 2024-03-30)
- [67c1538] - Create CHANGELOG_integrated.md (Maki, 2024-03-30)
- [0e1a13a] - Create CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [17127ed] - Create CHANGELOG_features.md (Maki, 2024-03-30)
- [9a7739b] - Create CHANGELOG_develop.md (Maki, 2024-03-30)
- [c346a22] - 変更の目的を明確にし、ファイル名や具体的な変更箇所の記述は最小限に抑えた簡潔なコミットメッセージを以下のように作成しました:

"ChangelogGeneratorクラスの導入によりコードの可読性と保守性を向上"

このコミットでは、以下の主な変更が行われています:

- `get_repo()`, `get_commits()`, `format_commit()` の各機能をChangelogGeneratorクラスにまとめ、インスタンス化して使用するように変更
- クラス化することで、関数の再利用性や拡張性が向上し、コードの可読性と保守性が改善されました
- 使用方法も簡潔になり、main関数の呼び出しが明確になりました (Maki, 2024-03-30)
- [0344765] - Update CHANGELOG.md (Maki, 2024-03-30)
- [5c5e6ac] - Create get_git_log.py (Maki, 2024-03-30)
- [8d4a253] - Create CHANGELOG.md (Maki, 2024-03-30)
- [f26fca5] - Merge branch 'feature/modules' into develop (Maki, 2024-03-30)
- [36d6a4a] - 簡潔にまとめると、このコミットでは以下の変更が行われています:

- `SourceSage.py` ファイルの内容を大幅に変更
- `sys.path.append()` を使ってモジュールのパスを追加
- `pprint.pprint()` を使ってシステムパスをデバッグ出力
- `SourceSage` クラスのインスタンス化と `generate_markdown()` 呼び出しの際に、設定ファイルのパスを変更

これらの変更は、ソースコードの構造を改善し、モジュールの読み込みを正しく行うことを目的としています。これにより、ソースコードの可読性と保守性が向上します。 (Maki, 2024-03-30)
- [60ccecb] - Update SourceSage.md (Maki, 2024-03-30)
- [6796a56] - Create language_map.json (Maki, 2024-03-30)
- [d6e1af6] - Delete language_map.json (Maki, 2024-03-30)
- [01a3876] - Merge branch 'feature/code-block' into develop (Maki, 2024-03-30)
- [b42c67d] - ソースコード生成ツールの改善

- 言語ごとのシンタックスハイライト機能を追加しました
- 対象フォルダの指定やファイルの除外設定を複数行対応しました
- コード生成時のエラー処理を改善しました
- 設定ファイルの場所を外部化し、柔軟性を高めました

これらの変更により、ソースコード抽出時の表示が改善され、ツールの使い勝手が向上しました。 (Maki, 2024-03-30)
- [c5cbeff] - Update SourceSage.md (Maki, 2024-03-30)
- [0229075] - Update README.md (Maki, 2024-03-30)
- [a7e2de5] - Merge branch 'feature/ignore-file' into develop (Maki, 2024-03-30)
- [7c2fcc8] - Create SourceSage.md (Maki, 2024-03-30)
- [d900f91] - Configured GitLens AI settings to use Anthropic's Claude-3 model and generate commit messages in Japanese. (Maki, 2024-03-30)
- [067e1b2] - ソースコードをより効率的に組織化するために、次の変更を行いました:

1. 無視するファイルやフォルダをリスト化した `.SourceSageignore` ファイルを追加しました。これにより、不要なファイルやフォルダを自動的に除外できるようになりました。
2. `SourceSage.py` の `_is_excluded()` メソッドを改善し、 `.SourceSageignore` ファイルに記載された除外パターンに従って、ファイルとフォルダの除外処理を行うようにしました。
3. 不要なコメントを削除し、コードの可読性と保守性を向上させました。

これらの変更により、SourceSageツールの使いやすさが向上し、プロジェクトの管理がスムーズになるはずです。 (Maki, 2024-03-30)
- [79705b5] - Refactor README for SourceSage project

Consolidated project structure and content into a single markdown file, enabling easier understanding and analysis for AI language models. Excluded unnecessary files and directories, enhancing clarity. Updated usage instructions and examples to reflect changes. Also localized link to GitHub repository.

No references. (Maki, 2024-03-30)
- [1c6ebb6] - Refactor exclude patterns for SourceSage

Update exclude patterns to better reflect current project structure and exclude unnecessary files and folders. This change ensures accurate and efficient markdown generation. No associated issues addressed. (Maki, 2024-03-30)
- [a7c5a82] - Refactor output file name for clarity

Change the output file name to 'SourceSage.md' for improved clarity and consistency with the class name. This enhances code readability and maintainability. No associated issues. (Maki, 2024-03-30)
- [d656a61] - Update README.md (Maki, 2024-03-29)
- [bc31164] - Create SourceSage.py (Maki, 2024-03-29)
- [c749d9a] - Create SourceSage_icon6.png (Maki, 2024-03-29)
- [407ddbe] - Update README.md (Maki, 2024-03-29)
- [330b107] - Create SourceSage_icon5.png (Maki, 2024-03-29)
- [77eafaf] - Update README.md (Maki, 2024-03-29)
- [167e71e] - Create SourceSage_icon4.png (Maki, 2024-03-29)
- [3d69364] - Update README.md (Maki, 2024-03-29)
- [4828ab0] - Create SourceSage_icon3.png (Maki, 2024-03-29)
- [7ed0982] - Update README.md (Maki, 2024-03-29)
- [3f2bb6d] - Update README.md (Maki, 2024-03-29)
- [7b2c70f] - Create SourceSage_icon.png (Maki, 2024-03-29)
- [8a96c27] - Initial commit (Maki, 2024-03-29)

## feature/git-refactor

- [51e3612] - [refactor] SourceSage.pyのリファクタリング

## 変更内容

- 環境変数の読み込みと.envファイルの作成処理を`modules.EnvFileHandler`モジュールに移動
 - `create_env_file()`関数を`create_or_append_env_file()`関数に変更し、.envファイルがない場合は作成、ある場合は追記するように修正
- 不要なコメントを削除
- importの順序を調整
 - 標準ライブラリ、外部ライブラリ、自作モジュールの順にimport
- `if __name__ == "__main__":`の条件を追加

## リファクタリングの目的

- コードの可読性と保守性の向上
- 環境変数の読み込みと.envファイルの作成処理の責務を分離
- PEP8に準拠したコードスタイルの適用

これらの変更により、SourceSage.pyの構造が改善され、より理解しやすく保守しやすいコードになりました。 (Maki, 2024-03-31)
- [5538d65] - 「環境ファイルの自動生成機能を追加」

このコミットでは、SourceSage.pyにenv_file関数を追加し、.envファイルが存在しない場合に自動で作成するようにしました。これにより、SourceSageプロジェクトを新しく始める際に、手動でenv_fileを作成する必要がなくなりました。開発者の生産性が向上し、プロジェクト開始がスムーズになることが期待されます。 (Maki, 2024-03-31)
- [e769b1e] - ソース管理用の環境変数ファイルを追加  #2

この変更は、ソースコード管理を容易にするためのプロジェクト設定ファイルを追加するものです。環境変数ファイルには、リポジトリのパス、ソースファイルの場所、出力ファイル名などの重要な構成情報が含まれています。これにより、プロジェクト全体のファイル構造が明確になり、コードの移植性と再現性が向上します。 (Maki, 2024-03-31)
- [91e0f37] - dotenvモジュールのインポートエラーをキャッチし、エラーが発生してもデフォルト値を使用するように変更 (Maki, 2024-03-31)
- [06b64fe] - [feat] issue#2 SourceSage.pyのパラメータを環境変数(.env)から設定できるようにする

SourceSage.pyで使用しているパラメータを環境変数(.env)から設定できるように変更しました。

## 変更内容

- python-dotenvパッケージをインストールし、.envファイルから環境変数を読み込めるようにしました
- .envファイルをプロジェクトルートに作成し、以下のパラメータを定義しました
  - REPO_PATH
  - SOURCE_SAGE_ASSETS_DIR
  - CONFIG_DIR
  - DOCS_DIR
  - FOLDERS
  - IGNORE_FILE
  - OUTPUT_FILE
  - LANGUAGE_MAP_FILE
  - OWNER
  - REPOSITORY
  - ISSUES_FILE_NAME
- SourceSage.pyを変更し、上記のパラメータを環境変数から読み込むようにしました
  - os.getenv()を使用して環境変数の値を取得
  - FOLDERSはカンマ区切りの文字列をリストに変換

## 利点

- .envファイルを変更するだけで、簡単にパラメータを変更できるようになりました
- コードを変更することなくパラメータを設定できるため、メンテナンス性が向上しました
- 複数のフォルダを指定する場合も、.envファイルのFOLDERSをカンマ区切りで指定するだけで対応可能です

以上の変更により、issue#2の要件を満たすことができました。 (Maki, 2024-03-31)
- [277db10] - 開いているIssueのデータを保存し、フィルタリングした結果を別ファイルとして保存する機能を追加しました。これにより、開発者がIssueの状況を詳細に把握しやすくなり、プロジェクト管理が効率化されます。 (Maki, 2024-03-31)
- [0b4a102] - demo md (Maki, 2024-03-31)
- [56e5def] - リファクタリング: SourceSage.pyの変数名とフォルダ名を統一

- ソースコード内の重複するフォルダ名や変数を統一し、コードの可読性を向上
  - source_sage_assets_dirを"SourceSageAssets"とし、関連するパスで使用するように修正
  - config_dirを"config"とし、設定ファイルのパスで使用するように修正
  - docs_dirを"docs"とし、テンプレートファイルのパスで使用するように修正
- 変数名を一部変更し、より分かりやすい名前に修正
  - save_pathをsource_sage_assets_dirに変更
  - file_nameをissues_file_nameに変更
  - output_dirをchangelog_output_dirとissues_markdown_output_dirに分けて使用するように修正
- IssuesToMarkdownのインスタンス化時の引数を、他の部分と同様にf-stringを使用して指定するように修正
- これらの変更により、コードの一貫性と可読性が向上し、保守性が改善された (Maki, 2024-03-31)
- [784acce] - 機能: IssuesToMarkdownクラスにloguruを使用したログ出力を追加

- loguruをインポートして使用できるようにした
- load_data()メソッド内で、データのロード状況をログ出力するようにした
- create_markdown_files()メソッド内で、マークダウンファイルの作成状況をログ出力するようにした
- これにより、処理の進行状況や重要な情報がログに記録されるようになり、デバッグやモニタリングがしやすくなった (Maki, 2024-03-31)
- [248d49b] - 機能: IssuesToMarkdownクラスをSourceSage.pyに統合

- modules/IssuesToMarkdown.pyからIssuesToMarkdownクラスをインポート
- if __name__ == "__main__":ブロックの最後に、IssuesToMarkdownクラスのインスタンス化と実行のコードを追加
- これにより、SourceSage.pyを実行することで、他の処理と一緒にIssuesToMarkdownクラスの処理も実行されるようになった (Maki, 2024-03-31)
- [b0e6da7] - 機能: 出力フォルダを指定できるオプションを追加

- IssuesToMarkdownクラスの初期化時に出力フォルダを指定できるようにした
- create_markdown_filesメソッド内で、os.path.joinを使用して出力フォルダとファイル名を結合
- main部分で出力フォルダを指定できるようにした
- これにより、出力先を柔軟に設定できるようになった (Maki, 2024-03-31)
- [6a33080] - [refactor] Git関係のモジュールのリファクタリング

- GitHubIssueRetrieve.pyとStagedDiffGenerator.pyの重複部分を削除し、GitHubUtils.pyというモジュールにまとめました。
- ChangelogGenerator.pyとDiffChangelogGenerator.pyの共通部分をChangelogUtils.pyモジュールに抽出しました。
- StageInfoGenerator.py内の不要なimport文を削除し、モジュールのインポート方法を修正しました。
- SourceSage.py内のモジュールのインポート方法を修正し、不要なimport文を削除しました。
- モジュール間の依存関係を整理し、コードの可読性と保守性を向上させました。 (Maki, 2024-03-31)
- [7f0765c] - Merge branch 'feature/issues-to-resolve' into develop (Maki, 2024-03-31)
- [c773352] - [refactor] Git関連モジュールのリファクタリング

## 概要

- `DiffChangelogGenerator.py`と`ChangelogGenerator.py`に重複があったため、`ChangelogGenerator.py`に統合
- `ChangelogGenerator.py`の不要なメソッドを削除し、コードを整理
- `SourceSage.py`から不要なimportを削除

## 詳細

### `DiffChangelogGenerator.py`の統合

- `ChangelogGenerator.py`に`DiffChangelogGenerator.py`の機能を統合し、`DiffChangelogGenerator.py`を削除
- `ChangelogGenerator`クラスに以下のメソッドを追加
  - `generate_diff_changelog(self, branch='main', num_commits=2)`
  - `generate_git_tree(self, branch, num_commits)`
  - `write_commit_details(self, file, commits, index)`
  - `write_changed_files(self, file, commits, index)`
  - `write_file_diff(self, file, diff_item, commit, previous_commit)`
  - `write_diff_content(self, file, diff_item, commit, previous_commit, language, file_path)`
  - `escape_code_block(self, content, language)`

### `ChangelogGenerator.py`の整理

- 不要なメソッド`ensure_directory_exists(self, path)`を削除
- `generate_changelog_for_all_branches(self)`メソッド内の不要な出力を削除

### `SourceSage.py`の整理

- 不要なimport文を削除
  - `from modules.DiffChangelogGenerator import RepositoryChangelogGenerator`

## まとめ

Git関連モジュールのリファクタリングにより、コードの重複を解消し、可読性と保守性を向上させました。`ChangelogGenerator`クラスに機能を集約することで、モジュール構造がシンプルになりました。 (Maki, 2024-03-31)
- [ccec5c2] - [feat] SourceSage.pyの機能追加と改善

## 概要

SourceSage.pyに以下の機能を追加し、既存の機能を改善しました。

## 詳細

### 新機能

- GitHubのIssue情報を取得する`GitHubIssueRetriever`クラスを追加
- ステージングされた変更点の差分を生成する`StagedDiffGenerator`クラスを追加
- ステージング情報とIssue情報を統合してMarkdownファイルに出力する`StageInfoGenerator`クラスを追加

### 改善点

- 出力ファイルのパスを`SourceSageAseets`から`SourceSageAssets`に修正
- `ChangelogGenerator`クラスの出力ディレクトリを`SourceSageAseets/Changelog`から`SourceSageAssets/Changelog`に変更

### 処理の流れ

1. `SourceSage`クラスを使用してMarkdownファイルを生成
2. `ChangelogGenerator`クラスを使用してすべてのブランチのChangelogを生成し、統合
3. `GitHubIssueRetriever`クラスを使用してGitHubのIssue情報を取得し、JSONファイルに保存
4. `StagedDiffGenerator`クラスを使用してステージングされた変更点の差分を生成
5. `StageInfoGenerator`クラスを使用して、ステージング情報とIssue情報を統合し、テンプレートに基づいてMarkdownファイルに出力
  - Issue情報を含むMarkdownファイルを生成
  - Issue情報を含まないMarkdownファイルを生成

これらの機能追加と改善により、SourceSage.pyはより多くの情報を生成し、ユーザーにとって有用なものになりました。 (Maki, 2024-03-31)
- [3626c75] - Merge branch 'feature/get-issue' into develop (Maki, 2024-03-31)
- [42d6009] - [feat] コミットメッセージのフォーマットとタイプの説明を追加

## 変更内容

- コミットメッセージのフォーマットを追加
  - タイトルに種類と概要を記載
  - 本文に詳細な説明を記載（必要に応じて）
- コミットメッセージの種類の説明を追加
  - feat: 新機能
  - fix: バグ修正
  - docs: ドキュメントのみの変更
  - style: コードの動作に影響しない変更（空白、フォーマット、セミコロンの欠落など）
  - refactor: バグの修正も機能の追加も行わないコードの変更
  - perf: パフォーマンスを向上させるコードの変更
  - test: 欠けているテストの追加や既存のテストの修正
  - chore: ビルドプロセスやドキュメント生成などの補助ツールやライブラリの変更

## 変更ファイル

- docs/STAGE_INFO/STAGE_INFO_AND_ISSUES_TEMPLATE.md
- docs/STAGE_INFO/STAGE_INFO_TEMPLATE.md

上記のファイルにコミットメッセージのフォーマットとタイプの説明を追加しました。これにより、コミットメッセージの書き方がわかりやすくなり、統一性が保たれます。 (Maki, 2024-03-31)
- [cd44f62] - ソースコードの自動修正とコミットメッセージ生成の機能を追加

## 概要

- GitHubのオープンなissueを取得し、AIによる自動修正機能を追加
- ステージされた変更からAIが適切なコミットメッセージを生成する機能を実装
- プロジェクトの統合とドキュメント化のためのツールを提供

## 詳細

### 1. 課題の確認とAIによる自動修正

- `get_issues.py`を使用してGitHubのオープンなissueを取得し、JSONファイルに保存
- issueの内容と現在のソースコードの情報をClaude AIに入力し、自動でissueの修正を行う
  - `SourceSage.py`を使用して現在のプロジェクトのソースコードとファイル構成を1つのマークダウンファイルに統合
  - `get_issues.py`で取得したissueデータと`SourceSage.py`で生成したマークダウンをClaude AIに入力
  - AIがissueの内容を理解し、現在のソースコードを分析して自動的にissueの修正を提案
  - 提案された修正内容を確認し、必要に応じて手動で調整を行う

### 2. ステージされた変更の確認とコミットメッセージの自動生成

- `StagedDiffGenerator`クラスを使用してステージされた差分を取得し、マークダウンファイルに出力
- ステージされた変更とissueの情報をAIに入力し、適切なコミットメッセージを生成
  - `get_issues.py`で取得したissueデータと`StagedDiffGenerator`で生成したマークダウンをClaude AIに入力
  - AIが既存のissueを考慮してコミットメッセージを自動生成

### 3. プロジェクトの統合とドキュメント化

- `SourceSage.py`を使用してプロジェクト全体のソースコードとファイル構成をAIが理解しやすい形式で統合
  - プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイルにまとめる
  - 不要なファイルやディレクトリを除外するための設定が可能
  - 複数のプログラミング言語に対応し、シンタックスハイライト機能を提供
- Gitの変更履歴を自動生成し、ドキュメント化
  - ブランチごとに変更履歴をマークダウンファイルに出力
  - すべてのブランチの変更履歴を1つのファイルに統合

## その他の変更

- README.mdのアイコン画像のパスを修正
- タイムラインのサンプルを追加し、CSSでスタイリング
- 各種アイコン画像を追加
- `GitHubIssueRetrieve.py`、`StageInfoGenerator.py`、`StagedDiffGenerator.py`のモジュールを追加し、機能を実装

以上の変更により、ソースコードの自動修正とコミットメッセージ生成の機能が追加されました。また、プロジェクトの統合とドキュメント化のためのツールも提供されています。 (Maki, 2024-03-31)
- [2e5517e] - feat: タイムライン機能の追加とissueの解決

このコミットには以下の変更が含まれています:

- マークダウンにかっこいいタイムラインの図を追加 (resolves #5)
  - 魅力的なタイムラインを作成するためのCSSスタイルを実装
  - タイムライン機能を紹介するサンプルマークダウンファイルを提供

また、このコミットにはドキュメントの更新も含まれています:
- 新しいタイムライン機能を紹介するタイムラインサンプルマークダウンファイルを追加
- タイムラインの図をサポートするためにCSSスタイルを更新 (Maki, 2024-03-31)
- [0c0296b] - feat: ステージの差分生成と課題の取得を実装

Resolves #1, #3

このコミットには以下の変更が含まれています:

1. `demo/get_issues.py` を追加しました。これは、GitHub API を使用してリポジトリのオープンな課題を取得するPythonスクリプトです。スクリプトはプルリクエストを除外し、関連する課題データ（番号、タイトル、本文）をJSONファイルに保存します。

2. `modules/StagedDiffGenerator.py` に `StagedDiffGenerator` クラスを実装しました。このクラスは、リポジトリのステージされた変更を含むマークダウンファイル `STAGED_DIFF.md` を生成します。このクラスは `gitpython` ライブラリを使用してステージされた差分を取得し、ファイルパス、差分の内容、ファイル拡張子に基づいたコードブロックのエスケープを使用して出力をフォーマットします。

3. `.gitignore` ファイルを更新し、`SourceSageAssets` ディレクトリを含めるようにしました。

4. `gitpython` ライブラリを使用してステージされた差分を取得するデモスクリプト `demo/get_diff.py` を追加しました。

`StagedDiffGenerator` クラスは、ステージされた変更の読みやすい差分を生成する便利な方法を提供し、コミット前の変更内容の確認と理解を容易にします。`get_issues.py` スクリプトを使用すると、リポジトリのオープンな課題を簡単に取得できます。これはプロジェクトのタスクの追跡と管理に役立ちます。

これらの変更は、課題 #1 と #3 で概説されている要件に対応し、プロジェクトの機能性とユーザビリティを向上させます。 (Maki, 2024-03-31)
- [6ee000e] - Merge branch 'feature/git-log-filter' into develop (Maki, 2024-03-30)
- [eb47be6] - add demo md (Maki, 2024-03-30)
- [7d71c6c] - ファイル構造の改善とコードの可読性向上

- ファイル構造の整理と命名規則の適用により、コードのメンテナンス性と可読性が向上しました。
- ランゲージマッピング機能を拡張し、さまざまな言語のハイライトに対応しました。
- コミットログの表示機能を追加し、変更内容の把握が容易になりました。

これらの変更により、ソースコードの効率的な管理と理解が促進されます。開発プロセスの改善と開発者の生産性向上につながることが期待されます。 (Maki, 2024-03-30)
- [cb246b4] - Create README.md (Maki, 2024-03-30)
- [5e103c4] - Update .gitignore (Maki, 2024-03-30)
- [e4bc9db] - 主要な変更点を簡潔にまとめました:

- コミット表示数を5から30に増やし、メインブランチ('main')で確認するように変更
- ファイルパスを更新して、CHANGELOG_Diff.mdへの出力先を変更

この変更により、より包括的な変更履歴を確認できるようになりました。開発チームにとって有益な情報が得られるはずです。 (Maki, 2024-03-30)
- [bd84a1a] - Merge branch 'feature/git-diff' into develop (Maki, 2024-03-30)
- [a3f0970] - リポジトリの言語マッピングを更新し、コミットログの表示を改善しました。

- ファイル拡張子またはファイル名から適切な言語を自動判定するように変更しました。これにより、コード差分の表示が読みやすくなります。
- 新規追加ファイルや削除ファイルの内容を表示する際に、言語の構文によってコード表示を適切に整形するようにしました。
- ファイルパスが見つからない場合の処理を改善し、ユーザーにより分かりやすいメッセージを表示します。
- コミットログの表示が簡潔で分かりやすくなり、変更内容の理解がしやすくなりました。 (Maki, 2024-03-30)
- [c9b9f9e] - 日本語での簡潔なコミットメッセージは以下の通りです:

`CHANGELOG ファイルの場所を変更`

この変更は、既存の CHANGELOG ファイルの保存場所を "Changelog" ディレクトリから "SourceSageAseets" ディレクトリに変更するものです。この変更により、CHANGELOG ファイルがソースコードに関連したディレクトリ構造に含まれるようになり、プロジェクト全体の管理がより一貫性を持つようになります。 (Maki, 2024-03-30)
- [8bcd15b] - コミットメッセージ:

ファイルディフを自動でMD形式の変更履歴に生成するスクリプトを追加

開発ブランチ上の最新5件のコミットを要約し、変更されたファイルとその変更内容を Changelog/CHANGELOG_Diff.md に記録するツールを追加しました。これにより、プロジェクトの変更履歴を簡単に把握できるようになります。コミットハッシュ、作者、日時、コミットメッセージ、変更ファイル一覧と差分を自動で生成することで、ドキュメンテーションの手間を大幅に削減できます。 (Maki, 2024-03-30)
- [3269ed1] - リポジトリ構造の変更とドキュメントのための出力パスの更新

- ソースコード出力ファイルのパスを'docs/SourceSage.md'から'SourceSageAseets/SourceSage.md'に変更
- 変更履歴ファイルの出力パスを'docs/Changelog'から'SourceSageAseets/Changelog'に変更
- これらの変更により、ソースコードとドキュメントファイルの一元管理が容易になり、リポジトリの構造が明確になりました (Maki, 2024-03-30)
- [9f25863] - Delete DIFF_CHANGELOG_main.md (Maki, 2024-03-30)
- [2c47802] - Delete DIFF_CHANGELOG_integrated.md (Maki, 2024-03-30)
- [5267304] - Delete DIFF_CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [a9af521] - Delete DIFF_CHANGELOG_develop.md (Maki, 2024-03-30)
- [3b77e50] - Create DIFF_CHANGELOG_main.md (Maki, 2024-03-30)
- [94e0be2] - Create DIFF_CHANGELOG_integrated.md (Maki, 2024-03-30)
- [084b538] - Create DIFF_CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [a70e351] - Create DIFF_CHANGELOG_develop.md (Maki, 2024-03-30)
- [077ced5] - Update .gitignore (Maki, 2024-03-30)
- [58662d9] - SourceSage 2.0.0 リリース
- ChangelogGeneratorクラスを導入し、コードの可読性と保守性を向上
- 言語ごとのシンタックスハイライト機能を追加
- 対象フォルダやファイルの除外設定を複数行に対応
- コード生成時のエラー処理を改善
- 設定ファイルの場所を外部化し、柔軟性を高化
- .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動除外 (Maki, 2024-03-30)
- [3bb857a] - Update CHANGELOG_develop.md (Maki, 2024-03-30)
- [c210513] - Update CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [e43afbe] - Update CHANGELOG_integrated.md (Maki, 2024-03-30)
- [53a0682] - Update CHANGELOG_main.md (Maki, 2024-03-30)
- [6e36d50] - Update SourceSage.md (Maki, 2024-03-30)
- [327a4ce] - Update README.md (Maki, 2024-03-30)
- [664664e] - コミットメッセージ:

ChangelogGeneratorクラスを導入し、コードの可読性と保守性を向上しました。
シンタックスハイライトの機能を追加し、複数の言語に対応しました。
ファイル/フォルダの除外設定を改善し、柔軟性を向上させました。
設定ファイルの場所を外部化することで、全体的な設定の管理が容易になりました。
.SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外できるようにしました。
Gitの変更履歴を自動生成し、ドキュメント化する機能を追加しました。 (Maki, 2024-03-30)
- [2129f83] - Update SourceSage.md (Maki, 2024-03-30)
- [d8d53bf] - Update CHANGELOG_integrated.md (Maki, 2024-03-30)
- [4a079c6] - Update CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [f93f470] - Update CHANGELOG_develop.md (Maki, 2024-03-30)
- [c980f40] - Merge branch 'feature/add-git-logs' into develop (Maki, 2024-03-30)
- [c67b909] - ソースコードの忽視対象ファイルリストを更新し、変更履歴生成機能を追加

- .SourceSageignoreファイルに"Changelog"ディレクトリを除外対象に追加
- ソースコード解析結果の出力ディレクトリを"docs/SourceSage.md"に変更
- 変更履歴生成機能を追加し、"docs/Changelog"ディレクトリへの出力を実装

これにより、ソースコード解析結果と変更履歴をドキュメント化して管理できるようになり、開発プロセスの透明性と可視性が向上します。 (Maki, 2024-03-30)
- [5813fc7] - Create SourceSage.md (Maki, 2024-03-30)
- [f58eeaa] - Delete CHANGELOG.md (Maki, 2024-03-30)
- [67d8074] - Delete SourceSage.md (Maki, 2024-03-30)
- [c7489ce] - Delete get_git_log.py (Maki, 2024-03-30)
- [83f7c55] - Create CHANGELOG_main.md (Maki, 2024-03-30)
- [67c1538] - Create CHANGELOG_integrated.md (Maki, 2024-03-30)
- [0e1a13a] - Create CHANGELOG_HEAD.md (Maki, 2024-03-30)
- [17127ed] - Create CHANGELOG_features.md (Maki, 2024-03-30)
- [9a7739b] - Create CHANGELOG_develop.md (Maki, 2024-03-30)
- [c346a22] - 変更の目的を明確にし、ファイル名や具体的な変更箇所の記述は最小限に抑えた簡潔なコミットメッセージを以下のように作成しました:

"ChangelogGeneratorクラスの導入によりコードの可読性と保守性を向上"

このコミットでは、以下の主な変更が行われています:

- `get_repo()`, `get_commits()`, `format_commit()` の各機能をChangelogGeneratorクラスにまとめ、インスタンス化して使用するように変更
- クラス化することで、関数の再利用性や拡張性が向上し、コードの可読性と保守性が改善されました
- 使用方法も簡潔になり、main関数の呼び出しが明確になりました (Maki, 2024-03-30)
- [0344765] - Update CHANGELOG.md (Maki, 2024-03-30)
- [5c5e6ac] - Create get_git_log.py (Maki, 2024-03-30)
- [8d4a253] - Create CHANGELOG.md (Maki, 2024-03-30)
- [f26fca5] - Merge branch 'feature/modules' into develop (Maki, 2024-03-30)
- [36d6a4a] - 簡潔にまとめると、このコミットでは以下の変更が行われています:

- `SourceSage.py` ファイルの内容を大幅に変更
- `sys.path.append()` を使ってモジュールのパスを追加
- `pprint.pprint()` を使ってシステムパスをデバッグ出力
- `SourceSage` クラスのインスタンス化と `generate_markdown()` 呼び出しの際に、設定ファイルのパスを変更

これらの変更は、ソースコードの構造を改善し、モジュールの読み込みを正しく行うことを目的としています。これにより、ソースコードの可読性と保守性が向上します。 (Maki, 2024-03-30)
- [60ccecb] - Update SourceSage.md (Maki, 2024-03-30)
- [6796a56] - Create language_map.json (Maki, 2024-03-30)
- [d6e1af6] - Delete language_map.json (Maki, 2024-03-30)
- [01a3876] - Merge branch 'feature/code-block' into develop (Maki, 2024-03-30)
- [b42c67d] - ソースコード生成ツールの改善

- 言語ごとのシンタックスハイライト機能を追加しました
- 対象フォルダの指定やファイルの除外設定を複数行対応しました
- コード生成時のエラー処理を改善しました
- 設定ファイルの場所を外部化し、柔軟性を高めました

これらの変更により、ソースコード抽出時の表示が改善され、ツールの使い勝手が向上しました。 (Maki, 2024-03-30)
- [c5cbeff] - Update SourceSage.md (Maki, 2024-03-30)
- [0229075] - Update README.md (Maki, 2024-03-30)
- [a7e2de5] - Merge branch 'feature/ignore-file' into develop (Maki, 2024-03-30)
- [7c2fcc8] - Create SourceSage.md (Maki, 2024-03-30)
- [d900f91] - Configured GitLens AI settings to use Anthropic's Claude-3 model and generate commit messages in Japanese. (Maki, 2024-03-30)
- [067e1b2] - ソースコードをより効率的に組織化するために、次の変更を行いました:

1. 無視するファイルやフォルダをリスト化した `.SourceSageignore` ファイルを追加しました。これにより、不要なファイルやフォルダを自動的に除外できるようになりました。
2. `SourceSage.py` の `_is_excluded()` メソッドを改善し、 `.SourceSageignore` ファイルに記載された除外パターンに従って、ファイルとフォルダの除外処理を行うようにしました。
3. 不要なコメントを削除し、コードの可読性と保守性を向上させました。

これらの変更により、SourceSageツールの使いやすさが向上し、プロジェクトの管理がスムーズになるはずです。 (Maki, 2024-03-30)
- [79705b5] - Refactor README for SourceSage project

Consolidated project structure and content into a single markdown file, enabling easier understanding and analysis for AI language models. Excluded unnecessary files and directories, enhancing clarity. Updated usage instructions and examples to reflect changes. Also localized link to GitHub repository.

No references. (Maki, 2024-03-30)
- [1c6ebb6] - Refactor exclude patterns for SourceSage

Update exclude patterns to better reflect current project structure and exclude unnecessary files and folders. This change ensures accurate and efficient markdown generation. No associated issues addressed. (Maki, 2024-03-30)
- [a7c5a82] - Refactor output file name for clarity

Change the output file name to 'SourceSage.md' for improved clarity and consistency with the class name. This enhances code readability and maintainability. No associated issues. (Maki, 2024-03-30)
- [d656a61] - Update README.md (Maki, 2024-03-29)
- [bc31164] - Create SourceSage.py (Maki, 2024-03-29)
- [c749d9a] - Create SourceSage_icon6.png (Maki, 2024-03-29)
- [407ddbe] - Update README.md (Maki, 2024-03-29)
- [330b107] - Create SourceSage_icon5.png (Maki, 2024-03-29)
- [77eafaf] - Update README.md (Maki, 2024-03-29)
- [167e71e] - Create SourceSage_icon4.png (Maki, 2024-03-29)
- [3d69364] - Update README.md (Maki, 2024-03-29)
- [4828ab0] - Create SourceSage_icon3.png (Maki, 2024-03-29)
- [7ed0982] - Update README.md (Maki, 2024-03-29)
- [3f2bb6d] - Update README.md (Maki, 2024-03-29)
- [7b2c70f] - Create SourceSage_icon.png (Maki, 2024-03-29)
- [8a96c27] - Initial commit (Maki, 2024-03-29)

