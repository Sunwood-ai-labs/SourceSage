import fnmatch
import os
from pathlib import Path, PurePosixPath


class FilePatternMatcher:
    """Process gitignore-style file patterns."""

    def __init__(self, ignore_file_or_files, base_dir=None):
        if isinstance(ignore_file_or_files, str):
            self.ignore_files = [ignore_file_or_files]
        else:
            self.ignore_files = ignore_file_or_files

        self.base_dir = base_dir
        self.default_patterns = [
            ".git/",
            "node_modules/",
            "__pycache__/",
            "*.pyc",
            ".DS_Store",
            ".SourceSageAssets/",
            "package-lock.json",
            "*.log",
        ]
        self.patterns = self._load_patterns()

    def _load_patterns(self):
        """Load exclude and include patterns from one or more ignore files."""
        include_patterns = []
        exclude_patterns = self.default_patterns.copy()

        for ignore_file in self.ignore_files:
            if not os.path.exists(ignore_file):
                continue

            with open(ignore_file, "r", encoding="utf-8") as handle:
                for raw_line in handle:
                    line = raw_line.strip()
                    if not line or line.startswith("#"):
                        continue

                    if line.startswith("!"):
                        include_patterns.append(line[1:])
                    else:
                        exclude_patterns.append(line)

        return {"include": include_patterns, "exclude": exclude_patterns}

    def should_exclude(self, path):
        """Check whether a path matches any exclude pattern."""
        normalized_path = self._normalize_path(path)
        if normalized_path is None or not normalized_path:
            return False

        protected_parts = {
            ".git",
            "__pycache__",
            "node_modules",
            ".SourceSageAssets",
        }
        if protected_parts.intersection(PurePosixPath(normalized_path).parts):
            return True

        excluded = any(
            self._match_pattern(normalized_path, pattern)
            for pattern in self.patterns["exclude"]
        )
        if not excluded:
            return False

        if self.patterns["include"]:
            return not any(
                self._match_pattern(normalized_path, pattern)
                for pattern in self.patterns["include"]
            )

        return excluded

    def _normalize_path(self, path):
        normalized_path = str(Path(path)).replace("\\", "/")

        if self.base_dir:
            base_dir_normalized = str(Path(self.base_dir)).replace("\\", "/").rstrip("/")
            if normalized_path == base_dir_normalized:
                return ""
            if normalized_path.startswith(f"{base_dir_normalized}/"):
                return normalized_path[len(base_dir_normalized) + 1 :]

        return self._strip_relative_prefix(normalized_path)

    def _match_pattern(self, path, pattern):
        pattern = self._strip_relative_prefix(pattern.replace("\\", "/"))

        if pattern.endswith("/"):
            return self._match_directory_pattern(path, pattern)

        if "**" in pattern:
            return self._match_recursive_pattern(path, pattern)

        return self._match_glob_pattern(path, pattern)

    def _match_directory_pattern(self, path, pattern):
        normalized_pattern = pattern.rstrip("/")
        normalized_path = path.rstrip("/")

        if not normalized_pattern:
            return False

        if "/" not in normalized_pattern and not any(
            token in normalized_pattern for token in "*?[]"
        ):
            return (
                normalized_path == normalized_pattern
                or normalized_path.startswith(f"{normalized_pattern}/")
                or f"/{normalized_pattern}/" in f"/{normalized_path}/"
            )

        return (
            normalized_path == normalized_pattern
            or normalized_path.startswith(f"{normalized_pattern}/")
            or PurePosixPath(normalized_path).match(normalized_pattern)
            or PurePosixPath(normalized_path).match(f"{normalized_pattern}/**")
        )

    def _match_recursive_pattern(self, path, pattern):
        path_object = PurePosixPath(path.rstrip("/"))
        return path_object.match(pattern) or path_object.match(pattern.rstrip("/"))

    def _match_glob_pattern(self, path, pattern):
        normalized_path = str(Path(path)).replace("\\", "/")
        basename = os.path.basename(normalized_path)

        if "/" in pattern:
            return fnmatch.fnmatch(normalized_path, pattern) or PurePosixPath(
                normalized_path
            ).match(pattern)

        return fnmatch.fnmatch(normalized_path, pattern) or fnmatch.fnmatch(
            basename, pattern
        )

    def _strip_relative_prefix(self, value):
        if value.startswith("./"):
            return value[2:]
        return value
