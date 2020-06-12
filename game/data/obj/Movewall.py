import pygame
from obj import Wall
'''속도 수정필요, 이보다 더 느리게 해야 될시 추가적인 변수로 좌포값을 따로 계산 및 저장하고 그값을 매번 집어 넣는 것이 필요'''

class Movewall(Wall.Wall):
    def __init__(self, img, start,end, area,FPS=60,speed=1):  # 이미지,설치좌표(튜플로 전달),폭과 높이를 튜플로 전달,이동 거리
        pygame.sprite.Sprite.__init__(self)  # 스프라이트 초기화
        self.image = pygame.transform.scale(img, area)  # 이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()  # 이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.topleft = start  # 위치설정
        self.mask = pygame.mask.from_surface(self.image)  # 충돌감지를 위한 마스크생성

        self.end=end
        self.start=start
        self.speed=[speed,speed]


    def Move(self):
        '''끝측정은 블럭의 끝으로 한다'''
        self.rect.topleft=(self.rect.topleft[0]+self.speed[0],self.rect.topleft[1]+self.speed[1]) #이동

        if self.rect.left>=self.end[0]:
            self.speed[0] = -self.speed[0]
        elif self.rect.left<=self.start[0]:
            self.speed[0]= -self.speed[0]

        if self.rect.top >= self.end[1]:
            self.speed[1] = -self.speed[1]
        elif self.rect.top <= self.start[1]:
            self.speed[1] = -self.speed[1]



    def get_center(self,index=2):
        '''rect.center를 반환 인자로 0을 넣으면 x좌표가 1을 넣으면 y좌표가 반환 됨'''
        try:
            return self.rect.center[index]
        except IndexError:
            return self.rect.center

    def set_location(self,loc):
        self.rect.center=loc


