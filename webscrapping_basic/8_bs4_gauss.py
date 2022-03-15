import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()    #cartoons는 현재 리스트 형태기 때문에 원하는 문자열을 가져오기 위한 코드를 다음과 같이 작성
# link = cartoons[0].a["href"]        #
# print(title)
# print("https://comic.naver.com" + link)

"""만화제목 + 링크가져오기"""
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

"""평점 구하기"""
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()      #문서상 caroon.strong.get_text() 바로 찍어도되지만 find함수 써봄
    print(rate)
    total_rates += float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))

"""파이썬은 컴파일을하는 C언어와 달리 인터프리터 언어기때문에
Terminal에서 python입력하고 이떄부터 코드를 입력하면서 바로바로 테스트하면서 진행할 수있음
파일에서 작성한 코드 복사해서 터미널에 붙여넣기하고 바로바로 하면됨
방향키 위로 누르면 직전에 했던 코드 붙여넣기가 됨
exit() 입력하면 원래 터미널로 빠져나옴"""
"""beautiful soup documentation 구글검색해서 한글번역된 것도 있으니 추가공부 가능"""