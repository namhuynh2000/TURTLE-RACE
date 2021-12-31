#co dinh toa do cua window
x = 50
y = 50
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
from pygame_functions import*
from random import*
from sys import exit
import pygame_textinput
from pygame.locals import *
import pygame, sys, os.path
from time import sleep
from BXH import *
from MINIGAME import *
from MAP import *
from CHARACTER import *
from NUMBER import *
from MENU2 import *
from Instruction import *
from select_bet import*
pygame.init()
pygame.font.init()

flag =0
flag2=0
cornerpoint=[0,0]
bigmapwidth = 2000
bigmapheight = 1200
scrollstepx = 15
scrollstepy = 15
width=800
height=600
money=0
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption("Horse Race")
fpsclock = pygame.time.Clock()
SpeedUpCharm = pygame.image.load('bua_tangtoc.png')
StunCharm=pygame.image.load('bua_dung.png')
ResetCharm=pygame.image.load('bua_vachxuatphat.png')
TurnBackCharm=pygame.image.load('bua_lui.png')
SlowDownCharm = pygame.image.load('bua_giamtoc.png')
DizzyDuck=[pygame.image.load('dizzy1.png'),pygame.image.load('dizzy2.png'),
           pygame.image.load('dizzy3.png'),pygame.image.load('dizzy4.png')]
bigmap=None
FPS=15
event=None
number=None
Ani_Count=0
SPEED=10
Hocky_Result=[]
Character_Movement=[]
Boost = []
NumberOfCharm = 6 #so bua moi duong dua
Is_flip = [0] * 10
Stun_Time = [0] * 10
Turnback_Time = [0] * 10
Is_Stun = [0] * 10
Is_Turnback = [0] * 10
Is_Slow_Fast=[0]*10
Slow_Fast_Time=[0]*10
dizzy=0
bool = 0
# Khai báo các loại màu (R,G,B) color:
blue = (0, 0, 255)
YELLOW = (235, 208, 33)
WHITE = (255, 253, 230)
pink = (255, 23, 255)
PURPLE = pygame.Color('lightskyblue3')
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BROWN = (85, 65, 0)
GREEN=(0,255,0)
#bien ham login:
tem=0
passwordstr1 = ""
usernamestr1 = ""
inputbool1 = 1
dem=0
#bein ham logup:
usernamestr = ""
passwordstr = ""
inputbool = 1
count=1
background_image2= pygame.image.load("login_ima.png")
background_image1 = pygame.image.load("sign_up_ima.png")
background_position = [0, 0]
usernameinput = pygame_textinput.TextInput()
passwordinput = pygame_textinput.TextInput()
mousex = 0
mousey = 0
SIGNUPMONEY = "100"  # khoi tao tien ban dau
myfont = pygame.font.SysFont('Comic Sans MS', 30)
myfont1 = pygame.font.SysFont('Comic Sans MS', 40)
getmoney=0

# Chèn hình trò chơi:
font = pygame.font.SysFont("comicsansms", 40)
Font = pygame.font.SysFont("freesansbold.ttf", 250)

ListCharms=[]
ListCharacters=[]
def collidewithmouse(rect2):
    global mousex
    global mousey
    return rect2.collidepoint(mousex, mousey)
def check_user():
    global count
    global bool
    text = myfont1.render('ERROR!!!username is existing', False, RED)
    check_file = open('information.txt', 'r')  # tao 1 file moi de chua thong tin
    for rline in check_file:
        values = rline.split(",")
        #password = values[1]
        username = values[0]
        if username==usernamestr:
            count+=1
    #print(count)
    if count!=1:
        DISPLAYSURF.blit(text, (70, 400))
    else:
        bool=2
    check_file.close()
    count=1
def logup_Process(event, events):
    global bool
    global mousex
    global mousey
    global inputbool
    global usernamestr
    global passwordstr
    global SIGNUPMONEY
    global data_file
    global username
    global password
    global getmoney
    global count
    DISPLAYSURF.blit(background_image1, background_position)  # to nen mau trang cho game

    (mousex, mousey) = pygame.mouse.get_pos()
    text = myfont1.render('ERROR!!!username is existing', False, RED)
    #entrytext = myfont.render("please input text in entry!    ", False, (0, 0, 0))
    #menutext = myfont1.render("PLEASE LOGUP!    ", False, (0, 0, 0))  # tieu de logup
    usernametext = myfont.render("new username:    ", False, (0, 0, 0))
    passwordtext = myfont.render("new password:    ", False, (0, 0, 0))
    oktext = myfont.render("OK!", False, (0, 0, 0))  # oktext tren nut ok

    rect1 = pygame.draw.rect(DISPLAYSURF, (PURPLE), (300, 168, 300, 30))#o de ghi ten
    rect8 = pygame.draw.rect(DISPLAYSURF, WHITE, (302, 170, 296, 26))

    rect2 = pygame.draw.rect(DISPLAYSURF, PURPLE, (300, 238, 300, 30))#oo de ghi pass
    rect9 = pygame.draw.rect(DISPLAYSURF, WHITE, (302, 240, 296, 26))

    rect3 = pygame.draw.rect(DISPLAYSURF, PURPLE, (300, 300, 80, 40))#o button ok
    if collidewithmouse(rect3) == 1:
        rect3 = pygame.draw.rect(DISPLAYSURF, RED, (300, 300, 80, 40))
    if collidewithmouse(rect1) == 1 and event.type == MOUSEBUTTONDOWN:
        inputbool = 1
    if collidewithmouse(rect2) == 1 and event.type == MOUSEBUTTONDOWN:
        inputbool = 0
    if inputbool == 1:
        usernameinput.update(events)
    elif inputbool == 0:
        passwordinput.update(events)
    DISPLAYSURF.blit(usernameinput.get_surface(), (300, 170))
    DISPLAYSURF.blit(passwordinput.get_surface(), (300, 240))
    DISPLAYSURF.blit(usernametext, (100, 160))
    DISPLAYSURF.blit(passwordtext, (100, 230))
    DISPLAYSURF.blit(oktext, (315, 302))
    #DISPLAYSURF.blit(menutext, (150, 30))
    if collidewithmouse(rect3) == 1 and event.type == MOUSEBUTTONDOWN:
        passwordstr = passwordinput.get_text()
        usernamestr = usernameinput.get_text()
        check_user()
        if bool==2:

            write_file=open('information.txt','a+')#tao 1 file moi de chua thong tin

            write_file.write(usernamestr + ",")
            write_file.write(passwordstr + ",")  # ghi mat khau vao file
            write_file.write(SIGNUPMONEY) # khoi tao tien ban dau(trong day t de money=10
            write_file.write("\n")
            write_file.close()
            bool=1
def login_Process(event, events):
    kq=0
    global tem
    global bool
    global mousex
    global mousey
    global inputbool1
    global usernamestr1
    global passwordstr1
    global data_file
    global username
    global password
    global getmoney
    global dem
    DISPLAYSURF.blit(background_image2, background_position)  # to nen mau trang cho game
    # set su kien exit gamelong11
    (mousex, mousey) = pygame.mouse.get_pos()
    ER2 = myfont1.render('ERROR!!!username is not existing', False, RED)
    #menutext = myfont1.render("PLEASE LOGIN!    ", False, (0, 0, 0))
    ER1 = myfont1.render("password is incorect,please login again!    ", False, RED)
    start = myfont1.render("start game!    ", False, GREEN)
    usernametext = myfont.render("    username:    ", False, (0, 0, 0))
    passwordtext = myfont.render("    password:    ", False, (0, 0, 0))
    oktext = myfont.render("OK!", False, (0, 0, 0))
    rect5 = pygame.draw.rect(DISPLAYSURF, (PURPLE), (300, 168, 300, 30))#o username trong ben login
    rect9 = pygame.draw.rect(DISPLAYSURF, WHITE, (302, 170, 296, 26))

    rect6 = pygame.draw.rect(DISPLAYSURF, PURPLE, (300, 238, 300, 30))#o password trong ben login
    rect9 = pygame.draw.rect(DISPLAYSURF, WHITE, (302, 240, 296, 26))

    rect4 = pygame.draw.rect(DISPLAYSURF, PURPLE, (300, 340, 80, 40))# ok button ben login
    if collidewithmouse(rect4) == 1:
        rect4 = pygame.draw.rect(DISPLAYSURF, RED, (300, 340, 80, 40))
    if collidewithmouse(rect5) == 1 and event.type == MOUSEBUTTONDOWN:
        inputbool1 = 1
    if collidewithmouse(rect6) == 1 and event.type == MOUSEBUTTONDOWN:
        inputbool1 = 0
    if inputbool1 == 1:
        usernameinput.update(events)
    elif inputbool1 == 0:
        passwordinput.update(events)
    DISPLAYSURF.blit(usernameinput.get_surface(), (300, 170))
    DISPLAYSURF.blit(passwordinput.get_surface(), (300, 240))
    DISPLAYSURF.blit(usernametext, (100, 160))
    DISPLAYSURF.blit(passwordtext, (100, 230))
    DISPLAYSURF.blit(oktext, (315, 342))
    #DISPLAYSURF.blit(menutext, (150, 30))
    if collidewithmouse(rect4) == 1 and event.type == MOUSEBUTTONDOWN:
        passwordstr1 = passwordinput.get_text()
        usernamestr1 = usernameinput.get_text()
        read_file=open('information.txt','r')#doc  file  chua thong tin


        for aline in read_file:
            values = aline.split(",")
            username = values[0]
            password = values[1]
            getmoney = int(values[2])

            if (username==usernamestr1):
                dem += 1
                if password==passwordstr1:
                   tem=1
                   kq=1
                   break

                else:
                    DISPLAYSURF.blit(ER1, (50, 400))
              #  else:
              #      tem=2
        if dem==0:
             DISPLAYSURF.blit(ER2, (70, 400))
            #else:
             #   tem=3
                #print('ten:  ', username, 'mk: ', password, 'tien: ', getmoney)
        if tem==1:
            DISPLAYSURF.blit(start, (250, 400))
            return
            read_file.close()

            dem = 0  # reset lai bien dem
            tem = 0  # reset lai bien tem
def Login_Logup(qqq):
    global bool
    bool=qqq
    while True:
        #DISPLAYSURF.blit(background_image, background_position)
        # set su kien exit game
        events = pygame.event.get()
        for event in events:
            if (event.type == QUIT):
                pygame.quit()
                sys.exit()
            if bool == 0:
                logup_Process(event, events)
            if bool == 1:
                login_Process(event, events)
                if tem==1:
                    return getmoney
            pygame.display.update()
            fpsclock.tick(FPS)
def Update_Info():
    global money
    global usernamestr1
    global passwordstr1
    accountlist = []
    with open('information.txt', 'r') as fileread:
        for line in fileread:
            values = line.split(",")
            if values[0] == usernamestr1 and values[1] == passwordstr1:
                values[2] = str(money)
                line = ','.join(values)
            line = line + '\n'
            accountlist.append(line)
    filewrite = open('information.txt', 'w')
    for index in range(0, len(accountlist)):
        filewrite.write(accountlist[index])
    filewrite.close()

#Load ảnh nhân vật
def load_image(map1,C_CHARACTER,number):
    global ListCharacters
    global ListCharms
    global bigmap
    CharacterName=['slime','horse','bird','nguoi','dinosour']
    mapname=['spring','summer','fall','winter']
    bigmap=pygame.image.load(mapname[map1-1]+'.png')
    #Load anh nhan vat
    for i in range(0,number):
        temp=[1]*7
        for k in range(1,8):
            temp[k-1]= pygame.image.load(str(i)+CharacterName[C_CHARACTER-1]+' ('+str(k)+').png')
        Character_Movement.append(temp)
    ListCharacters= [0]*len(Character_Movement)
    ListCharms= [0]*len(Character_Movement)*NumberOfCharm
#Tạo struct cho nhân vật
class Character:
    def __init__(self,Image, x, y):
        self.Image=Image
        self.x=x
        self.y=y
#Khởi tạo nhân vật
def Character_Generate():
    global Boost
    global Is_flip
    Is_flip = [0] * len(Character_Movement)
    Boost = [0] * len(Character_Movement)
    for index in range(0, len(Character_Movement)):
        ListCharacters[index]=(Character(Character_Movement[index][0], x=20, y=220 + 80 * index))
#Vẽ nhân vật chạy
def Start_Race(number):
    global Ani_Count
    global SPEED
    global Hocky_Result
    pos=[0]*number
    Ani_Count += 1
    for index in range(0, len(ListCharacters)):
        a=randint(3,6)
        pos[index]=ListCharacters[index].x
        if (ListCharacters[index].x>= 3000) and (index not in Hocky_Result):
            Hocky_Result.append(index)
        if(ListCharacters[index].x>=3000):
            ListCharacters[index].x=3000
        if number==5:
            if len(Hocky_Result)==number and pos[0]>3000 and pos[1]>3000 and pos[2]>3000 and pos[3]>3000 \
                    and pos[4]>3000 :
                return 1
        else:
            if len(Hocky_Result)==number and pos[0]>3000 and pos[1]>3000 and pos[2]>3000 and pos[3]>3000 \
                    and pos[4]>3000 and pos[5]>3000 and pos[6]>3000 and pos[7]>3000 and pos[8]>3000 \
                    and pos[9]>3000 :
                return 1
        ListCharacters[index].Image = Character_Movement[index][Ani_Count % 7]
        if Is_flip[index] == 0:
            DISPLAYSURF.blit(ListCharacters[index].Image,
                             (ListCharacters[index].x-2*cornerpoint[0],
                              ListCharacters[index].y-cornerpoint[1]))
        else:
            DISPLAYSURF.blit(pygame.transform.flip(ListCharacters[index].Image, True, False),
                             (ListCharacters[index].x-2*cornerpoint[0], ListCharacters[index].y-cornerpoint[1]))
        ListCharacters[index].x = ListCharacters[index].x + SPEED +a+Boost[index]  # Chua cong bua
#tạo struct cho bùa
class Charm:
    def __init__(self, image, type, x, y):
        self.image=image
        self.type=type #type=1:tăng tốc, -type=2:giảm tốc,type=3:quay lại từ đầu, type=4:quay đầu trong 2 giây, type=5:choáng
        self.x= x
        self.y= y
#Kiểm Tra xem nhân vật có va chạm vào bùa hay không
def Is_Collision(character, obj):
    Rect1=character.Image.get_rect(topleft=(character.x,character.y))
    Rect2=obj.image.get_rect(topleft=(obj.x,obj.y))
    return Rect1.colliderect(Rect2)
#Khởi tạo bùa ngẫu nhiên
def Charms_Generate():
    RandomCharm=None
    global Is_Turnback
    global Is_Stun

    global NumberOfCharm
    global Character_Movement
    for CharmColumn in range(0, len(Character_Movement)):
        for CharmLine in range(0,NumberOfCharm):
            RandomCharm=randint(1,5)
            if RandomCharm==1:
                ListCharms[CharmLine +CharmColumn*NumberOfCharm]= (Charm(SpeedUpCharm,1,300*(CharmLine+1),220+80*CharmColumn))
            elif RandomCharm==2:
                ListCharms[CharmLine+ CharmColumn*NumberOfCharm]= (Charm(SlowDownCharm,2, 300 * (CharmLine + 1), 220 + 80 * CharmColumn))
            elif RandomCharm==3:
                ListCharms[CharmLine + CharmColumn * NumberOfCharm] = (Charm(ResetCharm, 3, 300 * (CharmLine + 1), 220 + 80 * CharmColumn))
            elif RandomCharm==4:
                ListCharms[CharmLine + CharmColumn * NumberOfCharm] = (Charm(TurnBackCharm, 4, 300 * (CharmLine + 1), 220 + 80 * CharmColumn))
            else:
                ListCharms[CharmLine + CharmColumn * NumberOfCharm] = (Charm(StunCharm, 5, 300 * (CharmLine + 1), 220 + 80 * CharmColumn))
#Vẽ bùa lên màn hình
def Blit_Charms():
    for index in range(0,len(ListCharms)):
        DISPLAYSURF.blit(ListCharms[index].image,
                         (ListCharms[index].x-2*cornerpoint[0],ListCharms[index].y-cornerpoint[1]))
#Xử lý khi nhân vật chạm bùa
def Process_Charms_Hit():
    global dizzy
    global Stun_Time
    global Turnback_Time
    global Is_flip
    global Is_Slow_Fast
    global Slow_Fast_Time
    for index1 in range(0,len(ListCharacters)):
        for index2 in range(0,len(ListCharms)):
            if Is_Collision(ListCharacters[index1],ListCharms[index2])==1:
                ListCharms[index2].x=5000
                ListCharms[index2].y=5000
                if ListCharms[index2].type==1:
                    Boost[index1]=10
                    Is_Slow_Fast[index1]=1
                elif ListCharms[index2].type==3:
                    ListCharacters[index1].x=20
                elif ListCharms[index2].type==2:
                    Boost[index1]=-10
                    Is_Slow_Fast[index1]=1
                elif ListCharms[index2].type==5 :
                    Is_Stun[index1]=1
                elif ListCharms[index2].type==4:
                    Is_Turnback[index1]=1
    for index in range(0,len(ListCharacters)):
        if Stun_Time[index]<5*FPS and Is_Stun[index]==1:
            DISPLAYSURF.blit(DizzyDuck[dizzy%4],(ListCharacters[index].x-2*cornerpoint[0],ListCharacters[index].y-5-cornerpoint[1]))
            dizzy+=1
            Boost[index]= -SPEED-3
            Stun_Time[index] += 1
        if Stun_Time[index]>=5*FPS:
            Boost[index]=0
            Is_Stun[index]=0
            Stun_Time[index]=0
        if Turnback_Time[index]<2*FPS and Is_Turnback[index]==1:
            Is_flip[index]=1
            Boost[index]=-SPEED-randint(5,15)
            Turnback_Time[index] += 1
        if Turnback_Time[index]>=2*FPS:
            Boost[index]=0
            Is_Turnback[index]=0
            Turnback_Time[index]=0
            Is_flip[index]=0
        if Slow_Fast_Time[index]<2*FPS and Is_Slow_Fast[index]==1:
            Slow_Fast_Time[index] += 1
        if Slow_Fast_Time[index]>=2*FPS:
            Boost[index]=0
            Is_Slow_Fast[index]=0
            Slow_Fast_Time[index]=0
def Race(map1,number,C_CHARACTER,money,moneybet,hocky):
    global Hocky_Result
    global bigmap
    dizzy=0
    cornerpoint[0] = 0
    cornerpoint[1] = 100 # Để camera chĩa vào khung đua.\
    Hocky_Result=[]
    load_image(map1,C_CHARACTER,number)
    #Tạo nhân vật và bùa
    Character_Generate()
    Charms_Generate()
    #Tạo subsurface cho camera chạy
    background = pygame.Surface((DISPLAYSURF.get_size()))
    backgroundrect = background.get_rect()
    background = bigmap.subsurface((cornerpoint[0],cornerpoint[1],width,height))
    # -----------------------------------
    background = background.convert_alpha()
    DISPLAYSURF.blit(background, (0, 0))
    while True:
        DISPLAYSURF.blit(background,(0,0))
        # -------- Biến dùng để di chuyển map ----------
        scrollx = 0
        scrolly = 0
        # --- Nhận tín hiệu từ bán phím để di chuyển camera ----
        if keyPressed("left"):
            scrollx -= scrollstepx
        if keyPressed("right"):
            scrollx += scrollstepx
        if keyPressed("up"):
            scrolly -= scrollstepy
        if keyPressed("down"):
            scrolly += scrollstepy
        # -------- Camera chỉ lia đến phần nhìn thấy của Bigmap ------
        cornerpoint[0] += scrollx
        cornerpoint[1] += scrolly
        # --------- Không cho người dùng lia camera khỏi Biamap -----
        if cornerpoint[0] < 0:
            cornerpoint[0] = 0
            scrollx = 0
        elif cornerpoint[0] > bigmapwidth - width:
            cornerpoint[0] = bigmapwidth - width
            scrollx = 0
        if cornerpoint[1] < 0:
            cornerpoint[1] = 0
            scrolly = 0
        elif cornerpoint[1] > bigmapheight - height:
            cornerpoint[1] = bigmapheight - height
            scrolly = 0
        if scrollx == 0 and scrolly == 0:
            pygame.display.flip()
        else:
            background = bigmap.subsurface((cornerpoint[0],
                                            cornerpoint[1],
                                            width,
                                            height))
            DISPLAYSURF.blit(background, (0, 0))
        #-------------Vẽ bùa---------------
        Blit_Charms()
        #Cho cuộc đua bắt đầu và lấy kết qua cuộc đua
        b=Start_Race(number)
        #Kiểm tra va chạm giữa nhân vật và bùa
        Process_Charms_Hit()
        pygame.display.update()
        fpsclock.tick(FPS)  # Tốc độ chuyển frame
        #Phần Xử lý đặt cược
        if b==1:
            if hocky == Hocky_Result[0]+1:
                if number == 5:
                    moneywin = moneybet * 3
                    money += moneywin
                    return money,Hocky_Result[0:2],'win',moneywin
                elif number == 10:
                    moneywin = moneybet * 7
                    money+=moneywin
                    return money,Hocky_Result[0:2],'win',moneywin
            else:
                moneylose = moneybet
                money-=moneybet
                return money,Hocky_Result[0:2],'lose',moneylose

def main():
    global money
    Is_Game = Menu()

    if Is_Game == 1:
        is_login=1
        money=Login_Logup(is_login)
        game()
    elif Is_Game == 2:
        is_login=0
        money=Login_Logup(is_login)
        game()
    elif Is_Game == 3:
        i = huongdan()
        if (i == 1):
            main()
def game():
    global money
    global flag
    global Character_Movement
    Character_Movement=[]
    flag =0
    map1 = choose_map()
    if map1== 1 or map1==2 or map1==3 or map1==4:
        number = choose_number()
    C_CHARACTER = choose_character(number)
    moneybet,hocky=select(number,C_CHARACTER,money)
    if hocky==0:
        game()
    money, Hocky_Result[0:2], kq, money_receive = Race(map1, number, C_CHARACTER, money,moneybet , hocky)
    bool = drawbxh(Hocky_Result[0]+1, Hocky_Result[1]+1, Hocky_Result[2]+1, kq, moneybet, money_receive, money, C_CHARACTER)
    Update_Info()
    if bool == 0:
        main()
    if bool == 1 and money!=0:
        game()
    if bool==1 and money==0 and flag==0:
        money=minimain()
        flag+=1
        if money==0:
            print('you lose')
        else:
            game()
    if money==0 and flag!=0:
        print('you lose')
main()
