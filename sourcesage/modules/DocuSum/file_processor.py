import os

from loguru import logger


class FileProcessor:
    """Read repository files and render them as Markdown sections."""

    def __init__(self, language_detector, language="en"):
        self.language_detector = language_detector
        self.language = language
        self.binary_extensions = {
            ".pyc",
            ".pyo",
            ".pyd",
            ".so",
            ".dll",
            ".exe",
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".ico",
            ".pdf",
        }

    def process_file(self, file_path, base_path):
        """Convert a file into a Markdown code section."""
        try:
            relative_path = os.path.relpath(file_path, base_path)

            if self._is_binary_file(file_path):
                logger.debug(f"Skipping binary file: {relative_path}")
                return f"`{relative_path}` - Binary file\n\n"

            language = self.language_detector.detect_language(file_path)
            content = self._read_file_content(file_path)
            if content is None:
                return f"`{relative_path}` - Error: Failed to read file\n\n"

            file_info = self._get_file_info(file_path)
            return (
                f"`{relative_path}`\n\n"
                f"{file_info}\n"
                f"```{language}\n"
                f"{content}\n"
                f"```\n\n"
            )
        except Exception as exc:
            logger.error(f"File processing error {file_path}: {exc}")
            return f"`{os.path.relpath(file_path, base_path)}` - Error: {exc}\n\n"

    def _is_binary_file(self, file_path):
        """Detect whether a file should be treated as binary."""
        ext = os.path.splitext(file_path)[1].lower()
        if ext in self.binary_extensions:
            return True

        try:
            with open(file_path, "rb") as file:
                return b"\x00" in file.read(1024)
        except Exception:
            return True

    def _read_file_content(self, file_path, max_size=1024 * 1024):
        """Read a text file as UTF-8."""
        try:
            if os.path.getsize(file_path) > max_size:
                logger.warning(f"File too large to display: {file_path}")
                return "File too large to display"

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                return content if content else "(Empty file)"
        except UnicodeDecodeError:
            logger.warning(f"Encoding error while reading {file_path}")
            return None
        except Exception as exc:
            logger.error(f"Failed to read {file_path}: {exc}")
            return None

    def _get_file_info(self, file_path):
        """Build the metadata line shown above each code block."""
        try:
            stats = os.stat(file_path)
            size = self._format_size(stats.st_size)
            lines = self._count_lines(file_path)

            if self.language == "ja":
                size_label = "**サイズ**"
                lines_label = f"**行数**: {lines if lines is not None else 'N/A'}"
            else:
                size_label = "**Size**"
                lines_label = f"**Lines**: {lines if lines is not None else 'N/A'}"

            return " | ".join([f"{size_label}: {size}", lines_label])
        except Exception as exc:
            logger.error(f"Failed to gather file info for {file_path}: {exc}")
            return ""

    def _format_size(self, size):
        """Convert file size to a readable unit."""
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"

    def _count_lines(self, file_path):
        """Count text lines in a file."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return sum(1 for _ in file)
        except Exception:
            return None
