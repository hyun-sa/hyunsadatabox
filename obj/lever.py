import pygame
from obj import Wall,Ball

class block(Wall.Wall):
    def __init__(self, img, location, area):
        self.image_list=(pygame.transform.scale(img[0],area),pygame.transform.scale(img[1],area)) #(활설화이미지, 비활성화이미지)
        Wall.Wall.__init__(self,self.image_list[1],location,area)# 충돌감지를 위한 마스크생성시에 이미지가 바뀌어도 상관없는지 확인필요)

        self.state=True             #True시 활성 False시 비활성

    def change_state(self):
        '''상태 변경(ex:활성->비활성) 후 그에 맞는 이미지 입력'''
        self.state= not self.state
        self.image=self.image_list[self.state]

    def collision_check(self,ball):
        '''활성화 상태시만 충돌체크'''
        if(self.state):
            return self.collision(ball)
        return 0



class Lever(pygame.sprite.Sprite):
    def __init__(self,lever_img,block_img,lever_location,block_location,area):
        '''레버 이미지, 블록 켜짐 꺼짐 이미지(튜플), 레버위치(튜플로 이루어진 튜플),블록위치(튜플),면적(튜플)'''
        pygame.sprite.Sprite.__init__(self)             #스프라이트 초기화
        self.image= pygame.transform.scale(lever_img,area)    #이미지의 크기를 내가 원하는 크기로 조정
        self.rect= self.image.get_rect()                #이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.topleft= lever_location                     #위치설정
        self.mask=pygame.mask.from_surface(self.image)  #충돌감지를 위한 마스크생성

        self.block_list=pygame.sprite.Group()
        for b_loc in block_location:
            self.block_list.add(block(block_img,b_loc,area))

    def draw_block(self,background):
        self.block_list.draw(background)

    def collision(self,ball):
        '''벽과 충돌시의 행동'''
        #벽의 아래 또는 윗면과 부딧혔을때
        #y좌표는 낮을수록 위이기에 ball이 더 작을 경우가 wall이 아래 있음
        if self.rect.top >= ball.get_center(1) - ball.get_speed(1):
            #속도가 10이 넘을시 사망
            if ball.get_speed(1)>10:
                return 1
            ball.speed_set_y(-Ball.MAX_SPEED)
            #블럭 상태 반전
            for b in self.block_list:
                b.change_state()

        #wall의 좌표가 작을때 즉 더 위에 있을 경우
        elif self.rect.bottom<=ball.get_center(1)-ball.get_speed(1):
            if ball.get_speed(1)< 1:
                ball.speed_set_y(1)

        # 벽의 옆면과 부딪혔을때
        elif (self.rect.right <= ball.get_center(0)-ball.get_speed(0) and ball.get_speed(0) < 0) or (self.rect.left > ball.get_center(0)-ball.get_speed(0) and ball.get_speed(0) > 0):
            ball.set_dontchangespeed(10)  # 벽에 닿아서 튕겨 나올때 x축 속도를 못 바꾸게 하기위해서 사용(현재 10프레임동안 불가능)
            ball.reverse_speed_x()
            # 떨어질때 닿은 것이 아니라 올라갈때 닿으면 더 올라갈 수 있도록 y축 설정 (벽타기)
            if ball.get_speed_y() <= 0:
                ball.speed_set_y(-Ball.MAX_SPEED // 2)
        return 0