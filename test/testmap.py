#2019038026_이혁수
import pygame
import Wall
import Star
import Ball
import Fakewall
import Spring
import Thorn
import Magnetic
import Backblock
import Blckhole
import iccle


import time
import Map
import Movewall
img=['wall','star','setting','Exit',"thorn"]#이미지 이름


def map(screen):#스크린을 전달받음
    done = 1
    FPS = 60        #프레임
    key = 0         #공의 이동 방향 0이 바뀌지 않음 1이 오른쪽, -1이 왼쪽

    wall_list=pygame.sprite.Group()              #벽들을 모아둘 그룹
    fakewall_list=pygame.sprite.Group()          #fakewall들을 모아둘 그룹
    fakewall_disappear_list=pygame.sprite.Group()#사라진 fakewall들을 모아둘 그룹
    spring_list=pygame.sprite.Group()
    movewall_list=pygame.sprite.Group()
    thorn_list=pygame.sprite.Group()
    magnetic_list=pygame.sprite.Group()
    backblock_list=pygame.sprite.Group()
    Blckhole_list=pygame.sprite.Group()
    iccle_list=pygame.sprite.Group()
    iccle_disappear_list = pygame.sprite.Group()  # 사라진 iccle들을 모아둘 그룹


    background= pygame.Surface(screen.get_size())#스크린과 동일크기의 surface생성 이곳에 그린후 스크린에 복사
    clock=pygame.time.Clock()                    #프레임 설정시 사용

    #이미지를 불러와서 리스트에 저장
    image_list=[]
    for i in img:
        image_list.append(pygame.image.load("image/{}.png".format(i)).convert_alpha())


    star=Star.Star(image_list[1],(10,250),(50,50))

    ball=Ball.Ball(image_list[2],(400,900),(25,15))

    wall_list.add(Wall.Wall(image_list[0],(400,1000),(2000,150)))
    wall_list.add(Wall.Wall(image_list[0], (10, 800), (150, 1000)))
    wall_list.add(Wall.Wall(image_list[0], (230, 400), (150, 1000)))
    wall_list.add(Wall.Wall(image_list[0], (800, 800), (150, 1000)))

    fakewall_list.add(Fakewall.Fakewall(image_list[0], (500, 900), (30, 30),FPS))
    spring_list.add(Spring.Spring(image_list[3],(550,900),(30,30)))
    movewall_list.add(Movewall.Movewall(image_list[0],(550,800),(30,30),(100,100),FPS))

    thorn_list.add(Thorn.Thorn(image_list[4],(600,900),(30,30)))
    magnetic_list.add(Magnetic.Magnetic(image_list[3],(450,900),(30,30)))
    backblock_list.add(Backblock.Backblock(image_list[2],(550,700),(30,30),(400,900)))
    Blckhole_list.add(Blckhole.Blackhole(image_list[1],(650,850),(50,50)))
    #iccle_list.add(iccle.Iccle(image_list[0], (500, 700), (30, 30),,FPS))



    while done:
        clock.tick(FPS)     #프레임 설정

        #이벤트 받아오기
        event = pygame.event.get()
        for e in event:
            if e.type == pygame.MOUSEBUTTONDOWN:
                return 0
            #키보드 누름
            if e.type ==pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    key-=1
                elif e.key ==pygame.K_RIGHT:
                    key+=1
            #키보드 뗌
            if e.type ==pygame.KEYUP:
                if e.key == pygame.K_LEFT:
                    key+=1
                elif e.key ==pygame.K_RIGHT:
                    key-=1

        # 공이동
        ball.move_check(key)

        #벽과충돌
        collision_list = pygame.sprite.spritecollide(ball, wall_list, False, pygame.sprite.collide_mask)
        for wall in collision_list:
            wall.collision(ball)

        #기시와 충돌시 게임 오버
        collision_list = pygame.sprite.spritecollide(ball, thorn_list, False, pygame.sprite.collide_mask)
        for thorn in collision_list:
            return 0

        # 블랙홀과 충돌시 게임 오버
        collision_list = pygame.sprite.spritecollide(ball, Blckhole_list, False, pygame.sprite.collide_mask)
        for black in collision_list:
            return 0

        #자석블록과 충돌
        collision_list = pygame.sprite.spritecollide(ball, magnetic_list, False, pygame.sprite.collide_mask)
        for mag in collision_list:
            mag.collision(ball)

        # back블록과 충돌
        collision_list = pygame.sprite.spritecollide(ball, backblock_list, False, pygame.sprite.collide_mask)
        for back in collision_list:
           back.Back(ball)

        #fakewall과 충돌
        collision_list =pygame.sprite.spritecollide(ball,fakewall_list,True,pygame.sprite.collide_mask)
        for fake in collision_list:
            fake.collision(ball)
            fake.disappear(ball)
            fakewall_disappear_list.add(fake)
        #fakewall 재생성 확인
        for fake in fakewall_disappear_list:
            if fake.isnotdisappear():
                fakewall_disappear_list.remove(fake)
                fakewall_list.add(fake)

        #스프링과 충돌
        collision_list=pygame.sprite.spritecollide(ball,spring_list,False,pygame.sprite.collide_mask)
        for spring in collision_list:
            spring.spring(ball)

        # 이동체크
        for movewall in movewall_list:
            movewall.Move()
        #movewall충돌체크
        collision_list = pygame.sprite.spritecollide(ball, movewall_list, False, pygame.sprite.collide_mask)
        for movewall in collision_list:
            movewall.collision(ball)

        '''#공과충돌
        collision_list = pygame.sprite.spritecollide(ball, iccle_list, False, pygame.sprite.collide_mask)
        for ice in collision_list:
            return 0
        #이동
        for ice in iccle_list:
            ice.move()'''





        #클리어 체크
        if(pygame.sprite.collide_mask(ball,star)):
            done = 0

        #백르라운드에 그리기
        background.fill((255,255,255))                #그려진거 비우기
        background.blit(star.image, star.rect)
        background.blit(ball.image, ball.rect)
        wall_list.draw(background)
        fakewall_list.draw(background)
        spring_list.draw(background)
        movewall_list.draw(background)
        thorn_list.draw(background)
        magnetic_list.draw(background)
        backblock_list.draw(background)
        Blckhole_list.draw(background)
        #스크린에 그리고 새로고침
        screen.blit(background,(0,0))
        pygame.display.flip()

    else:
        print("클리어")
        return 0
