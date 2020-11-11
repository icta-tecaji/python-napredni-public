import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import DateTime, Integer, Float


def read_table_to_df(engine, table_name, columns, index):
    weblog = pd.read_sql_table(table_name, engine, columns=columns, index_col=index)
    return weblog


def read_query_to_df(engine, query):
    weblog_query_data = pd.read_sql_query(query, engine)
    return weblog_query_data


def write_df_to_sql(engine, df: pd.DataFrame, table_name: str, dtype_dict):
    df.to_sql(
        name=table_name, con=engine, index=False, dtype=dtype_dict, if_exists="append"
    )


if __name__ == "__main__":
    # engine = create_engine(
    #     "sqlite:///Del_04_Povezava_s_SQL_podatkovnimi_bazami/data/logs.db"
    # )

    # PRIMER 1
    # data = read_table_to_df(
    #     engine, "weblog", columns=["id", "status", "method"], index="id"
    # )
    # print(data.head())

    # PRIMER 2
    # data = read_query_to_df(
    #     engine, "SELECT * FROM weblog WHERE ip='10.128.2.1' AND method = 'GET'"
    # )
    # print(data.head())

    # PRIMER 3 - pisanje v bazo
    engine = create_engine(
        "sqlite:///Del_04_Povezava_s_SQL_podatkovnimi_bazami/data/iperf.db"
    )

    # iperf.csv -> to SQL
    iperf_df = pd.read_csv(
        "Del_03_Branje_in_pisanje_v_datoteke/data/iperf_clean.csv",
        parse_dates=["timestamp"],
    )
    dtype_dict = {
        "timestamp": DateTime(),
        "transfer_mbs": Integer(),
        "bandwidth_gbs": Float(),
        "retr": Integer(),
        "cwnd_kbs": Integer(),
    }

    write_df_to_sql(engine, iperf_df, "iperf_logs", dtype_dict)
