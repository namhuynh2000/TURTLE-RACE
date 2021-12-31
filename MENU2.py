from time import sleep 
import pygame, sys, random, os.path
from pygame.locals import *
import pygame_textinput

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
pygame.display.set_caption('Menu')
clock = pygame.time.Clock()


#Chèn hình trò chơi:
font = pygame.font.SysFont("comicsansms", 40)
Font = pygame.font.SysFont("freesansbold.ttf", 250)


#load các hình ảnh
nhom = pygame.image.load("GAME_NAME.png")
login = pygame.image.load("Login.png")
sign_up = pygame.image.load("Signup.png")
instruction = pygame.image.load("Instruction.png")
quits = pygame.image.load("Quit1.png")
background_image=pygame.image.load("spring.png")

def Menu():
    #load nnhạc
    pygame.mixer.music.load('nhacchaygame.mp3')
    pygame.mixer.music.play(-1)
    gameDisplay.blit(background_image,(0,0))
    gameDisplay.blit(nhom,(190,10))
    gameDisplay.blit(login,(305,240))
    gameDisplay.blit(sign_up,(305,330))
    gameDisplay.blit(instruction,(305,420))
    gameDisplay.blit(quits,(305,510))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = pygame.mouse.get_pos()
                if(mousex>=305 and mousex<=455 and mousey>=240 and mousey<=310):
                    return 1
                elif(mousex>=305 and mousex<=455 and mousey>=330 and mousey<=400):
                    return 2
                elif(mousex>=305 and mousex<=455 and mousey>=420 and mousey<=490):
                    return 3 
                elif(mousex>=305 and mousex<=455 and mousey>=510 and mousey<=580):
                    pygame.quit()
                    quit()
        pygame.display.update()


clock.tick(FPS)
pygame.display.update()
