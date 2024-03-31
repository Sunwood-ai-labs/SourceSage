# modules/EnvFileHandler.py

import os

def create_or_append_env_file():
    env_file = ".env"
    env_vars = """
    
REPO_PATH=./
SOURCE_SAGE_ASSETS_DIR=SourceSageAssets
CONFIG_DIR=config
DOCS_DIR=docs
FOLDERS=./
IGNORE_FILE=.SourceSageignore
OUTPUT_FILE=SourceSage.md
LANGUAGE_MAP_FILE=config/language_map.json
ISSUE_LOG_DIR=ISSUE_LOG

OWNER=Sunwood-ai-labs
REPOSITORY=SourceSage
ISSUES_FILE_NAME=open_issues_filtered.json

ISSUES_RESOLVE_DIR=ISSUES_RESOLVE
STAGE_INFO_DIR=STAGE_INFO
"""

    if not os.path.exists(env_file):
        with open(env_file, "w") as f:
            f.write(env_vars)
        print(f"{env_file} created successfully.")
    else:
        with open(env_file, "r") as f:
            existing_vars = f.read()
        if not all(var in existing_vars for var in env_vars.split("\n")):
            with open(env_file, "a") as f:
                f.write("\n" + env_vars)
            print(f"{env_file} updated successfully.")
        else:
            print(f"{env_file} already contains the required variables.")