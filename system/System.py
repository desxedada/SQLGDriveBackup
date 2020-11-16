import ctypes
import sys
from system import SW
from system import ERROR

class System:

 def checkIfAdmin(self):
    if ctypes.windll.shell32.IsUserAnAdmin():
            print(input("Echo: "))
    else:
        #activate Windows Admin
        hinstance = ctypes.windll.shell32.ShellExecuteW(
        None, 'runas', sys.executable, sys.argv[0], None, SW.SHOWNORMAL
        )
        if hinstance <= 32:
            raise RuntimeError(ERROR(hinstance))

