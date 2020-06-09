import pygame
import sys

pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

Start_Screen = True
MoveToolbox = False
CreateWall = False
CreateThorn = False
CreateStar = False
CreateStartpoint = False
Erase = False

Start_background = pygame.image.load("mapeditimage/Background.png")
default_toolbox = pygame.image.load('mapeditimage/toolbox.png')
default_move = pygame.image.load('mapeditimage/move.png')
default_wall = pygame.image.load('mapeditimage/wall.png')
default_thorn = pygame.image.load('mapeditimage/thorn.png')
default_star = pygame.image.load('mapeditimage/star.png')
default_startpoint = pygame.image.load('mapeditimage/startpoint.png')




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


#1920*1080기준30으로 나눔
#display[64][36] = {0}
display = []
for i in range(64):
    temp = []
    for j in range(36):
        temp.append("0")
    display.append(temp)

# 파일 입력 수정

size = 0
pixel_size = 30 + 2**size

default_toolbox = pygame.transform.scale(default_toolbox, (pixel_size * 6, pixel_size*2))
default_move = pygame.transform.scale(default_move, (int(pixel_size/2), int(pixel_size/2)))
default_wall = pygame.transform.scale(default_wall, (pixel_size, pixel_size))
default_thorn = pygame.transform.scale(default_thorn, (pixel_size, pixel_size))
default_star = pygame.transform.scale(default_star, (pixel_size, pixel_size))
default_startpoint = pygame.transform.scale(default_startpoint, (pixel_size, pixel_size))


toolbox = newicon(0, 0, "toolbox", pixel_size*6, pixel_size*2)
move = newicon(toolbox.x, toolbox.y, "move", int(pixel_size/2), int(pixel_size/2))
wall = newicon(toolbox.x + pixel_size*1, toolbox.y, "wall", pixel_size, pixel_size)
thorn = newicon(toolbox.x + pixel_size*2, toolbox.y, "thorn", pixel_size, pixel_size)
star = newicon(toolbox.x + pixel_size*3, toolbox.y, "star", pixel_size, pixel_size)
startpoint = newicon(toolbox.x + pixel_size*4, toolbox.y, "startpoint", pixel_size, pixel_size)


while True:
    if Start_Screen:
        screen.blit(Start_background, (0, 0))

        for i in range(64):
            for j in range(36):
                pygame.draw.rect(screen, (50, 50, 50), [i*30, j*30, 30, 30], 1)
        screen.blit(default_toolbox, (toolbox.x, toolbox.y))
        screen.blit(default_move, (move.x, move.y))
        screen.blit(default_wall, (wall.x, wall.y))
        screen.blit(default_thorn, (thorn.x, thorn.y))
        screen.blit(default_star, (star.x, star.y))
        screen.blit(default_startpoint, (startpoint.x, startpoint.y))
        for i in range(64):
            for j in range(36):
                #추후 사용한다면 수정필요
                if display[i][j].find("wall") != -1:
                    screen.blit(default_wall, (i*30, j*30))
                elif display[i][j].find("thorn") != -1:
                    screen.blit(default_thorn, (i*30, j*30))
                elif display[i][j].find("p") != -1:  # 4개중에 'p'가 들어가는게 이거만 있어서 가능했음
                    screen.blit(default_startpoint, (i * 30, j * 30))
                elif display[i][j].find("star") != -1:
                    screen.blit(default_star, (i*30, j*30))
                else:
                    continue

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if wall.isOver(pos):
                CreateWall = True
            elif thorn.isOver(pos):
                CreateThorn = True
            elif star.isOver(pos):
                CreateStar = True
            elif startpoint.isOver(pos):
                CreateStartpoint = True
            elif move.isOver(pos):
                MoveToolbox = True
            elif toolbox.isOver(pos):
                Erase = True
            else:
                continue

        if CreateWall and event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pos[0]//30, pos[1]//30
            display[x][y] = "wall" + " " + str(pos[0]) + " " + str(pos[1]) + " " + "0"
            CreateWall = False

        if CreateThorn and event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pos[0]//30, pos[1]//30
            display[x][y] = "thorn" + " " + str(pos[0]) + " " + str(pos[1]) + " " + "0"
            CreateThorn = False

        if CreateStar and event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pos[0]//30, pos[1]//30
            display[x][y] = "star" + " " + str(pos[0]) + " " + str(pos[1]) + " " + "0"
            CreateStar = False

        if CreateStartpoint and event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pos[0]//30, pos[1]//30
            display[x][y] = "startpoint" + " " + str(pos[0]) + " " + str(pos[1]) + " " + "0"
            CreateStartpoint = False

        if MoveToolbox and event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            toolbox.x, toolbox.y = pos[0], pos[1]
            move.x, move.y = toolbox.x, toolbox.y
            wall.x, wall.y = toolbox.x + pixel_size * 1, toolbox.y
            thorn.x, thorn.y = toolbox.x + pixel_size * 2, toolbox.y
            star.x, star.y = toolbox.x + pixel_size * 3, toolbox.y
            startpoint.x, startpoint.y = toolbox.x + pixel_size * 4, toolbox.y
            MoveToolbox = False

        if Erase and event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pos[0]//30, pos[1]//30
            display[x][y] = "0"
            Erase = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                #파일 출력 수정
                pygame.quit()
                sys.exit()


    pygame.display.update()

#최종수정된:1207