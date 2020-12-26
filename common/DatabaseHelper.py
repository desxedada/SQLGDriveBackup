import datetime
import sys
import apscheduler
import time
import pyodbc
import logging

from common.APS import customSchedule
from log.Logger import exception
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler, BaseScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

def initialize_params(server,trust_conn):
    params = (r"DRIVER={ODBC Driver 17 for SQL Server};"
                  f"SERVER={server};"
                  f"Trusted_Connection={trust_conn};"
                  )
    return params

   
def test_connection(server,trust_conn):

    for retry in range(3):
        try:
            params = initialize_params(server,trust_conn)
            conn = pyodbc.connect(params)
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            logging.info("Connection Established")
            conn.close()
            return "Connection established"
        except pyodbc.ProgrammingError as e:
            return "Connection Failed"

   
def displayAllDatabases(server,trust_conn):
    databases = []
    try:
        params = initialize_params(server, trust_conn)
        conn = pyodbc.connect(params)
        cursor = conn.cursor()

        cursor.execute("select name from sys.databases WHERE name NOT IN ('master','model','msdb','tempdb')")
        for row in cursor.fetchall():
            databases.append(row[0])
    except pyodbc.ProgrammingError as e:
        return "Connection Failed"

    return databases


def backup_database(server, trust_conn,name,path):
        params = initialize_params(server,trust_conn)
        conn = pyodbc.connect(params)
        cursor = conn.cursor()
        conn.autocommit = True
        timestamp = time.strftime("%Y-%m-%d_%H-%M")
        cursor.execute(
        f"BACKUP DATABASE {name} TO DISK = '{path}\\{name}_{timestamp}.bak'")
        logging.info(f"{name} is being backed up")

def run_cron_job(name, path, hour):
    # apscheduler defaults

    jobstores = {
            'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    }
    executors = {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(5)
    }
    job_defaults = {
        'coalesce': False,
        'max_instances': 3
    }

    scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
    scheduler.add_job(func=backup_database, args=(name, path), trigger="cron",hour=hour)
    try:
        scheduler.start()
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
         scheduler.shutdown()


