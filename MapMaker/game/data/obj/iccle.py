import pygame
from game.data.obj.Setting import setting as s

class Iccle(pygame.sprite.Sprite):
    def __init__(self,img,location,area,time=1.2,speed=1):
        '''블럭 이미지, 위치(튜플),면적(튜플), 고드름이 사라져있는 시간,속도'''
        pygame.sprite.Sprite.__init__(self)             #스프라이트 초기화
        self.image= pygame.transform.scale(img,area)    #이미지의 크기를 내가 원하는 크기로 조정
        self.rect= self.image.get_rect()                #이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.topleft= location                     #위치설정
        self.mask=pygame.mask.from_surface(self.image)  #충돌감지를 위한 마스크생성

        self.gravity=speed*s.Fall_speed/s.FPS

        self.speed=speed
        self.frame_counter = 0  # 1이상일 경우 사라져 있음
        self.disappear_time = time  # 사라져있을시간
        self.start_loc=location      #시작위치

    def disappear(self):
        self.frame_counter=s.FPS*self.disappear_time


    def isnotdisappear(self):
        '''출력전에 이것을 체크하고 반환된 값이 1일경우 출력 0일경우 출력 안해야함'''
        if self.frame_counter>0:
            self.frame_counter-=1
            return 0
        self.rect.topleft=self.start_loc
        self.speed=1
        return 1

    def move(self):
        '''아래로 떨어짐 만약 다른 블럭들과 부딪칠 경우 1 아닐경우 0반환'''
        if self.rect.right < 0 or self.rect.left>s.width or self.rect.top>s.height or self.rect.bottom<0:
            return 1

        collision_list = pygame.sprite.spritecollide(self, s.wall, False, pygame.sprite.collide_mask)
        if collision_list:
           return 1

        x,y=self.rect.center

        # 속도변화
        self.speed += self.gravity

        # y이동
        y += self.speed
        self.rect.center = (x, y)  # 좌표값변경

        return 0

    def get_center(self,index=2):
        '''rect.center를 반환 인자로 0을 넣으면 x좌표가 1을 넣으면 y좌표가 반환 됨'''
        try:
            return self.rect.center[index]
        except IndexError:
            return self.rect.center

    def set_location(self,loc):
        self.rect.center=loc

    def set_collision(self,obj_list):
        self.col_obj=obj_list

    def collision_check(self):
        if not self.col_obj:
            return -1
        return 0
