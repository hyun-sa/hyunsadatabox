import pygame
from game.data.obj import Wall
from game.data.obj.Setting import setting as s

'''포탈에 맞춰서 수정(레이저를 외부로 돌릴 수도 있음'''


class Layser(pygame.sprite.Sprite):
    img_size=((10,s.size),(s.size,10))
    def __init__(self,img,location,direction):
        pygame.sprite.Sprite.__init__(self)  # 스프라이트 초기화
        self.image = pygame.transform.scale(img, Layser.img_size[direction%2])  # 이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()  # 이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.center = location  # 위치설정
        self.mask = pygame.mask.from_surface(self.image)  # 충돌감지를 위한 마스크생성

        self.direction=direction


    def Move(self):
        '''방향에 따라 이동'''
        if self.direction==0:
            self.rect.centery=self.rect.centery-s.size
        elif self.direction==1:
            self.rect.centerx=self.rect.centerx+s.size
        elif self.direction==2:
            self.rect.centerx=self.rect.centery+s.size
        elif self.direction==3:
            self.rect.centerx=self.rect.centerx-s.size

        if self.rect.right < 0 or self.rect.left>s.width or self.rect.top>s.height or self.rect.bottom<0:
            return 1
        return 0

    def set_location(self, loc):
        self.rect.center = loc

    def get_center(self, index=2):
        '''rect.center를 반환 인자로 0을 넣으면 x좌표가 1을 넣으면 y좌표가 반환 됨'''
        try:
            return self.rect.center[index]
        except IndexError:
            return self.rect.center


class Layserblock(Wall.Wall):
    def __init__(self,block_img,layser_img,location,area,direction=1,time=5):
        '''블럭 이미지, 레이저 이미지, 위치(튜플),면적(튜플),방향:위(0),오른쪽(1),아래(2),왼쪽(3), FPS, 레이저가  나오고 안나오는 상태가 지속되는 시간'''
        Wall.Wall.__init__(self,block_img,location,area)
        self.layser_list=pygame.sprite.Group()
        self.layser_img=layser_img

        self.time=time
        self.frame_counter = s.FPS*self.time  # 1이상일 경우 상태유지
        self.state = False              # True 일때 레이저 발사x False일때 발사
        self.direction=direction
        self.shoot = self.state         #렉을 줄이기 위해 추가

        #레이저 생성 위치설정
        if self.direction==0:
            self.d=(self.rect.centerx,self.rect.centery-s.size)
        elif self.direction==1:
            self.d=(self.rect.centerx+s.size,self.rect.centery)
        elif self.direction==2:
            self.d=(self.rect.centerx,self.rect.centery+s.size)
        elif self.direction==3:
            self.d=(self.rect.centerx-s.size,self.rect.centery)

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
            self.shoot=self.state                #렉을 줄이기 위해추가
            self.frame_counter=s.FPS*self.time
            self.layser_list.empty()

        if self.state:
            return 0

        if not self.shoot :
            for layser in self.layser_list:
                if layser.Move():
                    self.layser_list.remove(layser)
                    self.shoot=True

            if pygame.sprite.groupcollide(s.wall, self.layser_list, False,True, pygame.sprite.collide_mask):
                self.shoot=True
            self.layser_list.add(Layser(self.layser_img,self.d,self.direction))     #레이저의 생성

    def draw_layser(self,background):
        self.layser_list.draw(background)

    def get_subgroup(self):
        return  self.layser_list

    def set_collision(self,obj_list):
        self.col_obj=obj_list

    def collision_check(self):
        if not self.col_obj:
            return -1
        return 0




