<p align="center">

<img src="docs/SourceSage_icon4.png" width="100%">

<br>

<h1 align="center">SourceSage</h1>

<h2 align="center">～Transforming code for AI～</h2>

</p>

SourceSageは、プロジェクトのソースコードとファイル構成を単一のマークダウンファイルに統合するPythonスクリプトです。これにより、大規模言語モデル（AI）がプロジェクト全体の構造と内容を容易に理解できるようになります。

## 更新内容

- 【2024/03/30】 ChangelogGenerator classを導入し、コードの可読性と保守性を向上
- 【2024/03/30】 言語ごとのシンタックスハイライト機能を追加
- 【2024/03/30】 対象フォルダの指定やファイルの除外設定を複数行対応
- 【2024/03/30】 コード生成時のエラー処理を改善
- 【2024/03/30】 設定ファイルの場所を外部化し、柔軟性を向上
- 【2024/03/30】 .SourceSageignoreファイルを導入し、不要なファイルやフォルダを自動的に除外
- 【2024/03/29】 初期リリース

## 特徴

- プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイルにまとめます
- AIがプロジェクトの概要を素早く把握できる構造化された形式で出力します
- 不要なファイルやディレクトリを除外する設定が可能です
- プロジェクトの全体像を明確かつ読みやすい方法で提示します
- 複数のプログラミング言語に対応し、シンタックスハイライト機能を提供します
- 設定ファイルを外部化することで、柔軟性と保守性を向上させています
- Gitの変更履歴を自動生成し、ドキュメント化することができます

## 使用方法

プロジェクトでSourceSageを使用するには、次の手順に従います：

1. `SourceSage.py`ファイルと`modules`フォルダを、分析対象のプロジェクトのルートディレクトリにコピーします。

2. 必要に応じて、`.SourceSageignore`ファイルを作成し、除外したいファイルやフォルダのパターンを記述します。

3. `config/language_map.json`ファイルを編集し、必要なプログラミング言語とそれに対応するシンタックスハイライトの識別子を設定します。

4. 必要に応じて、`SourceSage.py`内の以下の設定を変更します：

```python
folders = ['./'] # 分析対象のディレクトリ（現在のディレクトリを指定）
ignore_file = '.SourceSageignore' # 無視するファイル/フォルダのパターンを記述したファイル
output_file = 'docs/SourceSage.md' # 出力するマークダウンファイル名
language_map_file = 'config/language_map.json' # 言語マッピングの設定ファイル
```

5. ターミナルまたはコマンドプロンプトで、プロジェクトのルートディレクトリに移動し、以下のコマンドを実行します：

```bash
python SourceSage.py
```

これにより、AIがプロジェクトの構造と内容を理解しやすい形式のマークダウンファイル（デフォルトでは `docs/SourceSage.md`）が生成されます。また、Gitの変更履歴が`docs/Changelog`ディレクトリに自動生成されます。

## 出力例

生成されるマークダウンファイルの例は次のようになります：

````markdown
# Project: YourProjectName

```plaintext
OS: nt
Directory: C:\Prj\YourProjectName

├─ src/
│  ├─ main.py
│  ├─ utils/
│  │  ├─ helper.py
│  │  └─ constants.py
│  └─ tests/
│     └─ test_main.py
├─ docs/
│  └─ README.md
├─ .gitignore
└─ README.md
```

## src

### main.py

```python
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```

### utils

#### helper.py

```python
def greet(name):
    return f"Hello, {name}!"
```

#### constants.py

```python 
PI = 3.14159
```

...

## docs

### README.md

```markdown
# YourProjectName Documentation

This is the documentation for YourProjectName.

...
```
````

## 変更履歴の統合

SourceSageは、Gitリポジトリの変更履歴を自動的に生成し、ブランチごとにマークダウンファイルに出力します。さらに、すべてのブランチの変更履歴を1つのファイルに統合することができます。

生成される変更履歴の例は次のようになります：

````markdown
# Integrated Changelog

# Changelog

## develop

- [f26fca5] - Merge branch 'feature/modules' into develop (John Doe, 2023-03-30)
- [36d6a4a] - Refactor SourceSage.py to use modules (John Doe, 2023-03-30)
- [60ccecb] - Update SourceSage.md (John Doe, 2023-03-30)
- [6796a56] - Create language_map.json (John Doe, 2023-03-30)
- [d6e1af6] - Delete language_map.json (John Doe, 2023-03-30)

...

# Changelog - Features

## feature/add-git-logs

- [c346a22] - Introduce ChangelogGenerator class for improved readability and maintainability (Jane Smith, 2023-03-30)
- [0344765] - Update CHANGELOG.md (Jane Smith, 2023-03-30)
- [5c5e6ac] - Create get_git_log.py (Jane Smith, 2023-03-30)
- [8d4a253] - Create CHANGELOG.md (Jane Smith, 2023-03-30)

...
````

## 貢献

SourceSageの改善にご協力ください！バグの報告や機能追加の提案がある場合は、[GitHubリポジトリ](https://github.com/yourusername/SourceSage)でIssueを開くかプルリクエストを送信してください。

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

---