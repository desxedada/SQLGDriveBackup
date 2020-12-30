import time
import pyodbc
import logging
from pytz import utc


from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.jobstores.base import JobLookupError
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler


class DatabaseHelper():

    def __init__(self):
        pass

    def initialize_params(self, server, trust_conn):
        params = (r"DRIVER={ODBC Driver 17 for SQL Server};"
                  f"SERVER={server};"
                  f"Trusted_Connection={trust_conn};"
                  )
        return params

    def test_connection(self, params):

        for retry in range(3):
            try:
                conn = pyodbc.connect(params)
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                logging.info("Connection Established")
                conn.close()
                return "Connection established"
            except pyodbc.ProgrammingError as e:
                return "Connection Failed"

    def displayAllDatabases(self, params):
        databases = []
        try:
            conn = pyodbc.connect(params)
            cursor = conn.cursor()

            cursor.execute("select name from sys.databases WHERE name NOT IN ('master','model','msdb','tempdb')")
            for row in cursor.fetchall():
                databases.append(row[0])
        except pyodbc.ProgrammingError as e:
            return "Connection Failed"

        return databases

    def backup_database(self, params, name, path):
        conn = pyodbc.connect(params)
        cursor = conn.cursor()
        conn.autocommit = True
        timestamp = time.strftime("%Y-%m-%d__%H-%M")
        file_name = f'{name}_{timestamp}.bak'
        cursor.execute(
            f"BACKUP DATABASE {name} TO DISK = '{path}\\{file_name}'")
        logging.info(f"{name} is being backed up")


class APS:
    def __init__(self):
        self.sched = BackgroundScheduler()
        self.sched.start()
        self.job_id = ''

    def __del__(self):
        self.shutdown()

    def shutdown(self):
        self.sched.shutdown()

    def kill_scheduler(self, job_id):
        try:
            self.sched.remove_job(job_id)
        except JobLookupError as err:
            logging.error("fail to stop Scheduler: {err}".format(err=err))
            return

    def run_job(self):
        print("doing something")
        logging.info("Running Job")

    def add_schedule(self, hour, minute):
        logging.info("{type} Scheduler Start".format(type="cron"))
        self.sched.add_job(self.run_job, "cron", day_of_week='mon-fri'
                           , hour=hour
                           , minute=minute
                           , second=00
                           )


if __name__ == '__main__':
    dh = DatabaseHelper()
    params = dh.initialize_params(".\\DEVTEST", "yes")
    _schedule = APS()
    logging.info("Start Job")
    while True:
        _schedule.add_schedule(16,46)
        dh.backup_database(params, "developer", "C:\\Backups")


#https://gitlab.corp.sellmate.co.kr/sellmate/message-schedule/-/blob/e21531be3368f0e41d6d9c70786ae8634e8d6d53/main.py