import bz2
from functools import lru_cache
from pathlib import Path

import geopandas as gpd
import pandas as pd


def _get_kommune_metadata(coordinates, lat_key, lon_key) -> pd.DataFrame:
    """Add columns for which kommune and kommunenummer the coordinates belong to."""
    kommunedata = _load_kommunedata()

    goal = gpd.GeoDataFrame(
        coordinates,
        geometry=gpd.points_from_xy(
            coordinates[lon_key], coordinates[lat_key], crs="EPSG:4326"
        ),
    )
    return (
        gpd.sjoin(goal, kommunedata, how="left", op="within")
        .drop(["geometry", "index_right", "lat", "lon"], axis=1)
        .to_dict(orient="list")
    )


def _get_fylke_metadata(coordinates, lat_key, lon_key) -> pd.DataFrame:
    fylkesdata = _load_fylkesdata()

    goal = gpd.GeoDataFrame(
        coordinates,
        geometry=gpd.points_from_xy(
            coordinates[lon_key], coordinates[lat_key], crs="EPSG:4326"
        ),
    )
    return (
        gpd.sjoin(goal, fylkesdata, how="left", op="within")
        .drop(["geometry", "index_right"], axis=1)
        .to_dict(orient="list")
    )


@lru_cache(maxsize=None)
def _load_kommunedata():
    """Loads data for kommuner and kommunenummer"""
    filepath = (
        Path(__file__).joinpath("../resources/Kommuner-2020-large.json.bz2").resolve()
    )
    with bz2.open(filepath, mode="rt", encoding="utf-8") as f:
        return gpd.read_file(f).rename(
            mapper={"kommunenummer": "kommunenummer", "navn": "kommune"}, axis=1
        )


@lru_cache(maxsize=None)
def _load_fylkesdata():
    """Loads data for fylker and fylkesnummer"""
    filepath = (
        Path(__file__).joinpath("../resources/Fylker-2020-large.json.bz2").resolve()
    )
    with bz2.open(filepath, mode="rt", encoding="utf-8") as f:
        return gpd.read_file(f).rename(
            mapper={"fylkesnummer": "fylkesnummer", "navn": "fylke"}, axis=1
        )
