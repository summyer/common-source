# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:13:02 2018

@author: Administrator
"""

background_image_filename = 'sushiplate.jpg'
 
import pygame
from pygame.locals import *
from sys import exit
 
SCREEN_SIZE = (640, 480)
 
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
 
background = pygame.image.load(background_image_filename).convert()
 
while True:
 
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.quit()
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Window resized to "+str(event.size))
 
    screen_width, screen_height = SCREEN_SIZE
    # 这里需要重新填满窗口
    screen.blit(background, (x, y))
            
 
    pygame.display.update()