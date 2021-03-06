import pygame
from game.data.obj import Ball
from game.data.obj.Setting import setting as s

class block(pygame.sprite.Sprite):
    def __init__(self,img,location,area,time=5):
        '''블럭 이미지, 위치(튜플),면적(튜플), 상태가 지속되는 시간'''
        pygame.sprite.Sprite.__init__(self)  # 스프라이트 초기화
        self.image = pygame.transform.scale(img, area)  # 이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()  # 이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.topleft = location  # 위치설정
        self.mask = pygame.mask.from_surface(self.image)  # 충돌감지를 위한 마스크생성

        self.time=time  # 상태가 유지되어 있을 시간
        self.frame_counter = self.time*s.FPS  # 0이 될때 상태 반전 상태유지
        self.invisible=False                #안보이면 true 보이면 false

    def state(self):
        self.frame_counter-=1
        if self.frame_counter<=0:
            self.invisible= not self.invisible
            self.frame_counter=self.time*s.FPS

    def collision(self, ball):
        '''벽과 충돌시의 행동'''
        #안보일시 충돌감지x
        if self.invisible:
            return 0

        # 벽의 아래 또는 윗면과 부딧혔을때
        # y좌표는 낮을수록 위이기에 ball이 더 작을 경우가 wall이 아래 있음
        if self.rect.top >= ball.get_center(1) - ball.get_speed(1):
            # 속도가 10이 넘을시 사망
            if ball.get_speed(1) > 10:
                return 1
            ball.speed_set_y(-s.MAX_SPEED)
        # wall의 좌표가 작을때 즉 더 위에 있을 경우
        elif self.rect.bottom <= ball.get_center(1) - ball.get_speed(1):
            if ball.get_speed(1) < 1:
                ball.speed_set_y(1)

        # 벽의 옆면과 부딪혔을때
        elif (self.rect.right <= ball.get_center(0) - ball.get_speed(0) and ball.get_speed(0) < 0) or (
                self.rect.left > ball.get_center(0) - ball.get_speed(0) and ball.get_speed(0) > 0):
            ball.set_dontchangespeed(10)  # 벽에 닿아서 튕겨 나올때 x축 속도를 못 바꾸게 하기위해서 사용(현재 10프레임동안 불가능)
            ball.reverse_speed_x()
            # 떨어질때 닿은 것이 아니라 올라갈때 닿으면 더 올라갈 수 있도록 y축 설정 (벽타기)
            if ball.get_speed_y() <= 0:
                ball.speed_set_y(-s.MAX_SPEED // 2)

        else:
            return 1

    def draw(self,background):
        #보일시만 출력
        if not self.invisible:
            background.blit(self.image,self.rect)

