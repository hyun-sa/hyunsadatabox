import pygame
from obj import Wall


class Movewall(Wall.Wall):
    def __init__(self, img, location, area,distance,FPS=60,speed=1):  # 이미지,설치좌표(튜플로 전달),폭과 높이를 튜플로 전달,이동 거리
        pygame.sprite.Sprite.__init__(self)  # 스프라이트 초기화
        self.image = pygame.transform.scale(img, area)  # 이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()  # 이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.topleft = location  # 위치설정
        self.mask = pygame.mask.from_surface(self.image)  # 충돌감지를 위한 마스크생성
        self.end_x=(location[0]-distance[0],location[0]+distance[0]) #(왼쪽,오른쪽)
        self.end_y=(location[1]+distance[1],location[1]-distance[1])#(아래, 위)
        self.speed=[distance[0]/FPS*speed,distance[1]/FPS*speed]
        print(self.end_x,self.end_y,self.speed)

    def Move(self):
        '''끝측정은 블럭의 끝으로 한다'''
        self.rect.center=(self.rect.center[0]+self.speed[0],self.rect.center[1]+self.speed[1])

        if self.rect.left<=self.end_x[0] or self.rect.right>=self.end_x[1]:
            #이상하게 -를 할때가 속도가 빠름
            if self.speed[0] > 0:
                self.speed[0]= -self.speed[0]/2
            elif self.speed[0] < 0:
                self.speed[0] = -self.speed[0] * 2
        if self.rect.bottom >= self.end_y[0] or self.rect.top <= self.end_y[1]:
            # 이상하게 -를 할때가 속도가 빠름
            if self.speed[1] > 0:
                self.speed[1] = -self.speed[1] / 2
            elif self.speed[1] < 0:
                self.speed[1] = -self.speed[1] * 2


