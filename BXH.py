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
pygame.display.set_caption('Top Ranking')
clock = pygame.time.Clock()



#Chèn hình trò chơi:
font = pygame.font.SysFont("comicsansms", 40)
Font = pygame.font.SysFont("freesansbold.ttf", 250)


#Load bxh
bxh = pygame.image.load('bxh4.png')
youlose = pygame.image.load('youlose2.png')
youwin = pygame.image.load('youwin2.png')
Quit = pygame.image.load('quit.png')
Quit2 = pygame.image.load('quit2.png')
Continue =pygame.image.load('continue.png')
Continue2 =pygame.image.load('continue2.png')

#Load horse
horse1 = pygame.image.load('0horse (1).png')
horse2 = pygame.image.load('1horse (1).png')
horse3 = pygame.image.load('2horse (1).png')
horse4 = pygame.image.load('3horse (1).png')
horse5 = pygame.image.load('4horse (1).png')
horse6 = pygame.image.load('5horse (1).png')
horse7 = pygame.image.load('6horse (1).png')
horse8 = pygame.image.load('7horse (1).png')
horse9 = pygame.image.load('8horse (1).png')
horse10 = pygame.image.load('9horse (1).png')

#Load bird
bird1 = pygame.image.load('0bird (1).png')
bird2 = pygame.image.load('1bird (1).png')
bird3 = pygame.image.load('2bird (1).png')
bird4 = pygame.image.load('3bird (1).png')
bird5 = pygame.image.load('4bird (1).png')
bird6 = pygame.image.load('5bird (1).png')
bird7 = pygame.image.load('6bird (1).png')
bird8 = pygame.image.load('7bird (1).png')
bird9 = pygame.image.load('8bird (1).png')
bird10 = pygame.image.load('9bird (1).png')

#Load dragon
dragon1 = pygame.image.load('0dinosour (1).png')
dragon2 = pygame.image.load('1dinosour (1).png')
dragon3 = pygame.image.load('2dinosour (1).png')
dragon4 = pygame.image.load('3dinosour (1).png')
dragon5 = pygame.image.load('4dinosour (1).png')
dragon6 = pygame.image.load('5dinosour (1).png')
dragon7 = pygame.image.load('6dinosour (1).png')
dragon8 = pygame.image.load('7dinosour (1).png')
dragon9 = pygame.image.load('8dinosour (1).png')
dragon10 = pygame.image.load('9dinosour (1).png')

#Load slime
slime1 = pygame.image.load('0slime (1).png')
slime2 = pygame.image.load('1slime (1).png')
slime3 = pygame.image.load('2slime (1).png')
slime4 = pygame.image.load('3slime (1).png')
slime5 = pygame.image.load('4slime (1).png')
slime6 = pygame.image.load('5slime (1).png')
slime7 = pygame.image.load('6slime (1).png')
slime8 = pygame.image.load('7slime (1).png')
slime9 = pygame.image.load('8slime (1).png')
slime10 = pygame.image.load('9slime (1).png')

#Load man
man1 = pygame.image.load('0nguoi (1).png')
man2 = pygame.image.load('1nguoi (1).png')
man3 = pygame.image.load('2nguoi (1).png')
man4 = pygame.image.load('3nguoi (1).png')
man5 = pygame.image.load('4nguoi (1).png')



def draw_your_bet(x): #x ở đây là số tiền cược
    text = font.render(str(x), True, white)
    gameDisplay.blit(text,(400,245))
def draw_your_money(x): #x ở đây là tổng tiền sau khi kết thúc game
        text = font.render(str(x), True, white)
        gameDisplay.blit(text,(400,357))
def draw_money_received(money,kq):
    if kq == 'win':
        text = font.render(str(money), True, white)
        gameDisplay.blit(text,(400,300))
    elif kq == 'lose':
        text = font.render('-'+str(money), True, white)
        gameDisplay.blit(text,(400,300))
    
def top(x,y,z,character):
    if character == 2:
        top1horse(x)
        top2horse(y)
        top3horse(z)
    elif character == 5:
        top1dragon(x)
        top2dragon(y)
        top3dragon(z)
    elif character == 1:
        top1slime(x)
        top2slime(y)
        top3slime(z)
    elif character == 3:
        top1bird(x)
        top2bird(y)
        top3bird(z)
    elif character == 4:
        top1man(x)
        top2man(y)
        top3man(z)
    pygame.display.update()


#hàm chèn ngựa 
def top1horse(horse): #biến x kiểu int là số thứ tự của con ngựa đứng nhất
    if (horse == 1):
        gameDisplay.blit(horse1,(378,155))
    if (horse == 2):
        gameDisplay.blit(horse2,(378,155))
    if (horse == 3):
        gameDisplay.blit(horse3,(378,155))
    if (horse == 4):
        gameDisplay.blit(horse4,(378,155))
    if (horse == 5):
        gameDisplay.blit(horse5,(378,155))
    if (horse == 6):
        gameDisplay.blit(horse6,(378,155))
    if (horse == 7):
        gameDisplay.blit(horse7,(378,155))
    if (horse == 8):
        gameDisplay.blit(horse8,(378,155))
    if (horse == 9):
        gameDisplay.blit(horse9,(378,155))
    if (horse == 10):
        gameDisplay.blit(horse10,(378,155))
def top2horse(horse): #biến y kiểu int là số thứ tự của con ngựa đứng hai
    if (horse == 1):
        gameDisplay.blit(horse1,(218,278))
    if (horse == 2):
        gameDisplay.blit(horse2,(218,278))
    if (horse == 3):
        gameDisplay.blit(horse3,(218,278))
    if (horse == 4):
        gameDisplay.blit(horse4,(218,278))
    if (horse == 5):
        gameDisplay.blit(horse5,(218,278))
    if (horse == 6):
        gameDisplay.blit(horse6,(218,278))
    if (horse == 7):
        gameDisplay.blit(horse7,(218,278))
    if (horse == 8):
        gameDisplay.blit(horse8,(218,278))
    if (horse == 9):
        gameDisplay.blit(horse9,(218,278))
    if (horse == 10):
        gameDisplay.blit(horse10,(218,278))
def top3horse(horse): #biến z kiểu int là số thứ tự của con ngựa đứng ba
    if (horse == 1):
        gameDisplay.blit(horse1,(534,356))
    if (horse == 2):
        gameDisplay.blit(horse2,(534,356))
    if (horse == 3):
        gameDisplay.blit(horse3,(534,356))
    if (horse == 4):
        gameDisplay.blit(horse4,(534,356))
    if (horse == 5):
        gameDisplay.blit(horse5,(534,356))
    if (horse == 6):
        gameDisplay.blit(horse6,(534,356))
    if (horse == 7):
        gameDisplay.blit(horse7,(534,356))
    if (horse == 8):
        gameDisplay.blit(horse8,(534,356))
    if (horse == 9):
        gameDisplay.blit(horse9,(534,356))
    if (horse == 10):
        gameDisplay.blit(horse10,(534,356))

#hàm chèn dragon
def top1dragon(horse): #biến x kiểu int là số thứ tự của con ngựa đứng nhất
    if (horse == 1):
        gameDisplay.blit(dragon1,(378,145))
    if (horse == 2):
        gameDisplay.blit(dragon2,(378,145))
    if (horse == 3):
        gameDisplay.blit(dragon3,(378,145))
    if (horse == 4):
        gameDisplay.blit(dragon4,(378,145))
    if (horse == 5):
        gameDisplay.blit(dragon5,(378,145))
    if (horse == 6):
        gameDisplay.blit(dragon6,(378,145))
    if (horse == 7):
        gameDisplay.blit(dragon7,(378,145))
    if (horse == 8):
        gameDisplay.blit(dragon8,(378,145))
    if (horse == 9):
        gameDisplay.blit(dragon9,(378,145))
    if (horse == 10):
        gameDisplay.blit(dragon10,(378,145))
def top2dragon(horse): #biến y kiểu int là số thứ tự của con ngựa đứng hai
    if (horse == 1):
        gameDisplay.blit(dragon1,(218,268))
    if (horse == 2):
        gameDisplay.blit(dragon2,(218,268))
    if (horse == 3):
        gameDisplay.blit(dragon3,(218,268))
    if (horse == 4):
        gameDisplay.blit(dragon4,(218,268))
    if (horse == 5):
        gameDisplay.blit(dragon5,(218,268))
    if (horse == 6):
        gameDisplay.blit(dragon6,(218,268))
    if (horse == 7):
        gameDisplay.blit(dragon7,(218,268))
    if (horse == 8):
        gameDisplay.blit(dragon8,(218,268))
    if (horse == 9):
        gameDisplay.blit(dragon9,(218,268))
    if (horse == 10):
        gameDisplay.blit(dragon10,(218,268))
def top3dragon(horse): #biến z kiểu int là số thứ tự của con ngựa đứng ba
    if (horse == 1):
        gameDisplay.blit(dragon1,(534,346))
    if (horse == 2):
        gameDisplay.blit(dragon2,(534,346))
    if (horse == 3):
        gameDisplay.blit(dragon3,(534,346))
    if (horse == 4):
        gameDisplay.blit(dragon4,(534,346))
    if (horse == 5):
        gameDisplay.blit(dragon5,(534,346))
    if (horse == 6):
        gameDisplay.blit(dragon6,(534,346))
    if (horse == 7):
        gameDisplay.blit(dragon7,(534,346))
    if (horse == 8):
        gameDisplay.blit(dragon8,(534,346))
    if (horse == 9):
        gameDisplay.blit(dragon9,(534,346))
    if (horse == 10):
        gameDisplay.blit(dragon10,(534,346))

#hàm chèn slime
def top1slime(horse): #biến x kiểu int là số thứ tự của con ngựa đứng nhất
    if (horse == 1):
        gameDisplay.blit(slime1,(378,145))
    if (horse == 2):
        gameDisplay.blit(slime2,(378,145))
    if (horse == 3):
        gameDisplay.blit(slime3,(378,145))
    if (horse == 4):
        gameDisplay.blit(slime4,(378,145))
    if (horse == 5):
        gameDisplay.blit(slime5,(378,145))
    if (horse == 6):
        gameDisplay.blit(slime6,(378,145))
    if (horse == 7):
        gameDisplay.blit(slime7,(378,145))
    if (horse == 8):
        gameDisplay.blit(slime8,(378,145))
    if (horse == 9):
        gameDisplay.blit(slime9,(378,145))
    if (horse == 10):
        gameDisplay.blit(slime10,(378,145))
def top2slime(horse): #biến y kiểu int là số thứ tự của con ngựa đứng hai
    if (horse == 1):
        gameDisplay.blit(slime1,(218,268))
    if (horse == 2):
        gameDisplay.blit(slime2,(218,268))
    if (horse == 3):
        gameDisplay.blit(slime3,(218,268))
    if (horse == 4):
        gameDisplay.blit(slime4,(218,268))
    if (horse == 5):
        gameDisplay.blit(slime5,(218,268))
    if (horse == 6):
        gameDisplay.blit(slime6,(218,268))
    if (horse == 7):
        gameDisplay.blit(slime7,(218,268))
    if (horse == 8):
        gameDisplay.blit(slime8,(218,268))
    if (horse == 9):
        gameDisplay.blit(slime9,(218,268))
    if (horse == 10):
        gameDisplay.blit(slime10,(218,268))
def top3slime(horse): #biến z kiểu int là số thứ tự của con ngựa đứng ba
    if (horse == 1):
        gameDisplay.blit(slime1,(534,346))
    if (horse == 2):
        gameDisplay.blit(slime2,(534,346))
    if (horse == 3):
        gameDisplay.blit(slime3,(534,346))
    if (horse == 4):
        gameDisplay.blit(slime4,(534,346))
    if (horse == 5):
        gameDisplay.blit(slime5,(534,346))
    if (horse == 6):
        gameDisplay.blit(slime6,(534,346))
    if (horse == 7):
        gameDisplay.blit(slime7,(534,346))
    if (horse == 8):
        gameDisplay.blit(slime8,(534,346))
    if (horse == 9):
        gameDisplay.blit(slime9,(534,346))
    if (horse == 10):
        gameDisplay.blit(slime10,(534,346))

#hàm chèn bird
def top1bird(horse): #biến x kiểu int là số thứ tự của con ngựa đứng nhất
    if (horse == 1):
        gameDisplay.blit(bird1,(370,145))
    if (horse == 2):
        gameDisplay.blit(bird2,(370,145))
    if (horse == 3):
        gameDisplay.blit(bird3,(370,145))
    if (horse == 4):
        gameDisplay.blit(bird4,(370,145))
    if (horse == 5):
        gameDisplay.blit(bird5,(370,145))
    if (horse == 6):
        gameDisplay.blit(bird6,(370,145))
    if (horse == 7):
        gameDisplay.blit(bird7,(370,145))
    if (horse == 8):
        gameDisplay.blit(bird8,(370,145))
    if (horse == 9):
        gameDisplay.blit(bird9,(370,145))
    if (horse == 10):
        gameDisplay.blit(bird10,(370,155))
def top2bird(horse): #biến y kiểu int là số thứ tự của con ngựa đứng hai
    if (horse == 1):
        gameDisplay.blit(bird1,(210,268))
    if (horse == 2):
        gameDisplay.blit(bird2,(210,268))
    if (horse == 3):
        gameDisplay.blit(bird3,(210,268))
    if (horse == 4):
        gameDisplay.blit(bird4,(210,268))
    if (horse == 5):
        gameDisplay.blit(bird5,(210,268))
    if (horse == 6):
        gameDisplay.blit(bird6,(210,268))
    if (horse == 7):
        gameDisplay.blit(bird7,(210,268))
    if (horse == 8):
        gameDisplay.blit(bird8,(210,268))
    if (horse == 9):
        gameDisplay.blit(bird9,(210,268))
    if (horse == 10):
        gameDisplay.blit(bird10,(2180,268))
def top3bird(horse): #biến z kiểu int là số thứ tự của con ngựa đứng ba
    if (horse == 1):
        gameDisplay.blit(bird1,(527,346))
    if (horse == 2):
        gameDisplay.blit(bird2,(527,346))
    if (horse == 3):
        gameDisplay.blit(bird3,(527,346))
    if (horse == 4):
        gameDisplay.blit(bird4,(527,346))
    if (horse == 5):
        gameDisplay.blit(bird5,(527,346))
    if (horse == 6):
        gameDisplay.blit(bird6,(527,346))
    if (horse == 7):
        gameDisplay.blit(bird7,(527,346))
    if (horse == 8):
        gameDisplay.blit(bird8,(527,346))
    if (horse == 9):
        gameDisplay.blit(bird9,(527,346))
    if (horse == 10):
        gameDisplay.blit(bird10,(527,346))
#hàm chèn man
def top1man(horse): #biến x kiểu int là số thứ tự của con ngựa đứng nhất
    if (horse == 1):
        gameDisplay.blit(man1,(378,135))
    if (horse == 2):
        gameDisplay.blit(man2,(378,135))
    if (horse == 3):
        gameDisplay.blit(man3,(378,135))
    if (horse == 4):
        gameDisplay.blit(man4,(378,135))
    if (horse == 5):
        gameDisplay.blit(man5,(378,135))
def top2man(horse): #biến y kiểu int là số thứ tự của con ngựa đứng hai
    if (horse == 1):
        gameDisplay.blit(man1,(218,258))
    if (horse == 2):
        gameDisplay.blit(man2,(218,258))
    if (horse == 3):
        gameDisplay.blit(man3,(218,258))
    if (horse == 4):
        gameDisplay.blit(man4,(218,258))
    if (horse == 5):
        gameDisplay.blit(man5,(218,258))
def top3man(horse): #biến z kiểu int là số thứ tự của con ngựa đứng ba
    if (horse == 1):
        gameDisplay.blit(man1,(534,336))
    if (horse == 2):
        gameDisplay.blit(man2,(534,336))
    if (horse == 3):
        gameDisplay.blit(man3,(534,336))
    if (horse == 4):
        gameDisplay.blit(man4,(534,336))
    if (horse == 5):
        gameDisplay.blit(man5,(534,336))
def draw_quit_continue():
    gameDisplay.blit(Quit,(100,450))
    gameDisplay.blit(Continue,(500,450))
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
                if mousex >= 100 and mousex <= 190 and mousey>=450 and mousey<=495:
                    gameDisplay.blit(Quit2,(100,450))
                elif mousex >= 500 and mousex <=675 and mousey>=450 and mousey <= 495:
                    gameDisplay.blit(Continue2,(500,450))
                else:
                    gameDisplay.blit(Quit,(100,450))
                    gameDisplay.blit(Continue,(500,450))
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = pygame.mouse.get_pos()
                if mousex >= 100 and mousex <= 190 and mousey>=450 and mousey<=495:
                    return 0 #thoát ra ngoài cửa sổ menu
                elif mousex >= 500 and mousex <=675 and mousey>=450 and mousey <= 495:
                    return 1 #tiếp tục đặt cược
        pygame.display.update()
def drawbxh(x,y,z,kq,bet,money,money1,character):
    # x,y,z lần lượt là thứ tự của 3 con ngựa
    #kq là 'win' hay 'lose'
    #bet là số tiền cược
    #money là số tiền nhận được
    #money1 là số sau khi kết thúc trò chơi
    #character là loại nhân vật
    gameDisplay.blit(bxh,(90,80))
    top(x,y,z,character)
    sleep(3)
    if kq == 'win':
        gameDisplay.blit(youwin,(90,80))
        draw_your_bet(bet)
        draw_money_received(money,kq)
        draw_your_money(money1)
        return draw_quit_continue()
    elif kq == 'lose':
        gameDisplay.blit(youlose,(90,80))
        draw_your_bet(bet)
        draw_money_received(money,kq)
        draw_your_money(money1)
        return draw_quit_continue()
clock.tick(FPS)
pygame.display.update()