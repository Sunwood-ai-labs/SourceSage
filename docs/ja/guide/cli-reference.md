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
| `-o`, `--output` | 生成物の出力先 |
| `-l`, `--lang`, `--language` | 出力言語 (`en` / `ja`) |
| `--ignore-file` | ignore ファイルを上書き指定 |
| `--language-map` | 言語マップ JSON を上書き指定 |
| `--diff` | 互換性のため残っている旧来の差分レポートフロー |
| `--repo-path` | 旧来の diff フロー用 Git リポジトリパス |

## 補足

- カスタム ignore ファイルは `--ignore-file` が正式な指定方法です。
- `--diff` は互換性のため残っていますが、新しいリリース導線にはおすすめしません。
- `--repo` を指定して `-o` を省略した場合、生成物は対象リポジトリ側へ書き込まれます。
