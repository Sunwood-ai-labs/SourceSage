from loguru import logger
from rich.console import Console
from rich.text import Text
from rich.traceback import install as rich_traceback_install


def setup_rich_logging(level: str = "WARNING") -> Console:
    """Configure loguru to output using Rich styling.

    Returns a Console instance that renders the logs, so callers can reuse it.
    """
    console = Console()

    def rich_sink(message):
        r = message.record
        # Timestamp with milliseconds
        time_str = r["time"].strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        level_name = r["level"].name
        location = f"{r['name']}:{r['line']}"
        msg = r["message"]

        level_style = {
            "TRACE": "dim",
            "DEBUG": "dim",
            "INFO": "cyan",
            "SUCCESS": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold red",
        }

        text = Text()
        text.append(time_str + " ", style="green")
        text.append(f"{level_name:<8} ", style=level_style.get(level_name, "white"))
        text.append(f"{location:<45} ", style="cyan")
        text.append(msg)
        console.print(text)

    # Pretty tracebacks
    rich_traceback_install(show_locals=False)

    logger.remove()
    logger.add(rich_sink, level=level, backtrace=False, diagnose=False)
    return console
