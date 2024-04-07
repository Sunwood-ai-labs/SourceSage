

下記はgitはStageの情報です

issueは掲載しないで

見やすくコミットメッセージにして
章やパラグラフ、箇条書きを多用して見やすくして

コミットメッセージは日本語にして
正確にstep-by-stepで処理して

下記のマークダウンフォーマットで出力して

## フォーマット

```markdown

[種類] 概要

詳細な説明（必要に応じて）

```

## 種類

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