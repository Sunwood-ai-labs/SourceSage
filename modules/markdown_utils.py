import os
from modules.file_utils import is_excluded

def generate_markdown_for_folder(folder_path, exclude_patterns, language_map):
    markdown_content = "```plaintext\n"
    markdown_content += _display_tree(dir_path=folder_path, exclude_patterns=exclude_patterns)
    markdown_content += "\n```\n\n"
    base_level = folder_path.count(os.sep)
    for root, dirs, files in os.walk(folder_path, topdown=True):
        dirs[:] = [d for d in dirs if not is_excluded(os.path.join(root, d), exclude_patterns)]
        level = root.count(os.sep) - base_level + 1
        header_level = '#' * (level + 1)
        relative_path = os.path.relpath(root, folder_path)
        markdown_content += f"{header_level} {relative_path}\n\n"
        for f in files:
            file_path = os.path.join(root, f)
            if is_excluded(file_path, exclude_patterns):
                continue
            relative_file_path = os.path.relpath(file_path, folder_path)
            try:
                with open(file_path, 'r', encoding='utf-8') as file_content:
                    content = file_content.read().strip()
                    language = _get_language_for_file(f, language_map)
                    markdown_content += f"`{relative_file_path}`\n\n```{language}\n{content}\n```\n\n"
            except Exception as e:
                markdown_content += f"`{relative_file_path}` - Error reading file: {e}\n\n"
    return markdown_content

def _display_tree(dir_path='.', exclude_patterns=None, string_rep=True, header=True, max_depth=None, show_hidden=False):
    tree_string = ""
    if header:
        tree_string += f"OS: {os.name}\nDirectory: {os.path.abspath(dir_path)}\n\n"
    tree_string += _build_tree_string(dir_path, max_depth, show_hidden, exclude_patterns, depth=0)
    if string_rep:
        return tree_string.strip()
    else:
        print(tree_string.strip())

def _build_tree_string(dir_path, max_depth, show_hidden, exclude_patterns, depth=0):
    tree_string = ""
    if depth == max_depth:
        return tree_string
    for item in os.listdir(dir_path):
        if not show_hidden and item.startswith('.'):
            continue
        item_path = os.path.join(dir_path, item)
        if is_excluded(item_path, exclude_patterns):
            continue
        if os.path.isdir(item_path):
            tree_string += '│  ' * depth + '├─ ' + item + '/\n'
            tree_string += _build_tree_string(item_path, max_depth, show_hidden, exclude_patterns, depth + 1)
        else:
            tree_string += '│  ' * depth + '├─ ' + item + '\n'
    return tree_string

def _get_language_for_file(filename, language_map):
    _, extension = os.path.splitext(filename)
    extension = extension.lower()
    return language_map.get(extension, 'plaintext')