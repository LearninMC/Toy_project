import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
#headers 쓰는 이유, requests에서 가져오는 정보는 미국에서 접속했다고 가정하고 가져오기 때문에, 한국접속 데이터로 바꿔주기 위해서 바꿔줌
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
    "Accept-Language":"ko-KR,ko"#한글이 있으면 한글페이지를 갖고올 수 있는 기능
    }

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})  #f12로 확인하면 저 class가 영화에 대한 가격, 평점, 제목, 장르등 정보를 다 포함하고 있음

print(len(movies))  #영화가 수십개인데 처음 10개가 뜨고, 나중에 점점 영화가 뜨니까 이에대한 정보를 빼올수가 없음. 이를 위해서 셀레늄을 이용함

# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify())    #그냥 텍스트로 긁어오면 너무 지저분하고 보질못함. 그래서 soup객체를 가져오면서 prettify함수를 이용해 이쁘게 가져옴

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)