# 정규식

# 올바른 형식과 아닌형식 구별해야함

# 주민등록번호
# 901201-1111111
# abcdef-1111111

# 이메일 주소

# sbarasi114@naver.com
# sbarsai114@naver@naver.com

# 차량번호
# 11가 12344
# 123가 1234

# ip주소

# 192.175.03.2
# 10000.42244.24124124.2424


import re

p = re.compile("ca.e")  
# . (ca.e): 하나의 문자를 의미 / 번호판 4자리 중 한자리 모를때 사용 > cafe, cake
# ^ (^de): 문자열의 시작 > desk, destination
# $ (se$) : 문자열의 끝 > case, base

# m = p.match("case") #case 라는 문자열이 p의 그룹과 매칭이 되는것을 m으로 받음
# # print(m.group())    #매치되지 않으면 에러가 발생

# if m:   #매칭되면 print하고 안되면 안하고
#     print(m.group())
# else:
#     print("매칭되지 않음")

def print_match(m):
    if m:
        print("m.group():", m.group())  #일치하는 문자열 반환
        print("m.string():", m.string)  #입력받은 문자열, string은 함수가 아니라 변수기 때문에 괄호없이 쓴다
        print("m.start():", m.start())  #일치하는 문자열의 시작 index
        print("m.end():", m.end())      #일치하는 문자열의 끝 index
        print("m.span():", m.span())    #일치하는 문자열의 시작/끝 index
    else:
        print("매칭되지 않음")
    
# m = p.match("careless") #match : 주어진 문자열의 처음부터 일치하는지 확인하는 것이기 때문에 care가 매칭된다고 인식함
# print_match(m)

# m = p.search("good care")   #search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("careless good care cafe")   #findall : 일치하는 모든 것을 리스트 형태로 반환, 여러개있으면 다 반환 기존에는 첫번째것만 반환했음
# print(lst)

"""정리"""

# 1. re.compile("원하는 정규식 형태") 를 p 라는 변수로 받기
# 2. m = p.match("비교할 문자열")
# 3. m= p.search("비교할 문자열")
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e): 하나의 문자를 의미 / 번호판 4자리 중 한자리 모를때 사용 > cafe, cake
# ^ (^de): 문자열의 시작 > desk, destination
# $ (se$) : 문자열의 끝 > case, base

#추가 공부는 w3school 에서 파이썬 자료들도 있고, 구글에 python re 검색해서 docs.python.org 사이트 들어가서 공부할 수 도 있음
