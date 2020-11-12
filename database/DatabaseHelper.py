import pyodbc
import logging

class DatabaseHelper:

    def __init__(self, server, database, user, password):
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
        params =(
            "DRIVER={SQL Server};"
            f"SERVER={server};"
            f"username={username}"
            f"password={password}"
        )
        return params

    def test_connection(self):
        for retry in range(3):
            try:
                self.cursor.execute("SELECT 1")
                print("Connection established")
                return
            except pyodbc.ProgrammingError as e:
                raise Exception(e)


    def displayAllInstances(self):
        self.cursor.execute("select name from sys.databases WHERE name NOT IN ('master','model','msdb','tempdb')")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)


    def backup_database(self,dbname , name,path):
        self.cursor.execute(
            f'''
            OPEN db_cursor   
            FETCH NEXT FROM db_cursor INTO ?	 

            WHILE @@FETCH_STATUS = 0   
            BEGIN
             BACKUP DATABASE ? TO DISK = ?
             FETCH NEXT FROM db_cursor INTO ?
            END
            CLOSE db_cursor
            DEALLOCATE db_cursor
            ''', [dbname,name,path,dbname]
        )
        logging.info(f"{name} is being backed up")




