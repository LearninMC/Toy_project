import requests
import re
from bs4 import BeautifulSoup

"""http method 방식에는 Get / POST 두방식이 있음
GET은 주소창에 정보의 노출이 있고, 적은 데이터만 서버로 요청할 수 있음.
POST는 로그인할때 아이디 비밀번호같은 정보를 쓸때 어느정도 가려서
보냄. GET보다 많은 데이터를 보낼 수 있음.
GET방식은 사용하고자 하는 주소의 내용을 조작해서 원하는 사이트를
들어갈 수 있기 때문에 스크래핑하기 좋음.
다만 POST방식처럼 페이지 내용이 바뀌어도 주소가 바뀌지 않는 경우에는
웹스크래핑하기 까다로움"""

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
res = requests.get(url, headers =headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})    #li태그에서, class가 search-product로 시작하는 항목을 찾는다. 저 부호를 사용하기 위해 re.compile을 써줘야함
# print(items[0].find("div", attrs={"class":"name"}).get_text())  #첫번째 항목의 div 태그 에서 class가 name인 항목의 문자열을 가져와라
for item in items:

    #광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("  <광고 상품 제외합니다>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text()
    #애플 제품 제외
    if "Apple" in name:
        print("  <Apple 상품 제외합니다>")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    #리뷰 100개 이상, 평점 4.5이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"})    #평점없는것도있음
    if rate:
        rate = rate.get_text()
    else:
        print("  <평점 없는 상품 제외합니다>")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]   #괄호안의 숫자만 가져오기 위해서 두번째부터 맨뒷문자 앞까지 끌어옴
    else:
        print("  <평점 수 없는 상품 제외합니다>")
        continue

    if float(rate) >=4.5 and int(rate_cnt) >= 100:
        print(name,price,rate,rate_cnt)