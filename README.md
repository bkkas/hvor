# Hvor

[![example workflow](https://github.com/bkkas/hvor/actions/workflows/python-app.yml/badge.svg)](https://github.com/bkkas/hvor/actions/workflows/python-app.yml)
[![Documentation Status](https://readthedocs.org/projects/hvor/badge/?version=latest)](https://hvor.readthedocs.io/en/latest/?badge=latest)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

Har du en eller flere koordinater innenfor Norges geografiske grenser som du
gjerne skulle visst mer om? `hvor` er et Python-bibliotek for å hente ut ulike
typer data for koordinater i Norge. Data som kan hentes inkluderer:

- Kommunedata (kommune og kommunenummer)
- Fylkesdata (fylke og fylkesnummer)

Flere typer data vil bli lagt til etterhvert!

## Installering

Så enkelt som

```
pip install hvor
```

## Bruk

For et enkeltpunkt med latitude og longitude, bruk `point`

```python
>>> from hvor import point
>>> point(61.7327867684485, 5.540150406971685)
{'kommunenumer': [4602], 'kommune': ['Kinn'], 'fylkesnummer': [46], 'fylke': ['Vestland']}
```

For flere koordinater, igjen med latitude og longitude, bruk `points` (merk
**s** på slutten)

```python
>>> from hvor import points
>>> coordinates = {"lat": [63.414109, 69.14579124011655], "lon": [10.416230, 18.15361374220361]}
>>> points(coordinates)
{'kommunenummer': [5001, 5419], 'kommune': ['Trondheim', 'Sørreisa'], 'fylkesnummer': [50, 54], 'fylke': ['Trøndelag', 'Troms og Finnmark']}
```

Vipps, så har du kommune- og fylkesdata for koordinatene. (\*men kun hvis
nøklene for bredde- og lengdegradlistene dine het `lat` og `lon`😅).

## Credits

Tusen takk til

- [robhop](https://github.com/robhop) for deling av kommune- og fylkesdata.
- Kartverket for offentliggjøring av kartdata som robhop baserte seg på.
