# Changelog

## release/4.1.0

- [f81b386] - Merge branch 'feature/local-config-files' into develop (Maki, 2024-04-07)
- [b768351] - [feat] プロジェクト全体の出力ファイル名と各モジュールの出力フォルダ名の変更

- プロジェクト全体の出力ファイル名を "SourceSage" から "DocuMind" に変更
- 関連するディレクトリ名とファイル名を新しいプロジェクト全体の出力ファイル名に合わせて更新

## 変更の詳細

### setup.py
- バージョン番号を '4.0.11' から '4.0.12' に更新

### sourcesage/config/constants.py
- self.SOURCE_SAGE_MD の値を "SourceSage.md" から "DocuMind.md" に変更
- self.ISSUES_RESOLVE_DIR のパスを "SourceSageAssets/ISSUES_RESOLVE" から "SourceSageAssets/ISSUE_WISE/ISSUES_RESOLVE" に変更
- self.STAGE_INFO_DIR のパスを "SourceSageAssets/STAGE_INFO" から "SourceSageAssets/COMMIT_CRAFT/STAGE_INFO" に変更

これらの変更により、プロジェクト全体の出力ファイルの名称が "SourceSage" から "DocuMind" に切り替わり、関連するディレクトリ構造とファイル名が新しい名称に合わせて調整されました。 (Maki, 2024-04-07)
- [4d150e9] - [feat] PyPIのダウンロードバッジとCodacyのクオリティバッジを追加

## 概要

- README.mdにPyPIの日次ダウンロード数と週次ダウンロード数のバッジを追加
- README.mdにCodacyのクオリティバッジを追加
- README.mdにこのリポジトリ自体がSourceSageを活用していることを明記
- setup.pyのバージョンを4.0.10から4.0.11に更新
- setup.pyにclassifiersを追加し、プロジェクトの状態や対象ユーザー、トピックを明示

## 詳細

### README.mdの変更

- PyPIの日次ダウンロード数と週次ダウンロード数のバッジを追加することで、SourceSageの利用状況を可視化
- Codacyのクオリティバッジを追加し、コードの品質を保証
- このリポジトリ自体がSourceSageを活用していることを明記し、SourceSageの有用性を実証

### setup.pyの変更

- バージョンを4.0.10から4.0.11に更新し、新しいリリースを準備
- classifiersを追加することで、PyPIでのプロジェクトの分類や検索性を向上
 - Development Status: プロジェクトの開発状態がベータ版であることを明示
 - Intended Audience: 対象ユーザーが開発者であることを明示
 - Topic: SourceSageがユーティリティであることを明示 (Maki, 2024-04-07)
- [4771cfa] - [feat] setup.pyのバージョンを4.0.10に更新

setup.pyのバージョン番号を4.0.9から4.0.10に更新しました。この変更により、新しいバージョンのリリース準備が整いました。さらに、package_dataに新たな設定ファイル`config/.SourceSageignore`を追加しました。このファイルは、ソースコードのビルドやデプロイメント時に無視されるべきファイルを定義するために使用されます。

- バージョン番号を更新し、リリース準備を整える。
- 新しい設定ファイル`config/.SourceSageignore`を追加して、ビルドプロセスを改善する。 (Maki, 2024-04-07)
- [9afcee3] - [feat] SourceSageのバージョンアップとアスキーアートの追加

## 概要

- SourceSageのバージョンを4.0.5から4.0.9へアップデート
- SourceSageの起動時にアスキーアートでロゴを表示するように変更

## 詳細

### setup.py

- バージョン番号を4.0.5から4.0.9へ変更
- パッケージデータの指定方法を`'sourcesage': ['config/*']`から`'sourcesage': ['config/**/*']`へ変更し、サブディレクトリ以下のファイルも含めるように修正
- 依存ライブラリに`art`を追加

### sourcesage/core.py

- `art`ライブラリをインポート
- `SourceSage`クラスの`run`メソッドの先頭で、`tprint`関数を使用して"SourceSage"のアスキーアートロゴを表示するように変更

以上の変更により、SourceSageのバージョンアップとともに、起動時にアスキーアートでロゴが表示されるようになります。これにより、ユーザーにとってより印象的で認識しやすいツールになることが期待されます。 (Maki, 2024-04-07)
- [ae75e39] - [feat] CLI引数の追加とコアモジュールの修正

- `sourcesage/cli.py`と`sourcesage/core.py`に新しいCLI引数`--ignore-file`と`--language-map`を追加
  - デフォルト値はパッケージ内の設定ファイルを使用するように修正
- `SourceSage`クラスのコンストラクタに`ignore_file`と`language_map_file`の引数を追加
- `SourceSageModule`と`StagedDiffGenerator`の初期化時に、追加した引数を渡すように修正

[test] テストケースの修正

- `tests/test_sourcesage.py`のテストケースを修正
  - CLI引数のテストケースに`--ignore-file`と`--language-map`を追加
  - `SourceSage`クラスの直接実行テストケースで、追加した引数を渡すように修正 (Maki, 2024-04-07)
- [f04ab87] - [refactor] プロジェクトの構成とファイルの変更

以下のようなプロジェクトの構成とファイルの変更が行われました。

- `.env.example`ファイルを削除
- `SourceSage.py`ファイルを削除
- `docs/HTML/timeline_sample.md`ファイルを削除
- `docs/css/style.css`ファイルを削除
- `sourcesage/config/.SourceSageignore`ファイルを変更
  - `SourceSage`フォルダを除外対象から削除
  - `sourcesage.egg-info`フォルダを除外対象に追加
  - `.pytest_cache`フォルダを除外対象に追加
  - `dist`フォルダを除外対象に追加
  - `build`フォルダを除外対象に追加

これらの変更により、不要なファイルやフォルダが削除され、プロジェクトの構成がよりシンプルになりました。また、`.SourceSageignore`ファイルを更新することで、必要なフォルダや一時ファイルが除外対象になるように設定されました。 (Maki, 2024-04-07)
- [f1edd9c] - [docs] テストドキュメントの改善

## 概要

テストドキュメントを分かりやすく改善し、章立てやパラグラフ、箇条書きを使用して読みやすくしました。

## 詳細

- テストコマンドの説明を「テストの実行」という見出しに変更し、ユニットテストの実行方法を詳しく説明しました。
- 本番環境でのテストについて、新しい章を追加し、`sourcesage`コマンドの使用方法を説明しました。
- リポジトリの指定について、新しい章を追加し、オーナー名とリポジトリ名の指定方法を説明しました。
- コマンドのフォーマットをマークダウンのコードブロックで囲み、視覚的に分かりやすくしました。
- 各章の説明文を追加し、内容をより明確にしました。 (Maki, 2024-04-07)
- [556b275] - [feat] テストコードの修正とセットアップスクリプトの更新

## 変更内容

- テストコードの修正:
 - `test_sourcesage_cli` 関数内の `sys.argv` に `--owner` と `--repository` の引数を追加
 - `test_sourcesage_core` 関数内の `SourceSage` クラスのインスタンス化時に、`owner` と `repository` の引数を追加
 - これにより、テストコードが指定されたコマンド `sourcesage --owner Sunwood-ai-labs --repository SourceSage` に対応するように変更

- セットアップスクリプトの更新:
 - `setup.py` ファイルに `package_data` の設定を追加
 - これにより、`sourcesage` パッケージ内の `config` ディレクトリ以下のファイルがパッケージに含まれるように変更

## その他の変更

- `.gitignore` ファイルに `temp/` ディレクトリを追加
 - テスト実行時に生成される一時ディレクトリをGitの管理対象から除外するため (Maki, 2024-04-07)
- [1ea9ba4] - [style] README.mdにビジュアル要素を追加

README.mdファイルの見出し部分にビジュアル要素を追加し、ドキュメントの視覚的魅力を高めました。具体的な変更内容は以下の通りです：

1. プロジェクトの標語「～Transforming code for AI～」をより目立たせるために、中央揃えの見出しに変更し、周囲に余白を追加しました。
2. PyPIでの最新バージョンを示すバッジを挿入し、ユーザーが簡単に現在のバージョンを確認できるようにしました。このバッジは、プロジェクトが外部でどのように管理されているかの直感的な指標を提供します。
3. 余計な空白行を削除してドキュメントの整理を行い、情報の密度を高めました。

これらの変更により、読者はREADME.mdファイルを開いた瞬間に、プロジェクトの重要な情報を直感的に得られるようになります。 (Maki, 2024-04-05)
- [85a8f15] - [feat] README.mdの見出しとバッジの追加

README.mdの見出し部分にPyPIのバージョンバッジを追加し、見た目を改善しました。具体的には、以下の変更を行いました：

- 「Transforming code for AI」という見出しを中央揃えで改行を加えて明確にしました。
- PyPIの最新バージョンを示すバッジを追加し、ユーザーが最新のパッケージバージョンを一目で識別できるようにしました。
- 不要な空行を削除してドキュメントの構造を整理しました。

これらの変更により、README.mdの可読性と情報のアクセシビリティが向上し、ユーザーが必要な情報をより迅速に得られるようになります。 (Maki, 2024-04-05)
- [7246ba9] - [docs] README.md の更新

README.md ファイルにおけるセットアップ手順、実行方法、クイックスタートのセクションが更新されました。

### 変更内容の概要

- **セットアップ手順の追加**: SourceSageのインストールに必要な手順が追加されました。Pythonのパッケージマネージャーであるpipを使用したインストール方法が明記されています。

- **クイックスタートガイドの導入**: 新たにクイックスタートセクションを設け、SourceSageの基本的な使用方法についての手順が追加されました。このセクションでは、プロジェクトディレクトリへの移動からSourceSageの実行、生成されるファイルの説明までがステップバイステップで説明されています。

- **リポジトリのIssue取得方法に関する説明の改善**: GitHubのリポジトリIssueを取得する方法に関する説明が更新され、リポジトリのオーナー名とリポジトリ名をコマンドライン引数で指定する方法が詳述されました。
