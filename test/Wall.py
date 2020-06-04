#2019038026_이혁수
import pygame
import Ball

class Wall(pygame.sprite.Sprite):#스프라이트 상속
    def __init__(self,img,location,area):               #이미지,설치좌표(튜플로 전달),넓이와 높이를 튜플로 전달
        pygame.sprite.Sprite.__init__(self)             #스프라이트 초기화
        self.image= pygame.transform.scale(img,area)    #이미지의 크기를 내가 원하는 크기로 조정
        self.rect= self.image.get_rect()                #이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.center= location                      #위치설정
        self.mask=pygame.mask.from_surface(self.image)  #충돌감지를 위한 마스크생성

    def collision(self,ball):
        '''벽과 충돌시의 행동'''

        #벽의 아래 또는 윗면과 부딧혔을때
        #y좌표는 낮을수록 위이기에 ball이 더 작을 경우가 wall이 아래 있음
        if self.rect.top >= ball.rect.center[1] - ball.speed[1]:
            ball.speed[1] = -Ball.MAX_SPEED
        #wall의 좌표가 작을때 즉 더 위에 있을 경우
        elif self.rect.bottom<=ball.rect.center[1]-ball.speed[1]:
            ball.speed[1] = 1

        # 벽의 옆면과 부딪혔을때
        if (self.rect.right <= ball.rect.center[0] and ball.speed[0] < 0) or (self.rect.left > ball.rect.center[0] and ball.speed[0] > 0):
            ball.dontchangespeed = 10  # 벽에 닿아서 튕겨 나올때 x축 속도를 못 바꾸게 하기위해서 사용(현재 10프레임동안 불가능)
            ball.speed[0] = -ball.speed[0]
            # 떨어질때 닿은 것이 아니라 올라갈때 닿으면 더 올라갈 수 있도록 y축 설정 (벽타기)
            if ball.speed[1] <= 0:
                ball.speed[1] = -Ball.MAX_SPEED // 2


