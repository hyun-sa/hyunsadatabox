#2019038026 이혁수
import pygame
from obj import Ball


class Spring(pygame.sprite.Sprite):
    def __init__(self, img, location, area):            # 이미지,설치좌표(튜플로 전달),넓이와 높이를 튜플로 전달
        pygame.sprite.Sprite.__init__(self)             #스프라이트 초기화
        self.image = pygame.transform.scale(img, area)  #이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()               #이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.topleft = location                     #위치설정
        self.mask = pygame.mask.from_surface(self.image)#충돌감지를 위한 마스크생성

    def spring(self,ball):
        '''스프링이 밑에 있으면 공의 y축 위쪽방향으로 속도가 증가하여 튀어오른 것처럼'''
        # 벽의 옆면과 부딪혔을때
        if (self.rect.right <= ball.get_center(0) and ball.get_speed(0) < 0) or (self.rect.left > ball.get_center(0) and ball.get_speed(0) > 0):
            ball.set_dontchangespeed(10)  # 벽에 닿아서 튕겨 나올때 x축 속도를 못 바꾸게 하기위해서 사용(현재 10프레임동안 불가능)
            ball.reverse_speed_x()
            # 떨어질때 닿은 것이 아니라 올라갈때 닿으면 더 올라갈 수 있도록 y축 설정 (벽타기)
            if ball.get_speed_y() <= 0:
                ball.speed_set_y(-Ball.MAX_SPEED // 2)
        elif(self.rect.top>ball.get_center(1)-ball.get_speed_y()):
            if ball.get_speed(1)>10:
                return 1
            ball.speed_set_y(-Ball.MAX_SPEED * 1.5)
