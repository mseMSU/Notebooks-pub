"""Shared helpers for the instructional notebooks.

The module works both from a local repository checkout and from a notebook
opened independently in a hosted environment such as Google Colab.
"""

from pathlib import Path
from urllib.parse import quote


PUBLIC_DATA_ROOT = (
    "https://raw.githubusercontent.com/"
    "mseMSU/Notebooks-pub/main/notebooks/Data"
)


def data_source(relative_path):
    """Return a local data path when available, otherwise its public URL.

    ``relative_path`` is always interpreted relative to ``notebooks/Data``.
    Absolute paths and parent-directory traversal are rejected so local and
    hosted notebooks resolve the same logical data file.
    """

    relative_path = Path(relative_path)
    if relative_path.is_absolute() or ".." in relative_path.parts:
        raise ValueError("Data paths must be relative to notebooks/Data")

    for parent in (Path.cwd(), *Path.cwd().parents):
        for data_root in (parent / "Data", parent / "notebooks" / "Data"):
            candidate = data_root / relative_path
            if candidate.is_file():
                return candidate

    encoded_path = quote(relative_path.as_posix(), safe="/")
    return f"{PUBLIC_DATA_ROOT}/{encoded_path}"
