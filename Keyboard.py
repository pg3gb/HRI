# HRI - Keyboard Commands for Marley
#git push
import RPi.GPIO as GPIO
import time
import pygame
import RGB
from pygame.locals import *

pygame.init()

done = 0

while done == False:
    for event in pygame.event.get():
        # any other key event input
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == KEYDOWN:
            if event.key == K_ESC:
                done = 1

    # get key current state
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        print 'left pressed!'


