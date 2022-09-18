import pygame
from time import sleep as wait
import random
import os,sys
pygame.init()
pygame.mixer.init()
play = True
win = pygame.display.set_mode((640,480))
def resource_path0(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
icon = pygame.image.load(resource_path0('icon.png'))
pygame.display.set_caption('War/Battle Sound Simulator')
pygame.display.set_icon(icon)
run = 1

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            run = 0
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                play = not play
    if play:
        sound = pygame.mixer.Sound(resource_path0('explosion.wav'))
        if random.randint(0,3) == 0:
            ak47 = pygame.mixer.Sound(resource_path0('ak47.mp3'))
            ak47.set_volume(random.uniform(0,1))
            ak47.play()
            if random.randint(0,1) == 0:
                oof = pygame.mixer.Sound(resource_path0('oof.ogg'))
                oof.set_volume(random.uniform(0,.5))
                oof.play()
        if random.randint(0,2) == 0:
            pistol = pygame.mixer.Sound(resource_path0('pistol.wav'))
            #reloading = pygame.mixer.Sound('reload.wav')
            pistol.set_volume(random.uniform(0,1))
            #reloading.set_volume(1)
            pistol.play()
            #reloading.play()
            if random.randint(0,1) == 0:
                oof = pygame.mixer.Sound(resource_path0('oof.ogg'))
                oof.set_volume(random.uniform(0,.5))
                oof.play()
        if random.randint(0,7) == 0:
            rocket = pygame.mixer.Sound(resource_path0('rocket.wav'))
            rocket.set_volume(1)
            rocket.play()
            if random.randint(0,1) == 0:
                oof = pygame.mixer.Sound(resource_path0('oof.ogg'))
                oof.set_volume(random.uniform(0,.5))
                oof.play()
        if random.randint(0,11) == 0:
            sniper = pygame.mixer.Sound(resource_path0('sniper.wav'))
            sniper.set_volume(random.uniform(0.5,1))
            sniper.play()
        sound.set_volume(random.uniform(0,1))
        sound.play()
        wait(random.uniform(0,.02))