from pathlib import Path

try:
    from importlib.metadata import PackageNotFoundError, version
except Exception:  # Python <3.8 fallback (should not happen per requires-python)
    version = None
    PackageNotFoundError = Exception

__all__ = ["__version__"]


def _get_version() -> str:
    if version is None:
        return _get_version_from_pyproject()
    try:
        return version("sourcesage")
    except PackageNotFoundError:
        return _get_version_from_pyproject()


def _get_version_from_pyproject() -> str:
    pyproject_path = Path(__file__).resolve().parent.parent / "pyproject.toml"
    if not pyproject_path.exists():
        return "0.0.0"

    for line in pyproject_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("version ="):
            return line.split("=", maxsplit=1)[1].strip().strip('"').strip("'")

    return "0.0.0"


__version__ = _get_version()
