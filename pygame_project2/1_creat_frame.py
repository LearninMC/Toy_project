import pygame

pygame.init()   #초기화

#화면 크기 설정
screen_width = 480  #가로 크기
screen_height = 640 #세로 크기
screen  =  pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("SungQ Game")

#이벤트 루프
running = True      #게임이 진행중인가?
while running:
    for event in pygame.event.get():     #사용자가 마우스를 움직인다던지, 키보드를 입력한다던지 하는 이벤트를 계속해서 받겠다는 뜻. 키보드르 누르면 무기를 발사한다던지 등등
        if event.type == pygame.QUIT:   #창이 닫히는 이벤트가 발생하였는가?
            running = False             #게임이 진행중이 아님을 설정
#pygame 종료
pygame.quit()