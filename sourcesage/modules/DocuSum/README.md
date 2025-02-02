# 📄 DocuSum

リポジトリの構造とファイル内容を解析し、詳細なマークダウンドキュメントを生成するPythonモジュール

## 🌟 概要

DocuSumは、プロジェクトの構造を分析し、以下の情報を含む包括的なドキュメントを生成します：

- 📂 ディレクトリ構造
- 🔍 Gitリポジトリ情報
- 📊 プロジェクト統計
- 📝 ファイル内容とメタデータ
- 📈 言語別統計

## 🎯 主な機能

### 1. Git情報の収集
- リモートURL、ブランチ情報
- 最新のコミット詳細
- タグ情報（最新5件）
- コントリビューター統計（上位5名）

### 2. プロジェクト分析
- ディレクトリ構造の可視化
- ファイルサイズと行数の統計
- 言語別の使用状況
- 最大ディレクトリの特定

### 3. ファイル処理
- gitignoreスタイルのパターンマッチング
- 言語自動検出
- バイナリファイルの適切な処理
- 大容量ファイルの制御

## 💻 使用方法

```python
from docusum import DocuSum

# 基本的な使用方法
docusum = DocuSum()
docusum.generate_markdown()

# カスタム設定を使用する場合
docusum = DocuSum(
    folders=['/path/to/project'],
    ignore_file='.customignore',
    output_file='output.md'
)
docusum.generate_markdown()
```

### CLIでの使用例

```bash
python docusum.py --git-path /path/to/your/repo/.git
```

## 📁 ファイル構成

- `docusum.py`: メインのクラスと処理ロジック
- `file_pattern_matcher.py`: ファイルパターンマッチング機能
- `file_processor.py`: ファイル処理とコンテンツ抽出
- `git_info_collector.py`: Git関連情報の収集
- `language_detector.py`: プログラミング言語の検出
- `markdown_writer.py`: マークダウン形式での出力
- `stats_collector.py`: 統計情報の収集
- `tree_generator.py`: ディレクトリツリーの生成

## 🛠️ カスタマイズ

### 除外パターンの設定

`.SourceSageignore` ファイルを使用して、特定のファイルやディレクトリを除外できます：

```plaintext
# バージョン管理システム関連
.git/
.gitignore

# キャッシュファイル
__pycache__/
*.pyc

# ビルド・配布関連
build/
dist/
*.egg-info/
```

### 言語マッピング

`language_map.json` で言語の検出ルールをカスタマイズできます：

```json
{
  ".py": "python",
  ".js": "javascript",
  ".md": "markdown"
}
```

## 📅 更新履歴

最終更新日: 2025-02-02

- マークダウン出力の改善
  - Git情報の詳細表示
  - プロジェクト統計に作成日時を追加
  - コントリビューター情報の表形式表示

## 🔧 要件

- Python 3.8以上
- loguru
- GitPython（オプション、Git情報収集用）

## 📝 ライセンス

本プロジェクトはMITライセンスの下で公開されています。
