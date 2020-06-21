import pygame
from game.data.obj.Setting import setting as s
'''텔레포트 될곳에 객체가 있을경우 겹쳐지는 오류발생'''

class subpotal(pygame.sprite.Sprite):
    def __init__(self, img, location, area, obj,potal):  # 이미지,설치좌표(튜플로 전달),넓이와 높이를 튜플로 전달
        pygame.sprite.Sprite.__init__(self)  # 스프라이트 초기화
        self.image = pygame.transform.scale(img, area)  # 이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()  # 이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.topleft = location  # 위치설정
        self.mask = pygame.mask.from_surface(self.image)  # 충돌감지를 위한 마스크생성

        self.potal=potal
        self.col_obj=obj

    def teleport(self,ball):

        if(pygame.sprite.collide_mask(ball,self)):
            ball.set_location(self.potal.rect.center)
            return 1

        for obj in self.col_obj:
            if (pygame.sprite.collide_mask(obj, self)):
                loc = list(self.potal.rect.center)
                # 어디서 충돌했는지 확인
                if obj.get_center(0) < self.rect.left:
                    loc[0] += s.size
                elif obj.get_center(0) > self.rect.right:
                    loc[0] -= s.size
                if obj.get_center(1) < self.rect.top:
                    loc[1] += s.size
                elif obj.get_center(1) > self.rect.bottom:
                    loc[1] -= s.size
                obj.set_location(loc)
        return 0


class Potal(pygame.sprite.Sprite):
    def __init__(self, img1,img2, location1,location2, area,obj=[],group=[]):
        '''블럭 이미지1,2, 위치(튜플)1,2,면적(튜플),충돌 가능성이 있는 객체들 공제외 (리스트),충돌가능성이 있는 그룹들 (리스트)'''
        pygame.sprite.Sprite.__init__(self)  # 스프라이트 초기화
        self.image = pygame.transform.scale(img1, area)  # 이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()  # 이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.topleft = location1  # 위치설정
        self.mask = pygame.mask.from_surface(self.image)  # 충돌감지를 위한 마스크생성


        self.potal=subpotal(img2,location2,area,obj,self)
        self.col_obj=obj
        self.col_group=group


    def draw_portal(self,background):
        background.blit(self.image,self.rect)
        background.blit(self.potal.image,self.potal.rect)

    def teleport(self,ball):
        '''이동할 곳에  다른 객체가 존재할 경우 겹쳐지는 문제 발생'''
        if(pygame.sprite.collide_mask(ball,self)):
            ball.set_location(self.potal.rect.center)
            return 1

        for obj in self.col_obj:
            if (pygame.sprite.collide_mask(obj, self)):
                loc = list(self.potal.rect.center)
                # 어디서 충돌했는지 확인
                if obj.get_center(0) < self.rect.left:
                    loc[0] += s.size
                elif obj.get_center(0) > self.rect.right:
                    loc[0] -= s.size
                if obj.get_center(1) < self.rect.top:
                    loc[1] += s.size
                elif obj.get_center(1) > self.rect.bottom:
                    loc[1] -= s.size
                obj.set_location(loc)

        for group in self.col_group:
            col_list=pygame.sprite.spritecollide(self, group.get_subgroup(), False, pygame.sprite.collide_mask)
            for obj in col_list:
                loc = list(self.potal.rect.center)
                # 어디서 충돌했는지 확인
                if obj.get_center(0) < self.rect.left:
                    loc[0] += s.size
                elif obj.get_center(0) > self.rect.right:
                    loc[0] -= s.size
                if obj.get_center(1) < self.rect.top:
                    loc[1] += s.size
                elif obj.get_center(1) > self.rect.bottom:
                    loc[1] -= s.size
                obj.set_location(loc)

        return self.potal.teleport(ball)

    def set_collision_obj(self,obj_list):
        self.col_obj=obj_list
    def set_collision_group(self,group_list):
        self.col_group=group_list

    def collision_check(self):
        if not self.col_obj or not self.col_group:
            return -1
        return 0

