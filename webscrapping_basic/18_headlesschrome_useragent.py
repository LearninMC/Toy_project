from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True #눈에 보이지 않지만 백그라운드에서 진행함
options.add_argument("window-size=1920x1080")   #이 크기라고 가정하고 내부적으로 진행
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")


browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

#원래 agent user
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

#이처럼 headless chrome을 쓰면 user agent 가 할당된 값으로 나오는 것을 알 수있음
#이럴 경우 사이트로부터 차단 당할 가능성이 있음
#더 공부하고 싶으면 seleniun with python 검색해서 공부할 수 있음.