下記はissuesの情報です


```json

[
  {
    "number": 11,
    "title": "ModuleNotFoundError: No module named 'sourcesage.config'",
    "body": null
  },
  {
    "number": 8,
    "title": "クイックスタートの手順の記載",
    "body": null
  },
  {
    "number": 7,
    "title": "READMEの更新と生成物のリンクの対応",
    "body": "- リポジトリ全体の変更に合わせてREADMEの大幅変更\r\n- SourceSage.py の生成物に合わせて生成物へのリンクをREADMEに記載\r\n\r\n\r\n下記の内容を盛り込んで、必要に応じて内容を修正して\r\n\r\n```\r\n開発前\r\n\r\n課題の確認とAIによる自動修正\r\n\r\n- GitHubのオープンなissueを取得し、JSONファイルに保存する\r\n- SourceSage.pyを使用して現在のプロジェクトのソースコードとファイル構成を1つのマークダウンファイル(SourceSageAssetsDemo\\ISSUES_RESOLVE\\ISSUE_7.md)に統合する\r\n- issueデータとSourceSage.pyで生成したマークダウンをClaude AIに入力する\r\n- AIがissueの内容を理解し、現在のソースコードを分析して自動的にissueの修正を提案する\r\n- 提案された修正内容を確認し、必要に応じて手動で調整を行う\r\n\r\n開発中\r\n\r\nステージされた変更の確認とコミットメッセージの自動生成\r\n\r\n- StagedDiffGeneratorクラスを使用してステージされた差分を取得し、マークダウンファイルに出力する\r\n- ステージされた変更とissueの情報をAIに入力し、適切なコミットメッセージを生成する\r\n- get_issues.pyで取得したissueデータとStagedDiffGeneratorで生成したマークダウン（SourceSageAssetsDemo\\STAGED_DIFF.md）をClaude AIに入力する\r\n- AIが既存のissueを考慮してコミットメッセージを自動生成する\r\n\r\n\r\nリリース後\r\n\r\nプロジェクトの統合とドキュメント化\r\n\r\n- SourceSage.pyを使用してプロジェクト全体のソースコードとファイル構成をAIが理解しやすい形式で統合する\r\n- プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイル（SourceSageAssetsDemo\\SourceSage.md）にまとめる\r\n- 不要なファイルやディレクトリを除外するための設定が可能\r\n- 複数のプログラミング言語に対応し、シンタックスハイライト機能を提供\r\n- Gitの変更履歴を自動生成し、ドキュメント化する\r\n- ブランチごとに変更履歴をマークダウンファイルに出力する\r\n- すべてのブランチの変更履歴を1つのファイルに統合する\r\n```"
  }
]

```

また、下記はgitはStageの情報です

issueを解決していればそれも含めてコミットメッセージを書いて
解決していないissueは掲載しないで

見やすくコミットメッセージにして
章やパラグラフ、箇条書きを多用して見やすくして

コミットメッセージは日本語にして
正確にstep-by-stepで処理して

コミットメッセージは下記のフォーマットにして

## フォーマット

```markdown

[種類] 概要

詳細な説明（必要に応じて）

```

種類は下記を参考にして

例：
  - feat: 新機能
  - fix: バグ修正
  - docs: ドキュメントのみの変更
  - style: コードの動作に影響しない変更（空白、フォーマット、セミコロンの欠落など） 
  - refactor: バグの修正も機能の追加も行わないコードの変更
  - perf: パフォーマンスを向上させるコードの変更
  - test: 欠けているテストの追加や既存のテストの修正
  - chore: ビルドプロセスやドキュメント生成などの補助ツールやライブラリの変更


## Stageの情報

```markdown
# Staged Files Diff

## README.md

### 差分:

```diff
@@ -10,7 +10,9 @@
   <img alt="PyPI - Format" src="https://img.shields.io/pypi/format/sourcesage">
   <img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/sourcesage">
   <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/sourcesage">
-
+  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/sourcesage">
+  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/sourcesage">
+  <a href="https://app.codacy.com/gh/Sunwood-ai-labs/SourceSage/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/77ab7715dd23499d82caca4e7ea3b093"/></a>
 
   <br>
 
@@ -23,6 +25,8 @@
 
 SourceSageは、プロジェクトのソースコードとファイル構成を単一のマークダウンファイルに統合し、AIによる自動修正やドキュメント化を実現するPythonスクリプトです。開発のライフサイクル全体を通して、コードの品質向上と生産性の向上を支援します。
 
+**このリポジトリ自体もSourceSageを活用しており、リリースノートやREADME、コミットメッセージの9割はSourceSage X クロードで生成しています。**
+
 
 ## 更新内容
 

```

## setup.py

### 差分:

```diff
@@ -7,8 +7,13 @@ with open("README.md", "r", encoding="utf-8") as fh:
 
 setup(
     name='sourcesage',
-    version='4.0.10',
+    version='4.0.11',
     packages=find_packages(),
+    classifiers=[
+        "Development Status :: 4 - Beta",
+        "Intended Audience :: Developers",
+        "Topic :: Utilities",
+    ],
     package_data={
         'sourcesage': ['config/**/**', 
                        'config/.SourceSageignore'],

```



```