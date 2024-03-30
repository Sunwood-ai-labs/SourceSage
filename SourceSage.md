# Project: SourceSage

```plaintext
OS: nt
Directory: C:\Prj\SourceSage

├─ docs/
├─ README.md
├─ SourceSage.py
```

## .

`README.md`

```plaintext
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

```
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
```

`SourceSage.py`

```plaintext
import os
import fnmatch

class SourceSage:
    def __init__(self, folders, ignore_file='.SourceSageignore', output_file='output.md'):
        self.folders = folders
        self.ignore_file = ignore_file
        self.output_file = output_file
        self.exclude_patterns = self._load_ignore_patterns()

    def _load_ignore_patterns(self):
        if os.path.exists(self.ignore_file):
            with open(self.ignore_file, 'r') as f:
                return [line.strip() for line in f if line.strip() and not line.startswith('#')]
        else:
            return []

    def generate_markdown(self):
        with open(self.output_file, 'w', encoding='utf-8') as md_file:
            project_name = os.path.basename(os.path.abspath(self.folders[0]))
            md_file.write(f"# Project: {project_name}\n\n")
            for folder in self.folders:
                markdown_content = self._generate_markdown_for_folder(folder)
                md_file.write(markdown_content + '\n\n')

    def _generate_markdown_for_folder(self, folder_path):
        markdown_content = "```plaintext\n"
        markdown_content += self._display_tree(dir_path=folder_path)
        markdown_content += "\n```\n\n"
        base_level = folder_path.count(os.sep)
        for root, dirs, files in os.walk(folder_path, topdown=True):
            dirs[:] = [d for d in dirs if not self._is_excluded(os.path.join(root, d))]
            level = root.count(os.sep) - base_level + 1
            header_level = '#' * (level + 1)
            relative_path = os.path.relpath(root, folder_path)
            markdown_content += f"{header_level} {relative_path}\n\n"
            for f in files:
                file_path = os.path.join(root, f)
                if self._is_excluded(file_path):
                    continue
                relative_file_path = os.path.relpath(file_path, folder_path)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file_content:
                        content = file_content.read().strip()
                        markdown_content += f"`{relative_file_path}`\n\n```plaintext\n{content}\n```\n\n"
                except Exception as e:
                    markdown_content += f"`{relative_file_path}` - Error reading file: {e}\n\n"
        return markdown_content

    def _display_tree(self, dir_path='.', string_rep=True, header=True, max_depth=None, show_hidden=False):
        tree_string = ""
        if header:
            tree_string += f"OS: {os.name}\nDirectory: {os.path.abspath(dir_path)}\n\n"
        tree_string += self._build_tree_string(dir_path, max_depth, show_hidden, depth=0)
        if string_rep:
            return tree_string.strip()
        else:
            print(tree_string.strip())

    def _build_tree_string(self, dir_path, max_depth, show_hidden, depth=0):
        tree_string = ""
        if depth == max_depth:
            return tree_string
        for item in os.listdir(dir_path):
            if not show_hidden and item.startswith('.'):
                continue
            item_path = os.path.join(dir_path, item)
            if self._is_excluded(item_path):
                continue
            if os.path.isdir(item_path):
                tree_string += '│  ' * depth + '├─ ' + item + '/\n'
                tree_string += self._build_tree_string(item_path, max_depth, show_hidden, depth + 1)
            else:
                tree_string += '│  ' * depth + '├─ ' + item + '\n'
        return tree_string

    def _is_excluded(self, path):
        for pattern in self.exclude_patterns:
            if fnmatch.fnmatch(path, pattern):
                return True
            if fnmatch.fnmatch(os.path.basename(path), pattern):
                return True
        return False

# 使用例
folders = ['./']  # 現在のディレクトリを対象に
source_sage = SourceSage(folders, ignore_file='.SourceSageignore', output_file='SourceSage.md')
source_sage.generate_markdown()
```

## docs



