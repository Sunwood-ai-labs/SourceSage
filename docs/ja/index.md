---
layout: home

hero:
  name: "SourceSage"
  text: "コマンドラインから使える AI 向けリポジトリ要約 CLI"
  tagline: "リポジトリを解析し、ignore ルールを統合し、Git の文脈も含めた Markdown サマリを生成します。AI アシスタントがそのまま読める形に整えるためのツールです。"
  image:
    src: /hero.svg
    alt: SourceSage hero
  actions:
    - theme: brand
      text: はじめに
      link: /ja/guide/getting-started
    - theme: alt
      text: GitHub
      link: https://github.com/Sunwood-ai-labs/SourceSage
    - theme: alt
      text: English
      link: /

features:
  - title: "最初に欲しいのはリポジトリ要約"
    details: "`.SourceSageAssets/Repository_summary.md` に、ツリー構造、統計、Git 情報、ファイル抜粋をまとめて出力します。"
  - title: "馴染みのある ignore ルール"
    details: "`.gitignore` と `.SourceSageignore` を統合して使います。`.SourceSageignore` が無い場合はデフォルトテンプレートを自動生成します。"
  - title: "英語と日本語を切り替え可能"
    details: "`-l en` と `-l ja` で見出し言語を切り替えられ、ドキュメントも英日で揃えています。"
---

## SourceSage が役立つ場面

SourceSage は、AI アシスタントに作業を渡す前の下準備を軽くします。見通しの悪いディレクトリ一覧ではなく、構造化された Markdown のリポジトリ要約を渡せます。

## 次に見るページ

- [はじめに](/ja/guide/getting-started)
- [CLI リファレンス](/ja/guide/cli)
- [出力ガイド](/ja/guide/output)
