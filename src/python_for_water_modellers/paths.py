"""
Path utilities for Python for Water Modellers notebooks.

This module provides functions for resolving data paths that work
across local development and Binder sessions without relying on a
single working-directory assumption.
"""

from pathlib import Path


def get_data_path() -> Path:
    """
    Get the correct path to the data folder.

    Works in multiple environments:
    - Local development from the repository root
    - Local development from the tutorials/ directory
    - Binder cloud sessions
    - A fresh user project that doesn't have a data folder yet
      (one is created next to the current working directory)

    Returns:
    --------
    Path
        Path object pointing to the data directory. The directory is
        guaranteed to exist on return.

    Examples:
    ---------
    >>> from python_for_water_modellers.paths import get_data_path
    >>> DATA_PATH = get_data_path()
    >>> discharge_file = DATA_PATH / 'camels_01013500_discharge.csv'
    """
    repo_root = Path(__file__).resolve().parents[2]
    candidates = (
        Path.cwd() / "data",
        Path.cwd().parent / "data",
        repo_root / "data",
    )

    for candidate in candidates:
        if candidate.is_dir():
            return candidate.resolve()

    fallback = (Path.cwd() / "data").resolve()
    fallback.mkdir(parents=True, exist_ok=True)
    return fallback
