from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

executors = {
    'default': ThreadPoolExecutor(20)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 1
}

task_schedule = BackgroundScheduler(jobstores=jobstores,executors=executors,job_defaults=job_defaults)
task_schedule.start()
