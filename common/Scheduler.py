import schedule
from common import ServiceHandler
from common.DatabaseHelper import DatabaseHelper

class Scheduler(ServiceHandler):
    def __init__(self):
        self.schedule_time = None

    def Job(self,server,conn,databaseList,path):
        database_instance = DatabaseHelper(server,conn)

        database_instance.backup_database()



    def main(self):
        pass