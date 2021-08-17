import pandas as pd

from iout_foss.geo_locator_norway import add_metadata_columns_to_df


def test_add_kommune_columns_to_df():
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
    res = add_metadata_columns_to_df(
        goal,
        metadata_to_add=["kommunedata"],
        lat_column_name="lat",
        lon_column_name="lon",
    )
    print(res)
    assert list(res.kommunenummer.dropna()) == [4601, 4628, 4621]
    assert list(res.navn.dropna()) == ["Bergen", "Vaksdal", "Voss"]
    # assert False, "For debugging"
