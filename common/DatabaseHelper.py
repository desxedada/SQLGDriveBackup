import datetime
import sys
import threading
import time
import pyodbc
import logging
import win32com.client

from log.Logger import exception
from common.ServiceHandler import ScheduleSVC


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
        self.conn.autocommit = True
        timestamp = time.strftime("%Y-%m-%d_%H-%M")
        self.cursor.execute(
            f"BACKUP DATABASE {name} TO DISK = '{path}\\{name}_{timestamp}.bak'")
        logging.info(f"{name} is being backed up")

def startSchedule():
        schedule = win32com.client.Dispatch('Schedule.Service')
        schedule.Connect()
        root_folder = schedule.GetFolder('\\')
        task_def = schedule.NewTask(0)

        start_time = datetime.datetime.now() + datetime.timedelta(minutes=1)

        # For Daily Trigger set this variable to 2 ; for One time run set this value as 1
        TASK_TRIGGER_DAILY = 2
        trigger = task_def.Triggers.Create(TASK_TRIGGER_DAILY)

        #
        num_of_days = 2
        trigger.Repetition.Duration = "P" + str(num_of_days) + "D"

        # use PT2M for every 2 minutes, use PT1H for every 1 hour
        trigger.Repetition.Interval = "PT1M"
        trigger.StartBoundary = start_time.isoformat()
        print("something")
        # Create action
        TASK_ACTION_EXEC = 0
        action = task_def.Actions.Create(TASK_ACTION_EXEC)
        action.ID = 'TRIGGER BATCH'
        action.Path = 'powershell.exe'
        action.Arguments = '/c start "" "C:\\Users\\user\\Documents\\SQLScript\\SQl_BACKUP.ps1"'

        # Set paramenters
        task_def.RegistrationInfo.Description = 'Backup Task'
        task_def.Settings.Enabled = True
        task_def.Settings.StopIfGoingOnBatteries = False

        # Register task
        # If task already exists, it will be updated
        TASK_CREATE_OR_UPDATE = 6
        TASK_LOGON_NONE = 0
        root_folder.RegisterTaskDefinition(
            'Test Task',  # Task name
            task_def,
            TASK_CREATE_OR_UPDATE,
            '',  # No user
            '',  # No password
            TASK_LOGON_NONE
        )


if __name__ == "__main__":
    startSchedule()
