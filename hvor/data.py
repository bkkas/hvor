import bz2
from functools import lru_cache
from pathlib import Path

import geopandas as gpd


@lru_cache(maxsize=None)
def load_kommunedata():
    """Loads data for kommuner and kommunenummer"""
    filepath = (
        Path(__file__).joinpath("../resources/Kommuner-2020-large.json.bz2").resolve()
    )
    with bz2.open(filepath, mode="rt", encoding="utf-8") as f:
        return gpd.read_file(f).rename(
            mapper={"kommunenummer": "kommunenummer", "navn": "kommune"}, axis=1
        )


@lru_cache(maxsize=None)
def load_fylkesdata():
    """Loads data for fylker and fylkesnummer"""
    filepath = (
        Path(__file__).joinpath("../resources/Fylker-2020-large.json.bz2").resolve()
    )
    with bz2.open(filepath, mode="rt", encoding="utf-8") as f:
        return gpd.read_file(f).rename(
            mapper={"fylkesnummer": "fylkesnummer", "navn": "fylke"}, axis=1
        )
