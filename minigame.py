def minigame():
    import pygame
    from time import sleep
    import random
    import gif_pygame
    import pyautogui
    import subprocess
    pygame.init()
    clock = pygame.time.Clock()
    
    static = gif_pygame.load("static.gif")
    pygame.mixer.Sound('thenyouwilldie.mp3').play()
    sleep(4.4)
    #pyautogui.hotkey('winleft','d')
    screen = pygame.display.set_mode([1920,1200])
    freddy = pygame.image.load("freddy-right.png").convert()
    state = 0
    aggr = 0
    blackout = False
    colour = [0,0,0]
    pygame.mixer_music.load("freddy.mp3")
    pygame.mixer_music.set_volume(0.1)
    pygame.mixer_music.play()
    footstep = pygame.mixer.Sound("footstep.wav")
    jumpscare = gif_pygame.load("jumpscare.gif")
    jumpscare_time = 0
    scream = pygame.mixer.Sound("jumpscare.mp3")
    pygame.mouse.set_visible(False)
    pyautogui.leftClick(800,700)
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pass
        if aggr > 2400 and random.randint(1,800) == 1:
            pygame.mixer_music.stop()
            colour = [100,100,100]
            screen.fill(colour)
            colour = [0,0,0]
            pygame.display.update()
            aggr = 0
            blackout = True
        if blackout:
            screen.fill(colour)
            if random.randint(1,1200) == 1 and jumpscare_time == 0 and aggr > 1200:
                jumpscare_time += 1
                scream.set_volume(1.0)
                scream.play()
                continue
            if jumpscare_time >=87:
                scream.stop()
                break
            if jumpscare_time > 0:
                screen.fill(colour)
                jumpscare.render(screen,(0,120))
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
        freddy.set_alpha(random.randint(1,20)+aggr/75)
        screen.fill(colour)
        if random.randint(1,1) == 1 and aggr > 840:
            screen.blit(freddy,(0,0))
        if random.randint(1,200) == 1 and aggr > 840:
            freddy = pygame.image.load(random.choice(["freddy-left.png"])).convert()

        pygame.display.update()
        aggr += 1
        if random.randint(1,120) and aggr>420:
            pygame.mixer_music.set_volume(pygame.mixer_music.get_volume()+0.5)
        clock.tick(120)
    
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pass
        screen.fill(colour)
        static.render(screen,(0,0))
        pygame.display.update()
        clock.tick(120)
    
    pygame.quit()
    
if __name__ == "__main__":
    minigame()