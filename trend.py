## 최근7일간의 검색어 데이터
#-*- coding: utf-8 -*-
import os
import sys
import urllib.request
import json
client_id = "EGHuNEfboLaDawZGMRcD"
client_secret = "sS6WndGJJt"
url = "https://openapi.naver.com/v1/datalab/search";

#롯데월드
body_lotte = "{\"startDate\":\"2018-02-22\",\"endDate\":\"2018-11-30\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"롯데월드\",\"keywords\":[\"롯데월드\"]}]}";

request_lotte = urllib.request.Request(url)
request_lotte.add_header("X-Naver-Client-Id",client_id)
request_lotte.add_header("X-Naver-Client-Secret",client_secret)
request_lotte.add_header("Content-Type","application/json")
response_lotte = urllib.request.urlopen(request_lotte, data=body_lotte.encode("utf-8"))
rescode_lotte = response_lotte.getcode()
if(rescode_lotte==200):
    response_lotte_body = response_lotte.read()
else:
    print("Error Code:" + rescode_lotte)


search_lotte = json.loads(response_lotte_body)

length = len(search_lotte["results"][0]["data"])

print("")
print("기준날짜 : %s ~ %s" %(search_lotte["results"][0]["data"][length-7]["period"],search_lotte["results"][0]["data"][length-1]["period"]))
print("검색어 : %s" %search_lotte["results"][0]["keywords"])

for i in range (1,8,1):
    print(search_lotte["results"][0]["data"][length-(8-i)]["ratio"])


#경복궁
body_kb = "{\"startDate\":\"2018-02-22\",\"endDate\":\"2018-11-30\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"경복궁\",\"keywords\":[\"경복궁\"]}]}";

request_kb = urllib.request.Request(url)
request_kb.add_header("X-Naver-Client-Id",client_id)
request_kb.add_header("X-Naver-Client-Secret",client_secret)
request_kb.add_header("Content-Type","application/json")
response_kb = urllib.request.urlopen(request_kb, data=body_kb.encode("utf-8"))
rescode_kb = response_kb.getcode()
if(rescode_kb==200):
    response_kb_body = response_kb.read()
else:
    print("Error Code:" + rescode_kb)


search_kb = json.loads(response_kb_body)

length = len(search_kb["results"][0]["data"])

print("")
print("기준날짜 : %s ~ %s" %(search_kb["results"][0]["data"][length-7]["period"],search_kb["results"][0]["data"][length-1]["period"]))
print("검색어 : %s" %search_kb["results"][0]["keywords"])

for i in range (1,8,1):
    print(search_kb["results"][0]["data"][length-(8-i)]["ratio"])



#덕수궁
body_ds = "{\"startDate\":\"2018-02-22\",\"endDate\":\"2018-11-30\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"경복궁\",\"keywords\":[\"덕수궁\"]}]}";

request_ds = urllib.request.Request(url)
request_ds.add_header("X-Naver-Client-Id",client_id)
request_ds.add_header("X-Naver-Client-Secret",client_secret)
request_ds.add_header("Content-Type","application/json")
response_ds = urllib.request.urlopen(request_ds, data=body_ds.encode("utf-8"))
rescode_ds = response_ds.getcode()
if(rescode_ds==200):
    response_ds_body = response_ds.read()
else:
    print("Error Code:" + rescode_ds)


search_ds = json.loads(response_ds_body)

length = len(search_ds["results"][0]["data"])

print("")
print("기준날짜 : %s ~ %s" %(search_ds["results"][0]["data"][length-7]["period"],search_ds["results"][0]["data"][length-1]["period"]))
print("검색어 : %s" %search_ds["results"][0]["keywords"])

for i in range (1,8,1):
    print(search_ds["results"][0]["data"][length-(8-i)]["ratio"])



#북촌한옥마을
body_bc = "{\"startDate\":\"2018-02-22\",\"endDate\":\"2018-11-30\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"북촌한옥마을\",\"keywords\":[\"북촌한옥마을\"]}]}";

request_bc = urllib.request.Request(url)
request_bc.add_header("X-Naver-Client-Id",client_id)
request_bc.add_header("X-Naver-Client-Secret",client_secret)
request_bc.add_header("Content-Type","application/json")
response_bc = urllib.request.urlopen(request_bc, data=body_bc.encode("utf-8"))
rescode_bc = response_bc.getcode()
if(rescode_bc==200):
    response_bc_body = response_bc.read()
else:
    print("Error Code:" + rescode_bc)


search_bc = json.loads(response_bc_body)

length = len(search_bc["results"][0]["data"])

print("")
print("기준날짜 : %s ~ %s" %(search_bc["results"][0]["data"][length-7]["period"],search_bc["results"][0]["data"][length-1]["period"]))
print("검색어 : %s" %search_bc["results"][0]["keywords"])

for i in range (1,8,1):
    print(search_bc["results"][0]["data"][length-(8-i)]["ratio"])



#남산, 남산타워
body_namsan = "{\"startDate\":\"2018-02-22\",\"endDate\":\"2018-11-30\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"남산\",\"keywords\":[\"남산\",\"남산타워\"]}]}";

request_namsan = urllib.request.Request(url)
request_namsan.add_header("X-Naver-Client-Id",client_id)
request_namsan.add_header("X-Naver-Client-Secret",client_secret)
request_namsan.add_header("Content-Type","application/json")
response_namsan = urllib.request.urlopen(request_namsan, data=body_namsan.encode("utf-8"))
rescode_namsan = response_namsan.getcode()
if(rescode_namsan==200):
    response_namsan_body = response_namsan.read()
else:
    print("Error Code:" + rescode_namsan)


search_namsan = json.loads(response_namsan_body)

length = len(search_namsan["results"][0]["data"])

print("")
print("기준날짜 : %s ~ %s" %(search_namsan["results"][0]["data"][length-7]["period"],search_namsan["results"][0]["data"][length-1]["period"]))
print("검색어 : %s" %search_namsan["results"][0]["keywords"])

for i in range (1,8,1):
    print(search_namsan["results"][0]["data"][length-(8-i)]["ratio"])




#어린이대공원
body_chlidren = "{\"startDate\":\"2018-02-22\",\"endDate\":\"2018-11-30\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"어린이대공원\",\"keywords\":[\"어린이대공원\"]}]}";

request_chlidren = urllib.request.Request(url)
request_chlidren.add_header("X-Naver-Client-Id",client_id)
request_chlidren.add_header("X-Naver-Client-Secret",client_secret)
request_chlidren.add_header("Content-Type","application/json")
response_chlidren = urllib.request.urlopen(request_chlidren, data=body_chlidren.encode("utf-8"))
rescode_chlidren = response_chlidren.getcode()
if(rescode_chlidren==200):
    response_chlidren_body = response_chlidren.read()
else:
    print("Error Code:" + rescode_chlidren)


search_chlidren = json.loads(response_chlidren_body)

length = len(search_chlidren["results"][0]["data"])

print("")
print("기준날짜 : %s ~ %s" %(search_chlidren["results"][0]["data"][length-7]["period"],search_chlidren["results"][0]["data"][length-1]["period"]))
print("검색어 : %s" %search_chlidren["results"][0]["keywords"])

for i in range (1,8,1):
    print(search_chlidren["results"][0]["data"][length-(8-i)]["ratio"])
