import pygame

pygame.init()   #초기화

#화면 크기 설정
screen_width = 480  #가로 크기
screen_height = 640 #세로 크기
screen  =  pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("SungQ Game")
#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\seongkyu\\Desktop\\PythonWorkspace\\pygame_basic\\background.png") #이미지 파일 탭에서 오른쪽버튼 눌러서 copy path해준다음에 여기다 복사붙여넣기함. 다만 역슬러시일경우 2개씩 써주거나, 슬러시 하나로 써줘도 됨.

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\seongkyu\\Desktop\\PythonWorkspace\\pygame_basic\\character.png")
character_size = character.get_rect().size  #이미지의 크기를 구해옴
character_width = character_size[0]     #케릭터의 가로크기
character_height = character_size[1]    #케릭터의 세로크기
character_x_pos = (screen_width - character_width) / 2      #화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height         #화면 세로 크기의 가장 아래에 해당하는 곳에 위치(세로)

#이동할 좌표
to_x = 0
to_y = 0
#이벤트 루프
running = True      #게임이 진행중인가?
while running:
    for event in pygame.event.get():     #사용자가 마우스를 움직인다던지, 키보드를 입력한다던지 하는 이벤트를 계속해서 받겠다는 뜻. 키보드르 누르면 무기를 발사한다던지 등등
        if event.type == pygame.QUIT:   #창이 닫히는 이벤트가 발생하였는가?
            running = False             #게임이 진행중이 아님을 설정
        
        if event.type == pygame.KEYDOWN:    #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  #캐릭터를 왼쪽으로
                to_x -=0.5        #좌표 5만큼 왼쪽으로 이동
            elif event.key == pygame.K_RIGHT:   #캐릭터를 오른쪽으로
                to_x +=0.5        #좌표 5만큼 오른쪽으로 이동
            elif event.key == pygame.K_UP:
                to_y -=0.5
            elif event.key == pygame.K_DOWN:
                to_y +=0.5
        if event.type == pygame.KEYUP:      #방향키를떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x
    character_y_pos += to_y

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
    
    # screen.fill((50,100,10))    #RGB값에 해당하는 색깔을 배경으로 넣어줌
    screen.blit(background, (0, 0)) #배경 그리기 / 사진이 들어갈 위치 정해줌. 0,0은 제일 왼쪽, 제일 상단
    screen.blit(character, (character_x_pos, character_y_pos)) #케릭터

    pygame.display.update()     #게임화면 다시 그리기. 사진 그림을 계속 업데이트 하라는 뜻임. 이걸해야 사진화면이 뜸
#pygame 종료
pygame.quit()