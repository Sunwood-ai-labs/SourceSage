import os
from litellm import completion
from loguru import logger
from dotenv import load_dotenv
from art import *
import re
import markdown
from bs4 import BeautifulSoup
import html2text
from bs4 import BeautifulSoup, NavigableString

# import litellm
# litellm.set_verbose=True

class CommitCraftExtension(markdown.Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(CommitCraftPreprocessor(md), 'commit_craft', 175)

class CommitCraftPreprocessor(markdown.preprocessors.Preprocessor):
    def run(self, lines):
        new_lines = []
        in_commit_craft = False
        in_commit_msg = False
        for line in lines:
            if line.strip() == '```commit-craft':
                in_commit_craft = True
                new_lines.append('<div class="commit-craft">')
            elif line.strip() == '```commit-msg' and in_commit_craft:
                in_commit_msg = True
                new_lines.append('<div class="commit-msg">')
            elif line.strip() == '```' and in_commit_msg:
                in_commit_msg = False
                new_lines.append('</div>')
            elif line.strip() == '```' and in_commit_craft:
                in_commit_craft = False
                new_lines.append('</div>')
            else:
                new_lines.append(line)
        return new_lines

class CommitCraft:
    def __init__(self, model_name, stage_info_file, llm_output_file, html_output_file=None):
        self.model_name = model_name
        self.stage_info_file = stage_info_file
        self.llm_output_file = llm_output_file
        self.html_output_file = html_output_file
        
        tprint("CommitCraft")

    def html_to_markdown(self, element, indent=0):
        if isinstance(element, NavigableString):
            return element.strip()
        
        result = []
        if element.name == 'div' and 'commit-msg' in element.get('class', []):
            result.append('```commit-msg')
            for child in element.children:
                result.append(self.html_to_markdown(child, indent + 1))
            result.append('```')
        elif element.name in ['p', 'div']:
            for child in element.children:
                result.append(self.html_to_markdown(child, indent))
        elif element.name == 'ul':
            for li in element.find_all('li', recursive=False):
                result.append(f"{'  ' * indent}- {self.html_to_markdown(li, indent + 1)}")
        else:
            for child in element.children:
                result.append(self.html_to_markdown(child, indent))
        
        return '\n'.join(result)

    def extract_and_format_markdown_content(self, content):
        # Convert Markdown to HTML with custom extension
        html_content = markdown.markdown(content, extensions=[CommitCraftExtension()])
        
        # Save the HTML content to a file
        if(self.html_output_file):
            with open(self.html_output_file, "w", encoding="utf-8") as f:
                f.write(html_content)
        
        logger.success(f"HTML content saved to {self.html_output_file}")
        
        # Parse HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the commit-craft block
        commit_craft_block = soup.find('div', class_='commit-craft')
        
        if commit_craft_block:
            # Convert HTML back to Markdown
            markdown_content = self.html_to_markdown(commit_craft_block)
            
            return markdown_content.strip()
        else:
            return None

    def generate_commit_messages(self):
        if self.model_name is None:
            logger.info("モデル名が指定されていません。CommitCraftをスキップします。")
            return

        with open(self.stage_info_file, "r", encoding="utf-8") as f:
            stage_info_content = f.read()
            
        logger.info(f"ステージ情報ファイル : '{self.stage_info_file}'")
        logger.info(f"モデル'{self.model_name}'を使用してLLMにステージ情報を送信しています...")
        response = completion(
            model=self.model_name, 
            messages=[{"role": "user", "content": stage_info_content}]
        )

        # レスポンスからコンテンツを抽出
        content = response.get('choices', [{}])[0].get('message', {}).get('content')

        # コンテンツからcommit-craftブロック内の内容を抽出し整形
        extracted_content = self.extract_and_format_markdown_content(content)
        
        if extracted_content:
            logger.info("抽出・整形されたcommit-craftブロックの内容:")
            logger.info(extracted_content)
            
            # 抽出・整形されたコンテンツを指定されたファイルに書き込む
            with open(self.llm_output_file, "w", encoding="utf-8") as f:
                f.write(extracted_content)
            
            logger.success(f"抽出・整形されたcommit-craftブロックの内容が{self.llm_output_file}に保存されました。")
        else:
            logger.info("commit-craftブロックは見つかりませんでした。")

# 使用例
if __name__ == "__main__":
    # 注意: この例では実際のLLM呼び出しは行いません
    commit_craft = CommitCraft("gpt-3.5-turbo", "stage_info.md", "llm_output.md", "output.html")
    
    # LLMレスポンスのシミュレーション
    mock_llm_response = {
        'choices': [{
            'message': {
                'content': '''ここにLLMの応答が入ります。例えば：

```commit-craft
# ✨ feat: ファイル変換機能を実装

## feature/file-converter

### app.py

```commit-msg
✨ feat: ファイル変換機能を実装

- Streamlitを用いて.py、.ipynb、.mdファイルを変換するアプリを作成しました。
- ユーザーは変換したいファイルと出力形式を選択できます。
- Jupytextライブラリを用いてファイル変換を行います。
- 変換されたファイルはダウンロードできます。
```
```

これが抽出すべき内容です。'''
            }
        }]
    }
    
    # モックレスポンスからコンテンツを抽出
    content = mock_llm_response.get('choices', [{}])[0].get('message', {}).get('content')
    
    # コンテンツからcommit-craftブロック内の内容を抽出し整形
    extracted_content = commit_craft.extract_and_format_markdown_content(content)
    
    if extracted_content:
        print("抽出・整形されたcommit-craftブロックの内容:")
        print(extracted_content)
        
        # 抽出・整形されたコンテンツを指定されたファイルに書き込む
        with open("llm_output.md", "w", encoding="utf-8") as f:
            f.write(extracted_content)
    else:
        print("commit-craftブロックは見つかりませんでした。")
