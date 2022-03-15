import pygame
from random import *
#######################################################################################################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init()   

#화면 크기 설정
screen_width = 480  #가로 크기
screen_height = 640 #세로 크기
screen  =  pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정 (게임이름)
pygame.display.set_caption("SungQ Game")

#FPS
clock = pygame.time.Clock()
########################################################################################################################

# 1.사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\seongkyu\\Desktop\\PythonWorkspace\\pygame_basic\\background.png") #이미지 파일 탭에서 오른쪽버튼 눌러서 copy path해준다음에 여기다 복사붙여넣기함. 다만 역슬러시일경우 2개씩 써주거나, 슬러시 하나로 써줘도 됨.

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\seongkyu\\Desktop\\PythonWorkspace\\pygame_basic\\character.png")
character_size = character.get_rect().size  #이미지의 크기를 구해옴
character_width = character_size[0]     #케릭터의 가로크기
character_height = character_size[1]    #케릭터의 세로크기
character_x_pos = (screen_width - character_width) / 2      #화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height   

#이동할 좌표
to_x = 0
to_y = 0
to_enemy_x = 0
to_enemy_y = 0

#이동 속도
character_speed = 0.5

# 적 enemy 캐릭터
enemy = pygame.image.load("C:\\Users\\seongkyu\\Desktop\\PythonWorkspace\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size  #이미지의 크기를 구해옴
enemy_width = enemy_size[0]     #적의 가로크기
enemy_height = enemy_size[1]    #적의 세로크기
enemy_x_pos = (screen_width - enemy_width) / 2      #화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
enemy_y_pos = (screen_height - enemy_height) / 2         #화면 세로 크기의 가장 아래에 해당하는 곳에 위치(세로)

#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성(폰트종류, 크기)
ending_font = pygame.font.Font(None, 80)

#총 시간
total_time = 30

#시작 시간 정보
start_ticks = pygame.time.get_ticks()   #현재 tick을 받아옴

#이벤트 루프
running = True      #게임이 진행중인가?
while running:
    dt = clock.tick(60)     #게임화면의 초당 프레임 수, dt대신 아무이름이나 써도 먹힘. , clock은 pygame의 time에서 Clock클래스 임. 여기서 정의된 함수인 tick을 쓴것임. 근데 그 값을 변수에 지정을 했는데, 프레임이 먹히네 신기..

#케릭터가 1초에 100만큼 이동을해야함
#10fps : 1초 동안에 10번 동작 -> 한번에 10만큼 이동해야 100이동
#20fps : 1초 동안에 20번 동작 -> 한번에 5만큼 이동해야 100이동
#즉 fps가 다르디고 속도가 다르면 안됨. 해결책은 포지션에 dt만큼 곱해줌 tick()안의 숫자를 넣으면 1000/숫자 값이 int형으로 나옴

    #print("fps : " + str(clock.get_fps()))     #현재fps 값 출력
####################################################################################################################################
# 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():     #사용자가 마우스를 움직인다던지, 키보드를 입력한다던지 하는 이벤트를 계속해서 받겠다는 뜻. 키보드르 누르면 무기를 발사한다던지 등등
        if event.type == pygame.QUIT:   #창이 닫히는 이벤트가 발생하였는가?
            running = False             #게임이 진행중이 아님을 설정
        to_enemy_x = int(randrange(-5, 5)) / 10  
        to_enemy_y = int(randrange(-5, 5)) / 10

        if event.type == pygame.KEYDOWN:    #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  #캐릭터를 왼쪽으로
                to_x -=character_speed        #스피드 만큼 왼쪽으로 이동
            elif event.key == pygame.K_RIGHT:   #캐릭터를 오른쪽으로
                to_x +=character_speed        #스피드 만큼 오른쪽으로 이동
            elif event.key == pygame.K_UP:
                to_y -=character_speed
            elif event.key == pygame.K_DOWN:
                to_y +=character_speed
        if event.type == pygame.KEYUP:      #방향키를떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
#####################################################################################################################################
# 3. 게임 캐리터 위치 정의    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos> screen_width-character_width:
        character_x_pos = screen_width-character_width
    #세로경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos> screen_height-character_height:
        character_y_pos = screen_height-character_height

    enemy_x_pos += to_enemy_x * dt
    enemy_y_pos += to_enemy_y * dt

    #가로경계값 처리
    if enemy_x_pos < 0:
        enemy_x_pos = 0
    elif enemy_x_pos> screen_width-character_width:
        enemy_x_pos = screen_width-character_width
    #세로경계값 처리
    if enemy_y_pos < 0:
        enemy_y_pos = 0
    elif enemy_y_pos> screen_height-character_height:
        enemy_y_pos = screen_height-character_height
#########################################################################################################################################
# 4. 충돌 처리
    character_rect = character.get_rect()   #get_rect라는 함수를 보니까, 4개의 정보를 받는데 x좌표 y좌표 가로크기 세로크기 인것 같음.
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos


    #충돌 체크
    if character_rect.colliderect(enemy_rect):       #사각형이 충돌이 있었는지 감지하는 함수colliderect
        print("충돌했어요")
        running = False

#######################################################################################################################################
#5. 화면에 그리기
    # screen.fill((50,100,10))    #RGB값에 해당하는 색깔을 배경으로 넣어줌
    screen.blit(background, (0, 0)) #배경 그리기 / 사진이 들어갈 위치 정해줌. 0,0은 제일 왼쪽, 제일 상단
    screen.blit(character, (character_x_pos, character_y_pos))  #케릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))          #적 그리기

    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   #경과하는시간에서 시작한시간을 뺴주면 정확한 경과시간을 쓴다는것같은데.. 근데 안뺴줘도 결과는 똑같음. 1000으로 나누어서 초 단위로 표시 , 원래는 ms단위기 때문
    timer = game_font.render(str(round(total_time - elapsed_time)), True, (255, 255, 255))    #render함수(출력할 글자, True, 글자색상) 정수형으로 바꾸기 위해서 int로 싸줌. 그리고 render함수 안에 문자로 인식되게끔 str으로 감싸줌
    screen.blit(timer, (10, 10))

    #만약 시간이 0이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        screen.fill((10,150,20))
        winner = ending_font.render("Win!!", True, (255,255,255))
        screen.blit(winner, (180,280))
        running = False


    pygame.display.update()     #게임화면 다시 그리기. 사진 그림을 계속 업데이트 하라는 뜻임. 이걸해야 매 프레임별로 화면이 뜸!!!
###########################################################################################################################################
#6. 게임 종료
#종료 전 잠시 대기
pygame.time.delay(2000)     #2초 정도

#pygame 종료
pygame.quit()