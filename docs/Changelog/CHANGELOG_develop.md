# 変更履歴

## develop (v5.0.2..v5.0.3)

### [351693d] - 🔖 (#28)[chore] パッケージバージョンを5.0.2に更新

  - 作者: Maki
  - 日時: 2024-06-11 19:26:37 +0900
  - 詳細:
		- setup.pyにおけるバージョン情報を5.0.2に更新
		- パッケージの整合性を保つためのバージョン更新

  - 差分:

```diff
--- a/setup.py
+++ b/setup.py
@@ -14,7 +14,7 @@ setup(
-    version='5.0.1',
+    version='5.0.2',
```

---
### [e192375] - 📝 (#28)[docs] READMEファイルのリリースリンク更新

  - 作者: Maki
  - 日時: 2024-06-11 19:26:34 +0900
  - 詳細:
		- SourceSageの最新リリース情報を5.0.2に更新
		- リリースリンクとリリースノートの文書を整理

  - 差分:

```diff
--- a/README.md
+++ b/README.md
@@ -45,7 +45,7 @@ SourceSageは、プロジェクトのソースコードとファイル構成を
-- [【2024/06/10】 SourceSage 5.0.0](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/v5.0.0)
+- [【2024/06/10】 SourceSage 5.0.2](https://github.com/Sunwood-ai-labs/SourceSage/releases/tag/v5.0.2)
@@ -145,7 +145,7 @@ sourcesage --mode Sage GenerateReport CommitCraft --model-name "gemini/gemini-1.
-sourcesage --mode DocuMind --docuMind-model "gemini/gemini-1.5-pro-latest" --docuMind-db ".SourceSageAssets\DOCUMIND\Repository_summary.md" --docuMind-release-report ".SourceSageAssets\RELEASE_REPORT\Report_v5.0.0.md"  --docuMind-changelog ".SourceSageAssets\Changelog\CHANGELOG_release_5.0.0.md"  --docuMind-output ".SourceSageAssets/DOCUMIND/RELEASE_NOTES_v5.0.0.md"  --docuMind-prompt-output ".SourceSageAssets/DOCUMIND/_PROMPT_v5.0.0.md"  --repo-name "SourceSage" --repo-version "v0.5.0"
+sourcesage --mode DocuMind --docuMind-model "gemini/gemini-1.5-pro-latest" --docuMind-db ".SourceSageAssets\DOCUMIND\Repository_summary.md" --docuMind-release-report ".SourceSageAssets\RELEASE_REPORT\Report_v5.0.2.md"  --docuMind-changelog ".SourceSageAssets\Changelog\CHANGELOG_release_5.0.2.md"  --docuMind-output ".SourceSageAssets/DOCUMIND/RELEASE_NOTES_v5.0.2.md"  --docuMind-prompt-output ".SourceSageAssets/DOCUMIND/_PROMPT_v5.0.2.md"  --repo-name "SourceSage" --repo-version "v0.5.0"
```

---
### [3523c0c] - 🚀 [chore] .SourceSageignoreの更新

  - 作者: Maki
  - 日時: 2024-06-11 19:22:30 +0900
  - 詳細:
		- STAGE_INFO, example, ISSUES_RESOLVE, testsをignoreリストに追加
		- ドキュメントと環境設定ファイルの管理を改善

  - 差分:

```diff
--- a/.SourceSageignore
+++ b/.SourceSageignore
@@ -26,4 +26,8 @@ build
-.env
+.env
+STAGE_INFO
+example
+ISSUES_RESOLVE
+tests
```

---
### [abed214] - 🔧 [refactor] チェンジログ統合機能の堅牢性向上

  - 作者: Maki
  - 日時: 2024-06-11 19:22:27 +0900
  - 詳細:
		- Unicodeデコードエラーを処理する例外処理を追加
		- チェンジログファイルの読み込みをより堅牢にするためのロギングを改善

  - 差分:

```diff
--- a/sourcesage/modules/ChangelogGenerator.py
+++ b/sourcesage/modules/ChangelogGenerator.py
@@ -113,15 +113,18 @@ class ChangelogGenerator:
-
-            with open(os.path.join(self.output_dir, file), 'r', encoding='utf-8') as f:
-                content = f.read()
-                integrated_changelog += f"{content}\n\n"
+            file_path = os.path.join(self.output_dir, file)
+            try:
+                with open(file_path, 'r', encoding='utf-8') as f:
+                    content = f.read()
+                    integrated_changelog += f"{content}\n\n"
+            except UnicodeDecodeError as e:
+                logger.warning(f"ファイル '{file_path}' のデコードエラーをスキップします: {str(e)}")
```

---
