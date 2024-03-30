# Changelog

## master

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
