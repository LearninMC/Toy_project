import pygame
import os
#######################################################################################################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init()   

#화면 크기 설정
screen_width = 640  #가로 크기
screen_height = 480 #세로 크기
screen  =  pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정 (게임이름)
pygame.display.set_caption("SungQ pang")

#FPS
clock = pygame.time.Clock()
########################################################################################################################

# 1.사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

#배경 이미지 불러오기
current_path = os.path.dirname(__file__)                #지금 실행하고 있는 이 파일이 열려있는 주소를 반환해줌
image_path = os.path.join(current_path, "images")       #image 폴더 위치 반환
background = pygame.image.load(os.path.join(image_path, "background.png"))
#스테이지 불러오기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]                        #스테이지 높이 위에 캐릭터를 두기 위해 사용

#캐릭터(스프라이트) 불러오기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size  #이미지의 크기를 구해옴
character_width = character_size[0]     #케릭터의 가로크기
character_height = character_size[1]    #케릭터의 세로크기
character_x_pos = (screen_width - character_width) / 2      #화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height - stage_height


#무기 불러오기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 한번에 여러발 발사 가능
weapons = []

#무기 이동속도
weapon_speed = 10


#이동할 좌표
character_to_x = 0
character_to_y = 0

#캐릭터 이동 속도
character_speed = 5



#시작 시간 정보
start_ticks = pygame.time.get_ticks()   #현재 tick을 받아옴

#이벤트 루프
running = True      #게임이 진행중인가?
while running:
    dt = clock.tick(30)     #게임화면의 초당 프레임 수, dt대신 아무이름이나 써도 먹힘. , clock은 pygame의 time에서 Clock클래스 임. 여기서 정의된 함수인 tick을 쓴것임. 근데 그 값을 변수에 지정을 했는데, 프레임이 먹히네 신기..

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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_position = character_x_pos + (character_width/2) - (weapon_width/2)       #여기서 무기가 만들어져야하니깐 x position 정의해줌. 이것도 가능하구나..
                weapon_y_position = character_y_pos
                weapons.append([weapon_x_position, weapon_y_position])                   #즉, 키를 누를때마다 그위치에서 weapon이 생성되는거고 이거를 리스트형태로 저장함
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


#####################################################################################################################################
# 3. 게임 캐리터 위치 정의    
    character_x_pos += character_to_x

    #가로경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos> screen_width-character_width:
        character_x_pos = screen_width-character_width
    # #세로경계값 처리
    # if character_y_pos < 0:
    #     character_y_pos = 0
    # elif character_y_pos> screen_height-character_height:
    #     character_y_pos = screen_height-character_height

# 무기 위치 조정
    #  100, 200 - > 180, 140, 100 ...
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons] #무기 위치를 위로 , weapons 리스트에 있는 값 w를 빼서 그거를 weapon_speed 연산처리후 다시 weapons 리스트로 넣는다.

    #천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]      #천장에 닿지 않은 웨폰만 리스트에 다시 저장한다.
#########################################################################################################################################
# 4. 충돌 처리


#######################################################################################################################################
#5. 화면에 그리기
    # screen.fill((50,100,10))    #RGB값에 해당하는 색깔을 배경으로 넣어줌
    screen.blit(background, (0, 0)) #배경 그리기 / 사진이 들어갈 위치 정해줌. 0,0은 제일 왼쪽, 제일 상단
    
    for weapon_x_position, weapon_y_position in weapons:        #weapons 리스트에서 위치정보를 가져오겠다.
        screen.blit(weapon, (weapon_x_position, weapon_y_position))
    screen.blit(stage, (0, (screen_height - stage_height)))   #스테이지 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  #케릭터 그리기
    

    #타이머 집어 넣기
    #경과 시간 계산

    #만약 시간이 0이하이면 게임 종료


    pygame.display.update()     #게임화면 다시 그리기. 사진 그림을 계속 업데이트 하라는 뜻임. 이걸해야 매 프레임별로 화면이 뜸!!!
###########################################################################################################################################
#6. 게임 종료
#종료 전 잠시 대기
pygame.time.delay(2000)     #2초 정도

#pygame 종료
pygame.quit()