#2019038026이혁수
from game.data.obj import Wall
from game.data.obj.Setting import setting as s


class Fakewall(Wall.Wall):      #Wall상속
    def __init__(self, img, location, area,time=7):        #이미지,설치좌표(튜플로 전달),넓이와 높이를 튜플로 전달,FPS
        Wall.Wall.__init__(self, img, location, area)      #상속 받은 wall초기화

        self.frame_counter=0                               #1이상일 경우 사라져 있음
        self.disappear_time = time                         #사라져있을시간

    def disappear(self,ball):
        '''사라지게함'''
        if self.rect.top >= ball.get_center(1) - ball.get_speed(1):
            self.frame_counter=s.FPS*self.disappear_time

    def isnotdisappear(self):
        '''출력전에 이것을 체크하고 반환된 값이 1일경우 출력 0일경우 출력 안해야함'''
        if self.frame_counter>0:
            self.frame_counter-=1
            return 0
        return 1

