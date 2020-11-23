# msdn.microsoft.com/en-us/library/windows/desktop/bb762153(v=vs.85).aspx
import ctypes
import logging
import sys
import enum
import winreg
import itertools


class ERROR(enum.IntEnum):
    ZERO = 0
    FILE_NOT_FOUND = 2
    PATH_NOT_FOUND = 3
    BAD_FORMAT = 11
    ACCESS_DENIED = 5
    ASSOC_INCOMPLETE = 27
    DDE_BUSY = 30
    DDE_FAIL = 29
    DDE_TIMEOUT = 28
    DLL_NOT_FOUND = 32
    NO_ASSOC = 31
    OOM = 8
    SHARE = 26


class SW(enum.IntEnum):
    HIDE = 0
    MAXIMIZE = 3
    MINIMIZE = 6
    RESTORE = 9
    SHOW = 5
    SHOWDEFAULT = 10
    SHOWMAXIMIZED = 3
    SHOWMINIMIZED = 2
    SHOWMINNOACTIVE = 7
    SHOWNA = 8
    SHOWNOACTIVATE = 4
    SHOWNORMAL = 1


class Admin:

    def __init__(self):
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
                if name not in ['SQLEXPRESS','MSSQLSERVER',"."]:
                    name_list.append(name)
                count += 1
        except WindowsError:
            pass
        return name_list


