---
layout: home

hero:
  name: "SourceSage"
  text: "AI-friendly repository analysis and documentation from the command line"
  tagline: "Analyze a repository, merge ignore rules, collect Git context, and emit a structured Markdown documentation artifact that assistants can consume immediately."
  image:
    src: /hero.svg
    alt: SourceSage hero
  actions:
    - theme: brand
      text: Get Started
      link: /guide/getting-started
    - theme: alt
      text: View on GitHub
      link: https://github.com/Sunwood-ai-labs/SourceSage
    - theme: alt
      text: 日本語
      link: /ja/

features:
  - title: "Repository documentation first"
    details: "Generate `.SourceSageAssets/Repository_summary.md` as a structured documentation artifact with project structure, stats, Git context, and per-file excerpts."
  - title: "Ignore rules that feel familiar"
    details: "Merge `.gitignore` and `.SourceSageignore`, and create a default `.SourceSageignore` automatically when a repo does not have one yet."
  - title: "English and Japanese output"
    details: "Switch documentation headings with `-l en` or `-l ja` and keep the docs mirrored across both languages."
---

## Why SourceSage?

SourceSage is built for the moment before an assistant can help effectively. It gives an LLM a structured, repo-shaped documentation artifact instead of an opaque directory tree.

## What you can do next

- Start with the [Getting Started](/guide/getting-started) guide.
- Review the [CLI Reference](/guide/cli) for supported flags.
- Inspect the generated artifact layout in the [Output Guide](/guide/output).
