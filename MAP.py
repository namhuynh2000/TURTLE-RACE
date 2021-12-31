from time import sleep 
import pygame, sys, random, os
from pygame.locals import *


pygame.init()
FPS = 60
display_width = 800 #Dài
display_height = 600 #Rộng

#(R,G,B)
black = (0, 0, 0)
white = (255, 255, 255)
WHITE = (255, 253, 230)
red = (255, 0, 0)
yellow = (235, 208, 33)
green = (0, 255, 0)
YELLOW = (255, 222, 0)
blue = (0, 0, 255)
pink = (255, 23, 255)

#Setup màn hình game(width,height)
gameDisplay = pygame.display.set_mode((display_width,display_height))

#Tên cửa sổ game
pygame.display.set_caption('Map')
clock = pygame.time.Clock()



#Chèn hình trò chơi:
font = pygame.font.SysFont("comicsansms", 40)
Font = pygame.font.SysFont("freesansbold.ttf", 250)

#load ảnh:
Map = pygame.image.load('Choose_map.png')
xuan = pygame.image.load('xuan.png')
xuan2 = pygame.image.load('xuan2.png')
ha = pygame.image.load('ha.png')
ha2 = pygame.image.load('ha2.png')
thu = pygame.image.load('thu.png')
thu2 = pygame.image.load('thu2.png')
dong = pygame.image.load('dong.png')
dong2 = pygame.image.load('dong2.png')

def choose_map():
    global mousex
    global mousey
    gameDisplay.blit(Map,(0,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            mousex, mousey = pygame.mouse.get_pos()
            if event.type == MOUSEMOTION:

                if(mousex>=0 and mousex<=400 and mousey>=100 and mousey<=350):
                    gameDisplay.blit(Map,(0,0))
                    gameDisplay.blit(xuan2,(0,100))
                elif(mousex>=400 and mousex<=800 and mousey>=100 and mousey<=350):
                    gameDisplay.blit(Map,(0,0))
                    gameDisplay.blit(ha2,(400,100))
                elif(mousex>=0 and mousex<=400 and mousey>=350 and mousey<=600):
                    gameDisplay.blit(Map,(0,0))
                    gameDisplay.blit(thu2,(0,350))
                elif(mousex>=400 and mousex<=800 and mousey>=350 and mousey<=600):
                    gameDisplay.blit(Map,(0,0))
                    gameDisplay.blit(dong2,(401,350))
                else:
                    gameDisplay.blit(Map,(0,0))
            elif event.type == MOUSEBUTTONUP:
                if(mousex>=0 and mousex<=400 and mousey>=100 and mousey<=350):
                    return 1 #map xuân
                elif(mousex>=400 and mousex<=800 and mousey>=100 and mousey<=350):
                    return 2 #map hạ
                elif(mousex>=0 and mousex<=400 and mousey>=350 and mousey<=600):
                    return 3 #map thu
                elif(mousex>=400 and mousex<=800 and mousey>=350 and mousey<=600):
                    return 4 #map đông
        pygame.display.update()




clock.tick(FPS)
pygame.display.update()
