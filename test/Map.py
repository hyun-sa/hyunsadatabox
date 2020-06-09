import pygame
import Ball,Wall,Star,Spring,Thorn,Fakewall

def Wall_check(ball,wall_Group):
    collision_list = pygame.sprite.spritecollide(ball, wall_Group, False, pygame.sprite.collide_mask)
    for wall in collision_list:
        wall.collision(ball)

def Spring_check(ball,spring_list):
    collision_list = pygame.sprite.spritecollide(ball, spring_list, False, pygame.sprite.collide_mask)
    for spring in collision_list:
        spring.spring(ball)






class Map():
    __object_Func={"Wall": Wall_check,"Spring":Spring_check}
    def __init__(self,screen,ball_img,star_img,ball_loc,FPS):
        self.screen=screen
        self.object_group={}
        self.ball=Ball.Ball(ball_img,ball_loc,(25,25),FPS)
        self.key=0
        self.background = pygame.Surface(screen.get_size())  # 스크린과 동일크기의 surface생성 이곳에 그린후 스크린에 복사
        self.star = Star.Star(star_img, (10, 250), (50, 50))#수정필요

    def add_object(self,obj_name,obj):
        ''' 맵에 오브젝트를 추가 인자: 오브젝트 이름(ex: wall),오브젝트 객체(*이름은 고정)'''
        try:
            self.object_group[obj_name].add(obj)
        except KeyError:
            self.object_group[obj_name]=pygame.sprite.Group(obj)
            #fakewall일시 수정

    def check_obj(self):

        event = pygame.event.get()
        for e in event:
            if e.type == pygame.MOUSEBUTTONDOWN:
                return 0
            # 키보드 누름
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    self.key -= 1
                elif e.key == pygame.K_RIGHT:
                    self.key += 1
            # 키보드 뗌
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT:
                    self.key += 1
                elif e.key == pygame.K_RIGHT:
                    self.key -= 1

        for obj_name in self.object_group.keys():
            Map.__object_Func[obj_name](self.ball,self.object_group[obj_name])

        self.ball.move_check(self.key)

        # 백르라운드에 그리기
        self.background.fill((255, 255, 255))  # 그려진거 비우기
        self.background.blit(self.star.image, self.star.rect)
        self.background.blit(self.ball.image, self.ball.rect)
        for obj_name in self.object_group.keys():
            self.object_group[obj_name].draw(self.background)
        # 스크린에 그리고 새로고침
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        if (pygame.sprite.collide_mask(self.ball, self.star)):
            return 0

        return 1












