from time import sleep
import pygame, sys, random, os
from pygame.locals import *


#Tạo môi trường:
pygame.init() 
FPS = 60
display_width = 800 #Dài
display_height = 600 #Rộng
Revealspeed = 8 #speed biến mất và xuất hiện khi ta bấm vào 1 ngôi sao
Gapsize = 140 #khoảng cách giữa 2 ngôi sao theo chiều dài
gapsize = 120 #khoảng cách giữa 2 ngôi sao theo chiều rộng

#Khai báo các loại màu (R,G,B) color:
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
pygame.display.set_caption('Lucky Star')
clock = pygame.time.Clock()

#Chèn hình trò chơi:
font = pygame.font.SysFont("comicsansms", 40)
Font = pygame.font.SysFont("freesansbold.ttf", 250)
point2 = Font.render('200', True, red)
point3 = Font.render('300', True, red)

#gán biến starImg là hình ngôi sao
starImg = pygame.image.load('star2.png')
boomImg = pygame.image.load('boom.png')
themImg = pygame.image.load('them.png').convert()

#Hàm chèn hình starImg vào màn hình game tại tọa độ (x, y)
a = 180
b = 530
def drawcircle(x,y):
    global circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9, circle10, circle11, circle12, circle13, circle14, circle15, circle16
    circle13 = pygame.draw.circle(gameDisplay, WHITE, (a, b), 50, 0)
    circle14 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize, b), 50, 0)
    circle15 = pygame.draw.circle(gameDisplay, WHITE, (a + 2*Gapsize, b), 50, 0)
    circle16 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize*3, b), 50, 0)
    circle9 = pygame.draw.circle(gameDisplay, WHITE, (a, b - gapsize), 50, 0)
    circle10 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize, b - gapsize), 50, 0)
    circle11 = pygame.draw.circle(gameDisplay, WHITE, (a + 2*Gapsize, b - gapsize), 50, 0)
    circle12 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize*3, b - gapsize), 50, 0)
    circle5 = pygame.draw.circle(gameDisplay, WHITE, (a, b - gapsize*2), 50, 0)
    circle6 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize, b - gapsize*2), 50, 0)
    circle7 = pygame.draw.circle(gameDisplay, WHITE, (a + 2*Gapsize, b - gapsize*2), 50, 0)
    circle8 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize*3, b - gapsize*2), 50, 0)
    circle1 = pygame.draw.circle(gameDisplay, WHITE, (a, b - gapsize*3), 50, 0)
    circle2 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize, b - gapsize*3), 50, 0)
    circle3 = pygame.draw.circle(gameDisplay, WHITE, (a + 2*Gapsize, b - gapsize*3), 50, 0)
    circle4 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize*3, b - gapsize*3), 50, 0)

#hàm xóa toàn bộ circle
def erase_circle():
    circle13 = pygame.draw.circle(gameDisplay, WHITE, (a, b), 50, 0)
    circle14 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize, b), 50, 0)
    circle15 = pygame.draw.circle(gameDisplay, WHITE, (a + 2*Gapsize, b), 50, 0)
    circle16 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize*3, b), 50, 0)
    circle9 = pygame.draw.circle(gameDisplay, WHITE, (a, b - gapsize), 50, 0)
    circle10 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize, b - gapsize), 50, 0)
    circle11 = pygame.draw.circle(gameDisplay, WHITE, (a + 2*Gapsize, b - gapsize), 50, 0)
    circle12 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize*3, b - gapsize), 50, 0)
    circle5 = pygame.draw.circle(gameDisplay, WHITE, (a, b - gapsize*2), 50, 0)
    circle6 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize, b - gapsize*2), 50, 0)
    circle7 = pygame.draw.circle(gameDisplay, WHITE, (a + 2*Gapsize, b - gapsize*2), 50, 0)
    circle8 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize*3, b - gapsize*2), 50, 0)
    circle1 = pygame.draw.circle(gameDisplay, WHITE, (a, b - gapsize*3), 50, 0)
    circle2 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize, b - gapsize*3), 50, 0)
    circle3 = pygame.draw.circle(gameDisplay, WHITE, (a + 2*Gapsize, b - gapsize*3), 50, 0)
    circle4 = pygame.draw.circle(gameDisplay, WHITE, (a + Gapsize*3, b - gapsize*3), 50, 0)

#hàm đổi màu khi bấm vào 1 circle
def doimau(click):
    if click == circle1:
        pygame.draw.circle(gameDisplay, red, (a, b - gapsize*3), 50, 0)
    elif click == circle2:
        pygame.draw.circle(gameDisplay, red, (a + Gapsize, b - gapsize*3), 50, 0)
    elif click == circle3:
        pygame.draw.circle(gameDisplay, red, (a + 2*Gapsize, b - gapsize*3), 50, 0)
    elif click == circle4:
        pygame.draw.circle(gameDisplay, red, (a + Gapsize*3, b - gapsize*3), 50, 0)
    elif click == circle5:
        pygame.draw.circle(gameDisplay, red, (a, b - gapsize*2), 50, 0)
    elif click == circle6:
        pygame.draw.circle(gameDisplay, red, (a + Gapsize, b - gapsize*2), 50, 0)
    elif click == circle7:
        pygame.draw.circle(gameDisplay, red, (a + 2*Gapsize, b - gapsize*2), 50, 0)
    elif click == circle8:
        pygame.draw.circle(gameDisplay, red, (a + Gapsize*3, b - gapsize*2), 50, 0)
    elif click == circle9:
        pygame.draw.circle(gameDisplay, red, (a, b - gapsize), 50, 0)
    elif click == circle10:
        pygame.draw.circle(gameDisplay, red, (a + Gapsize, b - gapsize), 50, 0)
    elif click == circle11:
        pygame.draw.circle(gameDisplay, red, (a + 2*Gapsize, b - gapsize), 50, 0)
    elif click == circle12:
        pygame.draw.circle(gameDisplay, red, (a + Gapsize*3, b - gapsize), 50, 0)
    elif click == circle13:
        pygame.draw.circle(gameDisplay, red, (a, b), 50, 0)
    elif click == circle14:
        pygame.draw.circle(gameDisplay, red, (a + Gapsize, b), 50, 0)
    elif click == circle15:
        pygame.draw.circle(gameDisplay, red, (a + 2*Gapsize, b), 50, 0)
    elif click == circle16:
        pygame.draw.circle(gameDisplay, red, (a + Gapsize*3, b), 50, 0)

#Hàm trả về khi bấm vào 1 circle
def getButtonClicked(x, y):
    if circle1.collidepoint( (x, y) ):
        return circle1
    elif circle2.collidepoint( (x, y) ):
        return circle2
    elif circle3.collidepoint( (x, y) ):
        return circle3
    elif circle4.collidepoint( (x, y) ):
        return circle4
    elif circle5.collidepoint( (x, y) ):
        return circle5
    elif circle6.collidepoint( (x, y) ):
        return circle6
    elif circle7.collidepoint( (x, y) ):
        return circle7
    elif circle8.collidepoint( (x, y) ):
        return circle8
    elif circle9.collidepoint( (x, y) ):
        return circle9
    elif circle10.collidepoint( (x, y) ):
        return circle10
    elif circle11.collidepoint( (x, y) ):
        return circle11
    elif circle12.collidepoint( (x, y) ):
        return circle12
    elif circle13.collidepoint( (x, y) ):
        return circle13
    elif circle14.collidepoint( (x, y) ):
        return circle14
    elif circle15.collidepoint( (x, y) ):
        return circle15
    elif circle16.collidepoint( (x, y) ):
        return circle16
    return None



#hàm kiểm tra khi bấm
def kiemtra(circle):
    global DIEM #Biến trả về giá trị cuối cùng
    if circle != None:
        erase_circle()
        pygame.display.update()
        doimau(circle)
        pygame.display.update()
        sleep(0.1)
        erase_circle()
        pygame.display.update()
        RANDOM = random.randint(0,5)
        if RANDOM == 0:
            DIEM = 1000
            gameDisplay.blit(starImg, (220, 180))
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("VICTORY.mp3")
            pygame.mixer.music.play()
            sleep(3)
            return DIEM
        elif RANDOM == 1:
            DIEM = 0
            gameDisplay.blit(boomImg, (200, 200))
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("MarioGameOverNhacChuong-VA-4731955.mp3")
            pygame.mixer.music.play()
            sleep(3)
            return DIEM
        elif RANDOM == 2:
            DIEM = 200
            gameDisplay.blit(point2, (250, 230))
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("DING.mp3")
            pygame.mixer.music.play()
            sleep(3)
            return DIEM
        elif RANDOM == 3:
            DIEM = 300
            gameDisplay.blit(point3, (250, 230))
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("DING.mp3")
            pygame.mixer.music.play()
            sleep(3)
            return DIEM

            
            
        
        
#hàm thoát trò chơi                  
def terminate():
    pygame.quit()
    sys.exit()
    crashed = True




def minimain():
    #chèn nhạc nền:
    pygame.mixer.music.load("rainbow.mp3")
    pygame.mixer.music.play(-1)
    global  DIEM
    crashed = False
    gameDisplay.blit(themImg,(0,0))
    drawcircle(a, b)
    pygame.display.update()
    clickedButton = None
   
    while not crashed:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)
                DIEM=kiemtra(clickedButton)
                if DIEM !=None:
                    return DIEM
        pygame.display.update()
        clock.tick(FPS)


