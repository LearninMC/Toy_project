"""실행하면 드라이버 작동하면서 터미널이 막히는데, 끄고싶으면 ctrl + c누르면 됨
"""
import time
from selenium import webdriver


browser = webdriver.Chrome("./chromedriver.exe")    #파이썬이 실행되고 있는 폴더에 chromedriver설치되어있으면 괄호안에 아무것도 안써도되고, 이렇게 써도됨. 다른 폴더에있으면 그 폴더 주소 써줘야함.
#1. 네이버로 이동
browser.get("http://naver.com")

#2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

#4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)   #화면전환 대기시간떄문에 다음 커맨드입력을 정확히 하기 위해서 

#5. id를 새로 입력
browser.find_element_by_id("id").clear()    #기존 써져있던 id 제거
browser.find_element_by_id("id").send_keys("my_id")

#6. html 정보 출력
print(browser.page_source)

#7. 브라우저 종료
browser.quit()

"""터미널 창에서 진행
python입력
from selenium import webdriver 입력
browser = webdriver.Chrome() 입력
browser.get("http://naver.com") 입력
elem = browser.find_element_by_class_name("link_login") 입력
elem.click() 입력하면 로그인창 클릭한것과 같음
browser.back() 뒤로 돌아가고싶을경우
browser.forward() 앞으로 가고 싶을경우
browser.refresh() 새로고침기능
elem = browser.find_element_by_id("query") 검색창
from selenium.webdriver.common.keys import Keys 키 입력을 위해 라이브러리 사용
elem.send_keys("나도코딩") 이렇게 하면 검색창에 글 입력됨
elem.send_keys(Keys.ENTER) 입력하면 엔터가 입력됨 즉 위에 import Keys는 엔터입력을 위해서 한것임
elem = browser.find_elements_by_tag_name("a") 분명 a태그는 엄청 많을 것임. 따라서 element가 아닌 elements로 바꿔줌
for e in elem:
    e.get_attribute("href")  입력할떄 indent 확인 잘하고, 입력하면 아직 더 입력할 수 있는데 엔터 한번 더 누르면 값나옴
daum 사이트 넘어가서 진행
elem = browser.find_element_by_name("q") 이번에는 이름이 q인걸 찾아서 검색창 찾음
elem.send_keys("나도코딩") 입력해주고 이번에는 엔터가 아닌 검색이미지 클릭을해볼것임
xpath를 이용하는 방법인데, 커서로 갖다대고 오른쪽버튼으로 xpath 복사를 해줌
elem = browser.find_element_by_xpath("//*[@id="daumBtnSearch"]") xpath("")안에 오른쪽버튼 클릭하면 xpath주소 복사했던것
들어감. 근데 문제는 ""인식 때문에 이거를 ''으로 바꿔줘야 문제가 안생김. 
elem.click() 입력해서 확인
browser.close() 해주면 현재 켜져있는 tab만 끄는 거고
browser.quit() 해주면 전체 창을 끄게 해줌

"""