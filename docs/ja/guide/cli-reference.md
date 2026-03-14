# CLI リファレンス

## よく使うコマンド

```bash
uv run sage --repo .
uv run sage --repo . -l ja
uv run sage --repo . -o ./out
uv run sage --help
```

## オプション

| オプション | 説明 |
| --- | --- |
| `--repo` | 解析対象のリポジトリパス |
| `-o`, `--output` | 生成ファイルの出力先 |
| `-l`, `--lang`, `--language` | 出力言語 (`en` / `ja`) |
| `--ignore-file` | ignore ファイルの上書き指定 |
| `--language-map` | 言語マップ JSON の上書き指定 |
| `--diff` | 旧来の release diff レポートフロー |
| `--repo-path` | 旧来の diff フロー用 Git リポジトリパス |

## 補足

- カスタム ignore ファイルを渡すときは `--ignore-file` が正式な指定方法です。
- `--diff` は互換性のため残していますが、新しいリリース運用には推奨していません。
- `--repo` を指定して `-o` を省略した場合、生成物は対象リポジトリ側へ書き込まれます。
