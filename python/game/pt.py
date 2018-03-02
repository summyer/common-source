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

font = pygame.font.SysFont("arial", 64)
#这句话总是可以的，所以还是TTF文件保险啊
text_surface = font.render(u"hello", True, (0, 0, 255))
x1 = 0
y1 = (480 - text_surface.get_height())/2

while True:
    print('x --',x1)
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
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))

    if x1 < 480:
        #print(x)
        x1 = 2+x1
        #print(x)
 
    screen.blit(text_surface, (x1, y1))
    pygame.display.update()