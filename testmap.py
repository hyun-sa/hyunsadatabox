#2019038026_이혁수
import pygame
from obj import Magnetic, Backblock, Star, Movewall, Blckhole, Spring, Fakewall, Thorn, Ball, Wall, iccle,Laser,lever,potal

img=['wall','star','setting','Exit',"thorn","Help"]#이미지 이름


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
    restart_list=pygame.sprite.Group()
    Blckhole_list=pygame.sprite.Group()
    iccle_list=pygame.sprite.Group()
    iccle_disappear_list = pygame.sprite.Group()  # 사라진 iccle들을 모아둘 그룹
    Laser_list=pygame.sprite.Group()
    lever_list=pygame.sprite.Group()
    potal_list=pygame.sprite.Group()


    background= pygame.Surface(screen.get_size())#스크린과 동일크기의 surface생성 이곳에 그린후 스크린에 복사
    clock=pygame.time.Clock()                    #프레임 설정시 사용

    #이미지를 불러와서 리스트에 저장
    image_list=[]
    for i in img:
        image_list.append(pygame.image.load("image/{}.png".format(i)).convert_alpha())


    star= Star.Star(image_list[1], (10, 110), (50, 50))

    ball= Ball.Ball(image_list[2], (400, 900), (25, 15))

    #이부분은 일단 고드름을 위해서 이렇게 해 논것으로 재량껏 수정
    wall=Wall.Wall(image_list[0], (0, 1000), (2000, 150))
    movewall=Movewall.Movewall(image_list[0], (550, 850), (30, 30), (100, 100), FPS)
    #그룹에 추가
    wall_list.add(wall)
    wall_list.add(Wall.Wall(image_list[0], (0, 200), (150, 1000)))
    wall_list.add(Wall.Wall(image_list[0], (210, 50), (150, 900)))
    wall2=Wall.Wall(image_list[0], (1500, 200), (150, 1000))
    wall_list.add(wall2)

    fakewall_list.add(Fakewall.Fakewall(image_list[0], (500, 950), (30, 30), FPS))
    spring_list.add(Spring.Spring(image_list[3], (550, 950), (30, 30)))
    movewall_list.add(movewall)

    thorn_list.add(Thorn.Thorn(image_list[4], (600, 950), (30, 30)))
    magnetic_list.add(Magnetic.Magnetic(image_list[3], (450, 950), (30, 30)))
    restart_list.add(Backblock.Backblock(image_list[2], (550, 850), (30, 30), (400, 900)))
    Blckhole_list.add(Blckhole.Blackhole(image_list[1], (650, 900), (50, 50)))
    iccle_list.add(iccle.Iccle(image_list[0], (500, 700), (30, 30),[wall,movewall],FPS))#fakewall은 넣지 않음
    Laser_list.add(Laser.Layserblock(image_list[3],image_list[0],(800,950),(30,30),[wall2,wall],0))

    lever_list.add(lever.Lever(image_list[3],(image_list[5],image_list[0]),(450,950),[(350,950)],(30,30)))

    potal_list.add(potal.Potal(image_list[2],image_list[2],(900,950),(1000,800),(30,30),[]))



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
            if wall.collision(ball):
                return 0

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
            if mag.collision(ball):
                return 0

        # 재시작블록과 충돌 (버그 존재 나중에 수정)
        collision_list = pygame.sprite.spritecollide(ball, restart_list, False, pygame.sprite.collide_mask)
        for re in collision_list:
           return 1

        #fakewall과 충돌
        collision_list =pygame.sprite.spritecollide(ball,fakewall_list,True,pygame.sprite.collide_mask)
        for fake in collision_list:
            if fake.collision(ball):
                return 0
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
                return 0

        # 이동체크
        for movewall in movewall_list:
            movewall.Move()
        #movewall충돌체크
        collision_list = pygame.sprite.spritecollide(ball, movewall_list, False, pygame.sprite.collide_mask)
        for movewall in collision_list:
            if movewall.collision(ball):
                return 0

        #고드름
        #공과충돌
        collision_list = pygame.sprite.spritecollide(ball, iccle_list, False, pygame.sprite.collide_mask)
        for ice in collision_list:
            return 0
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
        for layblock in Laser_list:
            layblock.layser()
            #레이저와 충돌
            collision_list = pygame.sprite.spritecollide(ball, layblock.layser_list, False, pygame.sprite.collide_mask)
            for l in collision_list:
                return 0
        collision_list = pygame.sprite.spritecollide(ball, Laser_list, False, pygame.sprite.collide_mask)
        for layblock in collision_list:
            if layblock.collision(ball):
                return 0

        #레버블럭
        collision_list = pygame.sprite.spritecollide(ball, lever_list, False, pygame.sprite.collide_mask)
        for l in collision_list:
            if l.collision(ball):
                return 0
        for l in lever_list:
            collision_list = pygame.sprite.spritecollide(ball, l.block_list, False, pygame.sprite.collide_mask)
            for l in collision_list:
                if l.collision_check(ball):
                    return 0

        #포탈
        for p in potal_list:
            p.teleport(ball)
            p.return_subpotal().teleport(ball)









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
        restart_list.draw(background)
        Blckhole_list.draw(background)
        iccle_list.draw(background)
        Laser_list.draw(background)
        for l in Laser_list:
            l.draw_layser(background)
        lever_list.draw(background)
        for l in lever_list:
            l.draw_block(background)
        potal_list.draw(background)
        for p in potal_list:
            p.draw_potal(background)

        #스크린에 그리고 새로고침
        screen.blit(background,(0,0))
        pygame.display.flip()

    else:
        print("클리어")
        return 0
