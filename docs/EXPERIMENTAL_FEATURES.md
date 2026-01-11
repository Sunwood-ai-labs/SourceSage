
<div align="center">

![Image](https://github.com/user-attachments/assets/0ea1d6ce-c6f1-4e5a-95cf-098fc64e8f49)

# 🧪 実験的機能

SourceSageには以下の実験的機能が含まれています。これらの機能は開発中であり、将来的に変更される可能性があります。

</div>

## IssueWize：AIを活用した効率的なIssue作成

```bash
sourcesage --mode IssueWize --issue-summary "IssueWize.pyをSourceSageのCLIコマンドから実行できるようにコマンドを追加する。SourceSageのCLIコマンドからパラメータを指定できるようにしたい（repo_overview_fileやモデル名などのパラメータ）" --project-name "TaskSphere" --milestone-name "Sprint01" --repo-overview-file ".SourceSageAssets/Repository_summary.md" --issuewize-model "gemini/gemini-1.5-flash"
```

詳しくは[こちら`docs/ISSUEWIZE.md`](ISSUEWIZE.md)

## CommitCraft：AIを活用した効率的なコミットメッセージ生成

```bash
sourcesage --mode CommitCraft --model-name "gemini/gemini-1.5-pro-latest" --stage-info-file ".SourceSageAssets/COMMIT_CRAFT/STAGE_INFO/STAGE_INFO_AND_PROMT_GAIAH_B.md" --commit-craft-output ".SourceSageAssets/COMMIT_CRAFT/" --llm-output "llm_output.md"
```

詳しくは[こちら`docs/COMMITCRAFT.md`](COMMITCRAFT.md)

## DocuMind：AIを活用した効率的なリリースノート生成

```bash
sourcesage --mode DocuMind --docuMind-model "gemini/gemini-1.5-pro-latest" --docuMind-db ".SourceSageAssets/Repository_summary.md" --docuMind-release-report ".SourceSageAssets/RELEASE_REPORT/Report_v5.0.2.md"  --docuMind-changelog ".SourceSageAssets/Changelog/CHANGELOG_release_5.0.2.md"  --docuMind-output ".SourceSageAssets/RELEASE_NOTES_v5.0.2.md"  --docuMind-prompt-output ".SourceSageAssets/_PROMPT.md"  --repo-name "SourceSage" --repo-version "v0.5.0"
```

```bash
sourcesage --mode=DocuMind --yaml-file=docs\.sourcesage_releasenotes.yml
```

詳しくは[こちら`docs/DOCUMIND.md`](DOCUMIND.md)
