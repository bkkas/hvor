import geopandas as gpd
import pandas as pd

from hvor.data import load_fylkesdata, load_kommunedata


def _geolocate(coordinates, data, lon_key, lat_key):
    goal = gpd.GeoDataFrame(
        coordinates,
        geometry=gpd.points_from_xy(
            coordinates[lon_key], coordinates[lat_key], crs="EPSG:4326"
        ),
    )
    return (
        gpd.sjoin(goal, data, how="left", op="within")
        .drop(["geometry", "index_right", lat_key, lon_key], axis=1)
        .to_dict(orient="list")
    )


def get_kommune_metadata(coordinates, lat_key, lon_key) -> pd.DataFrame:
    """Add columns for which kommune and kommunenummer the coordinates belong to."""
    kommunedata = load_kommunedata()
    return _geolocate(coordinates, kommunedata, lon_key, lat_key)


def get_fylke_metadata(coordinates, lat_key, lon_key) -> pd.DataFrame:
    fylkesdata = load_fylkesdata()
    return _geolocate(coordinates, fylkesdata, lon_key, lat_key)
