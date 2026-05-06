"""Small CAMELS helpers used by the tutorial notebooks."""

import os

import pandas as pd

from python_for_water_modellers.paths import get_data_path


SAMPLE_STATION_ID = "01013500"
SAMPLE_STATION_NAME = "Fish River Near Fort Kent, Maine"
SAMPLE_AREA_KM2 = 2252.7


def is_binder_session() -> bool:
    """Return True when running in a Binder-launched notebook server."""
    binder_vars = ("BINDER_REQUEST", "BINDER_LAUNCH_HOST")
    return any(os.environ.get(name) for name in binder_vars)


def load_sample_camels_discharge(station_id: str = SAMPLE_STATION_ID) -> pd.DataFrame:
    """Load the small CAMELS discharge sample bundled with this repository."""
    sample_file = get_data_path() / f"camels_{station_id}_discharge.csv"
    return pd.read_csv(sample_file, parse_dates=["date"])


def sample_camels_attributes() -> pd.DataFrame:
    """Return lightweight station metadata for the bundled CAMELS sample."""
    sample_df = load_sample_camels_discharge()
    return pd.DataFrame(
        {
            "gauge_name": [SAMPLE_STATION_NAME],
            "area_gages2": [SAMPLE_AREA_KM2],
            "q_mean": [sample_df["discharge_mm_day"].mean()],
            "elev_mean": [float("nan")],
        },
        index=[SAMPLE_STATION_ID],
    )
