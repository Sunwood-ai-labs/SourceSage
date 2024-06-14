
# 使用方法

SourceSageを使用するには、まずPythonのパッケージマネージャーであるpipを使ってインストールします。

## セットアップ

```bash
pip install sourcesage
```

## 基本的な使い方

SourceSageをプロジェクトで使用するには、以下の手順に従ってください：

1. ターミナルまたはコマンドプロンプトを開きます。
2. `cd`コマンドを使って、解析対象のプロジェクトのルートディレクトリに移動します。
3. 次に、以下のコマンドを実行してSourceSageを起動します：
   ```bash
   sourcesage
   ```
4. SourceSageが実行されると、`SourceSageAssets`ディレクトリに各種ファイルが生成されます。

## リポジトリ情報の取得

デフォルトでは、SourceSageは現在のディレクトリをプロジェクトのルートとして解析します。ただし、GitHub上のリポジトリのIssueも取得したい場合は、以下のようにリポジトリのオーナー名とリポジトリ名をコマンドライン引数で指定します：

```bash
sourcesage --owner Sunwood-ai-labs --repository SourceSage
```

## 除外ファイルの指定

作業ディレクトリに`.SourceSageignore`ファイルを作成することで、任意のファイルやディレクトリを処理から除外できます。このファイルには、除外したいファイルやディレクトリのパターンを1行ずつ記述します。

`.SourceSageignore`ファイルを使用する場合は、以下のようにコマンドライン引数で指定します：

```bash
sourcesage --owner Sunwood-ai-labs --repository SourceSage --ignore-file .SourceSageignore
```
