

<p align="center">
    <img src="docs/SourceSage_icon4.png" width="100%">
    <br>
    <h1 align="center">SourceSage</h1>
    <h2 align="center">～Transforming code for AI～</h2>
</p>


SourceSageは、プロジェクトのソースコードを構造化されたマークダウン形式で表現するPythonスクリプトです。コードベースの構造と内容を分析し、理解するための簡単な方法を提供します。

## 特徴

- プロジェクトのディレクトリとファイルをツリー状の構造でマークダウンファイルに生成します
- 各ファイルの内容をマークダウン出力に含めます
- 出力から特定のファイルとディレクトリを除外できます
- プロジェクトの構造をわかりやすく読みやすい形式で表現します

## 使用方法

プロジェクトでSourceSageを使用するには、次の手順に従います：

1. `SourceSage.py`ファイルを、分析したいプロジェクトのルートディレクトリにコピーします。

2. 必要に応じて、`SourceSage.py`内の以下の設定を変更します：

```python
folders = ['./']  # 分析対象のディレクトリ（現在のディレクトリを指定）
exclude_patterns = ['.git', '__pycache__', 'LICENSE', 'output.md', 'README.md', 'docs']  # 除外するファイル/フォルダのパターン
output_file = 'output.md'  # 出力するマークダウンファイル名
```

3. ターミナルまたはコマンドプロンプトで、プロジェクトのルートディレクトリに移動し、以下のコマンドを実行します：

```
python SourceSage.py
```

これにより、プロジェクトのソースコードの構造化された表現を含むマークダウンファイル（デフォルトでは `output.md`）が生成されます。

## 出力例

生成されるマークダウンファイルの例は次のようになります：

```markdown
# プロジェクト名: YourProjectName

## ディレクトリ構造

├─ src/
│  ├─ main.py
│  ├─ utils/
│  │  ├─ helper.py
│  │  └─ constants.py
│  └─ tests/
│     └─ test_main.py
└─ README.md

## ファイルの内容

`src/main.py`

'''python
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
'''

...
```

## 貢献

貢献は大歓迎です！問題を見つけたり、改善のための提案がある場合は、[GitHubリポジトリ](https://github.com/yourusername/SourceSage)でIssueを開くかプルリクエストを送信してください。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下でライセンスされています。

---
