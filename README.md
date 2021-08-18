# Hvor

Har du en eller flere koordinater innenfor Norges geografiske grenser som du
gjerne skulle visst mer om? `hvor` er et Python-bibliotek for å hente ut ulike
typer data for koordinater i Norge. Vi baserer oss på bruk av `pandas` og
`geopandas`. Data som kan hentes inkluderer:

- Kommunedata (kommune og kommunenummer)
- Fylkesdata (fylke og fylkesnummer)

Flere typer data vil bli lagt til etterhvert!

## Installering

Så enkelt som

```
pip install hvor
```

## Bruk

```python
from hvor import add_metadata_columns_to_df

df = add_metadata_columns_to_df(df)
```

Vipps! Kommune- og fylkesdata har blitt lagt til dataframen med koordinatene
dine. (\*men kun hvis bredde- og lengdegradkolonnene dine het `lat` and
`lon`😅).

## Credits

Tusen takk til

- [robhop](https://github.com/robhop) for deling av lettprosesserte kommune- og fylkesdata.
- Kartverket for offentliggjøring av høykvalitets kartdata
