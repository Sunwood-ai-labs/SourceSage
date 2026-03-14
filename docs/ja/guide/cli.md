# CLI リファレンス

## 基本コマンド

```bash
uv run sage --help
```

このリポジトリでは `sage` と `sourcesage` の両方のエントリポイントを使えます。

## 主要オプション

| オプション | 役割 |
| --- | --- |
| `--repo <path>` | 解析対象のリポジトリを指定します。 |
| `-o, --output <dir>` | `<dir>/.SourceSageAssets/` 配下に生成物を書き出します。 |
| `-l, --lang {en,ja}` | 見出し言語を英語または日本語に切り替えます。 |
| `--ignore-file <path>` | SourceSage が使う ignore テンプレートの場所を明示します。 |
| `--language-map <path>` | 言語判定用の JSON を差し替えます。 |
| `-v, --version` | パッケージバージョンを表示します。 |

## 非推奨の差分レポート

```bash
uv run sage --repo . --diff
```

`--diff` は引き続き使えますが非推奨です。リポジトリに 2 つ以上のタグがある場合だけリリースレポートを生成します。

## Ignore の扱い

SourceSage は次の 2 つを統合して扱います。

- `.gitignore`
- `.SourceSageignore`

`.SourceSageignore` が無い場合は、解析開始前にデフォルトテンプレートを自動生成します。
