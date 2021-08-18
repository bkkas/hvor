import numpy as np
import pandas as pd

from hvor.hvor import points

coordinates = {
    "lat": [
        61.597637,  # Kinn (Florø)
        60.377332,
        60.52803424661631,
        60.52828281419722,
        78.27497452901882,  # nothing
    ],
    "lon": [
        4.998121,  # Kinn (Florø)
        5.309175,
        6.072824935209871,
        6.074214298488534,
        17.809175062996772,  # nothing
    ],
}


def test_get_kommunedata():
    """Test that several coordinates are assigned the correct kommune and kommunesnummer"""
    res = points(
        coordinates,
        metadata_to_add=["kommunedata"],
        lat_key="lat",
        lon_key="lon",
    )

    assert list(res["kommunenummer"][:-1]) == [4602, 4601, 4628, 4621]
    assert np.isnan(res["kommunenummer"][-1])
    assert list(res["kommune"][:-1]) == [
        "Kinn",
        "Bergen",
        "Vaksdal",
        "Voss",
    ]
    assert np.isnan(res["kommune"][-1])


def test_get_fylkesdata():
    """Test that several coordinates are assigned the correct fylke and fylkesnummer"""
    res = points(
        coordinates,
        metadata_to_add=["fylkesdata"],
        lat_key="lat",
        lon_key="lon",
    )
    print(res)
    assert list(res["fylkesnummer"][:-1]) == [46, 46, 46, 46]
    assert np.isnan(res["fylkesnummer"][-1])
    assert list(res["fylke"][:-1]) == ["Vestland", "Vestland", "Vestland", "Vestland"]
    assert np.isnan(res["fylke"][-1])
