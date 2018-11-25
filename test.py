import requests
from bs4 import BeautifulSoup

# request = requests.get(url).json()
# print(type(request)) # request는 list 타입
# print(request[0]["url"]) # url만 가져옴


## 운영시간 크롤링
# 롯데월드
url = "http://adventure.lotteworld.com/kor/usage-guide/service/index.do"
req = requests.get(url).text
doc = BeautifulSoup(req, "html.parser")
time = doc.select(".openDiv .leftArea .timeInfo .time .txt > span")[0].text
time2 = doc.select(".openDiv .leftArea .timeInfo .time .txt > span")[1].text.split(" ")[1]
print(time)
print(time2)

# 어린이 대공원
# 5~22
# https://www.sisul.or.kr/open_content/childrenpark/introduce/use.jsp

# 남산
# 월~금, 일
# 10 : 00 ~ 23 : 00
# 토
# 10 : 00 ~ 24 : 00
# http://www.nseoultower.co.kr/visit/use.asp

# 덕수궁
# 9~21(입장마감은 20:00)

# 경복궁
# 화요일 휴궁일
# 1~2월 09:00~17:00(입장마감은 16:00)
# 3~5월 09:00~18:00(입장마감은 17:00)
# 6월 ~ 8월  09:00~18:30(입장마감은 17:30)
# 9월 ~ 10월 09:00~18:00(입장마감은 17:00)
# 11월 ~ 12월 09:00~17:00(입장마감은 16:00)

# 북촌한옥마을
# 평일, 토  10~17
# 일     골목길 쉬는 날