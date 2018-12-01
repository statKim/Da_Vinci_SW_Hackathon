library(glue)
library(XML)
library(stringr)

api.key <- 'GJdKU2SKJ6oYQgTSsQrkT9BH2hIF%2FG6qtztAeyJHv9Zp31YlWhl%2FCKMmz0fKJnmxtPyQT9TY49AQqtpEeFCw9A%3D%3D'

url.format <- 
  'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo?ServiceKey={key}&solYear={year}&solMonth={month}'

holiday.request <- 
  function(key, year, month) glue(url.format)

# request and read data : year 2017
days<-c()
date<-c()
for(m in 1:12){
  data <- xmlToList(holiday.request(api.key, 2018, str_pad(m, 2, pad=0)))
  items <- data$body$items
  for(item in items){
    if(item$isHoliday == 'Y') days<-append(days, item$dateName); date<-append(date, item$locdate)
  }
}
holi <- data.frame(days,date)

holi$date<- as.character(holi$date)

#====================================
library(dplyr)

peo_201803_ori <- read.csv("C:/Users/Jiwan/Downloads/LOCAL_PEOPLE_DONG_201803/LOCAL_PEOPLE_DONG_201803.csv",encoding="UTF-8", stringsAsFactors=FALSE,skip = 1,header = F)
peo_201804_ori <- read.csv("C:/Users/Jiwan/Downloads/LOCAL_PEOPLE_DONG_201804/LOCAL_PEOPLE_DONG_201804.csv",encoding="UTF-8", stringsAsFactors=FALSE,skip = 1,header = F)
peo_201805_ori <- read.csv("C:/Users/Jiwan/Downloads/LOCAL_PEOPLE_DONG_201805/LOCAL_PEOPLE_DONG_201805.csv",encoding="UTF-8", stringsAsFactors=FALSE,skip = 1,header = F)
peo_201806_ori <- read.csv("C:/Users/Jiwan/Downloads/LOCAL_PEOPLE_DONG_201806/LOCAL_PEOPLE_DONG_201806.csv",encoding="UTF-8", stringsAsFactors=FALSE,skip = 1,header = F)
peo_201807_ori <- read.csv("C:/Users/Jiwan/Downloads/LOCAL_PEOPLE_DONG_201807/LOCAL_PEOPLE_DONG_201807.csv",encoding="UTF-8", stringsAsFactors=FALSE,skip = 1,header = F)
peo_201808_ori <- read.csv("C:/Users/Jiwan/Downloads/LOCAL_PEOPLE_DONG_201808/LOCAL_PEOPLE_DONG_201808.csv",encoding="UTF-8", stringsAsFactors=FALSE,skip = 1,header = F)
peo_201809_ori <- read.csv("C:/Users/Jiwan/Downloads/LOCAL_PEOPLE_DONG_201809/LOCAL_PEOPLE_DONG_201809.csv",encoding="UTF-8", stringsAsFactors=FALSE,skip = 1,header = F)
peo_201810_ori <- read.csv("C:/Users/Jiwan/Downloads/LOCAL_PEOPLE_DONG_201810/LOCAL_PEOPLE_DONG_201810.csv",encoding="UTF-8", stringsAsFactors=FALSE,skip = 1,header = F)

aa <- c("03","04","05","06","07","08","09","10")



#################
park<-data.frame(NA,NA,NA,NA)
j<- 0
for (i in aa){
  j <- j+1
  assign(paste0("peo_2018",i),get(paste0("peo_2018",i,"_ori"))[1:4])
  assign(paste0("peo_2018",i) , get(paste0("peo_2018",i)) %>% filter( V3 == 11215780 ) )
  print(dim(get(paste0("peo_2018",i))))
  if (j>1){
    park <- rbind( park , get(paste0("peo_2018",i)))
  }
  else {
    park <- get(paste0("peo_2018",i))
  }
} 
# 9월 18일~ 21일 데이터가 없음
dim(park)[1] == 744+720+744+720+744+720+624+744
head(park); tail(park)




#################
lotte<-data.frame(NA,NA,NA,NA)
j<- 0
for (i in aa){
  j <- j+1
  assign(paste0("peo_2018",i),get(paste0("peo_2018",i,"_ori"))[1:4])
  assign(paste0("peo_2018",i) , get(paste0("peo_2018",i)) %>% filter( V3 == 11710680 ) )
  print(dim(get(paste0("peo_2018",i))))
  if (j>1){
    lotte <- rbind( lotte , get(paste0("peo_2018",i)))
  }
  else {
    lotte <- get(paste0("peo_2018",i))
  }
} 
# 9월 18일~ 21일 데이터가 없음
dim(lotte)[1] == 744+720+744+720+744+720+624+744
head(lotte); tail(lotte)



#################
nam<-data.frame(NA,NA,NA,NA)
j<- 0
for (i in aa){
  j <- j+1
  assign(paste0("peo_2018",i),get(paste0("peo_2018",i,"_ori"))[1:4])
  assign(paste0("peo_2018",i) , get(paste0("peo_2018",i)) %>% filter( V3 == 11140570	 ) )
  print(dim(get(paste0("peo_2018",i))))
  if (j>1){
    nam <- rbind( nam , get(paste0("peo_2018",i)))
  }
  else {
    nam <- get(paste0("peo_2018",i))
  }
} 
# 9월 18일~ 21일 데이터가 없음
dim(nam)[1] == 744+720+744+720+744+720+624+744
head(nam); tail(nam)



#################
gyeong<-data.frame(NA,NA,NA,NA)
j<- 0
for (i in aa){
  j <- j+1
  assign(paste0("peo_2018",i),get(paste0("peo_2018",i,"_ori"))[1:4])
  assign(paste0("peo_2018",i) , get(paste0("peo_2018",i)) %>% filter( V3 == 11110515 ) )
  print(dim(get(paste0("peo_2018",i))))
  if (j>1){
    gyeong <- rbind( gyeong , get(paste0("peo_2018",i)))
  }
  else {
    gyeong <- get(paste0("peo_2018",i))
  }
} 
# 9월 18일~ 21일 데이터가 없음
dim(gyeong)[1] == 744+720+744+720+744+720+624+744
head(gyeong); tail(gyeong)



#################
duk<-data.frame(NA,NA,NA,NA)
j<- 0
for (i in aa){
  j <- j+1
  assign(paste0("peo_2018",i),get(paste0("peo_2018",i,"_ori"))[1:4])
  assign(paste0("peo_2018",i) , get(paste0("peo_2018",i)) %>% filter( V3 == 11140520	 ) )
  print(dim(get(paste0("peo_2018",i))))
  if (j>1){
    duk <- rbind( duk , get(paste0("peo_2018",i)))
  }
  else {
    duk <- get(paste0("peo_2018",i))
  }
} 
# 9월 18일~ 21일 데이터가 없음
dim(duk)[1] == 744+720+744+720+744+720+624+744
head(duk); tail(duk)



#################
buk<-data.frame(NA,NA,NA,NA)
j<- 0
for (i in aa){
  j <- j+1
  assign(paste0("peo_2018",i),get(paste0("peo_2018",i,"_ori"))[1:4])
  assign(paste0("peo_2018",i) , get(paste0("peo_2018",i)) %>% filter( V3 == 11110600	 ) )
  print(dim(get(paste0("peo_2018",i))))
  if (j>1){
    buk <- rbind( buk , get(paste0("peo_2018",i)))
  }
  else {
    buk <- get(paste0("peo_2018",i))
  }
} 
# 9월 18일~ 21일 데이터가 없음
dim(buk)[1] == 744+720+744+720+744+720+624+744
head(buk); tail(buk)

# park,lotte,nam,gyeong,duk,buk : 날씨 / 시간 / 장소코드 / 생활인구
# holi : 공휴일 데이터




################################################
### 롯데월드 생활인구 & 공휴일 & 요일 데이터 ###
################################################

# park,lotte,nam,gyeong,duk,buk : 날씨 / 시간 / 장소코드 / 생활인구
# holi : 공휴일 데이터
# 
names(lotte)<-c("date","time","code","people")
lotte %>% filter(time==15) -> lotte
lotte$date<- as.character(lotte$date)
day_levels <- c("일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일")
# 일요일 1부터 토요일 7까지.
as.numeric(factor(weekdays(as.Date(lotte$date,"%Y%m%d")), levels=day_levels, ordered=TRUE)) -> lotte$weekday
lotte %>% mutate( holiday = as.numeric(date %in% holi$date) )
head(lotte)

xf <- factor(lotte$weekday, levels = 1:7)
d <- model.matrix( ~ xf - 1)
lotte %>%
  mutate( holiday = as.numeric(date %in% holi$date) ) %>%
  select(date,people,holiday) -> lotte
data.frame(lotte,as.data.frame(d)) -> lotte

for (i in 1:nrow(lotte)){
  if (lotte[i,3] == 1){
    lotte[i,4:10] = c(0,0,0,0,0,0,0)
  }
}

################################################
### 롯데월드 트렌드  데이터 ###
################################################

library(xlsx)
trend_lotte <- read.xlsx2("C:/Users/Jiwan/Downloads/datalab_lotte.xlsx",sheetIndex=1,startRow=7,stringsAsFactors=F)
str(trend_lotte)
trend_lotte[,2]<-as.numeric(trend_lotte[,2])
names(trend_lotte) <- c("date","naver")

trend<-c()
for (i in 1:nrow(trend_lotte)){
  trend<-append(trend, sum(trend_lotte[i:(i+6),2])/7 )
}
c(rep(NA,7),trend)->trend1
length(trend1) -> length_trend
data.frame( rbind(trend_lotte,NA) , trend=trend1[1:(length_trend-6)] ) -> trend_lotte1
str(trend_lotte1)
gsub("-", "", trend_lotte1$date) -> trend_lotte1$date
trend_lotte1[,-2]->trend_lotte1







################################################
### 어린이대공원 생활인구 & 공휴일 & 요일 데이터 ###
################################################

# park,lotte,nam,gyeong,duk,buk : 날씨 / 시간 / 장소코드 / 생활인구
# holi : 공휴일 데이터
# 
library(dplyr)

names(park)<-c("date","time","code","people")
park %>% filter(time==15) -> park
park$date<- as.character(park$date)
day_levels <- c("일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일")
# 일요일 1부터 토요일 7까지.
as.numeric(factor(weekdays(as.Date(park$date,"%Y%m%d")), levels=day_levels, ordered=TRUE)) -> park$weekday
park %>% mutate( holiday = as.numeric(date %in% holi$date) )
head(park)

xf <- factor(park$weekday, levels = 1:7)
d <- model.matrix( ~ xf - 1)
park %>%
  mutate( holiday = as.numeric(date %in% holi$date) ) %>%
  select(date,people,holiday) -> park
data.frame(park,as.data.frame(d)) -> park

for (i in 1:nrow(park)){
  if (park[i,3] == 1){
    park[i,4:10] = c(0,0,0,0,0,0,0)
  }
}

################################################
### 어린이대공원트렌드  데이터 ###
################################################

library(xlsx)
trend_park <- read.xlsx2("C:/Users/Jiwan/Downloads/datalab_park.xlsx",sheetIndex=1,startRow=7,stringsAsFactors=F)
str(trend_park)
trend_park[,2]<-as.numeric(trend_park[,2])
names(trend_park) <- c("date","naver")

trend<-c()
for (i in 1:nrow(trend_park)){
  trend<-append(trend, sum(trend_park[i:(i+6),2])/7 )
}
c(rep(NA,7),trend)->trend1
length(trend1) -> length_trend
data.frame( rbind(trend_park,NA) , trend=trend1[1:(length_trend-6)] ) -> trend_park1
str(trend_park1)
gsub("-", "", trend_park1$date) -> trend_park1$date
trend_park1[,-2]->trend_park1




################################################
### 남산. 생활인구 & 공휴일 & 요일 데이터 ###
################################################

# park,lotte,nam,gyeong,duk,buk : 날씨 / 시간 / 장소코드 / 생활인구
# holi : 공휴일 데이터
# 
library(dplyr)

names(nam)<-c("date","time","code","people")
nam %>% filter(time==15) -> nam
nam$date<- as.character(nam$date)
day_levels <- c("일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일")
# 일요일 1부터 토요일 7까지.
as.numeric(factor(weekdays(as.Date(nam$date,"%Y%m%d")), levels=day_levels, ordered=TRUE)) -> nam$weekday
nam %>% mutate( holiday = as.numeric(date %in% holi$date) )
head(nam)

xf <- factor(nam$weekday, levels = 1:7)
d <- model.matrix( ~ xf - 1)
nam %>%
  mutate( holiday = as.numeric(date %in% holi$date) ) %>%
  select(date,people,holiday) -> nam
data.frame(nam,as.data.frame(d)) -> nam

for (i in 1:nrow(nam)){
  if (nam[i,3] == 1){
    nam[i,4:10] = c(0,0,0,0,0,0,0)
  }
}

################################################
### 남산 트렌드  데이터 ###
################################################

library(xlsx)
trend_nam <- read.xlsx2("C:/Users/Jiwan/Downloads/datalab_nam.xlsx",sheetIndex=1,startRow=7,stringsAsFactors=F)
str(trend_nam)
trend_nam[,2]<-as.numeric(trend_nam[,2])
names(trend_nam) <- c("date","naver")

trend<-c()
for (i in 1:nrow(trend_nam)){
  trend<-append(trend, sum(trend_nam[i:(i+6),2])/7 )
}
c(rep(NA,7),trend)->trend1
length(trend1) -> length_trend
data.frame( rbind(trend_nam,NA) , trend=trend1[1:(length_trend-6)] ) -> trend_nam1
str(trend_nam1)
gsub("-", "", trend_nam1$date) -> trend_nam1$date
trend_nam1[,-2]->trend_nam1




################################################
### 경복궁 생활인구 & 공휴일 & 요일 데이터 ###
################################################

# park,lotte,nam,gyeong,duk,buk : 날씨 / 시간 / 장소코드 / 생활인구
# holi : 공휴일 데이터
# 
library(dplyr)

names(gyeong)<-c("date","time","code","people")
gyeong %>% filter(time==15) -> gyeong
gyeong$date<- as.character(gyeong$date)
day_levels <- c("일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일")
# 일요일 1부터 토요일 7까지.
as.numeric(factor(weekdays(as.Date(gyeong$date,"%Y%m%d")), levels=day_levels, ordered=TRUE)) -> gyeong$weekday
gyeong %>% mutate( holiday = as.numeric(date %in% holi$date) )
head(gyeong)

xf <- factor(gyeong$weekday, levels = 1:7)
d <- model.matrix( ~ xf - 1)
gyeong %>%
  mutate( holiday = as.numeric(date %in% holi$date) ) %>%
  select(date,people,holiday) -> gyeong
data.frame(gyeong,as.data.frame(d)) -> gyeong

for (i in 1:nrow(gyeong)){
  if (gyeong[i,3] == 1){
    gyeong[i,4:10] = c(0,0,0,0,0,0,0)
  }
}

################################################
### 경복궁 트렌드  데이터 ###
################################################

library(xlsx)
trend_gyeong <- read.xlsx2("C:/Users/Jiwan/Downloads/datalab_gyeong.xlsx",sheetIndex=1,startRow=7,stringsAsFactors=F)
str(trend_gyeong)
trend_gyeong[,2]<-as.numeric(trend_gyeong[,2])
names(trend_gyeong) <- c("date","naver")

trend<-c()
for (i in 1:nrow(trend_gyeong)){
  trend<-append(trend, sum(trend_gyeong[i:(i+6),2])/7 )
}
c(rep(NA,7),trend)->trend1
length(trend1) -> length_trend
data.frame( rbind(trend_gyeong,NA) , trend=trend1[1:(length_trend-6)] ) -> trend_gyeong1
str(trend_gyeong1)
gsub("-", "", trend_gyeong1$date) -> trend_gyeong1$date
trend_gyeong1[,-2]->trend_gyeong1




################################################
### 덕수궁 생활인구 & 공휴일 & 요일 데이터 ###
################################################

# park,lotte,nam,gyeong,duk,buk : 날씨 / 시간 / 장소코드 / 생활인구
# holi : 공휴일 데이터
# 
library(dplyr)

names(duk)<-c("date","time","code","people")
duk %>% filter(time==15) -> duk
duk$date<- as.character(duk$date)
day_levels <- c("일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일")
# 일요일 1부터 토요일 7까지.
as.numeric(factor(weekdays(as.Date(duk$date,"%Y%m%d")), levels=day_levels, ordered=TRUE)) -> duk$weekday
duk %>% mutate( holiday = as.numeric(date %in% holi$date) )
head(duk)

xf <- factor(duk$weekday, levels = 1:7)
d <- model.matrix( ~ xf - 1)
duk %>%
  mutate( holiday = as.numeric(date %in% holi$date) ) %>%
  select(date,people,holiday) -> duk
data.frame(duk,as.data.frame(d)) -> duk

for (i in 1:nrow(duk)){
  if (duk[i,3] == 1){
    duk[i,4:10] = c(0,0,0,0,0,0,0)
  }
}

################################################
###  덕수궁  트렌드  데이터 ###
################################################

library(xlsx)
trend_duk <- read.xlsx2("C:/Users/Jiwan/Downloads/datalab_duk.xlsx",sheetIndex=1,startRow=7,stringsAsFactors=F)
str(trend_duk)
trend_duk[,2]<-as.numeric(trend_duk[,2])
names(trend_duk) <- c("date","naver")

trend<-c()
for (i in 1:nrow(trend_duk)){
  trend<-append(trend, sum(trend_duk[i:(i+6),2])/7 )
}
c(rep(NA,7),trend)->trend1
length(trend1) -> length_trend
data.frame( rbind(trend_duk,NA) , trend=trend1[1:(length_trend-6)] ) -> trend_duk1
str(trend_duk1)
gsub("-", "", trend_duk1$date) -> trend_duk1$date
trend_duk1[,-2]->trend_duk1



################################################
### 북촌한옥마을 생활인구 & 공휴일 & 요일 데이터 ###
################################################

# park,lotte,nam,gyeong,duk,buk : 날씨 / 시간 / 장소코드 / 생활인구
# holi : 공휴일 데이터
# 
library(dplyr)

names(buk)<-c("date","time","code","people")
buk %>% filter(time==15) -> buk
buk$date<- as.character(buk$date)
day_levels <- c("일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일")
# 일요일 1부터 토요일 7까지.
as.numeric(factor(weekdays(as.Date(buk$date,"%Y%m%d")), levels=day_levels, ordered=TRUE)) -> buk$weekday
buk %>% mutate( holiday = as.numeric(date %in% holi$date) )
head(buk)

xf <- factor(buk$weekday, levels = 1:7)
d <- model.matrix( ~ xf - 1)
buk %>%
  mutate( holiday = as.numeric(date %in% holi$date) ) %>%
  select(date,people,holiday) -> buk
data.frame(buk,as.data.frame(d)) -> buk

for (i in 1:nrow(buk)){
  if (buk[i,3] == 1){
    buk[i,4:10] = c(0,0,0,0,0,0,0)
  }
}

################################################
### 북촌한옥마을 트렌드  데이터 ###
################################################

library(xlsx)
trend_buk <- read.xlsx2("C:/Users/Jiwan/Downloads/datalab_buk.xlsx",sheetIndex=1,startRow=7,stringsAsFactors=F)
str(trend_buk)
trend_buk[,2]<-as.numeric(trend_buk[,2])
names(trend_buk) <- c("date","naver")

trend<-c()
for (i in 1:nrow(trend_buk)){
  trend<-append(trend, sum(trend_buk[i:(i+6),2])/7 )
}
c(rep(NA,7),trend)->trend1
length(trend1) -> length_trend
data.frame( rbind(trend_buk,NA) , trend=trend1[1:(length_trend-6)] ) -> trend_buk1
str(trend_buk1)
gsub("-", "", trend_buk1$date) -> trend_buk1$date
trend_buk1[,-2]->trend_buk1


################################################
### 기상변수 만들기 ### park,lotte,nam,gyeong,duk,buk
################################################

library(xlsx)
weather_data <- read.xlsx2("C:/Users/Jiwan/Downloads/data_weather.xlsx",sheetIndex=1,startRow=1,stringsAsFactors=F)
weather_data[,1:5]->weather_data
names(weather_data)<-c("date","sunny","cloudy","rainy","snowy")

################################################
### 데이터s Join ### park,lotte,nam,gyeong,duk,buk
################################################
dim(lotte)
merge(
  merge(lotte, trend_lotte1, all.x=TRUE)
  ,weather_data, all.x=TRUE) -> lotte_final
merge(
  merge(park, trend_park1, all.x=TRUE)
  ,weather_data, all.x=TRUE) -> park_final
merge(
  merge(nam, trend_nam1, all.x=TRUE)
  ,weather_data, all.x=TRUE) -> nam_final
merge(
  merge(gyeong, trend_gyeong1, all.x=TRUE)
  ,weather_data, all.x=TRUE) -> gyeong_final
merge(
  merge(duk, trend_duk1, all.x=TRUE)
  ,weather_data, all.x=TRUE) -> duk_final
merge(
  merge(buk, trend_buk1, all.x=TRUE)
  ,weather_data, all.x=TRUE) -> buk_final


write.csv(lotte_final,"lotte.csv")
write.csv(park_final,"park.csv")
write.csv(nam_final,"nam.csv")
write.csv(gyeong_final,"gyeong.csv")
write.csv(duk_final,"duk.csv")
write.csv(buk_final,"buk.csv")

summary(lotte_final$people)


