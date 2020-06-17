# Bouncy Dungeon Tech-alpha 0.1
import pygame, sys, os, configparser, testmap
from game.data import SaveScore

# Setting before Main
mainClock = pygame.time.Clock()

# Load Config.cfg
config = configparser.RawConfigParser()
configFilePath = os.path.join(os.path.dirname(__file__), 'game/data/Setting.cfg')
config.read(configFilePath)
FullToggle = config.get("Setting", "Fullscreen_Toggle")
SoundToggle = config.get("Setting", "Sound")
ScoreToggle = config.get("Setting", "Display_Score")
Frame = config.get("Setting", "Frame")

# Pygame Initialize
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('BOUNCY DUNGEON')
width, height = 1920, 1080
if FullToggle == "True":
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((0, 0))


Start_background = pygame.image.load("game/image/Background.png")
Start_Button = pygame.image.load("game/image/Game Start.png")
Help_Button = pygame.image.load("game/image/Help.png")
Score_Button = pygame.image.load("game/image/Score Board.png")
Setting_Button = pygame.image.load("game/image/Setting.png")
Exit_Button = pygame.image.load("game/image/Exit.png")
Gray_Background = pygame.image.load("game/image/Gray Background.png")
Score_Board = pygame.image.load("game/image/Score_Board.png")
Setting_Screen = pygame.image.load("game/image/Setting_Screen.png")
Chk = pygame.image.load("game/image/Chk.png")
Chk_2 = pygame.image.load("game/image/Chk.png")
Chk_Box = pygame.image.load("game/image/Chk_Box.png")
hidden_content = pygame.image.load("game/image/hidden_content.png")
Click_Sound = pygame.mixer.Sound("game/audio/click.wav")
die_sound = pygame.mixer.Sound("game/audio/diesound.wav")

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


s_button = button(0.64583*width, 0.5*height, 615, 141)
score_button = button(1240, 715, 615, 141)
setting_button = button(1770, 20, 122, 121)
help_button = button(1680, 20, 66, 105)
exit_button = button(1300, 880, 481, 110)


# Here is Main
def Start_Menu():
    #pygame.mixer.music.load('game/audio/Main_bgm.mp3')
    #pygame.mixer.music.play(-1)
    while True:
        show_screen()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if s_button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    #pygame.mixer.music.pause()
                    Game_Menu()
                    #pygame.mixer.music.unpause()
                if setting_button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    Setting_Menu()
                if score_button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    Score_Menu()
                if help_button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    Help_Menu()
                if exit_button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    pygame.time.wait(300)
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


def Game_Menu():
    running = 0
    Life = 4
    while Life != 0:
        running = testmap.Map(screen, Life)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if running == -1:
            die_sound.play()
            pygame.time.delay(250)
            Life -= 1
        elif running == -2 or running == 1:
            break

    if Life == 0:
        print("gameover")
        newscore = 597
        newname = SaveScore.get_name(screen)
        SaveScore.save_new_score(newscore, newname)
        Score_Menu()

    elif running ==1:
        print("클리어")
        newscore = 597
        newname = SaveScore.get_name(screen)
        SaveScore.save_new_score(newscore, newname)
        Score_Menu()

def Setting_Menu():
    running = True
    screen.blit(Setting_Screen, (0,0))
    Sound_Button = button(625, 335, 75, 75)
    Score_Button = button(970, 475, 75, 75)
    Frame_LOW_Button = button(780, 600, 160, 80)
    Frame_MID_Button = button(1065, 600, 160, 80)
    Frame_HIGH_Button = button(1380, 600, 160, 80)

    while running:
        global SoundToggle
        global ScoreToggle
        global Frame
        if SoundToggle == "True":
            screen.blit(Chk, (600, 320))
        else:
            screen.blit(Chk, (width, height))
        if ScoreToggle == "True":
            screen.blit(Chk_2, (945, 460))
        else:
            screen.blit(Chk_2, (width, height))
        if Frame == "Low":
            screen.blit(Chk_Box, (775, 600))
        if Frame == "Mid":
            screen.blit(Chk_Box, (1060, 600))
        if Frame == "High":
            screen.blit(Chk_Box, (1375, 600))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                show_screen()
                screen.blit(Setting_Screen, (0, 0))
                if Sound_Button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    if SoundToggle == "False":
                        config.set("Setting", "Sound", "True")
                        SoundToggle = "True"
                    else:
                        SoundToggle = "False"
                        config.set("Setting", "Sound", "False")
                if Score_Button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    if ScoreToggle == "False":
                        ScoreToggle = "True"
                        config.set("Setting", "Display_Score", "True")
                    else:
                        ScoreToggle = "False"
                        config.set("Setting", "Display_Score", "False")
                if Frame_LOW_Button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    Frame = "Low"
                    config.set("Setting", "Frame", "Low")
                if Frame_MID_Button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    Frame = "Mid"
                    config.set("Setting", "Frame", "Mid")
                if Frame_HIGH_Button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    Frame = "High"
                    config.set("Setting", "Frame", "High")
                ConfigFile = open('game/data/Setting.cfg', 'w')
                config.write(ConfigFile)
                ConfigFile.close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


def Score_Menu():
    running = True
    screen.blit(Score_Board, (0, 0))
    textheight = height // 2 - 160
    textwidth = width // 2 - 250
    while running:
        f = open('game/data/rank.txt', 'r')
        textheight = height // 2 - 160
        textwidth = width // 2 - 250
        while True:
            line = f.readline()
            if not line:
                break
            name, score = line.split(' ')
            text = name + "                                       " + score
            textfont = pygame.font.Font('game/data/NanumGothic.ttf', 40)
            text = textfont.render(text, True, (0, 0, 0))
            textpos = text.get_rect()
            textheight += 45
            textpos.center = (textwidth, textheight)
            screen.blit(text, textpos)
        f.close()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def Help_Menu():
    running = True
    screen.blit(Gray_Background, (0, 0))
    while running:
        screen.blit(hidden_content, (225, 225))
        screen.blit(hidden_content, (225, 570))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def show_screen():
    screen.blit(Start_background, (0, 0))
    screen.blit(Setting_Button, (1770, 20))
    screen.blit(Help_Button, (1680, 20))
    screen.blit(Start_Button, (1240, 540))
    screen.blit(Score_Button, (1240, 715))
    screen.blit(Exit_Button, (1300, 880))

Start_Menu()