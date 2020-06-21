import fileinput
import pygame
import sys

#############################################################################################
# 해당 파일은 랭킹을 기록하기 위한 파일입니다. 이 파일은 키의 코드를 얻기위해 별도의 프로그램으로 사용할 수 있습니다.
# 이 파일(SaveScore.py)의 CopyRight은
# 2019038011 윤석현
# 에게 있습니다.
#############################################################################################
# CopyRight 2019038011 윤석현
def get_key_code():
    pygame.init()
    screen = pygame.display.set_mode((300, 200))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break

    pygame.quit()
    sys.exit()


# CopyRight 2019038011 윤석현
def get_name(screen = pygame.display.set_mode((1920, 1080))):
    height = 1920
    width = 1080
    Enter_Name = pygame.image.load("game/image/Enter_Name.png")
    screen.blit(Enter_Name, (0, 0))
    textfont = pygame.font.Font('game/data/NanumGothic.ttf', 80)
    textheight = height // 2
    textwidth = width // 2
    name = ""
    while True:
        text = textfont.render(name, True, (0, 0, 0))
        textpos = text.get_rect()
        textpos.center = (textheight, textwidth)
        screen.blit(Enter_Name, (0, 0))
        screen.blit(text, textpos)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name
                if event.key == pygame.K_ESCAPE:
                    return name
                if event.key == pygame.K_BACKSPACE:
                    name = name[0:-1]
                    continue
                # 기타 문자 오류 있음
                name = name + '%c' % event.key


# CopyRight 2019038011 윤석현
def save_new_score(newscore, newname):
    newscore = str(newscore)
    newname = str(newname)
    contained = 0
    linecount = 0
    for line in fileinput.input('game/data/rank.txt', inplace=True):
        name, score = line.split(' ')
        if int(score) < int(newscore) and contained == 0:
            line = line.replace(line, newname + " " + newscore + "\n" + line)
            contained = 1
        linecount += 1
        if linecount+contained < 11:
            sys.stdout.write(line)

        else:
            fileinput.close()
            break


#get_key_code()