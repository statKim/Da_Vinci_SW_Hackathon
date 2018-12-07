# -*- coding: utf-8 -*-
from datetime import datetime, date
import pandas as pd
import urllib.request
import json
import weather_api      # 날씨API를 사용하는 사용자 정의 모듈 import

def dataencoding(mo, da, place):
    ## 네이버 트렌드 데이터 (최근7일간의 검색어 데이터)
    client_id = "ID"
    client_secret = "Secret"
    url = "https://openapi.naver.com/v1/datalab/search";

    today = str(date.today())
    
    # 장소와 날짜별 trend  데이터 가져오기
    if place == "lotte":
        # 롯데월드
        body_lotte = "{\"startDate\":\"2018-02-22\",\"endDate\":\""+today+"\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"롯데월드\",\"keywords\":[\"롯데월드\"]}]}";
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
    
        search = json.loads(response_lotte_body.decode('utf-8'))
    
        length = len(search["results"][0]["data"])        
    elif place == "park":
        #어린이대공원
        body_chlidren = "{\"startDate\":\"2018-02-22\",\"endDate\":\""+today+"\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"어린이대공원\",\"keywords\":[\"어린이대공원\"]}]}";
    
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
    
        search = json.loads(response_chlidren_body.decode('utf-8'))
    
        length = len(search["results"][0]["data"])        
    elif place == "gyeongbok":
        # 경복궁
        body_kb = "{\"startDate\":\"2018-02-22\",\"endDate\":\""+today+"\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"경복궁\",\"keywords\":[\"경복궁\"]}]}";
    
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
    
        search = json.loads(response_kb_body.decode('utf-8'))
    
        length = len(search["results"][0]["data"])        
    elif place == "duksu":
        # 덕수궁
        body_ds = "{\"startDate\":\"2018-02-22\",\"endDate\":\""+today+"\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"경복궁\",\"keywords\":[\"덕수궁\"]}]}";
    
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
    
        search = json.loads(response_ds_body.decode('utf-8'))
    
        length = len(search["results"][0]["data"])        
    elif place == "buk":
        # 북촌한옥마을
        body_bc = "{\"startDate\":\"2018-02-22\",\"endDate\":\""+today+"\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"북촌한옥마을\",\"keywords\":[\"북촌한옥마을\"]}]}";
    
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
    
        search = json.loads(response_bc_body.decode('utf-8'))
    
        length = len(search["results"][0]["data"])        
    else:
        # 남산, 남산타워
        body_namsan = "{\"startDate\":\"2018-02-22\",\"endDate\":\""+today+"\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"남산\",\"keywords\":[\"남산\",\"남산타워\"]}]}";
    
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
    
        search = json.loads(response_namsan_body.decode('utf-8'))
    
        length = len(search["results"][0]["data"])        
        
    # 1주일간의 평균 trend 데이터
    trend = []
    for i in range(1, 8, 1):
        trend.append(search["results"][0]["data"][length - (8 - i)]["ratio"])
    trend = sum(trend) / 7   


    ## 요일, 공휴일 변수 setting
    now = datetime.now()

    d30 = [4, 6, 9, 11]
    d31 = [1, 3, 5, 7, 8, 10, 12]
    month = [now.month]
    day = now.day

    if (day >= 25) and (month[0] in d30):  # 오늘부터 7일 이후까지 보여줄건데 30일이 넘어갈 경우
        month.append(now.month + 1)
        day_next = [d for d in range(1, 7 - (31 - day) + 1, 1)]
        day = [d for d in range(day, 31, 1)]
    elif (day >= 26) and (month[0] in d31):
        if month[0] == 12:
            month.append(1)
        else:
            month.append(now.month + 1)
        day_next = [d for d in range(1, 7 - (30 - day) + 1, 1)]
        day = [d for d in range(day, 32, 1)]
    elif (day >= 23) and (month[0] == 2):
        month.append(now.month + 1)
        day_next = [d for d in range(1, 7 - (28 - day) + 1, 1)]
        day = [d for d in range(day, 29, 1)]
    else:
        day = [d for d in range(day, day + 7, 1)]
        day_next = day
    d = day + day_next
    m = [mo for i in range(len(day))] + [mo+1 if mo != 12 else 1 for i in range(len(day_next))]
    # m : day_next가 같게 나오지만 사실상 뒤쪽것은 안쓸거임!

    ## onehot encoding
    indx = d.index(da)  # 날짜의 index
    
    # index에 해당하는 날짜 (사실 input받은 값과 동일, but 어차피 index를 구해야 날씨 찾을 수 있음!)
    month = m[indx]
    day = d[indx]

    # 한자리 일이면 앞에 "0" 붙여줌
    if len(str(day)) != 2:
        target_origin = str(now.year) + str(month) + "0" + str(day)
    else:
        target_origin = str(now.year) + str(month) + str(day)
        

    week = now.weekday() + indx
    # 월 화 수 목 금 토 일
    # 0  1  2  3  4  5  6
    if week >= 7:
        week = week - 7
        
    # 공휴일 & 요일 onehot
    holi = pd.read_csv('data/holi.csv', encoding='CP949').iloc[:,2]

    if int(target_origin) in holi.tolist():    # 공휴일 확인
        hol, xf1, xf2, xf3, xf4, xf5, xf6, xf7 = 0, 0, 0, 0, 0, 0, 0, 0
    else:
        # 요일 onehot
        if week == 0:
            hol, xf1, xf2, xf3, xf4, xf5, xf6, xf7 = 0, 1, 0, 0, 0, 0, 0, 0
        elif week == 1:
            hol, xf1, xf2, xf3, xf4, xf5, xf6, xf7 = 0, 0, 1, 0, 0, 0, 0, 0
        elif week == 2:
            hol, xf1, xf2, xf3, xf4, xf5, xf6, xf7 = 0, 0, 0, 1, 0, 0, 0, 0
        elif week == 3:
            hol, xf1, xf2, xf3, xf4, xf5, xf6, xf7 = 0, 0, 0, 0, 1, 0, 0, 0
        elif week == 4:
            hol, xf1, xf2, xf3, xf4, xf5, xf6, xf7 = 0, 0, 0, 0, 0, 1, 0, 0
        elif week == 5:
            hol, xf1, xf2, xf3, xf4, xf5, xf6, xf7 = 0, 0, 0, 0, 0, 0, 1, 0
        elif week == 6:
            hol, xf1, xf2, xf3, xf4, xf5, xf6, xf7 = 0, 0, 0, 0, 0, 0, 0, 1

    # 날씨 onehot
    weath = weather_api.weather(params={"version": "1",
                  "lat": "37.53255",
                  "lon": "127.10494"
                  })
    wth = weath["weather"]
    # print(weath) # 날씨

    if wth[indx] == 1:
        sunny, cloudy, rainy, snowy = 1, 0, 0, 0
    elif wth[indx] == 2:
        sunny, cloudy, rainy, snowy = 0, 1, 0, 0
    elif wth[indx] == 3:
        sunny, cloudy, rainy, snowy = 0, 0, 1, 0
    elif wth[indx] == 4:
        sunny, cloudy, rainy, snowy = 0, 0, 0, 1
    
    # LightGBM 모델로 predict하기 위한 데이터형태
    data = pd.DataFrame([[hol, xf1, xf2, xf3, xf4, xf5, xf6, xf7, trend, sunny, cloudy, rainy, snowy]])

    result = {
        "data": data,
        "weather": weath["weather"][indx],
        "tmax": str(weath["tmax"][indx])+"℃",
        "tmin": str(weath["tmin"][indx])+"℃"
    }

    return result
