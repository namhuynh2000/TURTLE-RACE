import pygame, sys, random, os
from pygame.locals import *
pygame.init()

#tọa độ màn hình
display_width=800
display_height=600

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

#chiều dài, rộng icon
icon_width = 70
icon_height = 60

#tọa độ các icon
icon_x1=168
icon_x2=273
icon_x3=375
icon_x4=477
icon_x5=573

icon_y1=405
icon_y2=495

#font
font = pygame.font.SysFont("comicsansms", 100)
font1 = pygame.font.SysFont("comicsansms", 50)
Font = pygame.font.SysFont("freesansbold.ttf", 250)


#Màn hình và caption
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Select bet")
clock=pygame.time.Clock()

#load hình ảnh
slime_bet = pygame.image.load("slime_bet2.png")
dinosour_bet = pygame.image.load("dinosour_bet2.png")
flappy_bird_bet = pygame.image.load("flappy_bird_bet2.png")
horse_bet = pygame.image.load("Horse_bet2.png")
person_bet = pygame.image.load("person_bet2.png")
star_select = pygame.image.load("star_select.png")
slime_bet2 = pygame.image.load("slime_bet2.png")
dinosour_bet2 = pygame.image.load("dinosour_bet2.png")
flappy_bird_bet2 = pygame.image.load("flappy_bird_bet2.png")
horse_bet2 = pygame.image.load("Horse_bet2.png")
person_bet2 = pygame.image.load("person_bet2.png")
selectcmm = pygame.image.load("selectcmm.png")


background_image_position =[0,0]

def select_bet(number, character, money):
    if(number == 5):
        if(character == 1):
            gameDisplay.blit(slime_bet,(0,0))
            draw_yourmoney(money)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x1, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x2, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x3, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x4, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x5, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        else:
                            gameDisplay.blit(slime_bet,(0,0))
                            draw_yourmoney(money)
                            pygame.display.update()



                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            return 1
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            return 2
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            return 3
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            return 4
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            return 5

        if (character == 2):
            gameDisplay.blit(horse_bet, (0, 0))
            draw_yourmoney(money)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x1, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x2, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x3, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x4, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x5, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        else:
                            gameDisplay.blit(horse_bet,(0,0))
                            draw_yourmoney(money)
                            pygame.display.update()

                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 1
                        elif (mousex >= icon_x2 and mousex <= icon_x2 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 2
                        elif (mousex >= icon_x3 and mousex <= icon_x3 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 3
                        elif (mousex >= icon_x4 and mousex <= icon_x4 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 4
                        elif (mousex >= icon_x5 and mousex <= icon_x5 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 5

        if (character == 3):
            gameDisplay.blit(flappy_bird_bet, (0, 0))
            draw_yourmoney(money)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x1, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x2, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x3, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x4, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x5, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        else:
                            gameDisplay.blit(flappy_bird_bet,(0,0))
                            draw_yourmoney(money)
                            pygame.display.update()

                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 1
                        elif (mousex >= icon_x2 and mousex <= icon_x2 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 2
                        elif (mousex >= icon_x3 and mousex <= icon_x3 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 3
                        elif (mousex >= icon_x4 and mousex <= icon_x4 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 4
                        elif (mousex >= icon_x5 and mousex <= icon_x5 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 5

        if (character == 4):
            gameDisplay.blit(person_bet, (0, 0))
            draw_yourmoney(money)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x1+20, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x2+20, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x3+20, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x4+20, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x5+20, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        else:
                            gameDisplay.blit(person_bet,(0,0))
                            draw_yourmoney(money)
                            pygame.display.update()

                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 1
                        elif (mousex >= icon_x2 and mousex <= icon_x2 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 2
                        elif (mousex >= icon_x3 and mousex <= icon_x3 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 3
                        elif (mousex >= icon_x4 and mousex <= icon_x4 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 4
                        elif (mousex >= icon_x5 and mousex <= icon_x5 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 5

        if (character == 5):
            gameDisplay.blit(dinosour_bet, (0, 0))
            draw_yourmoney(money)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x1, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x2, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x3, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x4, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x5, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        else:
                            gameDisplay.blit(dinosour_bet,(0,0))
                            draw_yourmoney(money)
                            pygame.display.update()

                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 1
                        elif (mousex >= icon_x2 and mousex <= icon_x2 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 2
                        elif (mousex >= icon_x3 and mousex <= icon_x3 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 3
                        elif (mousex >= icon_x4 and mousex <= icon_x4 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 4
                        elif (mousex >= icon_x5 and mousex <= icon_x5 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 5



    if(number == 10):
        if(character == 1):
            gameDisplay.blit(slime_bet,(0,0))
            draw_yourmoney(money)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x1, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x2, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x3, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x4, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x5, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x1, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x2, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x3, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x4, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x5, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        else:
                            gameDisplay.blit(slime_bet,(0,0))
                            draw_yourmoney(money)
                            pygame.display.update()

                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            return 1
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            return 2
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            return 3
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            return 4
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            return 5
                        elif (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 6
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 7
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 8
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 9
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 10

        if (character == 2):
            gameDisplay.blit(horse_bet, (0, 0))
            draw_yourmoney(money)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x1, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x2, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x3, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x4, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x5, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x1, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x2, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x3, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x4, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x5, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        else:
                            gameDisplay.blit(horse_bet,(0,0))
                            draw_yourmoney(money)
                            pygame.display.update()

                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 1
                        elif (mousex >= icon_x2 and mousex <= icon_x2 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 2
                        elif (mousex >= icon_x3 and mousex <= icon_x3 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 3
                        elif (mousex >= icon_x4 and mousex <= icon_x4 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 4
                        elif (mousex >= icon_x5 and mousex <= icon_x5 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 5
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            return 5
                        elif (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 6
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 7
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 8
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 9
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 10

        if (character == 3):
            gameDisplay.blit(flappy_bird_bet, (0, 0))
            draw_yourmoney(money)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x1, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x2, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x3, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x4, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x5, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x1, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x2, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x3, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x4, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x5, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        else:
                            gameDisplay.blit(flappy_bird_bet,(0,0))
                            draw_yourmoney(money)
                            pygame.display.update()

                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 1
                        elif (mousex >= icon_x2 and mousex <= icon_x2 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 2
                        elif (mousex >= icon_x3 and mousex <= icon_x3 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 3
                        elif (mousex >= icon_x4 and mousex <= icon_x4 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 4
                        elif (mousex >= icon_x5 and mousex <= icon_x5 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 5
                        elif (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 6
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 7
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 8
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 9
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 10



        if (character == 5):
            gameDisplay.blit(dinosour_bet, (0, 0))
            draw_yourmoney(money)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x1, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x2, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x3, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x4, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y1+icon_height):
                            gameDisplay.blit(star_select, (icon_x5, icon_y1))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x1, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x2, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x3, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x4, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y2 and mousey <= icon_y2+icon_height):
                            gameDisplay.blit(star_select, (icon_x5, icon_y2))
                            draw_yourmoney(money)
                            pygame.display.update()
                        else:
                            gameDisplay.blit(dinosour_bet,(0,0))
                            draw_yourmoney(money)
                            pygame.display.update()

                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = pygame.mouse.get_pos()
                        if (mousex >= icon_x1 and mousex <= icon_x1 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 1
                        elif (mousex >= icon_x2 and mousex <= icon_x2 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 2
                        elif (mousex >= icon_x3 and mousex <= icon_x3 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 3
                        elif (mousex >= icon_x4 and mousex <= icon_x4 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 4
                        elif (mousex >= icon_x5 and mousex <= icon_x5 + icon_width and mousey >= icon_y1 and mousey <= icon_y1 + icon_height):
                            return 5
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 5
                        elif (mousex >= icon_x1 and mousex <= icon_x1+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 6
                        elif (mousex >= icon_x2 and mousex <= icon_x2+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 7
                        elif (mousex >= icon_x3 and mousex <= icon_x3+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 8
                        elif (mousex >= icon_x4 and mousex <= icon_x4+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 9
                        elif (mousex >= icon_x5 and mousex <= icon_x5+icon_width and mousey >= icon_y1 and mousey <= icon_y2+icon_height):
                            return 10


            pygame.display.update()

    pygame.display.update()
    clock.tick(50)
def draw_yourmoney(money):
    yourmoney = font.render(str(money), True, red)
    gameDisplay.blit(yourmoney,(50,160))
    pygame.display.update()
def select(number,character,money):
    #money số tiền của bạn
    #numver là số nhân vật 5 hoặc 10
    #character là nhân vật
    hocky=select_bet(number,character,money)
    if (hocky!=0):
        bet=0
        yourbet = font1.render(str(bet), True, red)
        gameDisplay.blit(yourbet,(560,190))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = pygame.mouse.get_pos()
                    if 423<=mousex<=513 and 172<=mousey<=261 and bet >=10:
                        bet=bet-10
                        gameDisplay.blit(selectcmm,(400,0))
                        yourbet = font1.render(str(bet), True, red)
                        gameDisplay.blit(yourbet,(560,190))
                        pygame.display.update()
                    elif 693<=mousex<=783 and 172<=mousey<=261 and bet<=(money-10):
                        bet=bet+10
                        gameDisplay.blit(selectcmm,(400,0))
                        yourbet = font1.render(str(bet), True, red)
                        gameDisplay.blit(yourbet,(560,190))
                        pygame.display.update()
                    elif 9<=mousex<=103 and 492<=mousey<=579:
                         return 0,0 # quay lại
                    elif 690<=mousex<=782 and 492<=mousey<=579 and bet!=0:
                        return bet,hocky #next, bet trả về số tiền cược hocky là con vật
            pygame.display.update()