
from database import DatabaseHelper

class MSSQL:


    instance = ""
    db_username = ""
    db_password = ""
    trusted_cnxn = 'yes'

    def __init__(self,driver,instance, username,password,cnxn):
        self.driver = driver
        self.instance = instance
        self.db_username = username
        self.db_password = password
        self.trusted_cnxn = cnxn


    #GET Methods
    def get_driver(self):
        return self.driver

    def get_Instance(self):
        return self.instance

    def get_dbUsername(self):
        return self.db_username

    def get_dbPassword(self):
        return self.driver

    def getConnectionAuth(self):
        return self.trusted_cnxn