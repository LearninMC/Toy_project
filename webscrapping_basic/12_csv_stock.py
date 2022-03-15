import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"  #encoding은 utf-8-sig를 쓰는데, 이유는 엑셀파일에서도 한글형식이 안깨지게 하기 위해서. 그냥utf8쓰면 연습장은 문제없는데 엑셀에서 글씨 깨짐
f = open(filename, "w", encoding="utf-8-sig", newline="")    #newline=공백 넣어주는 이유는, 파일이 저장될때 저게 없으면 중간중간에 빈줄이 생기기 때문에 공백없이 쓰기 위해서임
writer = csv.writer(f)  #이제 우리는 csv파일형식으로 만들어서 쓰기가 가능해짐

#split함수를 사용해서 \t 으로 구분짓자. 그러면 탭으로 나뉜 항목들이 리스트(string) 형태로 들어감
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)
for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    #table태그의 type_2클래스에서 tbody태그에서 모든 tr태그를 리스트 형태로 가져오기
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:    #의미 없는 data skip. 5개씩 나뉨줄은 tr안에 td가 한개씩있음
            continue
        #.strip()을 사용하면 불필요한 /n /t 공백 띄어쓰기 같은 텍스트 정보는 가져오지 않음
        data = [column.get_text().strip() for column in columns]   #columns리스트에서 에서 하나씩 가져와서 이름을 column이라하고 진행함
        
        writer.writerow(data)
