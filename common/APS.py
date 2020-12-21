
from datetime import datetime
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler

class APS(object):
    def __init__(self):
        self._cron_jobs = {}
        self._scheduler = None

    def add_cron_job(self, job, **kwargs):
        self._cron_jobs[job.__name__] = (job, kwargs)
        return len(self._cron_jobs)

    def start_scheduler(self):
        if len(self._cron_jobs) <= 0:
            return False
        self._scheduler = Scheduler()
        for job, kwargs in self._cron_jobs.values():
            self._scheduler.add_job(job, 'cron', id=job.__name__, **kwargs)
        self._scheduler.start()
        return True

    def stop_scheduler(self):
        if self._scheduler is not None:
            self._scheduler.shutdown()

class customSchedule(APS):
    def __init__(self):
        APS.__init__(self)

    def add_schedule(self, job, time):
        self.add_cron_job(job, args=[name,path],second=time)


