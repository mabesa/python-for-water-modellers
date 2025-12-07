"""
Path utilities for Python for Water Modellers notebooks.

This module provides functions for resolving data paths that work
across different environments (local development, Binder, etc.).
"""

import os
from pathlib import Path


def get_data_path() -> Path:
    """
    Get the correct path to the data folder.

    Works in multiple environments:
    - Local development (VS Code, Jupyter Lab from repo root)
    - Binder cloud environment

    Returns:
    --------
    Path
        Path object pointing to the data directory

    Examples:
    ---------
    >>> from python_for_water_modellers.paths import get_data_path
    >>> DATA_PATH = get_data_path()
    >>> discharge_file = DATA_PATH / 'camels_01013500_discharge.csv'
    """
    # Check if running in Binder (cloud environment)
    if 'BINDER_REQUEST' in os.environ or 'BINDER_LAUNCH_HOST' in os.environ:
        # Binder: repo is cloned to home directory, data is at ~/data/
        data_path = Path.home() / 'data'
    elif Path('../data').exists():
        # Local: notebook is in tutorials/, data is at ../data/
        data_path = Path('../data')
    elif Path('data').exists():
        # Alternative: already at repo root
        data_path = Path('data')
    else:
        # Fallback: assume tutorials/ location
        data_path = Path('../data')

    return data_path
