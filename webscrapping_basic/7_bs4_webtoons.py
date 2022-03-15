import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


"""네이버 웹툰 전체 목록 가져오기"""
cartoons = soup.find_all("a", attrs={"class":"title"})    #all을하면 첫번쨰뿐만 아닌 해당하는 모든것을 가져옴
for cartoon in cartoons:        #class 속성이 title인 모든 a element의 text를 반환
    print(cartoon.get_text())

