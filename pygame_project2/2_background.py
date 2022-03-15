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

#이벤트 루프
running = True      #게임이 진행중인가?
while running:
    for event in pygame.event.get():     #사용자가 마우스를 움직인다던지, 키보드를 입력한다던지 하는 이벤트를 계속해서 받겠다는 뜻. 키보드르 누르면 무기를 발사한다던지 등등
        if event.type == pygame.QUIT:   #창이 닫히는 이벤트가 발생하였는가?
            running = False             #게임이 진행중이 아님을 설정
    
    # screen.fill((50,100,10))    #RGB값에 해당하는 색깔을 배경으로 넣어줌
    screen.blit(background, (0, 0)) #배경 그리기 / 사진이 들어갈 위치 정해줌. 0,0은 제일 왼쪽, 제일 상단

    pygame.display.update()     #게임화면 다시 그리기. 사진 그림을 계속 업데이트 하라는 뜻임. 이걸해야 사진화면이 뜸
#pygame 종료
pygame.quit()