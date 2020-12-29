import time
import pyodbc
import logging
from datetime import datetime, timedelta
from time import sleep

from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler

from common.APS import customSchedule


class APS(object):
    def __init__(self):
        self._cron_jobs = {}
        self._interval_jobs = {}
        self._scheduler = None

    def add_cron_job(self, job, **kwargs):
        self._cron_jobs[job.__name__] = (job, kwargs)
        return len(self._cron_jobs)

    def add_interval_jobs(self, job, **kwargs):
        self._interval_jobs[job.__name__] = (job, kwargs)
        return len(self._interval_jobs)

    def start_scheduler(self):
        if len(self._cron_jobs) <= 0:
            return False
        self._scheduler = Scheduler()
        for job, kwargs in self._interval_jobs.values():
            self._scheduler.add_job(job, 'interval', id=job.__name__, **kwargs)
        for job, kwargs in self._cron_jobs.values():
            self._scheduler.add_job(job, 'cron', id=job.__name__, **kwargs)
        self._scheduler.start()
        return True

    def stop_scheduler(self):
        if self._scheduler is not None:
            self._scheduler.shutdown()


class DatabaseHelper(APS):
    def __init__(self,server,trust_conn):
        APS.__init__(self)
        logging.basicConfig()
        logging.getLogger('apscheduler').setLevel(logging.DEBUG)
        self.server = server
        self.trust_conn = trust_conn


    def initialize_params(self):
        params = (r"DRIVER={ODBC Driver 17 for SQL Server};"
                  f"SERVER={self.server};"
                  f"Trusted_Connection={self.trust_conn};"
                  )
        return params

    def test_connection(self):

        for retry in range(3):
            try:
             params = self.initialize_params()
             conn = pyodbc.connect(params)
             cursor = conn.cursor()
             cursor.execute("SELECT 1")
             logging.info("Connection Established")
             conn.close()
             return "Connection established"
            except pyodbc.ProgrammingError as e:
                return "Connection Failed"

   
    def displayAllDatabases(self):
        databases = []
        try:
            params = self.initialize_params()
            conn = pyodbc.connect(params)
            cursor = conn.cursor()

            cursor.execute("select name from sys.databases WHERE name NOT IN ('master','model','msdb','tempdb')")
            for row in cursor.fetchall():
                databases.append(row[0])
        except pyodbc.ProgrammingError as e:
            return "Connection Failed"

        return databases

    def backup_database(self,name,path):
        params = self.initialize_params()
        conn = pyodbc.connect(params)
        cursor = conn.cursor()
        conn.autocommit = True
        timestamp = time.strftime("%Y-%m-%d_%H-%M")
        cursor.execute(
        f"BACKUP DATABASE {name} TO DISK = '{path}\\{name}_{timestamp}.bak'")
        logging.info(f"{name} is being backed up")

        #customS.stop_scheduler()

    def print_something(self):
        print("sdadsad")

    def add_schedule(self,job,time):
        time = datetime.now() + timedelta(minutes=1)
        self.add_cron_job(
            job, hour=time.hour, minute=time.minute
            )


if __name__ == '__main__':
    try:
        dh = DatabaseHelper(".\\DEVTEST","yes")
        dh.add_schedule(dh.print_something,5)
        dh.start_scheduler()
    except Exception:
        dh.stop_scheduler()
