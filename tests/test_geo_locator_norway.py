import pandas as pd

from iout_foss.geo_locator_norway import add_metadata_columns_to_df

df_coordinates = pd.DataFrame(
    {
        "lat": [
            61.597637,  # Kinn (Florø)
            60.377332,
            60.40970322109922,  # nothing
            60.52803424661631,
            60.52828281419722,
            78.27497452901882,  # nothing
        ],
        "lon": [
            4.998121,  # Kinn (Florø)
            5.309175,
            5.247345904183821,  # nothing
            6.072824935209871,
            6.074214298488534,
            17.809175062996772,  # nothing
        ],
    }
)


def test_add_kommune_columns_to_df():
    """Test that several coordinates are assigned the correct kommune and kommunesnummer"""
    res = add_metadata_columns_to_df(
        df_coordinates,
        metadata_to_add=["kommunedata"],
        lat_column_name="lat",
        lon_column_name="lon",
    )
    assert list(res.kommunenummer.dropna()) == [4602, 4601, 4628, 4621]
    assert list(res.navn.dropna()) == ["Kinn", "Bergen", "Vaksdal", "Voss"]


def test_add_fylke_columns_to_df():
    """Test that several coordinates are assigned the correct fylke and fylkesnummer"""
    res = add_metadata_columns_to_df(
        df_coordinates,
        metadata_to_add=["fylkesdata"],
        lat_column_name="lat",
        lon_column_name="lon",
    )
    print(res)
    assert list(res.fylkesnummer.dropna()) == [46, 46, 46, 46]
    assert list(res.navn.dropna()) == ["Vestland", "Vestland", "Vestland", "Vestland"]
