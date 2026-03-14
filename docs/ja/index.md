---
layout: home

hero:
  name: "SourceSage"
  text: "AI 向けのリポジトリ要約を CLI から生成"
  tagline: "リポジトリを解析し、ignore ルールを統合し、Git 情報を集め、アシスタントがそのまま読める Markdown にまとめます。"
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
  - title: リポジトリ要約を最優先
    details: `.SourceSageAssets/Repository_summary.md` に構造、統計、Git 文脈、ファイル抜粋をまとめて出力します。
  - title: 既存の ignore 運用と自然に共存
    details: `.gitignore` と `.SourceSageignore` を統合して扱い、後者がなければ自動生成します。
  - title: 英日バイリンガル出力
    details: `-l en` と `-l ja` で要約見出しを切り替え、ドキュメントも英日で同じ構成に揃えています。
---

## SourceSage が向いている場面

SourceSage は、アシスタントにコードベースの全体像を素早く渡したいときに向いています。単なるツリー表示ではなく、Git 文脈と要約済みの Markdown をセットで生成します。

## 次に見るページ

- [はじめに](/ja/guide/getting-started)
- [CLI リファレンス](/ja/guide/cli)
- [出力ガイド](/ja/guide/output)
