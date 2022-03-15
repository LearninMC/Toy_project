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

#공만들기(4개 크기엗해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

#공 크기에 따른 최초 스피드
ball_speed_y = [-13, -12, -10, -9]      #index 0, 1, 2, 3에 해당하는 값

#공들
balls = []

#최초 발생하는 큰 공 추가
balls.append({
    "pos_x" : 50,   #공의 x좌표
    "pos_y" : 50,   #공의 y좌표
    "img_idx" : 0,  #공의 이미지 인덱스
    "to_x" : 3,      #공의 x축이동방향
    "to_y" : -6,     #y축 이동방향,
    "init_spd_y": ball_speed_y[0]})     #y 최초 속도


#사라질 무기, 공 저장 변수
ball_to_remove = -1
weapon_to_remove = -1


# font 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks()   #t시작시간 정의
#게임 종료 메세지
game_result = "Game Over"



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
    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]      #dic으로 정의된 balls 에서 ball_val값을 ball_pos_x에 넣어줌
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size       #ball_image 리스트에 0,1,2,3 위치에 크기별로 ball이 있음. 그걸 idx 넘버로 지정해서 가져옴
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:        #가로벽에 닿았을 떄 공 이동 위치 변경
            ball_val["to_x"] = ball_val["to_x"] *-1
        if ball_pos_y >= screen_height - stage_height - ball_height:       #스테이지에 튕겨서 올라가는 처리
            ball_val["to_y"] = ball_val["init_spd_y"] 
        else:                                                              #그 외의 모든 경우에는 속도를 계속 줄여나감
            ball_val["to_y"] += 0.3

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
#########################################################################################################################################
# 4. 충돌 처리  공, 케릭터 충돌 = 게임오버 / 공, 무기 충돌 = 공 분리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]      #dic으로 정의된 balls 에서 ball_val값을 ball_pos_x에 넣어줌
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        
        #공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()       
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        if character_rect.colliderect(ball_rect):
            running = False
            break       

        #공과 무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]
        #무기 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y
        # 충돌체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx #해당 무기 없애기 위한 값 설정
                ball_to_remove = ball_idx   #마찬가지로 ball이 충돌하면 없어지도록 ball_to_ramove값에 index값을 넣어줌
                if ball_img_idx < 3:    #위에 코드처럼 일단 공이랑 무기랑 닿으면 닿은 공은 사라지는게 맞음,
                    #현재 공 크기 정보를 가지고 옴
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]


                    #나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()        #나눠진 공은 더 작기때문에 idx에 1을 더해줌
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    #왼쪽으로 튕겨나가는 작은공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width-small_ball_width)/2,   #공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height - small_ball_height)/2,   #공의 y좌표
                        "img_idx" : ball_img_idx + 1,  #공의 이미지 인덱스
                        "to_x" : -3,      #공의 x축이동방향 -면 왼쪽 / +면 오른쪽
                        "to_y" : -6,     #y축 이동방향,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]})  
                    #오른쪽으로 튕겨져 나가는 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width-small_ball_width)/2,   #공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height - small_ball_height)/2,   #공의 y좌표
                        "img_idx" : ball_img_idx + 1,  #공의 이미지 인덱스
                        "to_x" : 3,      #공의 x축이동방향 -면 왼쪽 / +면 오른쪽
                        "to_y" : -6,     #y축 이동방향,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]}) 
                break
        else:               #계속 게임을 진행, 안쪽 for문 조건이 맞지않으면 contivue
            continue        ##중요!!!! 버그 수정 for문 두개를 빠져나가기 위한 트릭
        break               #안쪽 for 문에서 break 를 만나면 여기로 집입 가능.
    

#충돌된 공 or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1     #없앨 거 초기화
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1  
    #모든 공을 없앤 경우 게임 종료
    if len(balls) == 0:     #balls라는 리스트의 길이가 0이면 공이 없다는 거니깐
        game_result = "MIssion Complete"
        running = False
# #######################################################################################################################################
#5. 화면에 그리기
    # screen.fill((50,100,10))    #RGB값에 해당하는 색깔을 배경으로 넣어줌
    screen.blit(background, (0, 0)) #배경 그리기 / 사진이 들어갈 위치 정해줌. 0,0은 제일 왼쪽, 제일 상단
    
    for weapon_x_position, weapon_y_position in weapons:        #weapons 리스트에서 위치정보를 가져오겠다.
        screen.blit(weapon, (weapon_x_position, weapon_y_position))
    
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    screen.blit(stage, (0, (screen_height - stage_height)))   #스테이지 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  #케릭터 그리기
    

    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/ 1000
    timer = game_font.render("Time: {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10,10))
    #만약 시간이 0이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    pygame.display.update()     #게임화면 다시 그리기. 사진 그림을 계속 업데이트 하라는 뜻임. 이걸해야 매 프레임별로 화면이 뜸!!!
###########################################################################################################################################
#6. 게임 종료
#게임 오버 메시지
msg = game_font.render(game_result, True, (255, 255, 0))    #노란색
msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height /2)))
screen.blit(msg, msg_rect)
pygame.display.update() #다시한번 업데이트를해줘야함
#종료 전 잠시 대기
pygame.time.delay(2000)     #2초 정도

#pygame 종료
pygame.quit()