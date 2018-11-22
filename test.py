# from datetime import datetime

# datetime.today()            # 현재 날짜 가져오기
# datetime.today().year        # 현재 연도 가져오기
# datetime.today().month      # 현재 월 가져오기
# datetime.today().day        # 현재 일 가져오기
# datetime.today().hour        # 현재 시간 가져오기

# print(datetime.today(), datetime.today().year, datetime.today().month, datetime.today().day, datetime.today().hour+9)

# print(datetime.today().strftime("%Y%m%d%H%M%S"))    # YYYYmmddHHMMSS 형태의 시간 출력

# print(datetime.today().strftime("%Y/%m/%d %H:%M:%S"))  # YYYY/mm/dd HH:MM:SS 형태의 시간 출력


from datetime import datetime
now = datetime.now() 

time = str(now.hour+9) + ":" + str(now.minute)

time = now.strftime("%Y.%m.%d") + " " + datetime.strptime(time, "%H:%M").strftime("%H:%M")
print(time)