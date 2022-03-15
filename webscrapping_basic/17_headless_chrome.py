from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True #눈에 보이지 않지만 백그라운드에서 진행함
options.add_argument("window-size=1920x1080")   #이 크기라고 가정하고 내부적으로 진행


browser = webdriver.Chrome(options=options)
browser.maximize_window()


#페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

import time
interval = 3 #2초에 한번씩 스크롤 내리게 하기위해 변수 지정

#현재 문서 높이를 가져와서 저장, 일종의 자바스크립트 명령임
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복 수행
while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")#현재 문서만큼의 높이로 내려라
    
    #페이지 로딩 대기
    time.sleep(interval)

    #현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")  #headless 에서 동작 잘했는지 안했는지 확인용 스크린샷

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")
#클래스명을 리스트 형태로 묶어주면 리스트 안의 동일한 클래스에 대한 정보를 다 가져옴 
# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
"""근데 위처럼 하면 실제로 상위 10개 영화가 class 두개 모두 속해있기 때문에 두번 중복해서 인식됨 따라서
후자에 있는 클래스로만 find하도록 다시 수정"""
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})

print(len(movies)) 

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    #할인 전 가격, 없을 경우도 있으니까 바로 get_text를 쓰지 않고 다음과 같이 구성함
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "할인되지 않은 영화 제외")
        continue
    #할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    
    #링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]    #a태그의 JC71ub클래스의 href정보를 가져온다.
    # 올바른 링크 : https://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : http://play.google.com" + link)
    print("-" * 90)

browser.quit()