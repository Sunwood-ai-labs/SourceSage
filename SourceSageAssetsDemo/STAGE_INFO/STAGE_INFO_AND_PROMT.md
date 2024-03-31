

下記はgitはStageの情報です

issueは掲載しないで

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
@@ -1,8 +1,6 @@
 
-<head>
-<link href="https://raw.githubusercontent.com/Sunwood-ai-labs/SourceSage/develop/docs/css/style.css" rel="stylesheet"></link>
-<link href="docs/css/style.css" rel="stylesheet"></link>
-</head>
+
+
 
 <p align="center">
 

```

## SourceSage.py

### 差分:

```diff
@@ -20,19 +20,24 @@ except ImportError:
 
 if __name__ == "__main__":
     repo_path = os.getenv("REPO_PATH")
-    source_sage_assets_dir = os.getenv("SOURCE_SAGE_ASSETS_DIR")
-    config_dir = os.getenv("CONFIG_DIR")
-    docs_dir = os.getenv("DOCS_DIR")
-    issue_log_dir = os.getenv("ISSUE_LOG_DIR")
+    source_sage_assets_dir = os.path.join(repo_path, os.getenv("SOURCE_SAGE_ASSETS_DIR"))
+    config_dir = os.path.join(repo_path, os.getenv("CONFIG_DIR"))
+    docs_dir = os.path.join(repo_path, os.getenv("DOCS_DIR"))
+    issue_log_dir = os.path.join(source_sage_assets_dir, os.getenv("ISSUE_LOG_DIR"))
+    issues_resolve_dir = os.path.join(source_sage_assets_dir, os.getenv("ISSUES_RESOLVE_DIR"))
+    stage_info_dir = os.path.join(source_sage_assets_dir, os.getenv("STAGE_INFO_DIR"))
 
+    os.makedirs(issue_log_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する
+    os.makedirs(issues_resolve_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する
+    os.makedirs(stage_info_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する
 
-    folders = os.getenv("FOLDERS").split(",")  # カンマ区切りの文字列をリストに変換
-    source_sage = SourceSage(folders, ignore_file=os.getenv("IGNORE_FILE"),
-                             output_file=os.getenv("OUTPUT_FILE"),
-                             language_map_file=os.getenv("LANGUAGE_MAP_FILE"))
+    folders = [os.path.join(repo_path, folder) for folder in os.getenv("FOLDERS").split(",")]  # カンマ区切りの文字列をリストに変換
+    source_sage = SourceSage(folders, ignore_file=os.path.join(config_dir, os.getenv("IGNORE_FILE")),
+                             output_file=os.path.join(source_sage_assets_dir, os.getenv("OUTPUT_FILE")),
+                             language_map_file=os.path.join(config_dir, os.getenv("LANGUAGE_MAP_FILE")))
     source_sage.generate_markdown()
 
-    changelog_output_dir = f"{source_sage_assets_dir}/Changelog"
+    changelog_output_dir = os.path.join(source_sage_assets_dir, "Changelog")
     os.makedirs(changelog_output_dir, exist_ok=True)  # ディレクトリが存在しない場合は作成する
 
     generator = ChangelogGenerator(repo_path, changelog_output_dir)
@@ -43,39 +48,37 @@ if __name__ == "__main__":
     repository = os.getenv("REPOSITORY")
     issues_file_name = os.getenv("ISSUES_FILE_NAME")
 
-    issue_retriever = GitHubIssueRetriever(owner, repository, source_sage_assets_dir + "/" + issue_log_dir, issues_file_name)
+    issue_retriever = GitHubIssueRetriever(owner, repository, issue_log_dir, issues_file_name)
     issue_retriever.run()
 
-
     diff_generator = StagedDiffGenerator(
         repo_path=repo_path,
         output_dir=source_sage_assets_dir,
-        language_map_file=f"{config_dir}/language_map.json"
+        language_map_file=os.path.join(config_dir, "language_map.json")
     )
     diff_generator.run()
 
     stage_info_generator = StageInfoGenerator(
-        issue_file_path=f"{source_sage_assets_dir}/{issue_log_dir}/{issues_file_name}",
-        stage_diff_file_path=f"{source_sage_assets_dir}/STAGED_DIFF.md",
-        template_file_path=f"{docs_dir}/STAGE_INFO/STAGE_INFO_AND_ISSUES_TEMPLATE.md",
-        output_file_path=f"{source_sage_assets_dir}/STAGE_INFO/STAGE_INFO_AND_ISSUES_AND_PROMT.md"
+        issue_file_path=os.path.join(issue_log_dir, issues_file_name),
+        stage_diff_file_path=os.path.join(source_sage_assets_dir, "STAGED_DIFF.md"),
+        template_file_path=os.path.join(docs_dir, os.getenv("STAGE_INFO_DIR"), "STAGE_INFO_AND_ISSUES_TEMPLATE.md"),
+        output_file_path=os.path.join(stage_info_dir, "STAGE_INFO_AND_ISSUES_AND_PROMT.md")
     )
     stage_info_generator.run()
 
     stage_info_generator = StageInfoGenerator(
-        issue_file_path=f"{source_sage_assets_dir}/{issue_log_dir}/{issues_file_name}",
-        stage_diff_file_path=f"{source_sage_assets_dir}/STAGED_DIFF.md",
-        template_file_path=f"{docs_dir}/STAGE_INFO/STAGE_INFO_TEMPLATE.md",
-        output_file_path=f"{source_sage_assets_dir}/STAGE_INFO/STAGE_INFO_AND_PROMT.md"
+        issue_file_path=os.path.join(issue_log_dir, issues_file_name),
+        stage_diff_file_path=os.path.join(source_sage_assets_dir, "STAGED_DIFF.md"),
+        template_file_path=os.path.join(docs_dir, os.getenv("STAGE_INFO_DIR"), "STAGE_INFO_TEMPLATE.md"),
+        output_file_path=os.path.join(stage_info_dir, "STAGE_INFO_AND_PROMT.md")
     )
     stage_info_generator.run()
 
-    issues_markdown_output_dir = f"{source_sage_assets_dir}/ISSUES_RESOLVE"
     converter = IssuesToMarkdown(
-        issues_file=f"{source_sage_assets_dir}/{issue_log_dir}/{issues_file_name}",
-        sourcesage_file=f"{source_sage_assets_dir}/SourceSage.md",
-        template_file=f"{docs_dir}/ISSUES_RESOLVE/ISSUES_RESOLVE_TEMPLATE.md",
-        output_folder=issues_markdown_output_dir
+        issues_file=os.path.join(issue_log_dir, issues_file_name),
+        sourcesage_file=os.path.join(source_sage_assets_dir, "SourceSage.md"),
+        template_file=os.path.join(docs_dir, os.getenv("ISSUES_RESOLVE_DIR"), "ISSUES_RESOLVE_TEMPLATE.md"),
+        output_folder=issues_resolve_dir
     )
     converter.load_data()
     converter.create_markdown_files()
\ No newline at end of file

```

## modules/EnvFileHandler.py

### 差分:

```diff
@@ -10,7 +10,7 @@ CONFIG_DIR=config
 DOCS_DIR=docs
 FOLDERS=./
 IGNORE_FILE=.SourceSageignore
-OUTPUT_FILE=SourceSageAssets/SourceSage.md
+OUTPUT_FILE=SourceSage.md
 LANGUAGE_MAP_FILE=config/language_map.json
 
 OWNER=Sunwood-ai-labs

```



```