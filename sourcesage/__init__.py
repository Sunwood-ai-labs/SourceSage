try:
    from importlib.metadata import PackageNotFoundError, version
except Exception:  # Python <3.8 fallback (should not happen per requires-python)
    version = None
    PackageNotFoundError = Exception

__all__ = ["__version__"]


def _get_version() -> str:
    if version is None:
        return "0.0.0"
    try:
        return version("sourcesage")
    except PackageNotFoundError:
        return "0.0.0"


__version__ = _get_version()
