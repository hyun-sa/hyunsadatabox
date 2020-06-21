#2019038026_이혁수
import pygame
import LoadMap
from game.data.obj import Magnetic, Backblock, Star, Movewall,  Spring, Fakewall, Thorn, Ball, Wall, iccle,Laser,lever,potal,Cannon
from game.data.obj.Setting import setting

img=['wall','star','setting','Exit',"thorn","Help"]#이미지 이름
exit = -2
die=-1
win=1

battery_0 = pygame.image.load("game/image/Battery_0.png")
battery_1 = pygame.image.load("game/image/Battery_1.png")
battery_2 = pygame.image.load("game/image/Battery_2.png")
battery_3 = pygame.image.load("game/image/Battery_3.png")
battery_4 = pygame.image.load("game/image/Battery_4.png")


def menu():
    print("메뉴")
    return 1

def Map(screen, Life, map_):#스크린을 전달받음
    done = 1
    FPS=setting.FPS
    key = 0         #공의 이동 방향 0이 바뀌지 않음 1이 오른쪽, -1이 왼쪽


    background= pygame.Surface(screen.get_size())#스크린과 동일크기의 surface생성 이곳에 그린후 스크린에 복사
    clock=pygame.time.Clock()                    #프레임 설정시 사용

    #list_collection = [backblock_list, ball, blckhole_list, fakewal_list, magnetic_list, movewal_list, star, thorn_list, wall_list\
    #        ,spring_list, icicle_list, laser_list, blinkblock_list, lever_list, portal_list, cannon_list]
    list_collection = LoadMap.loadmap(screen, map_) ################맵 이름 매개변수로 지정할 수 있음 default = 'map.txt'
    restart_list = list_collection[0]
    ball = list_collection[1]
    Blckhole_list = list_collection[2]
    fakewall_list = list_collection[3]
    fakewall_disappear_list = pygame.sprite.Group()  # 사라진 fakewall들을 모아둘 그룹
    magnetic_list = list_collection[4]
    movewall_list = list_collection[5]
    star = list_collection[6]
    thorn_list = list_collection[7]
    wall_list = list_collection[8]
    setting.wall=wall_list
    spring_list = list_collection[9]
    iccle_list = list_collection[10]
    iccle_disappear_list = pygame.sprite.Group()  # 사라진 iccle들을 모아둘 그룹
    laser_list = list_collection[11]
    blinkblock_list = list_collection[12]
    lever_list = list_collection[13]
    portal_list = list_collection[14]
    cannon_list = list_collection[15]

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        key-=1
    if keys[pygame.K_RIGHT]:
        key+=1

    while done:
        clock.tick(FPS)     #프레임 설정
        #이벤트 받아오기
        event = pygame.event.get()
        for e in event:

            #키보드 누름
            if e.type ==pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    key-=1
                elif e.key ==pygame.K_RIGHT:
                    key+=1
                elif e.key == pygame.K_ESCAPE:
                    if menu():
                        return exit
            #키보드 뗌
            if e.type ==pygame.KEYUP:
                if e.key == pygame.K_LEFT:
                    key+=1
                elif e.key ==pygame.K_RIGHT:
                    key-=1

        # 공이동
        if ball.move_check(key):
            return die

        #벽과충돌
        collision_list = pygame.sprite.spritecollide(ball, wall_list, False, pygame.sprite.collide_mask)
        for wall in collision_list:
            if wall.collision(ball):
                return die

        #기시와 충돌시 게임 오버
        collision_list = pygame.sprite.spritecollide(ball, thorn_list, False, pygame.sprite.collide_mask)
        for thorn in collision_list:
            return die

        # 블랙홀과 충돌시 게임 오버
        collision_list = pygame.sprite.spritecollide(ball, Blckhole_list, False, pygame.sprite.collide_mask)
        for black in collision_list:
            return die

        #자석블록과 충돌
        collision_list = pygame.sprite.spritecollide(ball, magnetic_list, False, pygame.sprite.collide_mask)
        for mag in collision_list:
            if mag.collision(ball):
                return die

        # 재시작블록과 충돌
        collision_list = pygame.sprite.spritecollide(ball, restart_list, False, pygame.sprite.collide_mask)
        for re in collision_list:
           return 0

        #fakewall과 충돌
        collision_list =pygame.sprite.spritecollide(ball,fakewall_list,True,pygame.sprite.collide_mask)
        for fake in collision_list:
            if fake.collision(ball):
                return die
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
            if spring.spring(ball):
                return die

        # 이동체크
        for movewall in movewall_list:
            movewall.Move()
        #movewall충돌체크
        collision_list = pygame.sprite.spritecollide(ball, movewall_list, False, pygame.sprite.collide_mask)
        for movewall in collision_list:
            if movewall.collision(ball):
                return die

        #고드름
        #공과충돌
        collision_list = pygame.sprite.spritecollide(ball, iccle_list, False, pygame.sprite.collide_mask)
        for ice in collision_list:
            return die
        #이동
        for ice in iccle_list:
            if ice.move():
                ice.disappear()
                iccle_list.remove(ice)
                iccle_disappear_list.add(ice)
        for ice in iccle_disappear_list:
            if ice.isnotdisappear():
                iccle_disappear_list.remove(ice)
                iccle_list.add(ice)

        #레이저 블럭
        for layblock in laser_list:
            layblock.layser()
            #레이저와 충돌
            collision_list = pygame.sprite.spritecollide(ball, layblock.get_subgroup(), False, pygame.sprite.collide_mask)
            for l in collision_list:
                return die
        collision_list = pygame.sprite.spritecollide(ball, laser_list, False, pygame.sprite.collide_mask)
        for layblock in collision_list:
            if layblock.collision(ball):
                return die

        #레버블럭
        collision_list = pygame.sprite.spritecollide(ball, lever_list, False, pygame.sprite.collide_mask)
        for l in collision_list:
            if l.collision(ball):
                return die
        for l in lever_list:
            collision_list = pygame.sprite.spritecollide(ball, l.block_list, False, pygame.sprite.collide_mask)
            for l in collision_list:
                if l.collision_check(ball):
                    return die

        #포탈
        for p in portal_list:
            if p.teleport(ball):
                portal_list.remove(p)

        #대포
        for c in cannon_list:
            c.shoot()
            #대포알과 충돌
            collision_list = pygame.sprite.spritecollide(ball, c.get_subgroup(), False, pygame.sprite.collide_mask)
            for l in collision_list:
                return die
        collision_list = pygame.sprite.spritecollide(ball, cannon_list, False, pygame.sprite.collide_mask)
        for cannon in collision_list:
            if cannon.collision(ball):
                return die

        #깜빡이는 블럭
        for b in blinkblock_list:
            b.state()
        collision_list = pygame.sprite.spritecollide(ball, blinkblock_list, False, pygame.sprite.collide_mask)
        for b in collision_list:
            if b.collision(ball):
                return die





        #클리어 체크
        if(pygame.sprite.collide_mask(ball,star)):
            done = 0

        #백르라운드에 그리기
        background.fill((255,255,255))                #그려진거 비우기
        background.blit(star.image, star.rect)
        background.blit(ball.image, ball.rect)
        fakewall_list.draw(background)
        spring_list.draw(background)
        movewall_list.draw(background)
        thorn_list.draw(background)
        magnetic_list.draw(background)
        restart_list.draw(background)
        Blckhole_list.draw(background)
        iccle_list.draw(background)
        laser_list.draw(background)
        for l in laser_list:
            l.draw_layser(background)
        lever_list.draw(background)
        for l in lever_list:
            l.draw_block(background)
        for p in portal_list:
            p.draw_portal(background) #이걸로 포탈을 둘다 그림
        cannon_list.draw(background)
        for c in cannon_list:
            c.draw_shell(background)

        wall_list.draw(background)
        for b in blinkblock_list:
            b.draw(background)
        if Life == 0:
            background.blit(battery_0, (20, 10))
        elif Life == 1:
            background.blit(battery_1, (20, 10))
        elif Life == 2:
            background.blit(battery_2, (20, 10))
        elif Life == 3:
            background.blit(battery_3, (20, 10))
        elif Life == 4:
            background.blit(battery_4, (20, 10))

        #스크린에 그리고 새로고침
        screen.blit(background,(0,0))
        pygame.display.flip()

    else:
        return win
