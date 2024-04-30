import os
from .file_utils import is_excluded, is_excluded_extension
from loguru import logger

def generate_markdown_for_folder(folder_path, exclude_patterns, language_map):
    markdown_content = "```plaintext\n"
    logger.info(f"folder_path is ... {folder_path}")
    markdown_content += _display_tree(dir_path=folder_path, exclude_patterns=exclude_patterns)
    markdown_content += "\n```\n\n"
    base_level = folder_path.count(os.sep)
    for root, dirs, files in os.walk(folder_path, topdown=True):
        dirs[:] = [d for d in dirs if not is_excluded(os.path.join(root, d), exclude_patterns)]
        files = [f for f in files if not is_excluded(os.path.join(root, f), exclude_patterns) and not is_excluded_extension(f, exclude_patterns)]
        level = root.count(os.sep) - base_level + 1
        header_level = '#' * (level + 1)
        relative_path = os.path.relpath(root, folder_path)
        markdown_content += f"{header_level} {relative_path}\n\n"
        for f in files:
            file_path = os.path.join(root, f)
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
        logger.info(tree_string.strip())

def _build_tree_string(dir_path, max_depth, show_hidden, exclude_patterns, depth=0):
    tree_string = ""
    if depth == max_depth:
        return tree_string
    
    logger.info(f"dir_path is ... {dir_path}")
    dir_contents = [(item, os.path.join(dir_path, item)) for item in os.listdir(dir_path)]
    dirs = [(item, path) for item, path in dir_contents if os.path.isdir(path) and not is_excluded(path, exclude_patterns)]
    files = [(item, path) for item, path in dir_contents if os.path.isfile(path) and not is_excluded(path, exclude_patterns) and not is_excluded_extension(item, exclude_patterns)]
    for item, path in dirs:
        if not show_hidden and item.startswith('.'):
            continue
        tree_string += '│  ' * depth + '├─ ' + item + '/\n'
        tree_string += _build_tree_string(path, max_depth, show_hidden, exclude_patterns, depth + 1)
    for item, path in files:
        if not show_hidden and item.startswith('.'):
            continue
        tree_string += '│  ' * depth + '├─ ' + item + '\n'
    return tree_string

def _get_language_for_file(filename, language_map):
    _, extension = os.path.splitext(filename)
    extension = extension.lower()
    return language_map.get(extension, 'plaintext')