"""사이트에 접속하면 이사람이 pc로 접속하는지 모바일로 접속하는지
알기 때문에, 그에 맞춰 사이트 화면 제공한다. 하지만 웹크롤링하면서
무단으로 정보를 긁어오고 하면 사이트에 과부하가 걸릴 수 있기 때문에
이런 접근은 원천적으로 차단하는 경우가 있다. 하지만 user agent를 통해
이것을 뚫을 수 있음."""

import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
