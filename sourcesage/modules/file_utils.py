import os
import fnmatch
import json

def load_ignore_patterns(ignore_file):
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    else:
        return []

def load_language_map(language_map_file):
    if os.path.exists(language_map_file):
        with open(language_map_file, 'r') as f:
            return json.load(f)
    else:
        return {}

def is_excluded(path, exclude_patterns):
    for pattern in exclude_patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
        if fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
    return False

def is_excluded_extension(filename, exclude_patterns):
    _, extension = os.path.splitext(filename)
    return any(fnmatch.fnmatch(extension, pattern) for pattern in exclude_patterns)