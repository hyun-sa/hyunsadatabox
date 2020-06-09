import pygame
from obj import Wall
width=1920
height=1080
size = 40

'''포탈에 맞춰서 수정(레이저를 외부로 돌릴 수도 있음'''

class Layser(pygame.sprite.Sprite):
    img_size=((10,size),(size,10))
    def __init__(self,img,location,direction):
        pygame.sprite.Sprite.__init__(self)  # 스프라이트 초기화
        self.image = pygame.transform.scale(img, Layser.img_size[direction%2])  # 이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()  # 이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.center = location  # 위치설정
        self.mask = pygame.mask.from_surface(self.image)  # 충돌감지를 위한 마스크생성



    def Move(self,direction):
        '''방향에 따라 이동'''
        if direction==0:
            self.rect.centery=self.rect.centery-size
        elif direction==1:
            self.rect.centerx=self.rect.centerx+size
        elif direction==2:
            self.rect.centerx=self.rect.centery+size
        elif direction==3:
            self.rect.centerx=self.rect.centerx-size

        if self.rect.right < 0 or self.rect.left>width or self.rect.top>height or self.rect.bottom<0:
            return 1
        return 0




class Layserblock(Wall.Wall):
    def __init__(self,block_img,layser_img,location,area,obj,direction=1,FPS=60,time=5):
        '''블럭 이미지, 레이저 이미지, 위치(튜플),면적(튜플),(충돌 가능성이 있는 객체들 공제외 (리스트),방향:위(0),오른쪽(1),아래(2),왼쪽(3), FPS, 레이저가  나오고 안나오는 상태가 지속되는 시간'''
        Wall.Wall.__init__(self,block_img,location,area)
        self.layser_list=pygame.sprite.Group()
        self.layser_img=layser_img
        self.col_obj = obj

        self.term=FPS*time              # 상태가 위지되어 있을 프레임 수
        self.frame_counter = self.term  # 1이상일 경우 상태유지
        self.state = False              # True 일때 레이저 발사x False일때 발사
        self.direction=direction

        #레이저 생성 위치설정
        if self.direction==0:
            self.d=(self.rect.centerx,self.rect.centery-size)
        elif self.direction==1:
            self.d=(self.rect.centerx+size,self.rect.centery)
        elif self.direction==2:
            self.d=(self.rect.centerx,self.rect.centery+size)
        elif self.direction==3:
            self.d=(self.rect.centerx-size,self.rect.centery)

        def get_center(self, index=2):
            '''rect.center를 반환 인자로 0을 넣으면 x좌표가 1을 넣으면 y좌표가 반환 됨'''
            try:
                return self.rect.center[index]
            except IndexError:
                return self.rect.center

        def set_location(self, loc):
            self.rect.center = loc

    def layser(self):
        self.frame_counter -= 1
        if self.frame_counter <=0:
            self.state= not self.state
            self.frame_counter=self.term
            self.layser_list.empty()

        if self.state:
            return 0

        for layser in self.layser_list:
            if layser.Move(self.direction):
                self.layser_list.remove(layser)

        for obj in self.col_obj:
            collision_list = pygame.sprite.spritecollide(obj, self.layser_list, False, pygame.sprite.collide_mask)
            for layser in collision_list:
                self.layser_list.remove(layser)

        self.layser_list.add(Layser(self.layser_img,self.d,self.direction))     #레이저의 생성

    def draw_layser(self,background):
        self.layser_list.draw(background)





