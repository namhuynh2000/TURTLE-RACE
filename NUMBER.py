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
pygame.display.set_caption('Character')
clock = pygame.time.Clock()



#Chèn hình trò chơi:
font = pygame.font.SysFont("comicsansms", 40)
Font = pygame.font.SysFont("freesansbold.ttf", 250)

#load ảnh:
number = pygame.image.load('Choose_number.png')
nam = pygame.image.load('Choose_number_5.png')
muoi = pygame.image.load('Choose_number_10.png')


def choose_number():
        gameDisplay.blit(number,(0,0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEMOTION:
                    mousex, mousey = pygame.mouse.get_pos()
                    if(mousex>=160 and mousex<=260 and mousey>=290 and mousey<=450):
                        gameDisplay.blit(nam,(0,0))
                    elif(mousex>=450 and mousex<=630 and mousey>=290 and mousey<=450):
                        gameDisplay.blit(muoi,(0,0))
                    else:
                        gameDisplay.blit(number,(0,0))
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = pygame.mouse.get_pos()
                    if(mousex>=160 and mousex<=260 and mousey>=290 and mousey<=450):
                        return 5
                    elif(mousex>=450 and mousex<=630 and mousey>=290 and mousey<=450):
                        return 10
                    
                        
                    
                pygame.display.update()
            


clock.tick(FPS)
pygame.display.update()
