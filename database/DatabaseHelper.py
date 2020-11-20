import threading

import pyodbc
import logging
import concurrent.futures
from threading import Thread

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

database_thread = threading.local()


class DatabaseHelper:
    def __init__(self, server, database, user, password):
        Thread.__init__(self)
        params = self.window_Auth(server, database)

        self.conn = pyodbc.connect(params)
        self.cursor = self.conn.cursor()

    def window_Auth(self, server, database):
        params = ("DRIVER={ODBC Driver 17 for SQL Server};"
                  f"SERVER={server};"
                  f"Trusted_Connection=yes;"
                  )
        return params

    def sql_Auth(self, server, database, username, password):
        params = (
            "DRIVER={ODBC Driver 13.1 for SQL Server};"
            f"SERVER={server};"
            f"username={username}"
            f"password={password}"
        )
        return params

    def test_connection(self):
        for retry in range(3):
            try:
                self.cursor.execute("SELECT 1")
                return "Connection established"
            except pyodbc.ProgrammingError as e:
                raise Exception(e)

    def displayAllDatabases(self):
        databases = []
        self.cursor.execute("select name from sys.databases WHERE name NOT IN ('master','model','msdb','tempdb')")
        for row in self.cursor.fetchall():
            databases.append(row[0])

        return databases

    def backup_database(self, name, path):
        self.conn.autocommit = True
        self.cursor.execute(
            f'''
            DECLARE @name VARCHAR(50)
            DECLARE @path VARCHAR(250)
            DECLARE @savePath VARCHAR(250)
            SET @name = ?
            SET @path = ?
            SET @savePath = @path+@name+ '.bak'
            BACKUP DATABASE @name TO DISK = @savepath 
    
            ''', [name, path]
        )
        logging.info(f"{name} is being backed up")


# TODO Program needs to check for admin privilieges
if __name__ == "__main__":
    path = "C:/Backups/"
    dh = DatabaseHelper(".\ML001", "", "", "")
    dh.test_connection()
    dh.displayAllDatabases()
