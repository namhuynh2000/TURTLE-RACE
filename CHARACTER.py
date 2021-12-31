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
character =pygame.image.load('Choose_character.png')
bird = pygame.image.load('Choose_bird.png')
dragon = pygame.image.load('Choose_dragon.png')
horse = pygame.image.load('Choose_horse.png')
man = pygame.image.load('Choose_man.png')
noman = pygame.image.load('Choose_noman.png')
slime = pygame.image.load('Choose_slime.png')

def choose_character(number):#number ở đây là số lượng 5 hay 10 nhân vật
    gameDisplay.blit(character,(0,0))
    pygame.display.update()
    if number == 5:
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEMOTION:
                    mousex, mousey = pygame.mouse.get_pos()
                    if(mousex>=81 and mousex<=186 and mousey>=440 and mousey<=520):
                        gameDisplay.blit(character,(0,0))
                        gameDisplay.blit(slime,(0,0))
                    elif(mousex>=225 and mousex<=321 and mousey>=440 and mousey<=523):
                        gameDisplay.blit(character,(0,0))
                        gameDisplay.blit(horse,(0,0))
                    elif(mousex>=365 and mousex<=450 and mousey>=444 and mousey<=520):
                        gameDisplay.blit(character,(0,0))
                        gameDisplay.blit(bird,(0,0))
                    elif(mousex>=500 and mousex<=581 and mousey>=421 and mousey<=525):
                        gameDisplay.blit(character,(0,0))
                        gameDisplay.blit(man,(0,0))
                    elif(mousex>=640 and mousex<=728 and mousey>=439 and mousey<=519):
                        gameDisplay.blit(character,(0,0))
                        gameDisplay.blit(dragon,(0,0))
                    else:
                        gameDisplay.blit(character,(0,0))
                elif event.type == MOUSEBUTTONUP:
                    if(mousex>=81 and mousex<=186 and mousey>=440 and mousey<=520):
                        return 1 #slime
                    elif(mousex>=225 and mousex<=321 and mousey>=440 and mousey<=523):
                        return 2 #horse
                    elif(mousex>=365 and mousex<=450 and mousey>=444 and mousey<=520):
                        return 3 #bird
                    elif(mousex>=500 and mousex<=581 and mousey>=421 and mousey<=525):
                        return 4 #man
                    elif(mousex>=640 and mousex<=728 and mousey>=439 and mousey<=519):
                         return 5 #dragon
                pygame.display.update()
    elif number == 10:
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEMOTION:
                    mousex, mousey = pygame.mouse.get_pos()
                    if(mousex>=81 and mousex<=186 and mousey>=440 and mousey<=520):
                        gameDisplay.blit(character,(0,0))
                        gameDisplay.blit(slime,(0,0))
                    elif(mousex>=225 and mousex<=321 and mousey>=440 and mousey<=523):
                        gameDisplay.blit(character,(0,0))
                        gameDisplay.blit(horse,(0,0))
                    elif(mousex>=365 and mousex<=450 and mousey>=444 and mousey<=520):
                        gameDisplay.blit(character,(0,0))
                        gameDisplay.blit(bird,(0,0))
                    elif(mousex>=500 and mousex<=581 and mousey>=421 and mousey<=525):
                        gameDisplay.blit(character,(0,0))
                        gameDisplay.blit(noman,(0,0))
                    elif(mousex>=640 and mousex<=728 and mousey>=439 and mousey<=519):
                        gameDisplay.blit(character,(0,0))
                        gameDisplay.blit(dragon,(0,0))
                    else:
                        gameDisplay.blit(character,(0,0))
                elif event.type == MOUSEBUTTONUP:
                    if(mousex>=81 and mousex<=186 and mousey>=440 and mousey<=520):
                        return 1 #slime
                    elif(mousex>=225 and mousex<=321 and mousey>=440 and mousey<=523):
                        return 2 #horse
                    elif(mousex>=365 and mousex<=450 and mousey>=444 and mousey<=520):
                        return 3 #bird
                    elif(mousex>=640 and mousex<=728 and mousey>=439 and mousey<=519):
                         return 5 #dragon
    
            pygame.display.update()


clock.tick(FPS)
pygame.display.update()
            
