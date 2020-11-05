# Del 03: Branje in pisanje v datoteke

## Branje datotek v Pythonu
- V Python-u datoteke beremo s pomočjo `open()` funkcije
- Za večino formatov obstajajo knjižnice, ki nam olajšajo delo

## Pandas
- Knjižnica za delo s podatki v Python-u.
- Namestitev: `pip install pandas` (v aktiviranem virtualnem okolju)
- [Navodila](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html) za uporabo knjižnice 

## CSV
- Delo s pomočjo vgrajene [knjižnice](https://docs.python.org/3/library/csv.html) `csv`
- Pandas ima [metodo](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.htmlm) `pd.read_csv()`, ki omogoča enostavno branje CSV datotek.

## JSON datoteke
- Branje datotek s pomočjo vgrajene `json` [knjižnice](https://docs.python.org/3/library/json.html) 
- Uvozimo z `import json`
- Glavne metode:
    - Serializing JSON (python objekti -> json file): `json.dump(<data>, <file_obj>)`
    - Deserializing JSON (json file -> pytohn objekte): `json.load(<file_obj>)`
- S pomočjo knjižnice pandas:
    - `pd.read_json(<file_name>`
