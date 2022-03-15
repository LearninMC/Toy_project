from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()   #창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)    #url 이동

#가는날 선택
browser.find_element_by_link_text("가는날 선택").click()   #a태그 안에 가는날 선택이라는 텍스트가 있었는데, 다음함수로 사용가능함

#이번달 8일, 다음달 9일 선택

browser.find_elements_by_link_text("8")[0].click()  #이번달 8일 다음달 8일이 존재하기때문에 모든 8일 elements를 가져와서 첫번째 elements선택해서 클릭
browser.find_elements_by_link_text("9")[1].click()  #이번달 9일 다음달 9일이 있고 두번째 9일을 선택해야하므로..


#제주도 선택
#제주도 사진 클릭하면 윗태그에 a href가 있어서 이걸 xpath copy이용함.
# 그리고 큰따옴표 헷갈리는것 방지위해서 안쪽에는 ''로바꿔줌
# 근데 이렇게 실행했는데, 제대로 클릭이 안됨. 따라서 더 윗태그인 li태그를 xpath 카피함

browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))    #10초동안 기다려라 하지만 XPATH기준으로 지정한 element 결과가 나올때까지만 기다려라.
    print(elem.text)
    #성공했을 때 동작수행
finally:
    browser.quit()

    
#첫번째 결과 출력
"""결과물이 나오기 전 로딩화면창이 있기 때문에 
대기시간을 줘야함. 하지만 몇초의 로딩시간이 걸릴지 모름.
로딩결과가 나올때까지만 대기하는 함수가 있어서 이걸 사용
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
