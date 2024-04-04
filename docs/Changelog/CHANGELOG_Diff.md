```
Git Commit Log Tree:
├── a105923 - Merge branch 'release/2.0.0'
├── 327a4ce - Update README.md
├── 664664e - コミットメッセージ:
├── 2129f83 - Update SourceSage.md
├── d8d53bf - Update CHANGELOG_integrated.md
├── 4a079c6 - Update CHANGELOG_HEAD.md
├── f93f470 - Update CHANGELOG_develop.md
├── c980f40 - Merge branch 'feature/add-git-logs' into develop
├── c67b909 - ソースコードの忽視対象ファイルリストを更新し、変更履歴生成機能を追加
└── 5813fc7 - Create SourceSage.md
```


### コミットハッシュ: a1059...

- **作者**: Maki
- **日時**: 2024-03-30 18:50:48+09:00
- **メッセージ**: 

    Merge branch 'release/2.0.0'
    

#### 変更されたファイル:

### コミットハッシュ: 327a4...

- **作者**: Maki
- **日時**: 2024-03-30 18:49:35+09:00
- **メッセージ**: 

    Update README.md
    

#### 変更されたファイル:

- README.md
    - **差分:**

```diff
@@ -14,13 +14,13 @@ SourceSageは、プロジェクトのソースコードとファイル構成を
 
 ## 更新内容
 
-【2024/03/30】 ChangelogGenerator classを導入し、コードの可読性と保守性を向上
-【2024/03/30】 言語ごとのシンタックスハイライト機能を追加
-【2024/03/30】 対象フォルダの指定やファイルの除外設定を複数行対応
-【2024/03/30】 コード生成時のエラー処理を改善
-【2024/03/30】 設定ファイルの場所を外部化し、柔軟性を向上
-【2024/03/30】 .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外
-【2024/03/29】 初期リリース
+- 【2024/03/30】 ChangelogGenerator classを導入し、コードの可読性と保守性を向上
+- 【2024/03/30】 言語ごとのシンタックスハイライト機能を追加
+- 【2024/03/30】 対象フォルダの指定やファイルの除外設定を複数行対応
+- 【2024/03/30】 コード生成時のエラー処理を改善
+- 【2024/03/30】 設定ファイルの場所を外部化し、柔軟性を向上
+- 【2024/03/30】 .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外
+- 【2024/03/29】 初期リリース
 
 ## 特徴
 

```

### コミットハッシュ: 66466...

- **作者**: Maki
- **日時**: 2024-03-30 18:48:12+09:00
- **メッセージ**: 

    コミットメッセージ:
    
    ChangelogGeneratorクラスを導入し、コードの可読性と保守性を向上しました。
    シンタックスハイライトの機能を追加し、複数の言語に対応しました。
    ファイル/フォルダの除外設定を改善し、柔軟性を向上させました。
    設定ファイルの場所を外部化することで、全体的な設定の管理が容易になりました。
    .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外できるようにしました。
    Gitの変更履歴を自動生成し、ドキュメント化する機能を追加しました。
    

#### 変更されたファイル:

- README.md
    - **差分:**

````diff
@@ -12,43 +12,64 @@
 
 SourceSageは、プロジェクトのソースコードとファイル構成を単一のマークダウンファイルに統合するPythonスクリプトです。これにより、大規模言語モデル（AI）がプロジェクト全体の構造と内容を容易に理解できるようになります。
 
+## 更新内容
+
+【2024/03/30】 ChangelogGenerator classを導入し、コードの可読性と保守性を向上
+【2024/03/30】 言語ごとのシンタックスハイライト機能を追加
+【2024/03/30】 対象フォルダの指定やファイルの除外設定を複数行対応
+【2024/03/30】 コード生成時のエラー処理を改善
+【2024/03/30】 設定ファイルの場所を外部化し、柔軟性を向上
+【2024/03/30】 .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外
+【2024/03/29】 初期リリース
+
 ## 特徴
 
 - プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイルにまとめます
 - AIがプロジェクトの概要を素早く把握できる構造化された形式で出力します
 - 不要なファイルやディレクトリを除外する設定が可能です
 - プロジェクトの全体像を明確かつ読みやすい方法で提示します
+- 複数のプログラミング言語に対応し、シンタックスハイライト機能を提供します
+- 設定ファイルを外部化することで、柔軟性と保守性を向上させています
+- Gitの変更履歴を自動生成し、ドキュメント化することができます
 
 ## 使用方法
 
 プロジェクトでSourceSageを使用するには、次の手順に従います：
 
-1. `SourceSage.py`ファイルを、分析対象のプロジェクトのルートディレクトリにコピーします。
+1. `SourceSage.py`ファイルと`modules`フォルダを、分析対象のプロジェクトのルートディレクトリにコピーします。
+
+2. 必要に応じて、`.SourceSageignore`ファイルを作成し、除外したいファイルやフォルダのパターンを記述します。
 
-2. 必要に応じて、`SourceSage.py`内の以下の設定を変更します：
+3. `config/language_map.json`ファイルを編集し、必要なプログラミング言語とそれに対応するシンタックスハイライトの識別子を設定します。
+
+4. 必要に応じて、`SourceSage.py`内の以下の設定を変更します：
 
 ```python
 folders = ['./'] # 分析対象のディレクトリ（現在のディレクトリを指定）
-exclude_patterns = ['.git', '__pycache__', 'LICENSE', 'output.md', 'README.md', 'docs'] # 除外するファイル/フォルダのパターン 
-output_file = 'output.md' # 出力するマークダウンファイル名
+ignore_file = '.SourceSageignore' # 無視するファイル/フォルダのパターンを記述したファイル
+output_file = 'docs/SourceSage.md' # 出力するマークダウンファイル名
+language_map_file = 'config/language_map.json' # 言語マッピングの設定ファイル
 ```
 
-3. ターミナルまたはコマンドプロンプトで、プロジェクトのルートディレクトリに移動し、以下のコマンドを実行します：
+5. ターミナルまたはコマンドプロンプトで、プロジェクトのルートディレクトリに移動し、以下のコマンドを実行します：
 
 ```bash
 python SourceSage.py
 ```
 
-これにより、AIがプロジェクトの構造と内容を理解しやすい形式のマークダウンファイル（デフォルトでは `output.md`）が生成されます。
+これにより、AIがプロジェクトの構造と内容を理解しやすい形式のマークダウンファイル（デフォルトでは `docs/SourceSage.md`）が生成されます。また、Gitの変更履歴が`docs/Changelog`ディレクトリに自動生成されます。
 
 ## 出力例
 
 生成されるマークダウンファイルの例は次のようになります：
 
-```markdown
-# プロジェクト名: YourProjectName
+````markdown
+# Project: YourProjectName
+
+```plaintext
+OS: nt
+Directory: C:\Prj\YourProjectName
 
-## ディレクトリ構造
 ├─ src/
 │  ├─ main.py
 │  ├─ utils/
@@ -56,21 +77,86 @@ python SourceSage.py
 │  │  └─ constants.py
 │  └─ tests/
 │     └─ test_main.py
+├─ docs/
+│  └─ README.md
+├─ .gitignore
 └─ README.md
+```
+
+## src
 
-## ファイルの内容
+### main.py
 
-`src/main.py`
-'''python
+```python
 def main():
     print("Hello, World!")
 
 if __name__ == "__main__":
     main()
-'''
+```
+
+### utils
+
+#### helper.py
+
+```python
+def greet(name):
+    return f"Hello, {name}!"
+```
+
+#### constants.py
+
+```python 
+PI = 3.14159
+```
+
+...
+
+## docs
+
+### README.md
+
+```markdown
+# YourProjectName Documentation
+
+This is the documentation for YourProjectName.
 
 ...
 ```
+````
+
+## 変更履歴の統合
+
+SourceSageは、Gitリポジトリの変更履歴を自動的に生成し、ブランチごとにマークダウンファイルに出力します。さらに、すべてのブランチの変更履歴を1つのファイルに統合することができます。
+
+生成される変更履歴の例は次のようになります：
+
+````markdown
+# Integrated Changelog
+
+# Changelog
+
+## develop
+
+- [f26fca5] - Merge branch 'feature/modules' into develop (John Doe, 2023-03-30)
+- [36d6a4a] - Refactor SourceSage.py to use modules (John Doe, 2023-03-30)
+- [60ccecb] - Update SourceSage.md (John Doe, 2023-03-30)
+- [6796a56] - Create language_map.json (John Doe, 2023-03-30)
+- [d6e1af6] - Delete language_map.json (John Doe, 2023-03-30)
+
+...
+
+# Changelog - Features
+
+## feature/add-git-logs
+
+- [c346a22] - Introduce ChangelogGenerator class for improved readability and maintainability (Jane Smith, 2023-03-30)
+- [0344765] - Update CHANGELOG.md (Jane Smith, 2023-03-30)
+- [5c5e6ac] - Create get_git_log.py (Jane Smith, 2023-03-30)
+- [8d4a253] - Create CHANGELOG.md (Jane Smith, 2023-03-30)
+
+...
+````
 
 ## 貢献
 

````

### コミットハッシュ: 2129f...

- **作者**: Maki
- **日時**: 2024-03-30 18:48:00+09:00
- **メッセージ**: 

    Update SourceSage.md
    

#### 変更されたファイル:

- docs/SourceSage.md
    - **差分:**

````diff
@@ -1,6 +1,6 @@
 # Project: SourceSage
 
-```bash
+```plaintext
 OS: nt
 Directory: C:\Prj\SourceSage
 

````

### コミットハッシュ: d8d53...

- **作者**: Maki
- **日時**: 2024-03-30 18:47:57+09:00
- **メッセージ**: 

    Update CHANGELOG_integrated.md
    

#### 変更されたファイル:

- docs/Changelog/CHANGELOG_integrated.md
    - **差分:**

```diff
@@ -4,6 +4,340 @@
 
 ## develop
 
+- [c980f40] - Merge branch 'feature/add-git-logs' into develop (Maki, 2024-03-30)
+- [c67b909] - ソースコードの忽視対象ファイルリストを更新し、変更履歴生成機能を追加
+
+- .SourceSageignoreファイルに"Changelog"ディレクトリを除外対象に追加
+- ソースコード解析結果の出力ディレクトリを"docs/SourceSage.md"に変更
+- 変更履歴生成機能を追加し、"docs/Changelog"ディレクトリへの出力を実装
+
+これにより、ソースコード解析結果と変更履歴をドキュメント化して管理できるようになり、開発プロセスの透明性と可視性が向上します。 (Maki, 2024-03-30)
+- [5813fc7] - Create SourceSage.md (Maki, 2024-03-30)
+- [f58eeaa] - Delete CHANGELOG.md (Maki, 2024-03-30)
+- [67d8074] - Delete SourceSage.md (Maki, 2024-03-30)
+- [c7489ce] - Delete get_git_log.py (Maki, 2024-03-30)
+- [83f7c55] - Create CHANGELOG_main.md (Maki, 2024-03-30)
+- [67c1538] - Create CHANGELOG_integrated.md (Maki, 2024-03-30)
+- [0e1a13a] - Create CHANGELOG_HEAD.md (Maki, 2024-03-30)
+- [17127ed] - Create CHANGELOG_features.md (Maki, 2024-03-30)
+- [9a7739b] - Create CHANGELOG_develop.md (Maki, 2024-03-30)
+- [c346a22] - 変更の目的を明確にし、ファイル名や具体的な変更箇所の記述は最小限に抑えた簡潔なコミットメッセージを以下のように作成しました:
+
+"ChangelogGeneratorクラスの導入によりコードの可読性と保守性を向上"
+
+このコミットでは、以下の主な変更が行われています:
+
+- `get_repo()`, `get_commits()`, `format_commit()` の各機能をChangelogGeneratorクラスにまとめ、インスタンス化して使用するように変更
+- クラス化することで、関数の再利用性や拡張性が向上し、コードの可読性と保守性が改善されました
+- 使用方法も簡潔になり、main関数の呼び出しが明確になりました (Maki, 2024-03-30)
+- [0344765] - Update CHANGELOG.md (Maki, 2024-03-30)
+- [5c5e6ac] - Create get_git_log.py (Maki, 2024-03-30)
+- [8d4a253] - Create CHANGELOG.md (Maki, 2024-03-30)
+- [f26fca5] - Merge branch 'feature/modules' into develop (Maki, 2024-03-30)
+- [36d6a4a] - 簡潔にまとめると、このコミットでは以下の変更が行われています:
+
+- `SourceSage.py` ファイルの内容を大幅に変更
+- `sys.path.append()` を使ってモジュールのパスを追加
+- `pprint.pprint()` を使ってシステムパスをデバッグ出力
+- `SourceSage` クラスのインスタンス化と `generate_markdown()` 呼び出しの際に、設定ファイルのパスを変更
+
+これらの変更は、ソースコードの構造を改善し、モジュールの読み込みを正しく行うことを目的としています。これにより、ソースコードの可読性と保守性が向上します。 (Maki, 2024-03-30)
+- [60ccecb] - Update SourceSage.md (Maki, 2024-03-30)
+- [6796a56] - Create language_map.json (Maki, 2024-03-30)
+- [d6e1af6] - Delete language_map.json (Maki, 2024-03-30)
+- [01a3876] - Merge branch 'feature/code-block' into develop (Maki, 2024-03-30)
+- [b42c67d] - ソースコード生成ツールの改善
+
+- 言語ごとのシンタックスハイライト機能を追加しました
+- 対象フォルダの指定やファイルの除外設定を複数行対応しました
+- コード生成時のエラー処理を改善しました
+- 設定ファイルの場所を外部化し、柔軟性を高めました
+
+これらの変更により、ソースコード抽出時の表示が改善され、ツールの使い勝手が向上しました。 (Maki, 2024-03-30)
+- [c5cbeff] - Update SourceSage.md (Maki, 2024-03-30)
+- [0229075] - Update README.md (Maki, 2024-03-30)
+- [a7e2de5] - Merge branch 'feature/ignore-file' into develop (Maki, 2024-03-30)
+- [7c2fcc8] - Create SourceSage.md (Maki, 2024-03-30)
+- [d900f91] - Configured GitLens AI settings to use Anthropic's Claude-3 model and generate commit messages in Japanese. (Maki, 2024-03-30)
+- [067e1b2] - ソースコードをより効率的に組織化するために、次の変更を行いました:
+
+1. 無視するファイルやフォルダをリスト化した `.SourceSageignore` ファイルを追加しました。これにより、不要なファイルやフォルダを自動的に除外できるようになりました。
+2. `SourceSage.py` の `_is_excluded()` メソッドを改善し、 `.SourceSageignore` ファイルに記載された除外パターンに従って、ファイルとフォルダの除外処理を行うようにしました。
+3. 不要なコメントを削除し、コードの可読性と保守性を向上させました。
+
+これらの変更により、SourceSageツールの使いやすさが向上し、プロジェクトの管理がスムーズになるはずです。 (Maki, 2024-03-30)
+- [79705b5] - Refactor README for SourceSage project
+
+Consolidated project structure and content into a single markdown file, enabling easier understanding and analysis for AI language models. Excluded unnecessary files and directories, enhancing clarity. Updated usage instructions and examples to reflect changes. Also localized link to GitHub repository.
+
+No references. (Maki, 2024-03-30)
+- [1c6ebb6] - Refactor exclude patterns for SourceSage
+
+Update exclude patterns to better reflect current project structure and exclude unnecessary files and folders. This change ensures accurate and efficient markdown generation. No associated issues addressed. (Maki, 2024-03-30)
+- [a7c5a82] - Refactor output file name for clarity
+
+Change the output file name to 'SourceSage.md' for improved clarity and consistency with the class name. This enhances code readability and maintainability. No associated issues. (Maki, 2024-03-30)
+- [d656a61] - Update README.md (Maki, 2024-03-29)
+- [bc31164] - Create SourceSage.py (Maki, 2024-03-29)
+- [c749d9a] - Create SourceSage_icon6.png (Maki, 2024-03-29)
+- [407ddbe] - Update README.md (Maki, 2024-03-29)
+- [330b107] - Create SourceSage_icon5.png (Maki, 2024-03-29)
+- [77eafaf] - Update README.md (Maki, 2024-03-29)
+- [167e71e] - Create SourceSage_icon4.png (Maki, 2024-03-29)
+- [3d69364] - Update README.md (Maki, 2024-03-29)
+- [4828ab0] - Create SourceSage_icon3.png (Maki, 2024-03-29)
+- [7ed0982] - Update README.md (Maki, 2024-03-29)
+- [3f2bb6d] - Update README.md (Maki, 2024-03-29)
+- [7b2c70f] - Create SourceSage_icon.png (Maki, 2024-03-29)
+- [8a96c27] - Initial commit (Maki, 2024-03-29)
+
+
+# Changelog - Features
+
+## feature/add-git-logs
+
+- [c346a22] - 変更の目的を明確にし、ファイル名や具体的な変更箇所の記述は最小限に抑えた簡潔なコミットメッセージを以下のように作成しました:
+
+"ChangelogGeneratorクラスの導入によりコードの可読性と保守性を向上"
+
+このコミットでは、以下の主な変更が行われています:
+
+- `get_repo()`, `get_commits()`, `format_commit()` の各機能をChangelogGeneratorクラスにまとめ、インスタンス化して使用するように変更
+- クラス化することで、関数の再利用性や拡張性が向上し、コードの可読性と保守性が改善されました
+- 使用方法も簡潔になり、main関数の呼び出しが明確になりました (Maki, 2024-03-30)
+- [0344765] - Update CHANGELOG.md (Maki, 2024-03-30)
+- [5c5e6ac] - Create get_git_log.py (Maki, 2024-03-30)
+- [8d4a253] - Create CHANGELOG.md (Maki, 2024-03-30)
+- [f26fca5] - Merge branch 'feature/modules' into develop (Maki, 2024-03-30)
+- [36d6a4a] - 簡潔にまとめると、このコミットでは以下の変更が行われています:
+
+- `SourceSage.py` ファイルの内容を大幅に変更
+- `sys.path.append()` を使ってモジュールのパスを追加
+- `pprint.pprint()` を使ってシステムパスをデバッグ出力
+- `SourceSage` クラスのインスタンス化と `generate_markdown()` 呼び出しの際に、設定ファイルのパスを変更
+
+これらの変更は、ソースコードの構造を改善し、モジュールの読み込みを正しく行うことを目的としています。これにより、ソースコードの可読性と保守性が向上します。 (Maki, 2024-03-30)
+- [60ccecb] - Update SourceSage.md (Maki, 2024-03-30)
+- [6796a56] - Create language_map.json (Maki, 2024-03-30)
+- [d6e1af6] - Delete language_map.json (Maki, 2024-03-30)
+- [01a3876] - Merge branch 'feature/code-block' into develop (Maki, 2024-03-30)
+- [b42c67d] - ソースコード生成ツールの改善
+
+- 言語ごとのシンタックスハイライト機能を追加しました
+- 対象フォルダの指定やファイルの除外設定を複数行対応しました
+- コード生成時のエラー処理を改善しました
+- 設定ファイルの場所を外部化し、柔軟性を高めました
+
+これらの変更により、ソースコード抽出時の表示が改善され、ツールの使い勝手が向上しました。 (Maki, 2024-03-30)
+- [c5cbeff] - Update SourceSage.md (Maki, 2024-03-30)
+- [0229075] - Update README.md (Maki, 2024-03-30)
+- [a7e2de5] - Merge branch 'feature/ignore-file' into develop (Maki, 2024-03-30)
+- [7c2fcc8] - Create SourceSage.md (Maki, 2024-03-30)
+- [d900f91] - Configured GitLens AI settings to use Anthropic's Claude-3 model and generate commit messages in Japanese. (Maki, 2024-03-30)
+- [067e1b2] - ソースコードをより効率的に組織化するために、次の変更を行いました:
+
+1. 無視するファイルやフォルダをリスト化した `.SourceSageignore` ファイルを追加しました。これにより、不要なファイルやフォルダを自動的に除外できるようになりました。
+2. `SourceSage.py` の `_is_excluded()` メソッドを改善し、 `.SourceSageignore` ファイルに記載された除外パターンに従って、ファイルとフォルダの除外処理を行うようにしました。
+3. 不要なコメントを削除し、コードの可読性と保守性を向上させました。
+
+これらの変更により、SourceSageツールの使いやすさが向上し、プロジェクトの管理がスムーズになるはずです。 (Maki, 2024-03-30)
+- [79705b5] - Refactor README for SourceSage project
+
+Consolidated project structure and content into a single markdown file, enabling easier understanding and analysis for AI language models. Excluded unnecessary files and directories, enhancing clarity. Updated usage instructions and examples to reflect changes. Also localized link to GitHub repository.
+
+No references. (Maki, 2024-03-30)
+- [1c6ebb6] - Refactor exclude patterns for SourceSage
+
+Update exclude patterns to better reflect current project structure and exclude unnecessary files and folders. This change ensures accurate and efficient markdown generation. No associated issues addressed. (Maki, 2024-03-30)
+- [a7c5a82] - Refactor output file name for clarity
+
+Change the output file name to 'SourceSage.md' for improved clarity and consistency with the class name. This enhances code readability and maintainability. No associated issues. (Maki, 2024-03-30)
+- [d656a61] - Update README.md (Maki, 2024-03-29)
+- [bc31164] - Create SourceSage.py (Maki, 2024-03-29)
+- [c749d9a] - Create SourceSage_icon6.png (Maki, 2024-03-29)
+- [407ddbe] - Update README.md (Maki, 2024-03-29)
+- [330b107] - Create SourceSage_icon5.png (Maki, 2024-03-29)
+- [77eafaf] - Update README.md (Maki, 2024-03-29)
+- [167e71e] - Create SourceSage_icon4.png (Maki, 2024-03-29)
+- [3d69364] - Update README.md (Maki, 2024-03-29)
+- [4828ab0] - Create SourceSage_icon3.png (Maki, 2024-03-29)
+- [7ed0982] - Update README.md (Maki, 2024-03-29)
+- [3f2bb6d] - Update README.md (Maki, 2024-03-29)
+- [7b2c70f] - Create SourceSage_icon.png (Maki, 2024-03-29)
+- [8a96c27] - Initial commit (Maki, 2024-03-29)
+
+## feature/add-git-logs
+
+- [c346a22] - 変更の目的を明確にし、ファイル名や具体的な変更箇所の記述は最小限に抑えた簡潔なコミットメッセージを以下のように作成しました:
+
+"ChangelogGeneratorクラスの導入によりコードの可読性と保守性を向上"
+
+このコミットでは、以下の主な変更が行われています:
+
+- `get_repo()`, `get_commits()`, `format_commit()` の各機能をChangelogGeneratorクラスにまとめ、インスタンス化して使用するように変更
+- クラス化することで、関数の再利用性や拡張性が向上し、コードの可読性と保守性が改善されました
+- 使用方法も簡潔になり、main関数の呼び出しが明確になりました (Maki, 2024-03-30)
+- [0344765] - Update CHANGELOG.md (Maki, 2024-03-30)
+- [5c5e6ac] - Create get_git_log.py (Maki, 2024-03-30)
+- [8d4a253] - Create CHANGELOG.md (Maki, 2024-03-30)
+- [f26fca5] - Merge branch 'feature/modules' into develop (Maki, 2024-03-30)
+- [36d6a4a] - 簡潔にまとめると、このコミットでは以下の変更が行われています:
+
+- `SourceSage.py` ファイルの内容を大幅に変更
+- `sys.path.append()` を使ってモジュールのパスを追加
+- `pprint.pprint()` を使ってシステムパスをデバッグ出力
+- `SourceSage` クラスのインスタンス化と `generate_markdown()` 呼び出しの際に、設定ファイルのパスを変更
+
+これらの変更は、ソースコードの構造を改善し、モジュールの読み込みを正しく行うことを目的としています。これにより、ソースコードの可読性と保守性が向上します。 (Maki, 2024-03-30)
+- [60ccecb] - Update SourceSage.md (Maki, 2024-03-30)
+- [6796a56] - Create language_map.json (Maki, 2024-03-30)
+- [d6e1af6] - Delete language_map.json (Maki, 2024-03-30)
+- [01a3876] - Merge branch 'feature/code-block' into develop (Maki, 2024-03-30)
+- [b42c67d] - ソースコード生成ツールの改善
+
+- 言語ごとのシンタックスハイライト機能を追加しました
+- 対象フォルダの指定やファイルの除外設定を複数行対応しました
+- コード生成時のエラー処理を改善しました
+- 設定ファイルの場所を外部化し、柔軟性を高めました
+
+これらの変更により、ソースコード抽出時の表示が改善され、ツールの使い勝手が向上しました。 (Maki, 2024-03-30)
+- [c5cbeff] - Update SourceSage.md (Maki, 2024-03-30)
+- [0229075] - Update README.md (Maki, 2024-03-30)
+- [a7e2de5] - Merge branch 'feature/ignore-file' into develop (Maki, 2024-03-30)
+- [7c2fcc8] - Create SourceSage.md (Maki, 2024-03-30)
+- [d900f91] - Configured GitLens AI settings to use Anthropic's Claude-3 model and generate commit messages in Japanese. (Maki, 2024-03-30)
+- [067e1b2] - ソースコードをより効率的に組織化するために、次の変更を行いました:
+
+1. 無視するファイルやフォルダをリスト化した `.SourceSageignore` ファイルを追加しました。これにより、不要なファイルやフォルダを自動的に除外できるようになりました。
+2. `SourceSage.py` の `_is_excluded()` メソッドを改善し、 `.SourceSageignore` ファイルに記載された除外パターンに従って、ファイルとフォルダの除外処理を行うようにしました。
+3. 不要なコメントを削除し、コードの可読性と保守性を向上させました。
+
+これらの変更により、SourceSageツールの使いやすさが向上し、プロジェクトの管理がスムーズになるはずです。 (Maki, 2024-03-30)
+- [79705b5] - Refactor README for SourceSage project
+
+Consolidated project structure and content into a single markdown file, enabling easier understanding and analysis for AI language models. Excluded unnecessary files and directories, enhancing clarity. Updated usage instructions and examples to reflect changes. Also localized link to GitHub repository.
+
+No references. (Maki, 2024-03-30)
+- [1c6ebb6] - Refactor exclude patterns for SourceSage
+
+Update exclude patterns to better reflect current project structure and exclude unnecessary files and folders. This change ensures accurate and efficient markdown generation. No associated issues addressed. (Maki, 2024-03-30)
+- [a7c5a82] - Refactor output file name for clarity
+
+Change the output file name to 'SourceSage.md' for improved clarity and consistency with the class name. This enhances code readability and maintainability. No associated issues. (Maki, 2024-03-30)
+- [d656a61] - Update README.md (Maki, 2024-03-29)
+- [bc31164] - Create SourceSage.py (Maki, 2024-03-29)
+- [c749d9a] - Create SourceSage_icon6.png (Maki, 2024-03-29)
+- [407ddbe] - Update README.md (Maki, 2024-03-29)
+- [330b107] - Create SourceSage_icon5.png (Maki, 2024-03-29)
+- [77eafaf] - Update README.md (Maki, 2024-03-29)
+- [167e71e] - Create SourceSage_icon4.png (Maki, 2024-03-29)
+- [3d69364] - Update README.md (Maki, 2024-03-29)
+- [4828ab0] - Create SourceSage_icon3.png (Maki, 2024-03-29)
+- [7ed0982] - Update README.md (Maki, 2024-03-29)
+- [3f2bb6d] - Update README.md (Maki, 2024-03-29)
+- [7b2c70f] - Create SourceSage_icon.png (Maki, 2024-03-29)
+- [8a96c27] - Initial commit (Maki, 2024-03-29)
+
+
+
+# Changelog
+
+## HEAD
+
+- [c980f40] - Merge branch 'feature/add-git-logs' into develop (Maki, 2024-03-30)
+- [c67b909] - ソースコードの忽視対象ファイルリストを更新し、変更履歴生成機能を追加
+
+- .SourceSageignoreファイルに"Changelog"ディレクトリを除外対象に追加
+- ソースコード解析結果の出力ディレクトリを"docs/SourceSage.md"に変更
+- 変更履歴生成機能を追加し、"docs/Changelog"ディレクトリへの出力を実装
+
+これにより、ソースコード解析結果と変更履歴をドキュメント化して管理できるようになり、開発プロセスの透明性と可視性が向上します。 (Maki, 2024-03-30)
+- [5813fc7] - Create SourceSage.md (Maki, 2024-03-30)
+- [f58eeaa] - Delete CHANGELOG.md (Maki, 2024-03-30)
+- [67d8074] - Delete SourceSage.md (Maki, 2024-03-30)
+- [c7489ce] - Delete get_git_log.py (Maki, 2024-03-30)
+- [83f7c55] - Create CHANGELOG_main.md (Maki, 2024-03-30)
+- [67c1538] - Create CHANGELOG_integrated.md (Maki, 2024-03-30)
+- [0e1a13a] - Create CHANGELOG_HEAD.md (Maki, 2024-03-30)
+- [17127ed] - Create CHANGELOG_features.md (Maki, 2024-03-30)
+- [9a7739b] - Create CHANGELOG_develop.md (Maki, 2024-03-30)
+- [c346a22] - 変更の目的を明確にし、ファイル名や具体的な変更箇所の記述は最小限に抑えた簡潔なコミットメッセージを以下のように作成しました:
+
+"ChangelogGeneratorクラスの導入によりコードの可読性と保守性を向上"
+
+このコミットでは、以下の主な変更が行われています:
+
+- `get_repo()`, `get_commits()`, `format_commit()` の各機能をChangelogGeneratorクラスにまとめ、インスタンス化して使用するように変更
+- クラス化することで、関数の再利用性や拡張性が向上し、コードの可読性と保守性が改善されました
+- 使用方法も簡潔になり、main関数の呼び出しが明確になりました (Maki, 2024-03-30)
+- [0344765] - Update CHANGELOG.md (Maki, 2024-03-30)
+- [5c5e6ac] - Create get_git_log.py (Maki, 2024-03-30)
+- [8d4a253] - Create CHANGELOG.md (Maki, 2024-03-30)
+- [f26fca5] - Merge branch 'feature/modules' into develop (Maki, 2024-03-30)
+- [36d6a4a] - 簡潔にまとめると、このコミットでは以下の変更が行われています:
+
+- `SourceSage.py` ファイルの内容を大幅に変更
+- `sys.path.append()` を使ってモジュールのパスを追加
+- `pprint.pprint()` を使ってシステムパスをデバッグ出力
+- `SourceSage` クラスのインスタンス化と `generate_markdown()` 呼び出しの際に、設定ファイルのパスを変更
+
+これらの変更は、ソースコードの構造を改善し、モジュールの読み込みを正しく行うことを目的としています。これにより、ソースコードの可読性と保守性が向上します。 (Maki, 2024-03-30)
+- [60ccecb] - Update SourceSage.md (Maki, 2024-03-30)
+- [6796a56] - Create language_map.json (Maki, 2024-03-30)
+- [d6e1af6] - Delete language_map.json (Maki, 2024-03-30)
+- [01a3876] - Merge branch 'feature/code-block' into develop (Maki, 2024-03-30)
+- [b42c67d] - ソースコード生成ツールの改善
+
+- 言語ごとのシンタックスハイライト機能を追加しました
+- 対象フォルダの指定やファイルの除外設定を複数行対応しました
+- コード生成時のエラー処理を改善しました
+- 設定ファイルの場所を外部化し、柔軟性を高めました
+
+これらの変更により、ソースコード抽出時の表示が改善され、ツールの使い勝手が向上しました。 (Maki, 2024-03-30)
+- [c5cbeff] - Update SourceSage.md (Maki, 2024-03-30)
+- [0229075] - Update README.md (Maki, 2024-03-30)
+- [a7e2de5] - Merge branch 'feature/ignore-file' into develop (Maki, 2024-03-30)
+- [7c2fcc8] - Create SourceSage.md (Maki, 2024-03-30)
+- [d900f91] - Configured GitLens AI settings to use Anthropic's Claude-3 model and generate commit messages in Japanese. (Maki, 2024-03-30)
+- [067e1b2] - ソースコードをより効率的に組織化するために、次の変更を行いました:
+
+1. 無視するファイルやフォルダをリスト化した `.SourceSageignore` ファイルを追加しました。これにより、不要なファイルやフォルダを自動的に除外できるようになりました。
+2. `SourceSage.py` の `_is_excluded()` メソッドを改善し、 `.SourceSageignore` ファイルに記載された除外パターンに従って、ファイルとフォルダの除外処理を行うようにしました。
+3. 不要なコメントを削除し、コードの可読性と保守性を向上させました。
+
+これらの変更により、SourceSageツールの使いやすさが向上し、プロジェクトの管理がスムーズになるはずです。 (Maki, 2024-03-30)
+- [79705b5] - Refactor README for SourceSage project
+
+Consolidated project structure and content into a single markdown file, enabling easier understanding and analysis for AI language models. Excluded unnecessary files and directories, enhancing clarity. Updated usage instructions and examples to reflect changes. Also localized link to GitHub repository.
+
+No references. (Maki, 2024-03-30)
+- [1c6ebb6] - Refactor exclude patterns for SourceSage
+
+Update exclude patterns to better reflect current project structure and exclude unnecessary files and folders. This change ensures accurate and efficient markdown generation. No associated issues addressed. (Maki, 2024-03-30)
+- [a7c5a82] - Refactor output file name for clarity
+
+Change the output file name to 'SourceSage.md' for improved clarity and consistency with the class name. This enhances code readability and maintainability. No associated issues. (Maki, 2024-03-30)
+- [d656a61] - Update README.md (Maki, 2024-03-29)
+- [bc31164] - Create SourceSage.py (Maki, 2024-03-29)
+- [c749d9a] - Create SourceSage_icon6.png (Maki, 2024-03-29)
+- [407ddbe] - Update README.md (Maki, 2024-03-29)
+- [330b107] - Create SourceSage_icon5.png (Maki, 2024-03-29)
+- [77eafaf] - Update README.md (Maki, 2024-03-29)
+- [167e71e] - Create SourceSage_icon4.png (Maki, 2024-03-29)
+- [3d69364] - Update README.md (Maki, 2024-03-29)
+- [4828ab0] - Create SourceSage_icon3.png (Maki, 2024-03-29)
+- [7ed0982] - Update README.md (Maki, 2024-03-29)
+- [3f2bb6d] - Update README.md (Maki, 2024-03-29)
+- [7b2c70f] - Create SourceSage_icon.png (Maki, 2024-03-29)
+- [8a96c27] - Initial commit (Maki, 2024-03-29)
+
+
+# Integrated Changelog
+
+# Changelog
+
+## develop
+
 - [f26fca5] - Merge branch 'feature/modules' into develop (Maki, 2024-03-30)
 - [36d6a4a] - 簡潔にまとめると、このコミットでは以下の変更が行われています:
 
@@ -1246,6 +1580,38 @@ Change the output file name to 'SourceSage.md' for improved clarity and consiste
 
 
 
+# Changelog
+
+## main
+
+- [79705b5] - Refactor README for SourceSage project
+
+Consolidated project structure and content into a single markdown file, enabling easier understanding and analysis for AI language models. Excluded unnecessary files and directories, enhancing clarity. Updated usage instructions and examples to reflect changes. Also localized link to GitHub repository.
+
+No references. (Maki, 2024-03-30)
+- [1c6ebb6] - Refactor exclude patterns for SourceSage
+
+Update exclude patterns to better reflect current project structure and exclude unnecessary files and folders. This change ensures accurate and efficient markdown generation. No associated issues addressed. (Maki, 2024-03-30)
+- [a7c5a82] - Refactor output file name for clarity
+
+Change the output file name to 'SourceSage.md' for improved clarity and consistency with the class name. This enhances code readability and maintainability. No associated issues. (Maki, 2024-03-30)
+- [d656a61] - Update README.md (Maki, 2024-03-29)
+- [bc31164] - Create SourceSage.py (Maki, 2024-03-29)
+- [c749d9a] - Create SourceSage_icon6.png (Maki, 2024-03-29)
+- [407ddbe] - Update README.md (Maki, 2024-03-29)
+- [330b107] - Create SourceSage_icon5.png (Maki, 2024-03-29)
+- [77eafaf] - Update README.md (Maki, 2024-03-29)
+- [167e71e] - Create SourceSage_icon4.png (Maki, 2024-03-29)
+- [3d69364] - Update README.md (Maki, 2024-03-29)
+- [4828ab0] - Create SourceSage_icon3.png (Maki, 2024-03-29)
+- [7ed0982] - Update README.md (Maki, 2024-03-29)
+- [3f2bb6d] - Update README.md (Maki, 2024-03-29)
+- [7b2c70f] - Create SourceSage_icon.png (Maki, 2024-03-29)
+- [8a96c27] - Initial commit (Maki, 2024-03-29)
+
+
+
+
 # Changelog
 
 ## main

```

### コミットハッシュ: 4a079...

- **作者**: Maki
- **日時**: 2024-03-30 18:47:55+09:00
- **メッセージ**: 

    Update CHANGELOG_HEAD.md
    

#### 変更されたファイル:

- docs/Changelog/CHANGELOG_HEAD.md
    - **差分:**

```diff
@@ -2,6 +2,23 @@
 
 ## HEAD
 
+- [c980f40] - Merge branch 'feature/add-git-logs' into develop (Maki, 2024-03-30)
+- [c67b909] - ソースコードの忽視対象ファイルリストを更新し、変更履歴生成機能を追加
+
+- .SourceSageignoreファイルに"Changelog"ディレクトリを除外対象に追加
+- ソースコード解析結果の出力ディレクトリを"docs/SourceSage.md"に変更
+- 変更履歴生成機能を追加し、"docs/Changelog"ディレクトリへの出力を実装
+
+これにより、ソースコード解析結果と変更履歴をドキュメント化して管理できるようになり、開発プロセスの透明性と可視性が向上します。 (Maki, 2024-03-30)
+- [5813fc7] - Create SourceSage.md (Maki, 2024-03-30)
+- [f58eeaa] - Delete CHANGELOG.md (Maki, 2024-03-30)
+- [67d8074] - Delete SourceSage.md (Maki, 2024-03-30)
+- [c7489ce] - Delete get_git_log.py (Maki, 2024-03-30)
+- [83f7c55] - Create CHANGELOG_main.md (Maki, 2024-03-30)
+- [67c1538] - Create CHANGELOG_integrated.md (Maki, 2024-03-30)
+- [0e1a13a] - Create CHANGELOG_HEAD.md (Maki, 2024-03-30)
+- [17127ed] - Create CHANGELOG_features.md (Maki, 2024-03-30)
+- [9a7739b] - Create CHANGELOG_develop.md (Maki, 2024-03-30)
 - [c346a22] - 変更の目的を明確にし、ファイル名や具体的な変更箇所の記述は最小限に抑えた簡潔なコミットメッセージを以下のように作成しました:
 
 "ChangelogGeneratorクラスの導入によりコードの可読性と保守性を向上"

```

### コミットハッシュ: f93f4...

- **作者**: Maki
- **日時**: 2024-03-30 18:47:53+09:00
- **メッセージ**: 

    Update CHANGELOG_develop.md
    

#### 変更されたファイル:

- docs/Changelog/CHANGELOG_develop.md
    - **差分:**

```diff
@@ -2,6 +2,35 @@
 
 ## develop
 
+- [c980f40] - Merge branch 'feature/add-git-logs' into develop (Maki, 2024-03-30)
+- [c67b909] - ソースコードの忽視対象ファイルリストを更新し、変更履歴生成機能を追加
+
+- .SourceSageignoreファイルに"Changelog"ディレクトリを除外対象に追加
+- ソースコード解析結果の出力ディレクトリを"docs/SourceSage.md"に変更
+- 変更履歴生成機能を追加し、"docs/Changelog"ディレクトリへの出力を実装
+
+これにより、ソースコード解析結果と変更履歴をドキュメント化して管理できるようになり、開発プロセスの透明性と可視性が向上します。 (Maki, 2024-03-30)
+- [5813fc7] - Create SourceSage.md (Maki, 2024-03-30)
+- [f58eeaa] - Delete CHANGELOG.md (Maki, 2024-03-30)
+- [67d8074] - Delete SourceSage.md (Maki, 2024-03-30)
+- [c7489ce] - Delete get_git_log.py (Maki, 2024-03-30)
+- [83f7c55] - Create CHANGELOG_main.md (Maki, 2024-03-30)
+- [67c1538] - Create CHANGELOG_integrated.md (Maki, 2024-03-30)
+- [0e1a13a] - Create CHANGELOG_HEAD.md (Maki, 2024-03-30)
+- [17127ed] - Create CHANGELOG_features.md (Maki, 2024-03-30)
+- [9a7739b] - Create CHANGELOG_develop.md (Maki, 2024-03-30)
+- [c346a22] - 変更の目的を明確にし、ファイル名や具体的な変更箇所の記述は最小限に抑えた簡潔なコミットメッセージを以下のように作成しました:
+
+"ChangelogGeneratorクラスの導入によりコードの可読性と保守性を向上"
+
+このコミットでは、以下の主な変更が行われています:
+
+- `get_repo()`, `get_commits()`, `format_commit()` の各機能をChangelogGeneratorクラスにまとめ、インスタンス化して使用するように変更
+- クラス化することで、関数の再利用性や拡張性が向上し、コードの可読性と保守性が改善されました
+- 使用方法も簡潔になり、main関数の呼び出しが明確になりました (Maki, 2024-03-30)
+- [0344765] - Update CHANGELOG.md (Maki, 2024-03-30)
+- [5c5e6ac] - Create get_git_log.py (Maki, 2024-03-30)
+- [8d4a253] - Create CHANGELOG.md (Maki, 2024-03-30)
 - [f26fca5] - Merge branch 'feature/modules' into develop (Maki, 2024-03-30)
 - [36d6a4a] - 簡潔にまとめると、このコミットでは以下の変更が行われています:
 

```

### コミットハッシュ: c980f...

- **作者**: Maki
- **日時**: 2024-03-30 18:41:59+09:00
- **メッセージ**: 

    Merge branch 'feature/add-git-logs' into develop
    

#### 変更されたファイル:

### コミットハッシュ: c67b9...

- **作者**: Maki
- **日時**: 2024-03-30 18:41:13+09:00
- **メッセージ**: 

    ソースコードの忽視対象ファイルリストを更新し、変更履歴生成機能を追加
    
    - .SourceSageignoreファイルに"Changelog"ディレクトリを除外対象に追加
    - ソースコード解析結果の出力ディレクトリを"docs/SourceSage.md"に変更
    - 変更履歴生成機能を追加し、"docs/Changelog"ディレクトリへの出力を実装
    
    これにより、ソースコード解析結果と変更履歴をドキュメント化して管理できるようになり、開発プロセスの透明性と可視性が向上します。
    

#### 変更されたファイル:

- .SourceSageignore
    - **差分:**

```diff
@@ -11,4 +11,5 @@ data
 SourceSage
 .gitignore
 .SourceSageignore
-*.png
\ No newline at end of file
+*.png
+Changelog
\ No newline at end of file

```

- SourceSage.py
    - **差分:**

```diff
@@ -8,10 +8,20 @@ sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
 pprint.pprint(sys.path)
 
 from modules.source_sage import SourceSage
+from modules.ChangelogGenerator import ChangelogGenerator
 
 if __name__ == "__main__":
     folders = ['./']
     source_sage = SourceSage(folders, ignore_file='.SourceSageignore',
-                             output_file='SourceSage.md',
+                             output_file='docs/SourceSage.md',
                              language_map_file='config/language_map.json')
-    source_sage.generate_markdown()
\ No newline at end of file
+    source_sage.generate_markdown()
+
+
+    repo_path = "./"
+    output_dir = "docs/Changelog"
+    os.makedirs(output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する
+
+    generator = ChangelogGenerator(repo_path, output_dir)
+    generator.generate_changelog_for_all_branches()
+    generator.integrate_changelogs()
\ No newline at end of file

```

- modules/ChangelogGenerator.py
    - **追加された内容:**

```python
import os
from git import Repo
from datetime import datetime
from loguru import logger

class ChangelogGenerator:
    def __init__(self, repo_path, output_dir):
        self.repo_path = repo_path
        self.output_dir = output_dir
        self.repo = self._get_repo()

    def _get_repo(self):
        return Repo(self.repo_path)

    def _get_commits(self, branch):
        return list(self.repo.iter_commits(branch))

    def _format_commit(self, commit):
        message = commit.message.strip()
        sha = commit.hexsha[:7]
        author = commit.author.name
        date = datetime.fromtimestamp(commit.committed_date).strftime("%Y-%m-%d")
        return f"- [{sha}] - {message} ({author}, {date})"

    def generate_changelog(self, branch, output_file):
        commits = self._get_commits(branch)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Changelog\n\n")
            f.write(f"## {branch}\n\n")

            for commit in commits:
                formatted_commit = self._format_commit(commit)
                f.write(formatted_commit + "\n")

        logger.info(f"Changelog generated successfully for branch '{branch}' at {output_file}")

    def generate_changelog_for_all_branches(self):
        local_branches = [ref.name for ref in self.repo.branches]
        remote_branches = [ref.name for ref in self.repo.remote().refs]

        branches = local_branches + remote_branches
        print(branches)

        feature_branches = [branch for branch in branches if 'feature/' in branch]
        other_branches = [branch for branch in branches if 'feature/' not in branch]

        for branch in other_branches:
            branch_name = branch.replace('origin/', '')
            output_file = os.path.join(self.output_dir, f"CHANGELOG_{branch_name}.md")
            logger.info(f"Generating changelog for branch '{branch_name}'...")
            self.generate_changelog(branch_name, output_file)

        if feature_branches:
            output_file = os.path.join(self.output_dir, "CHANGELOG_features.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# Changelog - Features\n\n")
                for branch in feature_branches:
                    branch_name = branch.replace('origin/', '')
                    f.write(f"## {branch_name}\n\n")
                    commits = self._get_commits(branch)
                    for commit in commits:
                        formatted_commit = self._format_commit(commit)
                        f.write(formatted_commit + "\n")
                    f.write("\n")
            logger.info(f"Changelog generated successfully for feature branches at {output_file}")

    def integrate_changelogs(self):
        changelog_files = [file for file in os.listdir(self.output_dir) if file.startswith("CHANGELOG_")]
        integrated_changelog = "# Integrated Changelog\n\n"

        for file in changelog_files:
            with open(os.path.join(self.output_dir, file), 'r', encoding='utf-8') as f:
                content = f.read()
                integrated_changelog += f"{content}\n\n"

        output_file = os.path.join(self.output_dir, "CHANGELOG_integrated.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(integrated_changelog)

        logger.info(f"Integrated changelog generated successfully at {output_file}")


if __name__ == "__main__":
    repo_path = "./"
    output_dir = "docs/Changelog"
    os.makedirs(output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    logger.add("changelog_generator.log", rotation="1 MB", retention="10 days")

    generator = ChangelogGenerator(repo_path, output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()
```

### コミットハッシュ: 5813f...

- **作者**: Maki
- **日時**: 2024-03-30 18:40:57+09:00
- **メッセージ**: 

    Create SourceSage.md
    

#### 変更されたファイル:

- docs/SourceSage.md
    - **追加された内容:**

````markdown
# Project: SourceSage

```bash
OS: nt
Directory: C:\Prj\SourceSage

├─ config/
│  ├─ language_map.json
├─ docs/
├─ modules/
│  ├─ ChangelogGenerator.py
│  ├─ file_utils.py
│  ├─ main.py
│  ├─ markdown_utils.py
│  ├─ source_sage.py
│  ├─ __init__.py
├─ README.md
├─ SourceSage.py
```

## .

`README.md`

```markdown
<p align="center">

<img src="docs/SourceSage_icon4.png" width="100%">

<br>

<h1 align="center">SourceSage</h1>

<h2 align="center">～Transforming code for AI～</h2>

</p>

SourceSageは、プロジェクトのソースコードとファイル構成を単一のマークダウンファイルに統合するPythonスクリプトです。これにより、大規模言語モデル（AI）がプロジェクト全体の構造と内容を容易に理解できるようになります。

## 特徴

- プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイルにまとめます
- AIがプロジェクトの概要を素早く把握できる構造化された形式で出力します
- 不要なファイルやディレクトリを除外する設定が可能です
- プロジェクトの全体像を明確かつ読みやすい方法で提示します

## 使用方法

プロジェクトでSourceSageを使用するには、次の手順に従います：

1. `SourceSage.py`ファイルを、分析対象のプロジェクトのルートディレクトリにコピーします。

2. 必要に応じて、`SourceSage.py`内の以下の設定を変更します：

```python
folders = ['./'] # 分析対象のディレクトリ（現在のディレクトリを指定）
exclude_patterns = ['.git', '__pycache__', 'LICENSE', 'output.md', 'README.md', 'docs'] # 除外するファイル/フォルダのパターン 
output_file = 'output.md' # 出力するマークダウンファイル名
```

3. ターミナルまたはコマンドプロンプトで、プロジェクトのルートディレクトリに移動し、以下のコマンドを実行します：

```bash
python SourceSage.py
```

これにより、AIがプロジェクトの構造と内容を理解しやすい形式のマークダウンファイル（デフォルトでは `output.md`）が生成されます。

## 出力例

生成されるマークダウンファイルの例は次のようになります：

```markdown
# プロジェクト名: YourProjectName

## ディレクトリ構造
├─ src/
│  ├─ main.py
│  ├─ utils/
│  │  ├─ helper.py
│  │  └─ constants.py
│  └─ tests/
│     └─ test_main.py
└─ README.md

## ファイルの内容

`src/main.py`
'''python
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
'''

...
```

## 貢献

SourceSageの改善にご協力ください！バグの報告や機能追加の提案がある場合は、[GitHubリポジトリ](https://github.com/yourusername/SourceSage)でIssueを開くかプルリクエストを送信してください。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

---
```

`SourceSage.py`

```python
import os
import sys
import pprint

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
pprint.pprint(sys.path)

from modules.source_sage import SourceSage
from modules.ChangelogGenerator import ChangelogGenerator

if __name__ == "__main__":
    folders = ['./']
    source_sage = SourceSage(folders, ignore_file='.SourceSageignore',
                             output_file='docs/SourceSage.md',
                             language_map_file='config/language_map.json')
    source_sage.generate_markdown()


    repo_path = "./"
    output_dir = "docs/Changelog"
    os.makedirs(output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    generator = ChangelogGenerator(repo_path, output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()
```

## .vscode

`.vscode\settings.json`

```json
{
    "gitlens.ai.experimental.openai.url": "",
    "gitlens.ai.experimental.provider": "anthropic",
    "gitlens.ai.experimental.anthropic.model": "claude-3-haiku-20240307",
    "gitlens.experimental.generateCommitMessagePrompt": "日本語でシンプルなコミットメッセージ"
}
```

## config

`config\language_map.json`

```json
{
    ".py": "python",
    ".js": "javascript",
    ".java": "java",
    ".c": "c",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".go": "go",
    ".php": "php",
    ".rb": "ruby",
    ".rs": "rust",
    ".ts": "typescript",
    ".html": "html",
    ".css": "css",
    ".json": "json",
    ".xml": "xml",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".md": "markdown",
    ".txt": "plaintext",
    ".sh": "bash",
    ".sql": "sql",
    "Dockerfile": "dockerfile",
    ".dockerfile": "dockerfile",
    "docker-compose.yml": "yaml",
    "docker-compose.yaml": "yaml"
}
```

## docs

## modules

`modules\ChangelogGenerator.py`

```python
import os
from git import Repo
from datetime import datetime
from loguru import logger

class ChangelogGenerator:
    def __init__(self, repo_path, output_dir):
        self.repo_path = repo_path
        self.output_dir = output_dir
        self.repo = self._get_repo()

    def _get_repo(self):
        return Repo(self.repo_path)

    def _get_commits(self, branch):
        return list(self.repo.iter_commits(branch))

    def _format_commit(self, commit):
        message = commit.message.strip()
        sha = commit.hexsha[:7]
        author = commit.author.name
        date = datetime.fromtimestamp(commit.committed_date).strftime("%Y-%m-%d")
        return f"- [{sha}] - {message} ({author}, {date})"

    def generate_changelog(self, branch, output_file):
        commits = self._get_commits(branch)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Changelog\n\n")
            f.write(f"## {branch}\n\n")

            for commit in commits:
                formatted_commit = self._format_commit(commit)
                f.write(formatted_commit + "\n")

        logger.info(f"Changelog generated successfully for branch '{branch}' at {output_file}")

    def generate_changelog_for_all_branches(self):
        local_branches = [ref.name for ref in self.repo.branches]
        remote_branches = [ref.name for ref in self.repo.remote().refs]

        branches = local_branches + remote_branches
        print(branches)

        feature_branches = [branch for branch in branches if 'feature/' in branch]
        other_branches = [branch for branch in branches if 'feature/' not in branch]

        for branch in other_branches:
            branch_name = branch.replace('origin/', '')
            output_file = os.path.join(self.output_dir, f"CHANGELOG_{branch_name}.md")
            logger.info(f"Generating changelog for branch '{branch_name}'...")
            self.generate_changelog(branch_name, output_file)

        if feature_branches:
            output_file = os.path.join(self.output_dir, "CHANGELOG_features.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# Changelog - Features\n\n")
                for branch in feature_branches:
                    branch_name = branch.replace('origin/', '')
                    f.write(f"## {branch_name}\n\n")
                    commits = self._get_commits(branch)
                    for commit in commits:
                        formatted_commit = self._format_commit(commit)
                        f.write(formatted_commit + "\n")
                    f.write("\n")
            logger.info(f"Changelog generated successfully for feature branches at {output_file}")

    def integrate_changelogs(self):
        changelog_files = [file for file in os.listdir(self.output_dir) if file.startswith("CHANGELOG_")]
        integrated_changelog = "# Integrated Changelog\n\n"

        for file in changelog_files:
            with open(os.path.join(self.output_dir, file), 'r', encoding='utf-8') as f:
                content = f.read()
                integrated_changelog += f"{content}\n\n"

        output_file = os.path.join(self.output_dir, "CHANGELOG_integrated.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(integrated_changelog)

        logger.info(f"Integrated changelog generated successfully at {output_file}")


if __name__ == "__main__":
    repo_path = "./"
    output_dir = "docs/Changelog"
    os.makedirs(output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する

    logger.add("changelog_generator.log", rotation="1 MB", retention="10 days")

    generator = ChangelogGenerator(repo_path, output_dir)
    generator.generate_changelog_for_all_branches()
    generator.integrate_changelogs()
```

`modules\file_utils.py`

```python
import os
import fnmatch
import json

def load_ignore_patterns(ignore_file):
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    else:
        return []

def load_language_map(language_map_file):
    if os.path.exists(language_map_file):
        with open(language_map_file, 'r') as f:
            return json.load(f)
    else:
        return {}

def is_excluded(path, exclude_patterns):
    for pattern in exclude_patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
        if fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
    return False
```

`modules\main.py`

```python
from modules.source_sage import SourceSage

if __name__ == "__main__":
    folders = ['./']
    source_sage = SourceSage(folders, ignore_file='.SourceSageignore',
                             output_file='SourceSage.md',
                             language_map_file='config/language_map.json')
    source_sage.generate_markdown()
```

`modules\markdown_utils.py`

```python
import os
from file_utils import is_excluded

def generate_markdown_for_folder(folder_path, exclude_patterns, language_map):
    markdown_content = "```plaintext\n"
    markdown_content += _display_tree(dir_path=folder_path, exclude_patterns=exclude_patterns)
    markdown_content += "\n```\n\n"
    base_level = folder_path.count(os.sep)
    for root, dirs, files in os.walk(folder_path, topdown=True):
        dirs[:] = [d for d in dirs if not is_excluded(os.path.join(root, d), exclude_patterns)]
        level = root.count(os.sep) - base_level + 1
        header_level = '#' * (level + 1)
        relative_path = os.path.relpath(root, folder_path)
        markdown_content += f"{header_level} {relative_path}\n\n"
        for f in files:
            file_path = os.path.join(root, f)
            if is_excluded(file_path, exclude_patterns):
                continue
            relative_file_path = os.path.relpath(file_path, folder_path)
            try:
                with open(file_path, 'r', encoding='utf-8') as file_content:
                    content = file_content.read().strip()
                    language = _get_language_for_file(f, language_map)
                    markdown_content += f"`{relative_file_path}`\n\n```{language}\n{content}\n```\n\n"
            except Exception as e:
                markdown_content += f"`{relative_file_path}` - Error reading file: {e}\n\n"
    return markdown_content

def _display_tree(dir_path='.', exclude_patterns=None, string_rep=True, header=True, max_depth=None, show_hidden=False):
    tree_string = ""
    if header:
        tree_string += f"OS: {os.name}\nDirectory: {os.path.abspath(dir_path)}\n\n"
    tree_string += _build_tree_string(dir_path, max_depth, show_hidden, exclude_patterns, depth=0)
    if string_rep:
        return tree_string.strip()
    else:
        print(tree_string.strip())

def _build_tree_string(dir_path, max_depth, show_hidden, exclude_patterns, depth=0):
    tree_string = ""
    if depth == max_depth:
        return tree_string
    for item in os.listdir(dir_path):
        if not show_hidden and item.startswith('.'):
            continue
        item_path = os.path.join(dir_path, item)
        if is_excluded(item_path, exclude_patterns):
            continue
        if os.path.isdir(item_path):
            tree_string += '│  ' * depth + '├─ ' + item + '/\n'
            tree_string += _build_tree_string(item_path, max_depth, show_hidden, exclude_patterns, depth + 1)
        else:
            tree_string += '│  ' * depth + '├─ ' + item + '\n'
    return tree_string

def _get_language_for_file(filename, language_map):
    _, extension = os.path.splitext(filename)
    extension = extension.lower()
    return language_map.get(extension, 'plaintext')
```

`modules\source_sage.py`

```python
import os
from modules.file_utils import load_ignore_patterns, load_language_map, is_excluded
from modules.markdown_utils import generate_markdown_for_folder

class SourceSage:
    def __init__(self, folders, ignore_file='.SourceSageignore', output_file='output.md', language_map_file='language_map.json'):
        self.folders = folders
        self.ignore_file = ignore_file
        self.output_file = output_file
        self.exclude_patterns = load_ignore_patterns(ignore_file)
        self.language_map = load_language_map(language_map_file)

    def generate_markdown(self):
        with open(self.output_file, 'w', encoding='utf-8') as md_file:
            project_name = os.path.basename(os.path.abspath(self.folders[0]))
            md_file.write(f"# Project: {project_name}\n\n")
            for folder in self.folders:
                markdown_content = generate_markdown_for_folder(folder, self.exclude_patterns, self.language_map)
                md_file.write(markdown_content + '\n\n')
```

`modules\__init__.py`

```python

```



````

