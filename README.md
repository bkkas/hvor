# Hvor

A library for assigning Norwegian metadata to coordinates. For example, if you
have a list of coordinates, and you'd like to know which county and municipality
each coordinate belongs to, `hvor` can help you.

## Installation

Simply run

```
pip install hvor
```

## Usage

```python
from hvor import add_metadata_columns_to_df

df = add_metadata_columns_to_df(df)
```

Voila! County and municipality metadata for your coordinates have been added to
your dataframe (\*but only if your latitude and longitude columns were called
`lat` and `lon`😅).

## Credits

Big thanks to [robhop](https://github.com/robhop) for sharing his lightly
processed county and municipality polygons. Also big thanks to Kartverket, for
supplying the original dataset.
