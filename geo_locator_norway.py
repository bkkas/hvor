import bz2
from functools import lru_cache

import geopandas as gpd
import pkg_resources


@lru_cache(maxsize=None)
def load_kommuner():
    filepath = pkg_resources.resource_filename(
        "resources", "Kommuner-2020-large.json.bz2"
    )
    with bz2.open(filepath, mode="rt", encoding="utf-8") as f:
        return gpd.read_file(f)


def get_kommune_owning_points(df, pos_col_name=None, lat_name=None, lon_name=None):
    kommuner = load_kommuner()
    if pos_col_name:
        latitudes = df[pos_col_name].map(lambda x: x[0])
        longitutes = df[pos_col_name].map(lambda x: x[1])
    elif lat_name and lon_name:
        latitudes = df[lat_name]
        longitutes = df[lon_name]
    else:
        raise ValueError(
            "Either pos_col_name or lat_name AND lon_name must be " "provided"
        )
    goal = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(longitutes, latitudes, crs="EPSG:4326")
    )
    return gpd.sjoin(goal, kommuner, how="inner", op="within").drop(
        ["geometry", "index_right"], axis=1
    )
