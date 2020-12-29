# msdn.microsoft.com/en-us/library/windows/desktop/bb762153(v=vs.85).aspx
import ctypes
import difflib
import sys
import winreg
import wmi
import win32con
import win32gui_struct

class Registry:

    def __init__(self):
        pass

    def check_Admin(self):
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
        if not isAdmin:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

    def sub_keys(self):
        reg_path = r"SOFTWARE\\Microsoft\\Microsoft SQL Server\\Instance Names\\SQL"
        parentKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, access=winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
        name_list = []
        try:
            count = 1
            while 1:
                name, key, value = winreg.EnumValue(parentKey, count)
                if name not in ['SQLEXPRESS', 'MSSQLSERVER', "."]:
                    name_list.append(name)
                count += 1
        except WindowsError:
            pass
        return name_list

    def get_instance(self):
        import wmi

        c = wmi.WMI()
        for svc in c.Win32_Service():
            print(svc.name)

