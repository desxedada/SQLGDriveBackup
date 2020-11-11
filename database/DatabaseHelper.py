import urllib
import pyodbc
import pandas as pd


class DatabaseHelper:

    def __init__(self, server, database, user, password):
        params = self.window_Auth(server, database)
        conn = pyodbc.connect(params)
        cursor = conn.cursor()
        cursor.execute("select name from sys.databases WHERE name NOT IN ('master','model','msdb','tempdb')")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def window_Auth(self, server, database):
        params = ("DRIVER={SQL Server};"
                  f"SERVER={server};"
                  f"Trusted_Connection=yes;"
                 )
        return params

    def sql_Auth(self, server, database, username, password):
        params =(
            "DRIVER={SQL Server};"
            f"SERVER={server};"
            f"username={username}"
            f"password={password}"
        )
        return params

    def test_connection(self):
        msg = ""

    def displayAllInstances(self):
        pass

    def get_Instance(self):
        pass

    def run_query(self):
        pass


if __name__ == "__main__":
    dh = DatabaseHelper("DESKTOP-NE47J00\ML001", "master", "", "")
    dh.test_connection()
