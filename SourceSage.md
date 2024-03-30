# Project: SourceSage

```plaintext
OS: nt
Directory: C:\Prj\SourceSage

├─ config/
│  ├─ language_map.json
├─ docs/
├─ modules/
│  ├─ file_utils.py
│  ├─ main.py
│  ├─ markdown_utils.py
│  ├─ source_sage.py
│  ├─ __init__.py
├─ README.md
├─ SourceSage.py
```

## .

`README.md`

```markdown
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
```

`SourceSage.py`

```python
import os
import sys

sys.path.append('modules')
import sys
import pprint
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

pprint.pprint(sys.path)

from modules.source_sage import SourceSage

if __name__ == "__main__":
    folders = ['./']
    source_sage = SourceSage(folders, ignore_file='.SourceSageignore',
                             output_file='SourceSage.md',
                             language_map_file='config/language_map.json')
    source_sage.generate_markdown()
```

## .vscode

`.vscode\settings.json`

```json
{
    "gitlens.ai.experimental.openai.url": "",
    "gitlens.ai.experimental.provider": "anthropic",
    "gitlens.ai.experimental.anthropic.model": "claude-3-haiku-20240307",
    "gitlens.experimental.generateCommitMessagePrompt": "日本語でシンプルなコミットメッセージ"
}
```

## config

`config\language_map.json`

```json
{
    ".py": "python",
    ".js": "javascript",
    ".java": "java",
    ".c": "c",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".go": "go",
    ".php": "php",
    ".rb": "ruby",
    ".rs": "rust",
    ".ts": "typescript",
    ".html": "html",
    ".css": "css",
    ".json": "json",
    ".xml": "xml",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".md": "markdown",
    ".txt": "plaintext",
    ".sh": "bash",
    ".sql": "sql",
    "Dockerfile": "dockerfile",
    ".dockerfile": "dockerfile",
    "docker-compose.yml": "yaml",
    "docker-compose.yaml": "yaml"
}
```

## docs

## modules

`modules\file_utils.py`

```python
import os
import fnmatch
import json

def load_ignore_patterns(ignore_file):
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    else:
        return []

def load_language_map(language_map_file):
    if os.path.exists(language_map_file):
        with open(language_map_file, 'r') as f:
            return json.load(f)
    else:
        return {}

def is_excluded(path, exclude_patterns):
    for pattern in exclude_patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
        if fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
    return False
```

`modules\main.py`

```python
from modules.source_sage import SourceSage

if __name__ == "__main__":
    folders = ['./']
    source_sage = SourceSage(folders, ignore_file='.SourceSageignore',
                             output_file='SourceSage.md',
                             language_map_file='config/language_map.json')
    source_sage.generate_markdown()
```

`modules\markdown_utils.py`

```python
import os
from file_utils import is_excluded

def generate_markdown_for_folder(folder_path, exclude_patterns, language_map):
    markdown_content = "```plaintext\n"
    markdown_content += _display_tree(dir_path=folder_path, exclude_patterns=exclude_patterns)
    markdown_content += "\n```\n\n"
    base_level = folder_path.count(os.sep)
    for root, dirs, files in os.walk(folder_path, topdown=True):
        dirs[:] = [d for d in dirs if not is_excluded(os.path.join(root, d), exclude_patterns)]
        level = root.count(os.sep) - base_level + 1
        header_level = '#' * (level + 1)
        relative_path = os.path.relpath(root, folder_path)
        markdown_content += f"{header_level} {relative_path}\n\n"
        for f in files:
            file_path = os.path.join(root, f)
            if is_excluded(file_path, exclude_patterns):
                continue
            relative_file_path = os.path.relpath(file_path, folder_path)
            try:
                with open(file_path, 'r', encoding='utf-8') as file_content:
                    content = file_content.read().strip()
                    language = _get_language_for_file(f, language_map)
                    markdown_content += f"`{relative_file_path}`\n\n```{language}\n{content}\n```\n\n"
            except Exception as e:
                markdown_content += f"`{relative_file_path}` - Error reading file: {e}\n\n"
    return markdown_content

def _display_tree(dir_path='.', exclude_patterns=None, string_rep=True, header=True, max_depth=None, show_hidden=False):
    tree_string = ""
    if header:
        tree_string += f"OS: {os.name}\nDirectory: {os.path.abspath(dir_path)}\n\n"
    tree_string += _build_tree_string(dir_path, max_depth, show_hidden, exclude_patterns, depth=0)
    if string_rep:
        return tree_string.strip()
    else:
        print(tree_string.strip())

def _build_tree_string(dir_path, max_depth, show_hidden, exclude_patterns, depth=0):
    tree_string = ""
    if depth == max_depth:
        return tree_string
    for item in os.listdir(dir_path):
        if not show_hidden and item.startswith('.'):
            continue
        item_path = os.path.join(dir_path, item)
        if is_excluded(item_path, exclude_patterns):
            continue
        if os.path.isdir(item_path):
            tree_string += '│  ' * depth + '├─ ' + item + '/\n'
            tree_string += _build_tree_string(item_path, max_depth, show_hidden, exclude_patterns, depth + 1)
        else:
            tree_string += '│  ' * depth + '├─ ' + item + '\n'
    return tree_string

def _get_language_for_file(filename, language_map):
    _, extension = os.path.splitext(filename)
    extension = extension.lower()
    return language_map.get(extension, 'plaintext')
```

`modules\source_sage.py`

```python
import os
from modules.file_utils import load_ignore_patterns, load_language_map, is_excluded
from modules.markdown_utils import generate_markdown_for_folder

class SourceSage:
    def __init__(self, folders, ignore_file='.SourceSageignore', output_file='output.md', language_map_file='language_map.json'):
        self.folders = folders
        self.ignore_file = ignore_file
        self.output_file = output_file
        self.exclude_patterns = load_ignore_patterns(ignore_file)
        self.language_map = load_language_map(language_map_file)

    def generate_markdown(self):
        with open(self.output_file, 'w', encoding='utf-8') as md_file:
            project_name = os.path.basename(os.path.abspath(self.folders[0]))
            md_file.write(f"# Project: {project_name}\n\n")
            for folder in self.folders:
                markdown_content = generate_markdown_for_folder(folder, self.exclude_patterns, self.language_map)
                md_file.write(markdown_content + '\n\n')
```

`modules\__init__.py`

```python

```



