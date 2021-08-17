import bz2
from functools import lru_cache
from pathlib import Path

import geopandas as gpd
import pandas as pd


def add_metadata_columns_to_df(
    df,
    metadata_to_add=["kommunedata", "fylkesdata"],
    lat_column_name="lat",
    lon_column_name="lon",
    how="left",
) -> pd.DataFrame:
    valid_metadata_options = ["kommunedata", "fylkesdata"]
    if not all(x in valid_metadata_options for x in metadata_to_add):
        raise KeyError(
            f"Invalid value specified in columns_to_add. Permitted values are {valid_metadata_options}"
        )

    if "kommunedata" in metadata_to_add:
        df = _add_kommune_metadata_columns_to_df(
            df,
            how=how,
            lat_column_name=lat_column_name,
            lon_column_name=lon_column_name,
        )

    if "fylkesdata" in metadata_to_add:
        df = _add_fylke_metadata_columns_to_df(
            df,
            how=how,
            lat_column_name=lat_column_name,
            lon_column_name=lon_column_name,
        )

    return df


def _add_kommune_metadata_columns_to_df(
    df, how, lat_column_name, lon_column_name
) -> pd.DataFrame:
    """Add columns for which kommune and kommunenummer the coordinates belong to."""
    kommunedata = _load_kommunedata()

    goal = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(
            df[lon_column_name], df[lat_column_name], crs="EPSG:4326"
        ),
    )
    return gpd.sjoin(goal, kommunedata, how=how, op="within").drop(
        ["geometry", "index_right"], axis=1
    )


def _add_fylke_metadata_columns_to_df(
    df, how, lat_column_name, lon_column_name
) -> pd.DataFrame:
    fylkesdata = _load_fylkesdata()

    goal = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(
            df[lon_column_name], df[lat_column_name], crs="EPSG:4326"
        ),
    )
    return gpd.sjoin(goal, fylkesdata, how=how, op="within").drop(
        ["geometry", "index_right"], axis=1
    )


@lru_cache(maxsize=None)
def _load_kommunedata():
    """Loads data for kommuner and kommunenummer"""
    filepath = (
        Path(__file__).joinpath("../resources/Kommuner-2020-large.json.bz2").resolve()
    )
    with bz2.open(filepath, mode="rt", encoding="utf-8") as f:
        return gpd.read_file(f)


@lru_cache(maxsize=None)
def _load_fylkesdata():
    """Loads data for fylker and fylkesnummer"""
    filepath = (
        Path(__file__).joinpath("../resources/Fylker-2020-large.json.bz2").resolve()
    )
    with bz2.open(filepath, mode="rt", encoding="utf-8") as f:
        return gpd.read_file(f)
