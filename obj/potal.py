import pygame
from obj import subpotal
size=40
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
            loc=list(self.potal.rect.center)
            #어디서 충ehf했는지 확인
            if ball.get_center(0)<self.rect.left:
                loc[0]+=size
            elif ball.get_center(0)>self.rect.right:
                loc[0] -= size
            if ball.get_center(1)<self.rect.top:
                loc[1]+=size
            elif ball.get_center(1)>self.rect.bottom:
                loc[1] -= size
            ball.set_location(loc)

        for obj in self.col_obj:
            if (pygame.sprite.collide_mask(obj, self)):
                loc = list(self.potal.rect.center)
                # 어디서 충돌했는지 확인
                if obj.get_center(0) < self.rect.left:
                    loc[0] += size
                elif obj.get_center(0) > self.rect.right:
                    loc[0] -= size
                if obj.get_center(1) < self.rect.top:
                    loc[1] += size
                elif obj.get_center(1) > self.rect.bottom:
                    loc[1] -= size
                obj.set_location(loc)


class Potal(pygame.sprite.Sprite):
    def __init__(self, img1,img2, location1,location2, area,obj):
        '''블럭 이미지1,2, 위치(튜플)1,2,면적(튜플),충돌 가능성이 있는 객체들 공제외 (리스트)'''
        pygame.sprite.Sprite.__init__(self)  # 스프라이트 초기화
        self.image = pygame.transform.scale(img1, area)  # 이미지의 크기를 내가 원하는 크기로 조정
        self.rect = self.image.get_rect()  # 이미지의 사각형에 해당하는 범위를 가져옴
        self.rect.topleft = location1  # 위치설정
        self.mask = pygame.mask.from_surface(self.image)  # 충돌감지를 위한 마스크생성

        self.potal=subpotal(img2,location2,area,obj,self)
        self.col_obj=obj

    def return_subpotal(self):
        return self.potal

    def draw_potal(self,background):
        background.blit(self.potal.image,self.potal.rect)

    def teleport(self,ball):
        if(pygame.sprite.collide_mask(ball,self)):
            loc=list(self.potal.rect.center)
            #어디서 충ehf했는지 확인
            if ball.get_center(0)<self.rect.left:
                loc[0]+=size
            elif ball.get_center(0)>self.rect.right:
                loc[0] -= size
            if ball.get_center(1)<self.rect.top:
                loc[1]+=size
            elif ball.get_center(1)>self.rect.bottom:
                loc[1] -= size
            ball.set_location(loc)

        for obj in self.col_obj:
            if (pygame.sprite.collide_mask(obj, self)):
                loc = list(self.potal.rect.center)
                # 어디서 충도했는지 확인
                if obj.get_center(0) < self.rect.left:
                    loc[0] += size
                elif obj.get_center(0) > self.rect.right:
                    loc[0] -= size
                if obj.get_center(1) < self.rect.top:
                    loc[1] += size
                elif obj.get_center(1) > self.rect.bottom:
                    loc[1] -= size
                obj.set_location(loc)


