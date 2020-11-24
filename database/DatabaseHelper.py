import threading
import time
from msilib.schema import Property
from time import sleep

import pyodbc
import logging
from log.Logger import exception
import concurrent.futures
from threading import Thread


class DatabaseHelper:
    @exception
    def __init__(self, server, trust_conn):
        params = (r"DRIVER={ODBC Driver 17 for SQL Server};"
                  f"SERVER={server};"
                  f"Trusted_Connection={trust_conn};"
                  )
        try:
            self.conn = pyodbc.connect(params)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e.__name__)

    @exception
    def test_connection(self):
        for retry in range(3):
            try:
                self.cursor.execute("SELECT 1")
                logging.info("Connection Established")
                return "Connection established"
            except pyodbc.ProgrammingError as e:
                return "Connection Failed"

    @exception
    def displayAllDatabases(self):
        databases = []
        self.cursor.execute("select name from sys.databases WHERE name NOT IN ('master','model','msdb','tempdb')")
        for row in self.cursor.fetchall():
            databases.append(row[0])

        return databases

    @exception
    def backup_database(self, name, path):
        self.conn.autocommit=True
        timestamp = time.strftime("%Y-%m-%d_%H-%M")
        self.cursor.execute(
            f"BACKUP DATABASE {name} TO DISK = '{path}\\{name}_{timestamp}.bak'")
        logging.info(f"{name} is being backed up")
