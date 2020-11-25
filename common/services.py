import os

import win32serviceutil
import win32service
import win32event
import servicemanager
import socket

class AppSVC(win32serviceutil.ServiceFramework):
    svc_name = "SQLBackupTool"
    svc_display_name = "SQLBackupTool Service"
    svc_description = "Backup Tool for SQL Database"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)


    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self.svc_name, ''))
        self.main()

    def start(self):
        # Override to add logic before the start
        pass

    def stop(self):
        # Override to add logic before the stop
        pass

    def main(self):
        # main class to be overridden
        pass
