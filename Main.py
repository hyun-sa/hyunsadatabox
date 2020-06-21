# Bouncy Dungeon Tech-alpha 0.3
# Main.py coded by 조민우
import pygame, sys, os, configparser, map, random
from game.data import SaveScore, Rankinit
from game.data.obj.Setting import setting as s
# Setting before Main
mainClock = pygame.time.Clock()

FPS_dic={"Low":30,"Mid":60,"High":60}

# Load Config.cfg
config = configparser.RawConfigParser()
configFilePath = os.path.join(os.path.dirname(__file__), 'game/data/Setting.cfg')
config.read(configFilePath)
FullToggle = config.get("Setting", "Fullscreen_Toggle")
SoundToggle = config.get("Setting", "Sound")
ScoreToggle = config.get("Setting", "Display_Score")
Frame = config.get("Setting", "Frame")
StoryToggle = config.get("Game", "Story_Toggle")
s.set_FPS(FPS_dic[config.get("Setting", "Frame")])

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

difficulty = 0
map_List = []


def initialze_map():
    map_L = [[],[],[],[]]
    for i in range(1, 9):
        txt = "easy_map"
        txt += str(i)
        txt += ".txt"
        map_L[0].append(txt)
    for i in range(1, 8):
        txt = "normal_map"
        txt += str(i)
        txt += ".txt"
        map_L[1].append(txt)
    for i in range(1, 5):
        txt = "hard_map"
        txt += str(i)
        txt += ".txt"
        map_L[2].append(txt)
    for i in range(1, 4):
        txt = "hell_map"
        txt += str(i)
        txt += ".txt"
        map_L[3].append(txt)
    return map_L


def suffle_map(map_t, map_L):
    global difficulty
    while len(map_L[difficulty]) == 0:
        difficulty += 1
        if difficulty == 4:
            difficulty = 0
    map_t = map_L[difficulty].pop(random.randrange(0, len(map_L[difficulty])))
    return map_t


# Here is Main
def Start_Menu():
    while True:
        show_screen()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if s_button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    pygame.mixer.music.pause()
                    Game_Menu()
                    pygame.mixer.music.unpause()
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
    global difficulty
    difficulty = 0
    running = 0
    Life = 4
    map_txt = ''
    map_List = initialze_map()
    map_txt = suffle_map(map_txt, map_List)
    newscore = 0
    while Life != 0:
        running = map.Map(screen, Life, map_txt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if running == -1:
            die_sound.play()
            pygame.time.delay(250)
            Life -= 1
        elif running == 1:
            if len(map_List[0]) == 0 and len(map_List[1]) == 0 and len(map_List[2]) == 0 and len(map_List[3]) == 0:
                break
            difficulty += 1
            map_txt = suffle_map(map_txt, map_List)
            newscore += 1
        elif running == -2 or running == 1:
            break

    if Life == 0:
        print("gameover")
        newname = SaveScore.get_name(screen)
        SaveScore.save_new_score(newscore, newname)
        Score_Menu()

    elif running ==1:
        print("클리어")
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
                    s.set_FPS(30)
                if Frame_MID_Button.isOver(pos):
                    pygame.mixer.Sound.play(Click_Sound)
                    Frame = "Mid"
                    config.set("Setting", "Frame", "Mid")
                    s.set_FPS(60)
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


# CopyRight 2019038011 윤석현
def Score_Menu():
    running = True
    screen.blit(Score_Board, (0, 0))
    while running:
        f = open('game/data/rank.txt', 'r')
        textheight = height // 2 - 160
        textwidth = width // 2 - 450
        cnt = 0
        while True:
            cnt += 1
            line = f.readline()
            if not line or cnt > 10:
                break
            name, score = line.split(' ')
            textfont = pygame.font.Font('game/data/NanumGothic.ttf', 40)
            name = textfont.render(name, True, (0, 0, 0))
            score = textfont.render(score, True, (0, 0, 0))
            namepos = name.get_rect()
            scorepos = score.get_rect()
            textheight += 45
            namepos.center = (textwidth, textheight)
            scorepos.center = (textwidth + 450, textheight)
            screen.blit(name, namepos)
            screen.blit(score, scorepos)
        f.close()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = 0
                if event.key == pygame.K_F5:
                    Rankinit.rank_init()
                    show_screen()
                    screen.blit(Score_Board, (0, 0))
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


def Show_Story():
    running = 6
    Story_1 = pygame.image.load("game/image/Story_1.png")
    Story_2 = pygame.image.load("game/image/Story_2.png")
    Story_3 = pygame.image.load("game/image/Story_3.png")
    Story_4 = pygame.image.load("game/image/Story_4.png")
    Story_5 = pygame.image.load("game/image/Story_5.png")
    Story_6 = pygame.image.load("game/image/Story_6.png")
    while running:
        if running == 6:
            screen.blit(Story_1, (0, 0))
        if running == 5:
            screen.blit(Story_2, (0, 0))
        if running == 4:
            screen.blit(Story_3, (0, 0))
        if running == 3:
            screen.blit(Story_4, (0, 0))
        if running == 2:
            screen.blit(Story_5, (0, 0))
        if running == 1:
            screen.blit(Story_6, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running -= 1
                if event.key == pygame.K_ESCAPE:
                    running = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



pygame.mixer.music.load('game/audio/Main_bgm.mp3')
pygame.mixer.music.play(-1)
if StoryToggle == "False":
    Show_Story()
    StoryToggle = "True"
    config.set("Game", "Story_Toggle", "True")
    ConfigFile = open('game/data/Setting.cfg', 'w')
    config.write(ConfigFile)
    ConfigFile.close()
Start_Menu()