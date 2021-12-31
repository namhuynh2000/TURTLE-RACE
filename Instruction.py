from time import sleep 
import pygame, sys, random, os
from pygame.locals import *
from MENU2 import *

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
#gameDisplay = pygame.display.set_mode((display_width,display_height))

#Tên cửa sổ game
#pygame.display.set_caption('Instruction')
clock = pygame.time.Clock()


#Chèn hình trò chơi:
font = pygame.font.SysFont("comicsansms", 40)
Font = pygame.font.SysFont("freesansbold.ttf", 250)
#Load ảnh:
hd1 = pygame.image.load('hd1.png')
hd2 = pygame.image.load('hd2.png')
hd3 = pygame.image.load('hd3.png')
hd4 = pygame.image.load('hd4.png')
hd5 = pygame.image.load('hd5.png')
hd6 = pygame.image.load('hd6.png')
hd7 = pygame.image.load('hd7.png')
hd8 = pygame.image.load('hd8.png')
hd9 = pygame.image.load('hd9.png')
hd10 = pygame.image.load('hd10.png')
hd11 = pygame.image.load('hd11.png')
hd12 = pygame.image.load('hd12.png')
hd13 = pygame.image.load('hd13.png')
hd14 = pygame.image.load('hd14.png')
hd15 = pygame.image.load('hd15.png')
hd16 = pygame.image.load('hd16.png')
Quit = pygame.image.load('quit.png')
Quit2 = pygame.image.load('quit2.png')

def draw_hd(x):
    if x==1:
        gameDisplay.blit(hd1,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==2:
        gameDisplay.blit(hd2,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==3:
        gameDisplay.blit(hd3,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==4:
        gameDisplay.blit(hd4,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==5:
        gameDisplay.blit(hd5,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==6:
        gameDisplay.blit(hd6,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==7:
        gameDisplay.blit(hd7,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==8:
        gameDisplay.blit(hd8,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==9:
        gameDisplay.blit(hd9,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==10:
        gameDisplay.blit(hd10,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==11:
        gameDisplay.blit(hd11,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==12:
        gameDisplay.blit(hd12,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==13:
        gameDisplay.blit(hd13,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()
    if x==14:
        gameDisplay.blit(hd14,(0,0))
        gameDisplay.blit(Quit,(350,550))
        pygame.display.update()



def huongdan():
    dem = 1
    gameDisplay.blit(hd1,(0,0))
    gameDisplay.blit(Quit,(350,550))
    pygame.display.update()  
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
                if 440>=mousex >=350 and 550<=mousey<= 595:
                    gameDisplay.blit(Quit2,(350,550))
                    pygame.display.update()  
                else:
                    gameDisplay.blit(Quit,(350,550))
                    pygame.display.update()  
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = pygame.mouse.get_pos()
                if 790>=mousex >=700 and 490<=mousey<= 577:
                    dem+=1
                    if(dem>=14):
                        dem=14
                    draw_hd(dem)
                elif 5<=mousex<=97 and 490<=mousey<=577:
                    dem-=1
                    if(dem<=1):
                        dem=1
                    draw_hd(dem)
                elif 440>=mousex >=350 and 550<=mousey<= 595:
                    return 1



clock.tick(FPS)
pygame.display.update()
