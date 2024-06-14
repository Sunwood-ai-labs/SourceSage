# sourcesage\modules\GitCommander.py
from loguru import logger
import subprocess

# logger.level("SUBCMD", no=25, color="<green>", icon="✓")
logger.level("SUBPROCESS", no=15, color="<cyan>", icon="🔍")

def run_command(command, cwd=None, check=True, preview=True):
    """
    指定されたコマンドを実行し、出力をキャプチャして表示します。
    """
    # logger.info(f">>>>>> 実行コマンド: {' '.join(command)}")
    if preview:
        logger.log("SUBPROCESS", f">>>>>> 実行コマンド: {' '.join(command)}")
    
    try:
        # result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
        result = subprocess.run(command, cwd=cwd, check=check, capture_output=True, text=True, encoding='utf-8')
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        error_message = e.stderr.strip()
        logger.error(f"コマンドが失敗しました: : {' '.join(command)}")
        logger.error(f"Error message: {error_message}")
        raise
        
    
