# Hvor

A library for assigning Norwegian metadata to coordinates. For example, if you
have a list of coordinates, and you'd like to know which county and municipality
each coordinate belongs to, `hvor` can help you.

## Installation

´´´
pip install hvor
´´´

## Usage

```python
from hvor import add_metadata_columns_to_df

df = add_metadata_columns_to_df(df)
```

Voila! County and municipality metadata for your coordinates have been added to
your dataframe.
