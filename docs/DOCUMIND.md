
# DocuMind：AIを活用した効率的なリリースノート生成

DocuMindは、リリース後のプロジェクトの統合とドキュメント化を支援するツールです。SourceSageが生成するプロジェクトの概要と、自動生成されたGitの変更履歴を組み合わせることで、プロジェクトの全体像を明確に把握できます。これにより、開発者はプロジェクトのドキュメントを効率的に作成し、メンテナンス性を向上させることができます。

## 使用方法

1. SourceSageのCLIコマンドから、以下のようにパラメータを指定してDocuMindを実行します。

```bash
sourcesage --mode DocuMind --docuMind-model "使用するAIモデル名" --docuMind-db "DocuMindのデータベースファイルのパス" --docuMind-release-report "リリースレポートのパス" --docuMind-changelog "変更履歴のパス" --docuMind-output "リリースノートの出力パス" --docuMind-prompt-output "リリースノート作成のプロンプト" --repo-name "リポジトリの名前" --repo-version "リポジトリのバージョン"
```

2. DocuMindは指定されたデータベースファイル、リリースレポート、変更履歴を読み込み、AIを使用してリリースノートを自動的に生成します。

3. 生成されたリリースノートは、指定された出力パスに保存されます。また、リリースノート作成のプロンプトも別ファイルに保存されます。

## パラメータ

- `--docuMind-model`: 使用するAIモデル名を指定します。
- `--docuMind-db`: DocuMindのデータベースファイルのパスを指定します。
- `--docuMind-release-report`: リリースレポートのパスを指定します。
- `--docuMind-changelog`: 変更履歴のパスを指定します。
- `--docuMind-output`: リリースノートの出力パスを指定します。
- `--docuMind-prompt-output`: リリースノート作成のプロンプトの出力パスを指定します。
- `--repo-name`: リポジトリの名前を指定します。
- `--repo-version`: リポジトリのバージョンを指定します。

## サンプル

以下は、SourceSageのCLIコマンドを使用してDocuMindを実行するサンプルです。

```bash
sourcesage --mode DocuMind --docuMind-model "gemini/gemini-1.5-pro-latest" --docuMind-db ".SourceSageAssets\DOCUMIND\Repository_summary.md" --docuMind-release-report ".SourceSageAssets\RELEASE_REPORT\Report_v5.0.2.md"  --docuMind-changelog ".SourceSageAssets\Changelog\CHANGELOG_release_5.0.2.md"  --docuMind-output ".SourceSageAssets/DOCUMIND/RELEASE_NOTES_v5.0.2.md"  --docuMind-prompt-output ".SourceSageAssets/DOCUMIND/_PROMPT_v5.0.2.md"  --repo-name "SourceSage" --repo-version "v0.5.0"
```

このコマンドでは、以下のパラメータを指定しています。

- `--docuMind-model "gemini/gemini-1.5-pro-latest"`: 使用するAIモデル名を"gemini/gemini-1.5-pro-latest"に指定します。
- `--docuMind-db ".SourceSageAssets\DOCUMIND\Repository_summary.md"`: DocuMindのデータベースファイルのパスを指定します。
- `--docuMind-release-report ".SourceSageAssets\RELEASE_REPORT\Report_v5.0.2.md"`: リリースレポートのパスを指定します。
- `--docuMind-changelog ".SourceSageAssets\Changelog\CHANGELOG_release_5.0.2.md"`: 変更履歴のパスを指定します。
- `--docuMind-output ".SourceSageAssets/DOCUMIND/RELEASE_NOTES_v5.0.2.md"`: リリースノートの出力パスを指定します。
- `--docuMind-prompt-output ".SourceSageAssets/DOCUMIND/_PROMPT_v5.0.2.md"`: リリースノート作成のプロンプトの出力パスを指定します。
- `--repo-name "SourceSage"`: リポジトリの名前を"SourceSage"に指定します。
- `--repo-version "v0.5.0"`: リポジトリのバージョンを"v0.5.0"に指定します。

DocuMindは、指定されたデータベースファイル、リリースレポート、変更履歴を読み込み、AIを使用してリリースノートを自動的に生成します。生成されたリリースノートは、指定された出力パスに保存されます。また、リリースノート作成のプロンプトも別ファイルに保存されます。

以下は、DocuMindで使用されるデータベースファイルと変更履歴のサンプルです。

- [DocuMindのサンプル](./SAMPLE/SAMPLE_DocuMind.md)
- [変更履歴のサンプル](./SAMPLE/SAMPLE_CHANGELOG_release_4.1.0.md)

これらのサンプルファイルは、DocuMindがAIを使用してリリースノートを生成する際の入力として使用されます。開発者は、これらのサンプルを参考にしてデータベースファイルや変更履歴を作成することができます。

DocuMindを使用することで、開発者はドキュメント作成の負担を軽減し、常に最新の状態を反映したドキュメントを自動的に生成できます。これにより、プロジェクトのメンテナンス性が向上し、開発者はより重要なタスクに集中できるようになります。