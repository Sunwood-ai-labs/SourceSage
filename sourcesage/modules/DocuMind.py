# sourcesage\modules\DocuMind.py
import os
from litellm import completion
from loguru import logger
from dotenv import load_dotenv
from art import *

class DocuMind:
    def __init__(self, model_name, documen_db_path, release_report_path, changelog_path, repo_name, repo_version, prompt_output_path):
        
        tprint("DocuMind")
        
        self.model_name = model_name
        self.documen_db_path = documen_db_path
        self.release_report_path = release_report_path.format(latest_tag=repo_version)
        self.changelog_path = changelog_path.format(version=repo_version)
        self.repo_name = repo_name
        self.repo_version = repo_version
        self.prompt_output_path = prompt_output_path
        self.documen_db = self.load_documen_db()
        self.release_report = self.load_release_report()
        self.changelog = self.load_changelog()
        

    def load_documen_db(self):
        """DocuMindファイルを読み込む"""
        with open(self.documen_db_path, "r", encoding="utf-8") as file:
            return file.read()

    def load_release_report(self):
        """リリースレポートファイルを読み込む"""
        if os.path.exists(self.release_report_path):
            with open(self.release_report_path, "r", encoding="utf-8") as file:
                return file.read()
        else:
            logger.warning(f"リリースレポートファイル'{self.release_report_path}'が見つかりませんでした。スキップします。")
            return ""

    def load_changelog(self):
        """変更履歴ファイルを読み込む"""
        if os.path.exists(self.changelog_path):
            with open(self.changelog_path, "r", encoding="utf-8") as file:
                return file.read()
        else:
            logger.warning(f"変更履歴ファイル'{self.changelog_path}'が見つかりませんでした。スキップします。")
            return ""

    def generate_release_notes(self):
        """リリースノートを生成する"""

        prompt = f"""
以下の情報を元に、リリースノートの要件に従って{self.repo_name}の新バージョン{self.repo_version}の日本語のリリースノートを生成してください。

# リリースノートの要件:
<Release notes requirements>
1. 簡潔で明確な概要から始めてください。
2. 主要な新機能、改善点、バグ修正を箇条書きで列挙してください。
3. 各項目に関連するコミットハッシュがある場合は、(commit: abc1234のように)括弧内に記載してください。ハッシュは最初の7文字のみ使用してください。
4. 重要な変更や注意が必要な点があれば、別セクションで強調してください。
5. アップグレード手順や互換性に関する注意事項があれば記載してください。
6. 貢献者への謝辞を含めてください（もし情報があれば）。
7. 各セクションに適切な絵文字を使用して、視覚的に分かりやすくしてください。
8. 完成されたマークダウン形式のリリースノートを作成してください。

下記の情報を基に、要件とフォーマットに従ってリリースノートを生成してください。
情報が不足している場合は、適切に省略するか、一般的な表現で補完してください。
コミットハッシュが提供されていない場合は、その項目にハッシュを含めないでください。
絵文字は適切に使用し、読みやすさと視覚的魅力を向上させてください。

</Release notes requirements>

# 絵文字の使用ガイドライン:
<Emoji usage guidelines>
- 新機能: 🎉 (パーティーポッパー)
- 改善点: 🚀 (ロケット)
- バグ修正: 🐛 (バグ)
- 重要な変更: ⚠️ (警告)
- セキュリティ関連: 🔒 (鍵)
- パフォーマンス改善: ⚡ (稲妻)
- ドキュメント: 📚 (本)
- 非推奨: 🗑️ (ゴミ箱)
- 削除された機能: 🔥 (炎)
</Emoji usage guidelines>

# リリースノートのフォーマット:
<Release notes format>
# 🚀 {self.repo_name} v{self.repo_version} リリースノート

## 📋 概要
[全体的な変更の要約と主要なハイライトを1-2文で]

## ✨ 新機能
- 🎉 [新機能1の説明] (commit: 1234567)
- 🎉 [新機能2の説明] (commit: 89abcde)

## 🛠 改善点
- 🚀 [改善点1の説明] (commit: fghijkl)
- ⚡ [パフォーマンス改善の説明] (commit: mnopqrs)

## 🐛 バグ修正
- 🐛 [修正されたバグ1の説明] (commit: tuvwxyz)
- 🐛 [修正されたバグ2の説明] (commit: 0123456)

## ⚠️ 重要な変更
- ⚠️ [重要な変更点や注意が必要な点]
- 🔥 [削除された機能の説明]

## 📦 アップグレード手順
[必要に応じてアップグレード手順や注意事項を記載]

## 👏 謝辞
[貢献者への謝辞]
</Release notes format>

# 入力情報:
<Input information>

## リポジトリ情報
<Repository information>
{self.documen_db}
</Repository information>

## 前のVerとの差分レポート
<Difference report with previous version>
{self.release_report}
</Difference report with previous version>

## 変更履歴
<change history>
{self.changelog}
</change history>

</Input information>

        """

        self.save_prompt(prompt)

        if self.model_name is None:
            logger.warning("モデル名が指定されていないため、リリースノートの生成をスキップします。")
            return ""

        logger.info(f"モデル'{self.model_name}'を使用してLLMにリリースノート生成を依頼しています...")
        try:
            response = completion(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            release_notes = response.get('choices', [{}])[0].get('message', {}).get('content', '')
            return release_notes
        except Exception as e:
            logger.error(f"リリースノートの生成中にエラーが発生しました: {str(e)}")
            return ""

    def save_prompt(self, prompt):
        """プロンプトを保存する"""
        with open(self.prompt_output_path, "w", encoding="utf-8") as file:
            file.write(prompt)
        logger.success(f"プロンプトが{self.prompt_output_path}に保存されました。")

    def save_release_notes(self, output_path, release_notes):
        """リリースノートを保存する"""
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(release_notes)
        logger.success(f"リリースノートが{output_path}に保存されました。")
