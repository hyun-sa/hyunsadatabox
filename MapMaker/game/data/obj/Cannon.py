import pygame
from game.data.obj import Wall
from game.data.obj.Setting import setting as s

class Shell(pygame.sprite.Sprite):
    def __init__(self, img, location, direction,speed):
        pygame.sprite.Sprite.__init__(self)  # 스프라이트 초기화
        self.image = pygame.transform.scale(img, (10,10))  # 이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()  # 이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.center = location  # 위치설정
        self.mask = pygame.mask.from_surface(self.image)  # 충돌감지를 위한 마스크생성

        self.direction = direction
        self.speed=speed

    def Move(self):
        '''방향에 따라 이동'''
        if self.direction==0:
            self.rect.centery=self.rect.centery-self.speed*s.time_adjustment
        elif self.direction==1:
            self.rect.centerx=self.rect.centerx+self.speed*s.time_adjustment
        elif self.direction==2:
            self.rect.centerx=self.rect.centery+self.speed*s.time_adjustment
        elif self.direction==3:
            self.rect.centerx=self.rect.centerx-self.speed*s.time_adjustment

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

class Cannon(Wall.Wall):
    def __init__(self,cannon_img,shell_img,location,area,direction=1,time=2,speed=4):
        '''블럭 이미지, 대포알 이미지, 위치(튜플),면적(튜플),방향:위(0),오른쪽(1),아래(2),왼쪽(3), FPS, 포탄발사 시간,스피드,속도'''
        Wall.Wall.__init__(self,cannon_img,location,area)
        self.shell_list=pygame.sprite.Group()
        self.shell_img=shell_img

        self.time=time              # 상태가 유지되어 있을 프레임 수
        self.frame_counter = self.time*s.FPS  # 0보다 클 경우 상태유지
        self.direction=direction
        self.speed=speed

        # 포탄 생성 위치설정
        if self.direction == 0:
            self.d = self.rect.midtop
        elif self.direction == 1:
            self.d = self.rect.midright
        elif self.direction == 2:
            self.d = self.rect.midbottom
        elif self.direction == 3:
            self.d = self.rect.midleft

    def shoot(self):
        self.frame_counter -= 1
        if self.frame_counter <= 0:
            self.frame_counter=s.FPS*self.time
            self.shell_list.add(Shell(self.shell_img, self.d, self.direction,self.speed))  # 대포 발사

        for sh in self.shell_list:
            if sh.Move():
                self.shell_list.remove(sh)

        pygame.sprite.groupcollide(s.wall, self.shell_list, False,True, pygame.sprite.collide_mask)

    def draw_shell(self,background):
        self.shell_list.draw(background)

    def get_subgroup(self):
        return self.shell_list

    def set_collision(self,obj_list):
        self.col_obj=obj_list

    def collision_check(self):
        if not self.col_obj:
            return -1
        return 0