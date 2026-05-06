"""
Python for Water Modellers - Utilities and Examples

A Python tutorial for water modellers covering numerical methods,
data analysis, and hydraulic modeling.
"""

from python_for_water_modellers.camels import (
    SAMPLE_AREA_KM2,
    SAMPLE_STATION_ID,
    SAMPLE_STATION_NAME,
    is_binder_session,
    load_sample_camels_discharge,
    sample_camels_attributes,
)
from python_for_water_modellers.paths import get_data_path

__all__ = [
    "SAMPLE_AREA_KM2",
    "SAMPLE_STATION_ID",
    "SAMPLE_STATION_NAME",
    "get_data_path",
    "is_binder_session",
    "load_sample_camels_discharge",
    "sample_camels_attributes",
]
