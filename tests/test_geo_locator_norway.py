import pandas as pd

from iout_foss.geo_locator_norway import get_kommune_owning_points


def test_get_kommune_owning_points():
    """Tests a few points with and without kommuner."""
    goal = pd.DataFrame(
        {
            "lat": [
                60.377332,
                60.40970322109922,  # nothing
                60.52803424661631,
                60.52828281419722,
                78.27497452901882,  # nothing
            ],
            "lon": [
                5.309175,
                5.247345904183821,  # nothing
                6.072824935209871,
                6.074214298488534,
                17.809175062996772,  # nothing
            ],
        }
    )
    res = get_kommune_owning_points(goal, lat_name="lat", lon_name="lon")
    assert list(res.kommunenummer) == [4601, 4628, 4621]
    assert list(res.navn) == ["Bergen", "Vaksdal", "Voss"]
