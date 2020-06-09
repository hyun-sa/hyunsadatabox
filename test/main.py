import pygame
import sys



import testmap


pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

Start_background = pygame.image.load("image/Background.png")
Start_Button = pygame.image.load("image/Game Start.png")
Help_Button = pygame.image.load("image/Help.png")
Score_Button = pygame.image.load("image/Score Board.png")
Setting_Button = pygame.image.load("image/Setting.png")
Exit_Button = pygame.image.load("image/Exit.png")

Start_Screen = True
Show_setting = False
Show_score = False
Show_help = False
Score_Board = False
Game_screen = False


class button():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True


s_button = button(1240, 540, 615, 141)
score_button = button(1240, 715, 615, 141)
setting_button = button(1770, 20, 122, 121)
help_button = button(1680, 20, 66, 105)
exit_button = button(1300, 880, 481, 110)


while True:

    if Start_Screen:
        screen.blit(Start_background, (0, 0))
        screen.blit(Setting_Button, (1770, 20))
        screen.blit(Help_Button, (1680, 20))
        screen.blit(Start_Button, (1240, 540))
        screen.blit(Score_Button, (1240, 715))
        screen.blit(Exit_Button, (1300, 880))

    if Show_setting:
        continue
    if Show_score:
        continue
    if Game_screen:
        run=1
        while run:
            run=testmap.map(screen)
        Start_Screen = True
        Game_screen = False
    if Score_Board:
        Score_Board = False
    if Show_help:
        continue

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if s_button.isOver(pos):
                Start_Screen = False
                Game_screen = True
            if setting_button.isOver(pos):
                Show_setting = True
            if score_button.isOver(pos):
                Start_Screen=False
                Show_score = True
            if help_button.isOver(pos):
                Show_help = True
            if exit_button.isOver(pos):
                pygame.quit()
                sys.exit()


    pygame.display.flip()