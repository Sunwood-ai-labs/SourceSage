![](https://raw.githubusercontent.com/Sunwood-ai-labs/zoltraak/celsius/assets/images/test_icon.jpeg)

# Test

このドキュメントでは、テストを実行するためのコマンドラインについて説明します。

## テストの実行

ユニットテストを実行するには、以下のコマンドを使用します。

```bash
pytest tests/test_sourcesage.py
```

このコマンドにより、`tests/test_sourcesage.py`ファイルに定義されたテストケースが実行されます。

## 本番環境でのテスト

SourceSageを本番環境でテストするには、以下のコマンドを実行します。

```bash
sourcesage
```

このコマンドにより、SourceSageが実行され、本番環境での動作を確認できます。

## リポジトリの指定

特定のリポジトリに対してSourceSageを実行する場合は、以下のようにオーナー名とリポジトリ名を指定します。

```bash
sourcesage --owner Sunwood-ai-labs --repository SourceSage
```

このコマンドにより、指定されたリポジトリ（この例では`Sunwood-ai-labs/SourceSage`）に対してSourceSageが実行されます。また、このコマンドを使用することで、指定したリポジトリのIssue情報も取得できます。