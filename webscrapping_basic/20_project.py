import re
import requests
from bs4 import BeautifulSoup

#url로 중복되는 작업 많이 하니까, 밑에 처럼 따로 정리함
def create_soup(url):
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
    }    
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup    


def print_news(index, title, link):
    print(f"{index+1}. {title}")
    print("  (링크 : {})".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    #흐림, 어제보다 OO" 높아요
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    #현재 OO"C  (최저 OO" / 최고 OO")
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("도씨", "")
    # min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    # max_temp = soup.find("span", attrs={"class":"max"}).get_text()
    # 오전 강수확률 OO%  / 오후 강수확률 OO%
    morning_rain_rate = soup.find("dd", attrs={"class":"desc"}).get_text().strip()  #오전 강수 확률
    afternoon_rain_rate = soup.find("dd", attrs={"class":"desc"}).get_text().strip()  #오후 강수 확률
    #미세먼지 정보
    dust = soup.find("dl", attrs={"class":"indicator"})
    # pm10 = dust.find_all("dd")[0].get_text()     #미세먼지
    # pm25 = dust.find_all("dd")[1].get_text()    #초미세먼지
    # dust = soup.find("dl", attrs={"class":"indicator"}, text=["미세먼지", "초미세먼지"]) 이렇게도 쓸 수있음. 여러개면 리스트 형태로 감싸는 것 가능하고, attrs안에 "id":"블라블라" 처럼 더 추가적인 정보제공해도 됨

    #출력
    print(cast)
    print(f"현재 {curr_temp} ") # (최저 {min_temp} / 최고 {max_temp})
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    # print("미세먼지 {}".format(pm10))
    # print("초미세먼지 {}".format(pm25))

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=4)  #"li"태그가 여러개인데 limit를 이용해 가져오는 개수를 제한해줄 수 있음
    for index, news in enumerate(news_list):
        # title = news.div.a.get_text().strip()   #div태그 밑의 a태그의 텍스트를 가져온다. 이렇게 간단하게 써도됨
        title = news.find("a").get_text().strip() #위와 동일하면서 다른 표현방식
        link = url + news.find("a")["href"]
        print_news(index, title, link)

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)  #3개까지 가져옴
    for index, news in enumerate(news_list):
        a_idx=0
        img = news.find("img")
        if img:
            a_idx = 1   #img 태그가 있으면 2번째 img태그의 정보를 사용
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()   #처음에 이렇게쓰니까 기사제목이 안가져와짐. 이유는 첫번째 a태그에는 이미지 파일에 대한 정보만 있었기 때문. 2번째 a태그로부터 정보가져와야함
        link = a_tag["href"]
        print_news(index, title, link)
    print() #빈줄

def scrape_english():
    print("[오늘의 영어회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})  #import re 정규식 사용.  ^로 시작하는 id 선택
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: #8문장이 있다고 가정할 때, 5~8까지 잘라서 가져옴(index 기준 4~7) 중간부터 끝까지 가져오겠다는 것. 슬래시//2개 사용한 이유는 혹시 만약에 홀수일경우 정수형으로 몫만 가져오게끔 하기위해서
        print(sentence.get_text().strip())
    print()    
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
    print()


#프로그램을 여기서 직접실행할때는 밑의 함수들 실행, but 외부호출일 경우 실행 X
if __name__ == "__main__":
    scrape_weather()    #오늘의 날씨 가져오기
    scrape_headline_news()    #헤드라인 뉴스 가져오기
    scrape_it_news()  #오늘의 IT뉴스 가져오기
    scrape_english()  #오늘의 영어 회화 가져오기