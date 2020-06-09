#2019038026_이혁수
import pygame

MAX_SPEED=3     #최대 속도
def to_Zero(num):
    '''관성구현을 휘한 함수'''
    if num < 0:
        return 1
    elif num > 0:
        return -1
    else:
        return 0


class Ball(pygame.sprite.Sprite):
    def __init__(self, img, location, area,FPS=30):     # 이미지,설치좌표(튜플로 전달),넓이와 높이를 튜플로 전달  ex: (가로,세로),FPS
        pygame.sprite.Sprite.__init__(self)             #스프라이트 초기화
        self.image = pygame.transform.scale(img, area)  # 이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()               # 이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.topleft = location                     #위치 설정
        self.mask = pygame.mask.from_surface(self.image)#충돌감지를 위한 마스크 생성

        #함수내용 구현시 필요 한것
        self.gravity=MAX_SPEED/FPS                        #왕복하는데 걸리는 프레임
        self.speed=[0,0]                                    #공의 속도를 조정 [x,y]
        self.dontchangespeed=0                            # 좌우스피드 변경 불가능하게 하는 프레임수


    def move_y(self):
        '''y이동을 계산하는 함수로 y는 공기준으로 위가 - 아래가 +'''
        x,y=self.rect.center

        #속도변화
        self.speed[1]+=self.gravity

        #y이동
        y+=self.speed[1]
        self.rect.center=(x,y)      #좌표값변경



    def move_x(self,a):
        '''x를 이동 a는 가속도(속도 최대 값 있음)'''
        #x는 공기준으로 오른쪽이 + 왼쪽이 -
        x,y=self.rect.center

        #속도변화
        if a==0:
            self.speed[0]+=to_Zero(self.speed[0])
        else:
            self.speed[0] += a

            #최대 속도 제한
        if self.speed[0]<-MAX_SPEED:
            self.speed[0]=-MAX_SPEED

        elif self.speed[0]>MAX_SPEED:
            self.speed[0]=MAX_SPEED

        #x이동
        x += self.speed[0]
        self.rect.center=(x,y)      #좌표값변경


    def movex(self):
        '''x를 외부 요인 없이 그냥이동'''
        x,y=self.rect.center

        x += self.speed[0]

        self.rect.center = (x, y)  # 좌표값변경


    def move_check(self,key):
        '''어떻게 이동할 것인지 체크 후 이동'''
        if self.dontchangespeed==0:
            self.move_x(key)
        #x축 속도 변화 없음
        else:
            self.dontchangespeed-=1
            self.movex()

        self.move_y()

    def speed_set_y(self,s):
        '''y축 속도 변경'''
        self.speed[1]=s

    def speed_set_x(self,s):
        '''x축 속도 변경'''
        self.speed[0]=s

    def get_speed_x(self):
        '''y의 속도를 받아옴'''
        return self.speed[0]

    def get_speed_y(self):
        '''y의 속도를 받아옴'''
        return self.speed[1]

    def get_speed(self,index=2):
        '''speed를 반환 인자로 0을 넣으면 x의 속도가 1을 넣으면 y의 속도가 반환 됨'''
        try:
            return self.speed[index]
        except IndexError:
            return self.speed

    def set_dontchangespeed(self,num):
        '''몇프레임 동안 못움직이게 하는지 체크하는 변수의 값변경'''
        self.dontchangespeed=num

    def reverse_speed_x(self):
        '''x축의 속도를 뒤집음(즉, 방향을 바꿈)'''
        self.speed[0]=-self.speed[0]

    def reverse_speed_y(self):
        '''y축의 속도를 뒤집음(즉, 방향을 바꿈)'''
        self.speed[1]=-self.speed[1]

    def get_center(self,index=2):
        '''rect.center를 반환 인자로 0을 넣으면 x좌표가 1을 넣으면 y좌표가 반환 됨'''
        try:
            return self.rect.center[index]
        except IndexError:
            return self.rect.center

    def set_location(self,loc):
        self.rect.center=loc