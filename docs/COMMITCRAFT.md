# CommitCraft：AIを活用した効率的なコミットメッセージ生成

CommitCraftは、開発中のステージされた変更を追跡し、AIを活用して適切なコミットメッセージを自動生成するツールです。これにより、開発者はコミットの内容を正確に記述することができ、プロジェクトの変更履歴をより明確に管理できます。

## 使用方法

1. SourceSageのCLIコマンドから、以下のようにパラメータを指定してCommitCraftを実行します。

```bash
sourcesage --mode CommitCraft --model-name "使用するAIモデル名" --stage-info-file "ステージ情報のマークダウンファイルパス" --commit-craft-output "CommitCraftの出力ディレクトリ" --llm-output "LLMの出力ファイル名"
```

2. CommitCraftは指定されたステージ情報のマークダウンファイルを読み込み、AIを使用して適切なコミットメッセージを自動的に生成します。

3. 生成されたコミットメッセージは、指定された出力ディレクトリ内のLLMの出力ファイルに保存されます。

## パラメータ

- `--model-name`: 使用するAIモデル名を指定します（デフォルトは`None`）。
- `--stage-info-file`: ステージ情報のマークダウンファイルのパスを指定します。
- `--commit-craft-output`: CommitCraftの出力ディレクトリを指定します。
- `--llm-output`: LLMの出力ファイル名を指定します。

## サンプル

以下は、SourceSageのCLIコマンドを使用してCommitCraftを実行するサンプルです。

```bash
sourcesage --mode CommitCraft --model-name "gemini/gemini-1.5-pro-latest" --stage-info-file ".SourceSageAssets\COMMIT_CRAFT/STAGE_INFO\STAGE_INFO_AND_PROMT_GAIAH_B.md" --commit-craft-output ".SourceSageAssets/COMMIT_CRAFT/" --llm-output "llm_output.md"
```

このコマンドでは、以下のパラメータを指定しています。

- `--model-name "gemini/gemini-1.5-pro-latest"`: 使用するAIモデル名を"gemini/gemini-1.5-pro-latest"に指定します。
- `--stage-info-file ".SourceSageAssets\COMMIT_CRAFT/STAGE_INFO\STAGE_INFO_AND_PROMT_GAIAH_B.md"`: ステージ情報のマークダウンファイルのパスを指定します。
- `--commit-craft-output ".SourceSageAssets/COMMIT_CRAFT/"`: CommitCraftの出力ディレクトリを指定します。
- `--llm-output "llm_output.md"`: LLMの出力ファイル名を"llm_output.md"に指定します。

CommitCraftは、指定されたステージ情報のマークダウンファイルを読み込み、AIを使用して適切なコミットメッセージを自動生成します。生成されたコミットメッセージは、指定された出力ディレクトリ内のLLMの出力ファイルに保存されます。

以下は、CommitCraftで使用されるステージ情報のマークダウンファイルのサンプルです。

- [ステージ情報とプロンプトのサンプル](../SAMPLE/SAMPLE_STAGE_INFO_AND_PROMT.md)
- [絵文字を使用したサンプル](../SAMPLE/SAMPLE_STAGE_INFO_AND_PROMT_EMOJI.md)
- [Gaiah用のサンプル](../SAMPLE/SAMPLE_STAGE_INFO_AND_PROMT_GAIAH.md)
- [Issueとマージされたサンプル](../SAMPLE/SAMPLE_STAGE_INFO_AND_ISSUES_AND_PROMT.md)

これらのサンプルファイルは、CommitCraftがAIを使用してコミットメッセージを生成する際の入力として使用されます。開発者は、これらのサンプルを参考にしてステージ情報のマークダウンファイルを作成することができます。

CommitCraftを使用することで、開発者はコミットメッセージを考える負担を軽減し、一貫性のある適切なコミットメッセージを自動的に生成できます。これにより、プロジェクトの変更履歴がより明確になり、コードレビューやコラボレーションがスムーズに行えるようになります。