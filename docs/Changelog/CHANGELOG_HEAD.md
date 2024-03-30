# Changelog

## HEAD

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
