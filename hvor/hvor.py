from hvor.geolocator import get_fylke_metadata, get_kommune_metadata

funcs_dict = {
    "kommunedata": get_kommune_metadata,
    "fylkesdata": get_fylke_metadata,
}
PERMITTED_FIELDS = funcs_dict.keys()


def points(
    coordinates,
    metadata_to_add=PERMITTED_FIELDS,
    lat_key="lat",
    lon_key="lon",
) -> dict:
    """Takes multiple coordinates and returns metadata about each point.

    Args:
        coordinates (dict): dict-like with keys "lat" and "lon", where at each key there
            is a list-like object containing latitude/longitude floats.
        metadata_to_add (list): list of strings of what you'd like to know about the
            specified coordinates, e.g. "kommunedata" or "fylkesdata"
        lat_key (str): the key to use with ``coordinates`` to get latitudes.
        lon_key (str): the key to use with ``coordinates`` to get longitudes.


    """
    coordinates_metadata = {}

    _check_valid_user_input(metadata_to_add)
    for field in metadata_to_add:
        metadata = funcs_dict[field](
            coordinates=coordinates,
            lat_key=lat_key,
            lon_key=lon_key,
        )
        for key in metadata.keys():
            coordinates_metadata[key] = metadata[key]

    return coordinates_metadata


def point(
    lat: float,
    lon: float,
    metadata_to_add: list = PERMITTED_FIELDS,
    lat_key: str = "lat",
    lon_key: str = "lon",
) -> dict:
    """Takes multiple coordinates and returns metadata about each point. Implemented as
    a wrapper around ``points``

    Args:
        lat (float): latitude of a single coordinate
        lon (float): longitude of a single coordinate
        metadata_to_add (list): list of strings of what you'd like to know about the
            specified coordinates, e.g. "kommunedata" or "fylkesdata"
        lat_key (str): the key to use with ``coordinates`` to get latitudes.
        lon_key (str): the key to use with ``coordinates`` to get longitudes.

    """

    coordinates = {"lat": [lat], "lon": [lon]}
    return points(
        coordinates=coordinates,
        metadata_to_add=metadata_to_add,
        lat_key=lat_key,
        lon_key=lon_key,
    )


def _check_valid_user_input(metadata_to_add):
    permitted_fields = PERMITTED_FIELDS
    if not all(x in permitted_fields for x in metadata_to_add):
        raise KeyError(
            f"Invalid value specified in columns_to_add. Permitted values are {PERMITTED_FIELDS}"
        )
