import os

class SourceSage:
    def __init__(self, folders, exclude_patterns=None, output_file='output.md'):
        self.folders = folders
        self.exclude_patterns = exclude_patterns or []
        self.output_file = output_file

    def generate_markdown(self):
        with open(self.output_file, 'w', encoding='utf-8') as md_file:
            project_name = os.path.basename(os.path.abspath(self.folders[0]))
            md_file.write(f"# Project: {project_name}\n\n")
            for folder in self.folders:
                markdown_content = self._generate_markdown_for_folder(folder)
                md_file.write(markdown_content + '\n\n')

    def _generate_markdown_for_folder(self, folder_path):
        markdown_content = "```plaintext\n"
        markdown_content += self._display_tree(dir_path=folder_path)
        markdown_content += "\n```\n\n"
        base_level = folder_path.count(os.sep)
        for root, dirs, files in os.walk(folder_path, topdown=True):
            if self._is_excluded(root):
                dirs[:] = []  # Don't walk into excluded directories
                continue
            level = root.count(os.sep) - base_level + 1
            header_level = '#' * (level + 1)
            relative_path = os.path.relpath(root, folder_path)
            markdown_content += f"{header_level} {relative_path}\n\n"
            for f in files:
                file_path = os.path.join(root, f)
                if self._is_excluded(file_path):
                    continue
                relative_file_path = os.path.relpath(file_path, folder_path)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file_content:
                        content = file_content.read().strip()
                        markdown_content += f"`{relative_file_path}`\n\n```plaintext\n{content}\n```\n\n"
                except Exception as e:
                    markdown_content += f"`{relative_file_path}` - Error reading file: {e}\n\n"
        return markdown_content

    def _display_tree(self, dir_path='.', string_rep=True, header=True, max_depth=None, show_hidden=False):
        tree_string = ""
        if header:
            tree_string += f"OS: {os.name}\nDirectory: {os.path.abspath(dir_path)}\n\n"
        tree_string += self._build_tree_string(dir_path, max_depth, show_hidden, depth=0)
        if string_rep:
            return tree_string.strip()
        else:
            print(tree_string.strip())

    def _build_tree_string(self, dir_path, max_depth, show_hidden, depth=0):
        tree_string = ""
        if depth == max_depth:
            return tree_string
        for item in os.listdir(dir_path):
            if not show_hidden and item.startswith('.'):
                continue
            if self._is_excluded(item):
                continue
            item_path = os.path.join(dir_path, item)
            if os.path.isdir(item_path):
                tree_string += '│  ' * depth + '├─ ' + item + '/\n'
                tree_string += self._build_tree_string(item_path, max_depth, show_hidden, depth + 1)
            else:
                tree_string += '│  ' * depth + '├─ ' + item + '\n'
        return tree_string

    def _is_excluded(self, path):
        return any(pattern in path for pattern in self.exclude_patterns)

# 使用例
folders = ['./']  # 現在のディレクトリを対象に
exclude_patterns = ['.git', '__pycache__', 'LICENSE', 'output.md', 'README.md', 'docs']  # 除外するファイル/フォルダのパターン
source_sage = SourceSage(folders, exclude_patterns=exclude_patterns, output_file='SourceSage.md')
source_sage.generate_markdown()