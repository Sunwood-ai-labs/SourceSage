<p align="center">

<img src="docs/SourceSage_icon4.png" width="100%">

<br>

<h1 align="center">SourceSage</h1>

<h2 align="center">～Transforming code for AI～</h2>

</p>

SourceSageは、プロジェクトのソースコードとファイル構成を単一のマークダウンファイルに統合するPythonスクリプトです。これにより、大規模言語モデル（AI）がプロジェクト全体の構造と内容を容易に理解できるようになります。

## 特徴

- プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイルにまとめます
- AIがプロジェクトの概要を素早く把握できる構造化された形式で出力します
- 不要なファイルやディレクトリを除外する設定が可能です
- プロジェクトの全体像を明確かつ読みやすい方法で提示します

## 使用方法

プロジェクトでSourceSageを使用するには、次の手順に従います：

1. `SourceSage.py`ファイルを、分析対象のプロジェクトのルートディレクトリにコピーします。

2. 必要に応じて、`SourceSage.py`内の以下の設定を変更します：

```python
folders = ['./'] # 分析対象のディレクトリ（現在のディレクトリを指定）
exclude_patterns = ['.git', '__pycache__', 'LICENSE', 'output.md', 'README.md', 'docs'] # 除外するファイル/フォルダのパターン 
output_file = 'output.md' # 出力するマークダウンファイル名
```

3. ターミナルまたはコマンドプロンプトで、プロジェクトのルートディレクトリに移動し、以下のコマンドを実行します：

```bash
python SourceSage.py
```

これにより、AIがプロジェクトの構造と内容を理解しやすい形式のマークダウンファイル（デフォルトでは `output.md`）が生成されます。

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

SourceSageの改善にご協力ください！バグの報告や機能追加の提案がある場合は、[GitHubリポジトリ](https://github.com/yourusername/SourceSage)でIssueを開くかプルリクエストを送信してください。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

---