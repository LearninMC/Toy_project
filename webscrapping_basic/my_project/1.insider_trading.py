"""Web scraping for insider trading with python"""

import csv
import requests
from bs4 import BeautifulSoup

#변수 설정
year_1 = str(365)
months_3 = str(90)
# trade_range = months_3                  #기간
limit = 5                               #가져오고 싶은 데이터의 수

#알고싶은 기업 티커, 리스트 형태로 작성
tickers = []
while True:
    input_value = str(input("원하는 종목의 ticker를 입력하세요 (모두 입력했을 경우 end 를 입력): "))
    if input_value != "end":
        tickers.append(input_value)
    else:
        break
while True:
    input_value = str(input("검색하고 싶은 기간(일) 다음 숫자 중 하나 입력(3, 7, 14, 30, 60, 90, 180, 365, 730): "))
    if 2 < int(input_value) < 731:
        trade_range = input_value
        break
    else:
        break

#기본 세팅
url_ticker = ""
for ticker in tickers:
    if url_ticker == "":
        url_ticker = ticker
    else:
        url_ticker = ticker + "%2C+" + url_ticker

filename_ticker = ""
for ticker in tickers:
    filename_ticker = ticker + "_" + filename_ticker 

filename = "{}{}_trading_data.csv".format(filename_ticker, trade_range)

#웹스크래핑 통한 파일 작성
with open(filename, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    title = "Date Ticker Company_name Insider_Name Title Trade_Type Price Qty Owned Delta_Own Value".split(" ")
    writer.writerow(title)

    url = f"http://openinsider.com/screener?s={url_ticker}&o=&pl=&ph=&ll=&lh=&fd={trade_range}&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1"
    headers = {                                             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"tinytable"}).find("tbody").find_all("tr")
    for ticker in tickers:
        chk_cnt = 0
        for idx, row in enumerate(data_rows):       
            columns = row.find_all("td")    
            modified_columns = columns[2:-4]
            data = [column.get_text().strip() for column in modified_columns]  
            # print(idx, ticker, data[1])
            if data[1] == ticker and chk_cnt < 10:
                writer.writerow(data)
                chk_cnt += 1
