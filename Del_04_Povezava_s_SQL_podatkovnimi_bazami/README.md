# Del 04: Branje in pisanje podatkov iz SQL podatkovnih baz

- [SQL Alchemy](https://www.sqlalchemy.org/): SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

## Namestitev
- `python -m pip install SQLAlchemy`
- Dodatno treba namestit še DBAPI driverje za posamezno podatkovno bazo:
    - MySQL database via the PyMySQL driver: `pip install PyMySQL`
    - PostgreSQL database via the psycopg2 driver: `pip install psycopg2`
    - Več informaciji [tukaj](https://docs.sqlalchemy.org/en/13/dialects/index.html)


## Povezava
- Na bazo se povežemo s pomočjo funkcije `create_engine`
```python
from sqlalchemy import create_engine
engine = create_engine('<DB_URL>', echo=True)
```
- Tipičen format URL-ja:
    - `dialect+driver://username:password@host:port/database`
    - Primer PostgreSQL: `postgresql+psycopg2://scott:tiger@localhost/mydatabase`
    - Primer MySQL: `mysql+pymysql://scott:tiger@localhost/foo`
    - Primer SQLite: `sqlite:///foo.db`
    - Več info: [Engine Configuration](https://docs.sqlalchemy.org/en/13/core/engines.html)


## Podatkovne baze in pandas
- Ustvarimo SQLAlchemy engine in se nato povežemo s pomočjo naslednjih funkcij:
    - `read_sql_table(table_name, con[, schema, …])`: Read SQL database table into a DataFrame.
    - `read_sql_query(sql, con[, index_col, …])`: Read SQL query into a DataFrame.
    - `read_sql(sql, con[, index_col, …])`: Read SQL query or database table into a DataFrame.
    - `DataFrame.to_sql(self, name, con[, schema, …])`: Write records stored in a DataFrame to a SQL database.