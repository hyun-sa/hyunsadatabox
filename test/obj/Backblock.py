import pygame
'''재시작블록 대신 임시로 사용'''
class Backblock(pygame.sprite.Sprite):
    def __init__(self,img,location,area,start_loc):               #이미지,설치좌표(튜플로 전달),넓이와 높이를 튜플로 전달
        pygame.sprite.Sprite.__init__(self)             #스프라이트 초기화
        self.image= pygame.transform.scale(img,area)    #이미지의 크기를 내가 원하는 크기로 조정
        self.rect= self.image.get_rect()                #이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.topleft= location                      #위치설정
        self.mask=pygame.mask.from_surface(self.image)  #충돌감지를 위한 마스크생성
        self.start_loc=start_loc

    def Back(self,ball):
        ball.set_location(self.start_loc)