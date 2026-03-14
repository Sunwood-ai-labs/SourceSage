# CLI リファレンス

## 基本コマンド

```bash
uv run sage --help
```

このリポジトリでは `sage` と `sourcesage` の両方のエントリポイントを利用できます。

## 主なオプション

| オプション | 役割 |
| --- | --- |
| `--repo <path>` | 解析対象のリポジトリを指定します。 |
| `-o, --output <dir>` | 生成ファイルを `<dir>/.SourceSageAssets/` 配下へ出力します。 |
| `-l, --lang {en,ja}` | ドキュメントの見出し言語を英語または日本語に切り替えます。 |
| `--lite` | ツリー、Git 情報、統計、ルート README だけを残し、全ファイル抜粋を省略します。 |
| `--ignore-file <path>` | SourceSage が使う ignore ファイルを上書きします。 |
| `--language-map <path>` | 言語マップ JSON を差し替えます。 |
| `-v, --version` | パッケージのバージョンを表示します。 |

## 非推奨の diff レポート

```bash
uv run sage --repo . --diff
```

`--diff` は互換性のために残っていますが、新しい運用では非推奨です。Git タグが 2 つ以上ある場合にだけリリース差分レポートを生成します。

## Ignore の扱い

SourceSage は次の 2 つを統合して使います。

- `.gitignore`
- `.SourceSageignore`

`.SourceSageignore` が無い場合は、解析前にデフォルトテンプレートを自動生成します。

## 初回探索におすすめの実行

```bash
uv run sage --repo . --lite
```

`--lite` は、ignore ルールを詰める前でもサマリーが全ファイル抜粋で膨らみすぎないようにするための軽量モードです。
