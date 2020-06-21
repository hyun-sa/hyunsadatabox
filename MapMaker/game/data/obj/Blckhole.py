from game.data.obj import Thorn


class Blackhole(Thorn.Thorn):
    '''충돌시 종료는 사실상 가시 블럭과 동일하지만 별도구현'''
    def __init__(self,img,location,area):               #이미지,설치좌표(튜플로 전달),넓이와 높이를 튜플로 전달
        Thorn.Thorn.__init__(self, img, location, area)


