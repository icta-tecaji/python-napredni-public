import sqlite3


class DataConn:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise


if __name__ == "__main__":
    db = "Del_12_Context_Managers/data/test3.db"

    with DataConn(db) as conn:
        cursor = conn.cursor()

        cursor.execute(
            """CREATE TABLE stocks
                        (date text, trans text, symbol text, qty real, price real)"""
        )

        cursor.execute(
            "INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)"
        )
        conn.commit()
        cursor.execute("select * from stocks")
        print(cursor.fetchall())
