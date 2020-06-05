import pygame
# import SaveScore
# import sys

class button(): #수정할거임
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

def score_board(isplaygame, newscore, width, height):
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #수정할거임
    newname = "Tlqkf" #수정할거임

    Score_Board = pygame.image.load('Score_Board.png')
    X_Button = pygame.image.load('x_mark.png') # 이미지 크기50*50

    x_button = button(width*0.85, height*0.2, 50, 50)
    while True:
        screen.blit(Score_Board, (0, 0))
        screen.blit(X_Button, (x_button.x, x_button.y))
        f = open('rank.txt', 'r')
        textheight = height / 2 - 160
        textwidth = width / 2 - 250
        while True:
            line = f.readline()
            if not line: break
            name, score = line.split(' ')
            text = name + "                                       " + score
            textfont = pygame.font.Font('NanumGothic.ttf', 40)
            text = textfont.render(text, True, (0, 0, 0))
            textpos = text.get_rect()
            textheight += 45
            textpos.center = (textwidth, textheight)
            screen.blit(text, textpos)
        f.close()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if x_button.isOver(pos):
                    return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0

#if isplaygame:     #수정할거임
    #SaveScore.save_new_score(newscore, newname)



