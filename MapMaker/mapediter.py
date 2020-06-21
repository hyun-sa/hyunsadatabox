import pygame
import sys
import shutil
from tkinter import *
from tkinter.filedialog import *

#############################################################################################
# 해당 파일은 게임파일과 직접적인 관련이 없으며 맵제작을 더 쉽게 하기위해 만든 별도의 프로그램입니다.
# 이 파일(mapediter.py)의 CopyRight은
# 2019038011 윤석현
# 에게 있습니다.
#############################################################################################

from tkinter import messagebox

# CopyRight 2019038011 윤석현
def searchfile():
    global filename
    filename = askopenfilename(parent=window, filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")))


# 아래 코드는 다음과 같은 해상도에 맞춰 작성되었습니다. 이외의 해상도에서 정상적인 작동은 확인되지 않았습니다.
width, height = 1920, 1080  # 1920*1080 (윈도우 디스플레이 배율 설정에 따라 원활히 동작되지 않을 수 있습니다.)

Start_Screen = True
MoveToolbox = False

CheckCode = 9

MoveEndPoint = -6
MoveLeverOn = -14
MoveSubPortal = -15

Erase = 0

CreateBackBlock = 1
CreateBall = 2
CreateBlckhole = 3
CreateFakeWal = 4
CreateMagnetic = 5
CreateMoveWal = 6
CreateStar = 7
CreateThorn = 8
CreateWall = 9
CreateSpring = 10

CreateIcicle = 11
CreateLaser = 12
CreateBlinkBlock = 13
CreateLever = 14
CreatePortal = 15
CreateCannon = 16

# blocks = ['backblock', 'ball', 'blckhole', 'fakewal', 'magnetic', 'movewal', 'star', 'thorn', 'wall', 'spring', 'icicle'\
#     , 'laser', 'endpoint', 'blinkblock', 'lever', 'portal', 'cannon']
# default_blocks = ['default_backblock', 'default_ball', 'default_blckhole', 'default_fakewal', 'default_magnetic', 'default_movewal',\
#           'default_star', 'default_thorn', 'default_wall', 'default_spring', 'default_icicle'\
#     , 'default_laser', 'default_endpoint', 'default_blinkblock', 'default_lever', 'default_portal', 'default_cannon']

################################################################
# 아래에서 pixel_size(크기)를 지정할 수 있습니다.
# 디스플레이 해상도에 따라 변경시 올바르게 동작하지 않을 수 있습니다.
# 해당 해상도(1920*1080)에서는 최대공약수인 120의 약수만 사용할 것을 권고합니다.
# 아래는 수정할 수 있는 변수들 입니다.
# !!!!!!!!!!!!!맵의 경우 "확장자"를 꼭 포함하여 적어주세요!!!!!!!!!!!!!!!!!!!
pixel_size = 40
OpenFile = "testmap.txt"
SaveFile = "testmap.txt"
################################################################

display = []
movepos = []
try:
    f = open('game/data/maps/{0}'.format(OpenFile), 'r', encoding='UTF8')
except:
    window = Tk()
    window.title("배경이미지 선택")
    window.geometry("600x500")
    label1 = Label(window, text="선택된 파일 이름")
    label2 = Label(window, text="지정된 배경이미지가 없습니다.배경 이미지를 선택해 주세요!")
    label1.pack()
    label2.pack()

    filename = askopenfilename(parent=window, filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")))
    label2.configure(text=str(filename))
    background = PhotoImage(file=filename)
    label4 = Label(window, image=background)
    label4.pack()
    window.mainloop()
    direct = filename.split('/')
    shutil.copy(filename, 'game/image/mapeditimage/Backgrounds/{0}'.format(direct[-1]))
    filename = direct[-1]

    for i in range(width // pixel_size):
        temp = []
        for j in range(height // pixel_size):
            temp.append("0\n")
        display.append(temp)
else:
    size = f.readline().split(' ')
    width = int(size[0])
    height = int(size[1])
    pixel_size = int(size[2])
    filename = f.readline()
    filename = filename.replace("\n", "")
    if filename == "0":
        filename = "Background.png"
    for i in range(width//pixel_size):
        temp = []
        for j in range(height//pixel_size):
            line = f.readline()
            temp.append(line)
        display.append(temp)
    f.close()

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

Start_background = pygame.image.load("game/image/mapeditimage/Backgrounds/{0}".format(filename))
default_toolbox = pygame.image.load('game/image/mapeditimage/toolbox.png')
default_move = pygame.image.load('game/image/mapeditimage/move.png')
default_eraser = pygame.image.load('game/image/mapeditimage/eraser.png')
default_select = pygame.image.load('game/image/mapeditimage/select.png')
default_xmark = pygame.image.load('game/image/mapeditimage/xmark.png')

default_blackdot = pygame.image.load('game/image/mapeditimage/blackdot.png')

default_subportal = pygame.image.load('game/image/mapeditimage/subportal.png')
default_leverOnOff = pygame.image.load('game/image/mapeditimage/leverOFF.png')

default_backblock = pygame.image.load('game/image/mapeditimage/backblock.png')
default_ball = pygame.image.load('game/image/mapeditimage/ball.png')
default_blckhole = pygame.image.load('game/image/mapeditimage/blckhole.png')
default_fakewal = pygame.image.load('game/image/mapeditimage/fakewal.png')
default_magnetic = pygame.image.load('game/image/mapeditimage/magnetic.png')
default_movewal = pygame.image.load('game/image/mapeditimage/movewal.png')
default_star = pygame.image.load('game/image/mapeditimage/star.png')
default_thorn = pygame.image.load('game/image/mapeditimage/thorn.png')
default_wall = pygame.image.load('game/image/mapeditimage/wall.png')
default_spring = pygame.image.load('game/image/mapeditimage/spring.png')
default_icicle = pygame.image.load('game/image/mapeditimage/icicle.png')
default_laser = pygame.image.load('game/image/mapeditimage/laser.png')
default_endpoint = pygame.image.load('game/image/mapeditimage/endpoint.png')

default_blinkblock = pygame.image.load('game/image/mapeditimage/blinkblock.png')
default_lever = pygame.image.load('game/image/mapeditimage/lever.png')
default_portal = pygame.image.load('game/image/mapeditimage/portal.png')
default_cannon = pygame.image.load('game/image/mapeditimage/cannon.png')

class newicon():
    def __init__(self, x, y, blocktype, width, height):
        self.x = x
        self.y = y
        self.blocktype = blocktype
        self.width = width
        self.height = height

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

# 파일 입력 수정

size = 0

#크기조정
Start_background = pygame.transform.scale(Start_background, (width, height))
default_toolbox = pygame.transform.scale(default_toolbox, (pixel_size * 7, pixel_size*3))
default_move = pygame.transform.scale(default_move, (int(pixel_size/2), int(pixel_size/2)))
default_eraser = pygame.transform.scale(default_eraser, (pixel_size, pixel_size))
default_select = pygame.transform.scale(default_select, (pixel_size+2, pixel_size+2))

default_blackdot = pygame.transform.scale(default_blackdot, (pixel_size, pixel_size))

default_subportal = pygame.transform.scale(default_subportal, (pixel_size, pixel_size))

default_backblock = pygame.transform.scale(default_backblock, (pixel_size, pixel_size))
default_ball = pygame.transform.scale(default_ball, ((pixel_size//4)*3, (pixel_size//4)*3))
default_blckhole = pygame.transform.scale(default_blckhole, (pixel_size, pixel_size))
default_fakewal = pygame.transform.scale(default_fakewal, (pixel_size, pixel_size))
default_magnetic = pygame.transform.scale(default_magnetic, (pixel_size, pixel_size))
default_movewal = pygame.transform.scale(default_movewal, (pixel_size, pixel_size))
default_star = pygame.transform.scale(default_star, (pixel_size, pixel_size))
default_thorn = pygame.transform.scale(default_thorn, (pixel_size, pixel_size))
default_wall = pygame.transform.scale(default_wall, (pixel_size, pixel_size))
default_spring = pygame.transform.scale(default_spring, (pixel_size, pixel_size))
default_icicle = pygame.transform.scale(default_icicle, (pixel_size, pixel_size))
default_laser = pygame.transform.scale(default_laser, (pixel_size, pixel_size))
default_endpoint = pygame.transform.scale(default_endpoint, (pixel_size, pixel_size))

default_blinkblock = pygame.transform.scale(default_blinkblock, (pixel_size, pixel_size))
default_lever = pygame.transform.scale(default_lever, (pixel_size, pixel_size))
default_portal = pygame.transform.scale(default_portal, (pixel_size, pixel_size))
default_cannon = pygame.transform.scale(default_cannon, (pixel_size, pixel_size))
default_leverOnOff = pygame.transform.scale(default_leverOnOff, (pixel_size, pixel_size))

#아이콘 객체 생성
toolbox = newicon(0, 0, "toolbox", pixel_size*7, pixel_size*3)
move = newicon(toolbox.x, toolbox.y, "move", int(pixel_size/2), int(pixel_size/2))
eraser = newicon(toolbox.x + pixel_size*6, toolbox.y + pixel_size*2, "eraser", pixel_size, pixel_size)
select = newicon(toolbox.x + pixel_size*4 - 1, toolbox.y + pixel_size * 1 - 1, "select", pixel_size+2, pixel_size+2)
xmark = newicon(-pixel_size, -pixel_size, "xmark", pixel_size, pixel_size)

blackdot = newicon(-pixel_size, -pixel_size, "blackdot", pixel_size, pixel_size)

subportal = newicon(-pixel_size, -pixel_size, "subpotal", pixel_size, pixel_size)
levon = newicon(-pixel_size, -pixel_size, "levon", pixel_size, pixel_size)

backblock = newicon(toolbox.x + pixel_size*1, toolbox.y, "backblock", pixel_size, pixel_size)
ball = newicon(toolbox.x + pixel_size*2, toolbox.y, "ball", pixel_size, pixel_size)
blckhole = newicon(toolbox.x + pixel_size*3, toolbox.y, "blckhole", pixel_size, pixel_size)
fakewal = newicon(toolbox.x + pixel_size*4, toolbox.y, "fakewal", pixel_size, pixel_size)
magnetic = newicon(toolbox.x + pixel_size*5, toolbox.y, "magnetic", pixel_size, pixel_size)
movewal = newicon(toolbox.x + pixel_size*1, toolbox.y + pixel_size*1, "movewal", pixel_size, pixel_size)
star = newicon(toolbox.x + pixel_size*2, toolbox.y + pixel_size*1, "star", pixel_size, pixel_size)
thorn = newicon(toolbox.x + pixel_size*3, toolbox.y + pixel_size*1, "thorn", pixel_size, pixel_size)
wall = newicon(toolbox.x + pixel_size*4, toolbox.y + pixel_size*1, "wall", pixel_size, pixel_size)
spring = newicon(toolbox.x, toolbox.y + pixel_size*1, "spring", pixel_size, pixel_size)
icicle = newicon(toolbox.x + pixel_size*5, toolbox.y + pixel_size*1, "icicle", pixel_size, pixel_size)
laser = newicon(toolbox.x + pixel_size*6, toolbox.y, "laser", pixel_size, pixel_size)
endpoint = newicon(-pixel_size, -pixel_size, "endpoint", pixel_size, pixel_size)

blinkblock = newicon(toolbox.x + pixel_size*6, toolbox.y + pixel_size*1, "blinkblock", pixel_size, pixel_size)
lever = newicon(toolbox.x + pixel_size*0, toolbox.y + pixel_size*2, "lever", pixel_size, pixel_size)
portal = newicon(toolbox.x + pixel_size*1, toolbox.y + pixel_size*2, "portal", pixel_size, pixel_size)
cannon = newicon(toolbox.x + pixel_size*2, toolbox.y + pixel_size*2, "cannon", pixel_size, pixel_size)

while True:
    if Start_Screen:
        screen.blit(Start_background, (0, 0))

        for i in range(width//pixel_size):
            for j in range(height//pixel_size):
                pygame.draw.rect(screen, (50, 50, 50), [i*pixel_size, j*pixel_size, pixel_size, pixel_size], 1)

        for i in range(width//pixel_size):
            for j in range(height//pixel_size):
                temp = display[i][j].split(' ')
                if display[i][j].find('backblock') != -1:
                    default_backblock = pygame.transform.rotate(default_backblock, 90*int(temp[4]))
                    screen.blit(default_backblock, (i * pixel_size, j * pixel_size))
                    default_backblock = pygame.transform.rotate(default_backblock, -90*int(temp[4]))

                elif display[i][j].find('ball') != -1:
                    screen.blit(default_ball, (i*pixel_size+int((0.1)*pixel_size), j*pixel_size+int((0.1)*pixel_size)))

                elif display[i][j].find('blckhole') != -1:
                    default_blckhole = pygame.transform.rotate(default_blckhole, 90 * int(temp[4]))
                    screen.blit(default_blckhole, (i * pixel_size, j * pixel_size))
                    default_blckhole = pygame.transform.rotate(default_blckhole, -90 * int(temp[4]))

                elif display[i][j].find('fakewal') != -1:
                    default_fakewal = pygame.transform.rotate(default_fakewal, 90 * int(temp[4]))
                    screen.blit(default_fakewal, (i * pixel_size, j * pixel_size))
                    default_fakewal = pygame.transform.rotate(default_fakewal, -90 * int(temp[4]))

                elif display[i][j].find('magnetic') != -1:
                    default_magnetic = pygame.transform.rotate(default_magnetic, 90 * int(temp[4]))
                    screen.blit(default_magnetic, (i * pixel_size, j * pixel_size))
                    default_magnetic = pygame.transform.rotate(default_magnetic, -90 * int(temp[4]))

                elif display[i][j].find('movewal') != -1:
                    default_movewal = pygame.transform.rotate(default_movewal, 90 * int(temp[4]))
                    screen.blit(default_movewal, (i * pixel_size, j * pixel_size))
                    default_movewal = pygame.transform.rotate(default_movewal, -90 * int(temp[4]))

                elif display[i][j].find('endpoint') != -1:
                    default_endpoint = pygame.transform.rotate(default_endpoint, 90 * int(temp[4]))
                    screen.blit(default_endpoint, (i * pixel_size, j * pixel_size))
                    default_endpoint = pygame.transform.rotate(default_endpoint, -90 * int(temp[4]))

                elif display[i][j].find('star') != -1:
                    default_star = pygame.transform.rotate(default_star, 90 * int(temp[4]))
                    screen.blit(default_star, (i * pixel_size, j * pixel_size))
                    default_star = pygame.transform.rotate(default_star, -90 * int(temp[4]))

                elif display[i][j].find('thorn') != -1:
                    default_thorn = pygame.transform.rotate(default_thorn, 90 * int(temp[4]))
                    screen.blit(default_thorn, (i * pixel_size, j * pixel_size))
                    default_thorn = pygame.transform.rotate(default_thorn, -90 * int(temp[4]))

                elif display[i][j].find('wall') != -1:
                    default_wall = pygame.transform.rotate(default_wall, 90 * int(temp[4]))
                    screen.blit(default_wall, (i * pixel_size, j * pixel_size))
                    default_wall = pygame.transform.rotate(default_wall, -90 * int(temp[4]))

                elif display[i][j].find('spring') != -1:
                    default_spring = pygame.transform.rotate(default_spring, 90 * int(temp[4]))
                    screen.blit(default_spring, (i * pixel_size, j * pixel_size))
                    default_spring = pygame.transform.rotate(default_spring, -90 * int(temp[4]))

                elif display[i][j].find('icicle') != -1:
                    default_icicle = pygame.transform.rotate(default_icicle, 90 * int(temp[4]))
                    screen.blit(default_icicle, (i * pixel_size, j * pixel_size))
                    default_icicle = pygame.transform.rotate(default_icicle, -90 * int(temp[4]))

                elif display[i][j].find('laser') != -1:
                    default_laser = pygame.transform.rotate(default_laser, 90 * int(temp[4]))
                    screen.blit(default_laser, (i * pixel_size, j * pixel_size))
                    default_laser = pygame.transform.rotate(default_laser, -90 * int(temp[4]))

                elif display[i][j].find('subpotal') != -1:
                    default_subportal = pygame.transform.rotate(default_subportal, 90 * int(temp[4]))
                    screen.blit(default_subportal, (i * pixel_size, j * pixel_size))
                    default_subportal = pygame.transform.rotate(default_subportal, -90 * int(temp[4]))

                elif display[i][j].find('blinkblock') != -1:
                    default_blinkblock = pygame.transform.rotate(default_blinkblock, 90 * int(temp[4]))
                    screen.blit(default_blinkblock, (i * pixel_size, j * pixel_size))
                    default_blinkblock = pygame.transform.rotate(default_blinkblock, -90 * int(temp[4]))

                elif display[i][j].find('lever') != -1:
                    default_lever = pygame.transform.rotate(default_lever, 90 * int(temp[4]))
                    screen.blit(default_lever, (i * pixel_size, j * pixel_size))
                    default_lever = pygame.transform.rotate(default_lever, -90 * int(temp[4]))

                elif display[i][j].find('levon') != -1:
                    default_leverOnOff = pygame.transform.rotate(default_leverOnOff, 90 * int(temp[4]))
                    screen.blit(default_leverOnOff, (i * pixel_size, j * pixel_size))
                    default_leverOnOff = pygame.transform.rotate(default_leverOnOff, -90 * int(temp[4]))

                elif display[i][j].find('portal') != -1:
                    default_portal = pygame.transform.rotate(default_portal, 90 * int(temp[4]))
                    screen.blit(default_portal, (i * pixel_size, j * pixel_size))
                    default_portal = pygame.transform.rotate(default_portal, -90 * int(temp[4]))

                elif display[i][j].find('cannon') != -1:
                    default_cannon = pygame.transform.rotate(default_cannon, 90 * int(temp[4]))
                    screen.blit(default_cannon, (i * pixel_size, j * pixel_size))
                    default_cannon = pygame.transform.rotate(default_cannon, -90 * int(temp[4]))
                else:
                    pass

        screen.blit(default_toolbox, (toolbox.x, toolbox.y))
        screen.blit(default_move, (move.x, move.y))
        screen.blit(default_eraser, (eraser.x, eraser.y))

        #screen.blit(default_blackdot, (blackdot.x, blackdot.y))

        # screen.blit(default_subportal, (subportal.x, subportal.y))
        # screen.blit(default_leverOnOff, (levon.x, levon.y))

        screen.blit(default_backblock, (backblock.x, backblock.y))
        screen.blit(default_ball, (ball.x, ball.y))
        screen.blit(default_blckhole, (blckhole.x, blckhole.y))
        screen.blit(default_fakewal, (fakewal.x, fakewal.y))
        screen.blit(default_magnetic, (magnetic.x, magnetic.y))
        screen.blit(default_movewal, (movewal.x, movewal.y))
        screen.blit(default_star, (star.x, star.y))
        screen.blit(default_thorn, (thorn.x, thorn.y))
        screen.blit(default_wall, (wall.x, wall.y))
        screen.blit(default_spring, (spring.x, spring.y))
        screen.blit(default_icicle, (icicle.x, icicle.y))
        screen.blit(default_laser, (laser.x, laser.y))

        screen.blit(default_blinkblock, (blinkblock.x, blinkblock.y))
        screen.blit(default_lever, (lever.x, lever.y))
        screen.blit(default_portal, (portal.x, portal.y))
        screen.blit(default_cannon, (cannon.x, cannon.y))

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                f = open('game/data/maps/{0}'.format(SaveFile), 'w', encoding='UTF8')
                save = str(width) + " " + str(height) + " " + str(pixel_size) + "\n"
                f.write(save)
                f.write(filename + "\n")
                for i in range(width // pixel_size):
                    for j in range(height // pixel_size):
                        f.write(display[i][j])
                f.close()
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if backblock.isOver(pos):
                CheckCode = CreateBackBlock

            elif ball.isOver(pos):
                CheckCode = CreateBall

            elif blckhole.isOver(pos):
                CheckCode = CreateBlckhole

            elif fakewal.isOver(pos):
                CheckCode = CreateFakeWal

            elif magnetic.isOver(pos):
                CheckCode = CreateMagnetic

            elif movewal.isOver(pos):
                CheckCode = CreateMoveWal

            elif star.isOver(pos):
                CheckCode = CreateStar

            elif thorn.isOver(pos):
                CheckCode = CreateThorn

            elif wall.isOver(pos):
                CheckCode = CreateWall

            elif spring.isOver(pos):
                CheckCode = CreateSpring

            elif icicle.isOver(pos):
                CheckCode = CreateIcicle

            elif laser.isOver(pos):
                CheckCode = CreateLaser

            elif blinkblock.isOver(pos):
                CheckCode = CreateBlinkBlock

            elif lever.isOver(pos):
                CheckCode = CreateLever

            elif portal.isOver(pos):
                CheckCode = CreatePortal

            elif cannon.isOver(pos):
                CheckCode = CreateCannon

            elif eraser.isOver(pos):
                CheckCode = Erase
            elif move.isOver(pos):
                MoveToolbox = True

            elif display[pos[0] // pixel_size][pos[1] // pixel_size].find('endpoint') != -1:
                print(display[pos[0] // pixel_size][pos[1] // pixel_size])
                print(pos)
                movepos = [pos[0], pos[1]]
                print(movepos)
                CheckCode = MoveEndPoint

            elif display[pos[0] // pixel_size][pos[1] // pixel_size].find('levon') != -1:
                print(display[pos[0] // pixel_size][pos[1] // pixel_size])
                print(pos)
                movepos = [pos[0], pos[1]]
                print(movepos)
                CheckCode = MoveLeverOn

            elif display[pos[0] // pixel_size][pos[1] // pixel_size].find('subpotal') != -1:
                print(display[pos[0] // pixel_size][pos[1] // pixel_size])
                print(pos)
                movepos = [pos[0], pos[1]]
                print(movepos)
                CheckCode = MoveSubPortal
            else:
                continue

        if MoveToolbox and event.type == pygame.MOUSEBUTTONUP:
            CheckCode = -1
            toolbox.x, toolbox.y = pos[0], pos[1]
            move.x, move.y = toolbox.x, toolbox.y
            eraser.x, eraser.y = toolbox.x + pixel_size * 6, toolbox.y + pixel_size * 2

            backblock.x, backblock.y = toolbox.x + pixel_size * 1, toolbox.y
            ball.x, ball.y = toolbox.x + pixel_size * 2, toolbox.y
            blckhole.x, blckhole.y = toolbox.x + pixel_size * 3, toolbox.y
            fakewal.x, fakewal.y = toolbox.x + pixel_size * 4, toolbox.y
            magnetic.x, magnetic.y = toolbox.x + pixel_size * 5, toolbox.y
            movewal.x, movewal.y = toolbox.x + pixel_size * 1, toolbox.y + pixel_size * 1
            star.x, star.y = toolbox.x + pixel_size * 2, toolbox.y + pixel_size * 1
            thorn.x, thorn.y = toolbox.x + pixel_size * 3, toolbox.y + pixel_size * 1
            wall.x, wall.y = toolbox.x + pixel_size * 4, toolbox.y + pixel_size * 1
            spring.x, spring.y = toolbox.x, toolbox.y + pixel_size * 1
            icicle.x, icicle.y = toolbox.x + pixel_size * 5, toolbox.y + pixel_size * 1
            laser.x, laser.y = toolbox.x + pixel_size * 6, toolbox.y
            blinkblock.x, blinkblock.y = toolbox.x + pixel_size * 6, toolbox.y + pixel_size * 1
            lever.x, lever.y = toolbox.x + pixel_size * 0, toolbox.y + pixel_size * 2
            portal.x, portal.y = toolbox.x + pixel_size * 1, toolbox.y + pixel_size * 2
            cannon.x, cannon.y = toolbox.x + pixel_size * 2, toolbox.y + pixel_size * 2
            MoveToolbox = False

        if CheckCode == 0 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            if display[x][y].find('movewal') != -1 or display[x][y].find('endpoint') != -1\
                    or display[x][y].find('portal') != -1 or display[x][y].find('subpotal') != -1\
                    or display[x][y].find('lever') != -1 or display[x][y].find('levon') != -1:
                point = display[x][y].split(' ')
                display[x][y] = "0\n"
                display[int(point[5]) // pixel_size][int(point[6]) // pixel_size] = "0\n"
            else:
                display[x][y] = "0\n"

        #저장방식 ['0:blocktype' '1:x위치' '2:y위치' '3:pixel_size' '4:방향' '5:기타 x위치' '6:기타 y위치']
        #방향 0: 12시 방향(default), 1: 3시 방향, 2: 6시 방향, 3: 9시 방향
        elif CheckCode == 1 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "backblock" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + "0" + " " + "0" + "\n"

        elif CheckCode == 2 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "ball" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + "0" + " " + "0" + "\n"

        elif CheckCode == 3 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "blckhole" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + "0" + " " + "0" + "\n"

        elif CheckCode == 4 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "fakewal" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + "0" + " " + "0" + "\n"

        elif CheckCode == 5 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "magnetic" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + "0" + " " + "0" + "\n"

        elif CheckCode == 6 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            if x > width//pixel_size:
                print("오른쪽 공간을 비워주세요!")
                continue
            display[x][y] = "movewal" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + str((x+1)*pixel_size) + " " + str(y*pixel_size) + "\n"
            display[x+1][y] = "endpoint" + " " + str((x+1)*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + "\n"

        elif CheckCode == 7 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "star" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + "0" + " " + "0" + "\n"

        elif CheckCode == 8 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "thorn" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + "0" + " " + "0" + "\n"

        elif CheckCode == 9 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "wall" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + "0" + " " + "0" + "\n"

        elif CheckCode == 10 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "spring" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + "0" + " " + "0" + "\n"

        elif CheckCode == 11 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            display[x][y] = "icicle" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + "0" + " " + "0" + "\n"

        elif CheckCode == 12 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0] // pixel_size, pos[1] // pixel_size
            display[x][y] = "laser" + " " + str(x * pixel_size) + " " + str(y * pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + "0" + " " + "0" + "\n"

        elif CheckCode == 13 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0] // pixel_size, pos[1] // pixel_size
            display[x][y] = "blinkblock" + " " + str(x * pixel_size) + " " + str(y * pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + "0" + " " + "0" + "\n"


        elif CheckCode == 14 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0] // pixel_size, pos[1] // pixel_size
            if x > width // pixel_size:
                print("오른쪽 공간을 비워주세요!")
                continue
            display[x][y] = "lever" + " " + str(x * pixel_size) + " " + str(y * pixel_size) + " " + str(pixel_size) \
                            + " " + "0" + " " + str((x + 1) * pixel_size) + " " + str(y * pixel_size) + "\n"
            display[x + 1][y] = "levon" + " " + str((x + 1) * pixel_size) + " " + str(y * pixel_size) + " " + str(pixel_size) \
                            + " " + "0" + " " + str(x * pixel_size) + " " + str(y * pixel_size) + "\n"

        elif CheckCode == 15 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0]//pixel_size, pos[1]//pixel_size
            if x > width//pixel_size:
                print("오른쪽 공간을 비워주세요!")
                continue
            display[x][y] = "portal" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + str((x+1)*pixel_size) + " " + str(y*pixel_size) + "\n"
            display[x+1][y] = "subpotal" + " " + str((x+1)*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + "\n"

        elif CheckCode == 16 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0] // pixel_size, pos[1] // pixel_size
            display[x][y] = "cannon" + " " + str(x * pixel_size) + " " + str(y * pixel_size) + " " + str(pixel_size)\
                            + " " + "1" + " " + "0" + " " + "0" + "\n"
        elif CheckCode == -14 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0] // pixel_size, pos[1] // pixel_size
            a, b = movepos[0] // pixel_size, movepos[1] // pixel_size
            endp = display[a][b].split(' ')
            startp = display[int(endp[5])//pixel_size][int(endp[6])//pixel_size].split(' ')
            display[a][b] = "0\n"
            display[x][y] = "levon" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + str(startp[1]) + " " + str(startp[2]) + "\n"
            display[int(endp[5])//pixel_size][int(endp[6])//pixel_size] = "lever" + " " + str(startp[1]) + " " + str(startp[2]) + " " + str(pixel_size)\
                            + " " + "0" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + "\n"
            CheckCode = -1


        elif CheckCode == -6 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0] // pixel_size, pos[1] // pixel_size
            a, b = movepos[0] // pixel_size, movepos[1] // pixel_size
            endp = display[a][b].split(' ')
            startp = display[int(endp[5])//pixel_size][int(endp[6])//pixel_size].split(' ')
            display[a][b] = "0\n"
            display[x][y] = "endpoint" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + str(startp[1]) + " " + str(startp[2]) + "\n"
            display[int(endp[5])//pixel_size][int(endp[6])//pixel_size] = "movewal" + " " + str(startp[1]) + " " + str(startp[2]) + " " + str(pixel_size)\
                            + " " + "0" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + "\n"
            CheckCode = -1

        elif CheckCode == -15 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x, y = pos[0] // pixel_size, pos[1] // pixel_size
            a, b = movepos[0] // pixel_size, movepos[1] // pixel_size
            endp = display[a][b].split(' ')
            startp = display[int(endp[5])//pixel_size][int(endp[6])//pixel_size].split(' ')
            display[a][b] = "0\n"
            display[x][y] = "subpotal" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + " " + str(pixel_size)\
                            + " " + "0" + " " + str(startp[1]) + " " + str(startp[2]) + "\n"
            display[int(endp[5])//pixel_size][int(endp[6])//pixel_size] = "portal" + " " + str(startp[1]) + " " + str(startp[2]) + " " + str(pixel_size)\
                            + " " + "0" + " " + str(x*pixel_size) + " " + str(y*pixel_size) + "\n"
            CheckCode = -1

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            x, y = pos[0] // pixel_size, pos[1] // pixel_size
            if display[x][y].find('movewal') != -1 or display[x][y].find('endpoint') != -1 \
                    or display[x][y].find('portal') != -1 or display[x][y].find('subpotal') != -1\
                    or display[x][y].find('lever') != -1 or display[x][y].find('levon') != -1:
                point = display[x][y].split(' ')
                display[x][y] = "0\n"
                display[int(point[5]) // pixel_size][int(point[6]) // pixel_size] = "0\n"
            else:
                display[x][y] = "0\n"



        #방향잡는건 나중에 함
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 4:  #마우스 휠 위로
            x, y = pos[0] // pixel_size, pos[1] // pixel_size
            if display[x][y] == "0\n":
                break
            temp = display[x][y].split(' ')
            side = (int(temp[4])+1) % 4
            display[x][y] = temp[0] + " " + temp[1] + " " + temp[2] + " " + temp[3]\
                            + " " + str(side) + " " + temp[5] + " " + temp[6]

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 5:  #마우스 휠 아래로
            x, y = pos[0] // pixel_size, pos[1] // pixel_size
            if display[x][y] == "0\n":
                break
            temp = display[x][y].split(' ')
            side = (int(temp[4])-1) % 4
            display[x][y] = temp[0] + " " + temp[1] + " " + temp[2] + " " + temp[3]\
                            + " " + str(side) + " " + temp[5] + " " + temp[6]

        else:
            continue

    pygame.display.update()

#최종수정시간:2020.06.19.
