#-*- coding: utf-8 -*-
import os
import sys
import urllib.request
import json
client_id = "tMgi4goC6FUL5Enj7TNY"
client_secret = "9UZY11sNF6"
url = "https://openapi.naver.com/v1/datalab/search";
body = "{\"startDate\":\"2018-02-22\",\"endDate\":\"2018-11-30\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"롯데월드\",\"keywords\":[\"롯데월드\"]}]}";

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
else:
    print("Error Code:" + rescode)


j=json.loads(response_body)


print(j)