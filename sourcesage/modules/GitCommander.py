import subprocess
from collections.abc import Sequence

from loguru import logger


logger.level("SUBPROCESS", no=15, color="<cyan>", icon="🔍")


def run_command(command: Sequence[str], cwd=None, check=True, preview=True):
    """Run a subprocess command and return stdout."""
    normalized_command = [str(part) for part in command]

    if preview:
        logger.log("SUBPROCESS", f">>>>>> Running command: {' '.join(normalized_command)}")

    try:
        result = subprocess.run(
            normalized_command,
            cwd=cwd,
            check=check,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as exc:
        logger.error(f"Command failed: {' '.join(normalized_command)}")
        logger.error(f"Error message: {exc.stderr.strip()}")
        raise
    except FileNotFoundError:
        logger.error(f"Command not found: {' '.join(normalized_command)}")
        raise
