import requests
from bs4 import BeautifulSoup


for year in range(2015, 2020):
    
    url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(year)

    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        #파일명 겹치기 때문에 연도에 대한 것도 format형태로 추가
        with open("movie{}_{}.jpg".format(year, idx+1), "wb") as f:  #글자가 아닌 데이터기 때문에 binary이기 때문에 write binary 입력
            f.write(image_res.content)  #그림파일의 형태가 쓰여짐
        
        if idx >=4: #상위 5개 이미지까지만 다운로드
            break
