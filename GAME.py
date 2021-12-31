from time import sleep 
import pygame, sys, random, os
from pygame.locals import *
from BXH import *
from MINIGAME import *
from MAP import *
from CHARACTER import *
from NUMBER import *
from MENU2 import *
from Instruction import *




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
pygame.display.set_caption('RACE')
clock = pygame.time.Clock()



#Chèn hình trò chơi:
font = pygame.font.SysFont("comicsansms", 40)
Font = pygame.font.SysFont("freesansbold.ttf", 250)

def Continue():
        MAP = choose_map()
        NUMBER = choose_number()
        C_CHARACTER = choose_character(NUMBER)
        return drawbxh(3,2,1,'lose',100,300,2500,CHARACTER)

def main():
        x=Menu()
        if x == 1:
                MAP = choose_map()
                NUMBER = choose_number()
                C_CHARACTER = choose_character(NUMBER)
                bet(MAP,NUMBER,C_CHARACTER,100,50,2)

        elif x == 2:
                MAP = choose_map()
                NUMBER = choose_number()
                CHARACTER = choose_character(NUMBER)
                minimain()
        elif x == 3:
                i=huongdan()
                if(i==1):
                        main()


while True:
        main()

clock.tick(FPS)
pygame.display.update()






    
