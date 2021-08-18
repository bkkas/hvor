import geopandas as gpd
import pandas as pd

from hvor.data import _load_fylkesdata, _load_kommunedata


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
