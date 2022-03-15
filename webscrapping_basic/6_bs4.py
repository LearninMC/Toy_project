import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() #문제있으면 바로 종료되게끔

soup = BeautifulSoup(res.text, "lxml")  #lxml 을통해 res로 가져온걸 bs객체로 만들었다는 것
# print(soup.title)               #title이 뭐로 설정되어있는지
# print(soup.title.get_text())    #타이틀에 쓰인 글자 그대로 가져오기
# print(soup.a)                       #처음으로 보이는 element a요소에 관해서만 보여줌
# print(soup.a.attrs)         #a가 가지고 있는 속성정보를 보여줌
# print(soup.a["href"])       #a가 가지고 있는 속성을 대괄호 안에 쓰면 값 정보를 보여줌
"""페이지에 관해 이해가 높을때 위의 방식을 씀. 필요한 정보를 딱딱 지저해줘서 뺴냄"""

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# print(soup.find(attrs={"class":"Nbtn_upload"})) #여기에 Nbtn 속성이 하나기 때문에 "a"없애도 실행은 됨. 범주를 써주면 더 정확하게 원하는 정보를 찾을수 있는것

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a)
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling       #다음항목
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling   #이전항목
# print(rank2.a.get_text())
# print(rank1.parent) #부모 태크로 올라감. 

# rank2 = rank1.find_next_sibling("li")   #find와 함께 조건을 주면, 깔끔하게 다음번 원하는 항목을 골라낼수 있음
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())
# siblings = rank1.find_next_siblings("li")      #rank1기준으로 다음 형제들 쭉 가져옴

webtoon = soup.find("a", text="신도림-시즌2 68. 용 서") #a태그 이면서 text가 저것인 걸 가져와라
print(webtoon)