# トラブルシューティング

## ドキュメント成果物に `.git` ファイルが含まれる

SourceSage は通常 `.git/` を除外します。Git の内部ファイルが見えている場合は、カスタム ignore ファイルで既定の除外ルールを上書きしていないか確認してください。

## 古い `uvx` キャッシュが使われている

```bash
uv cache clean
uv cache prune
```

## 独自の ignore ルールを使いたい

対象リポジトリの `.SourceSageignore` を作成または編集してから、次を実行してください。

```bash
uv run sage --repo .
```

## diff レポートが生成されない

`--diff` には最低 2 つの Git タグが必要です。タグが不足している場合、コマンド全体は失敗せず diff レポートだけをスキップします。
