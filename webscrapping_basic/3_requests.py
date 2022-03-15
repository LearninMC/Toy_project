import requests
res = requests.get("http://google.com") #""안에 있는 url주소로부터 정보를 가져오겠다.
res.raise_for_status()      #올바른 웹주소면 밑에 명령을 실행하고, 아닐경우 에러처리 띄우고 종료해버림
# print("응답코드 : ", res.status_code) #200이면 정상, 403은 페이지에 접근할 수 있는 권한이 없다. 이럴경우 정상적으로 웹스크래핑을 할 수 없어서 다른방식을 써야함

# if res.status_code == requests.codes.ok:    #requests.codes.ok는 정상적이면 200이라는 값을 반환해줌
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code, "]")
# print("웹 스크래핑을 진행합니다")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)