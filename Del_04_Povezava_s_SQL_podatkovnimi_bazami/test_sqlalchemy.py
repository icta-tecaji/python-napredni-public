from sqlalchemy import create_engine


def get_one_row(engine, sql_query):
    with engine.connect() as con:
        rs = con.execute(sql_query)
        data = rs.fetchone()
    return data


def get_n_rows(engine, sql_query, n_rows):
    with engine.connect() as con:
        rs = con.execute(sql_query)
        data = rs.fetchmany(n_rows)
    return data


def get_all_rows(engine, sql_query):
    with engine.connect() as con:
        rs = con.execute(sql_query)
        data = rs.fetchall()
    return data


if __name__ == "__main__":
    engine = create_engine(
        "sqlite:///Del_04_Povezava_s_SQL_podatkovnimi_bazami/data/logs.db"
    )

    # one_row = get_one_row(engine, "SELECT * FROM weblog LIMIT 5;")
    # print(one_row)

    # three_rows = get_n_rows(engine, "SELECT * FROM weblog LIMIT 5;", 3)
    # print(three_rows)

    all_rows = get_all_rows(engine, "SELECT * FROM weblog LIMIT 5;")
    print(all_rows)
