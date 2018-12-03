import os
from flask import Flask, render_template, request, redirect, json
from flask_sqlalchemy import SQLAlchemy # ORM 사용하기 위해 (DB 구축)
from datetime import datetime           # 날짜, 시간 얻기 위함
import requests                         # 크롤링
from bs4 import BeautifulSoup           # 크롤링
import lightgbm as lgb                  # 혼잡도 예측 모델 predict 위함
import dataEncoding                     # 혼잡도 예측 모델 predict하기 위한 데이터 형식에 맞추기 위함

app = Flask(__name__)   # 우리가 만든 flask app의 서버 이름(?)

# sqlite3를 이용해서 DB 구축하기 위한 단계
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myapp.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.init_app(app)

# 아래에는 DB table 생성
# 게시글 table(posts)
class Post(db.Model): # db.Model을 상속받은 것
    __tablename__ = "posts"                         # DB 내에서의 table 이름
    id = db.Column(db.Integer, primary_key=True)    # sql문과 비슷한 형식!!
    name = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)
    date_update = db.Column(db.String, nullable=False)

# 많은 쪽에서 적은 쪽을 참조 (즉, 댓글 table에서 게시글 table을 참조)
# 댓글 table(comments)
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)

# 혼잡도 예측 table(congest)
class Congest(db.Model):
    __tablename__ = "congests"
    id = db.Column(db.Integer, primary_key=True)    # id(사실상 순서 구분하기 위함)
    date = db.Column(db.String, nullable=False)     # 혼잡도 알고싶은 날짜
    people = db.Column(db.Integer, nullable=False)  # 생활인구(response)
    hol = db.Column(db.Integer, nullable=False)     # 공휴일
    sun = db.Column(db.Integer, nullable=False)	    # 일요일
    mon = db.Column(db.Integer, nullable=False)	    # 월요일
    tue = db.Column(db.Integer, nullable=False)     # 화요일
    wed = db.Column(db.Integer, nullable=False)     # 수요일
    thu = db.Column(db.Integer, nullable=False)     # 목요일
    fri = db.Column(db.Integer, nullable=False)     # 금요일
    sat = db.Column(db.Integer, nullable=False)     # 토요일
    sun = db.Column(db.Integer, nullable=False)     # 일요일
    trend = db.Column(db.Integer, nullable=False)   # 네이버트렌드
    sunny = db.Column(db.Integer, nullable=False)   # 맑음
    cloudy = db.Column(db.Integer, nullable=False)  # 구름많음
    rainy = db.Column(db.Integer, nullable=False)   # 비
    snowy = db.Column(db.Integer, nullable=False)   # 눈

db.create_all()     # 모든 table을 생성하겠다!!


# 메인 page
@app.route("/")
def root():
    # 매일 바뀌는 롯데월드의 운영시간을 크롤링
    url = "http://adventure.lotteworld.com/kor/usage-guide/service/index.do"
    req = requests.get(url).text
    doc = BeautifulSoup(req, "html.parser")
    time = doc.select(".openDiv .leftArea .timeInfo .time .txt > span")[0].text
    time2 = doc.select(".openDiv .leftArea .timeInfo .time .txt > span")[1].text.split(" ")[1]
    # url이 "/"이면 "index.html"을 띄우고 time, time2의 값을 서버에서 보내주겠다!
    return render_template("index.html", time=time, time2=time2)


# 게시판 page
# 게시글의 제목, 작성자, 작성일, 조회수를 표시 => DB에서 가져옴
@app.route("/board/<int:page>")     # int형식의 page변수의 값을 url에서 받아옴
def board(page):
    # myapp.db에 있는 모든 레코드(db의 한 행)를 불러와 보여줌
    # select * from posts; 과 같은 구문이라고 생각하면 됨
    posts = Post.query.all()    # 리스트 형태로 반환됨!!
    comments = Comment.query.all()
    # 게시글에 해당하는 댓글 수 세는 코드
    comment_count = {}
    for p in posts:
        count = 0
        for c in comments:
            if p.id == c.post_id:
                count += 1
        comment_count[p] = count
    if len(posts) % 10 != 0:
        numpage = (len(posts) // 10) + 1  # 한 페이지에 10개의 게시글만 오게 하고 나머지는 다음 쪽수로 넘겨야 볼수 있게!
    else:
        numpage = (len(posts) // 10)    # 만약 10개의 게시글이 존재한다면 1쪽만 있게 하기 위해
    numpage = range(1, numpage+1, 1)    # 넘길 때 리스트 형태로 넘김
    end = (len(posts)) - (10*(page - 1))
    start = end - 10
    if (len(posts) - 10*page) <= 0:  # 이 페이지가 마지막일 때
        posts = posts[0:len(posts)-10*(page-1)]   # 있는 것까지만 보여주기
    else:
        posts = posts[start:end]
    if len(posts) >= 2:  # 최근것부터 나와야 하기 때문
        posts = reversed(posts)
    return render_template("board.html", posts=posts, comment_count=comment_count, numpage=numpage, page=page)


# 게시판 글쓰기 page
@app.route("/write")
def write():
    return render_template("write.html")


# 게시판 글 쓸 때 잠깐 스치는 페이지 => 서버에서만 이 과정이 이루어지고 바로 "board/1" 페이지로 넘겨버림
# => 그로인해 이 페이지는 눈으로는 보이지 않음
@app.route("/create")
def create():
    # 작성 시간 입력하기 위한 부분
    now = datetime.now()
    time = now.strftime("%Y.%m.%d %H:%M")
    # DB에 입력할 값들 가져옴
    name = request.args.get("name")
    password = request.args.get("password")
    title = request.args.get("title")
    content = request.args.get("content")
    count = 0
    date = time
    date_update = time
    # SQL문의 Insert 구문과 동일
    post = Post(name=name, password=password, title=title, content=content,
                count=count, date=date, date_update=date_update)
    db.session.add(post)            # 데이터베이스에 내용 추가할거야!(session은 추가할 때마다 부르는 거라고 생각하면 됨)
    db.session.commit()             # commit으로 확정시킴!(확실히 저장!)
    return redirect("/board/1")     # create.html을 거치지 않고 바로 board.html로 오는 방법


# 게시글 수정하는 페이지로 넘어가게 하는 부분
@app.route("/edit/<int:id>")
def edit(id):
    # 수정하고자 하는 레코드를 선택
    post = Post.query.get(id)   # 우리가 선택한 게시글을 가져옴 (id로 구분돼있기 때문)
    return render_template("edit.html", post=post)


# 게시글 update
@app.route("/update/<int:id>")
def update(id):
    # 작성 시간 입력하기 위한 부분
    now = datetime.now()
    time = now.strftime("%Y.%m.%d %H:%M")
    # 1. 수정하고자 하는 레코드를 선택
    post = Post.query.get(id)
    # 2. 수정한다
    post.title = request.args.get("title")
    post.content = request.args.get("content")
    post.date_update = time
    # 3. 확정하고 DB에 반영한다.
    db.session.commit()    
    return redirect("/board/1")


# 게시글 삭제
@app.route("/delete/<int:id>")  # id를 받아오는데 int로 바로 변환해줌
def delete(id):
    # 1. 지우려하는 레코드를 선택
    post = Post.query.get(id)
    comment = Comment.query.filter_by(post_id=id).all()     # 게시글에 해당하는 댓글도 삭제하기 위해 가져옴
    # 2. 지운다
    db.session.delete(post)
    for i in range(len(comment)):
        db.session.delete(comment[i])
        # db.session.commit()   # 해야할까??
    # 3. 확정하고 DB에 반영한다.
    db.session.commit()
    return redirect("/board/1")


# 게시글 보기
@app.route("/read/<int:id>")
def readpost(id):
    post = Post.query.get(id)
    post.count = post.count + 1     # 조회수 + 1
    db.session.commit()
    post = Post.query.get(id)       # 누른 게시글에 해당하는 내용 모두 가져옴
    comment = Comment.query.all()   # 댓글 모두 가져옴
    return render_template("read.html", post=post, comment=comment)


# 댓글 저장하는 부분 => 여기도 잠깐 스치기만 하는 페이지 (눈에 안보임)
@app.route("/create_comment")
def create_comment():
    # comment 테이블에 입력받은 내용을 저장
    name = request.args.get("name")
    content = request.args.get("comment_content")
    post_id = int(request.args.get("post_id"))
    comment = Comment(name=name, content=content, post_id=post_id)  # SQL의 Insert문과 동일
    db.session.add(comment)
    db.session.commit()
    return redirect("/read/"+str(post_id))


# 혼잡도 예측 page
@app.route("/predict")
def predict():
    # 날짜 선택하는 부분
    # 1. 오늘부터 7일 이내까지 보여줘야함
    # 2. 7일이 다음달로 넘어가는 경우를 모두 생각해줘야함(30일, 31일, 28일 등)
    now = datetime.now()
    d30 = [4, 6, 9, 11]             # 30일인 달
    d31 = [1, 3, 5, 7, 8, 10, 12]   # 31일인 달
    month = [now.month]
    day = now.day
    danger = True
    if (day >= 25) and (month[0] in d30):       # 오늘부터 7일 이후까지 보여줄건데 30일이 넘어갈 경우
        month.append(now.month + 1)
        day_next = [d for d in range(1, 7-(31-day)+1, 1)]
        day = [d for d in range(day, 31, 1)]
    elif (day >= 26) and (month[0] in d31):     # 31일인 달의 경우
        if month[0] == 12:               # 오늘이 12월이면
            month.apped(1)               # 다음달은 1월이기 때문에 1을 append
        else:                            # 오늘이 12월이 아니면
            month.append(now.month+1)    # 다음달 추가
        day_next = [d for d in range(1, 7-(30-day)+1, 1)]
        day = [d for d in range(day, 32, 1)]
    elif (day >= 23) and (month[0] == 2):       # 2월인 경우
        month.append(now.month + 1)
        day_next = [d for d in range(1, 7-(28-day)+1, 1)]
        day = [d for d in range(day, 29, 1)]
    else:
        day = [d for d in range(day, day+7, 1)]     # 달이 넘어가지 않는 경우
        day_next = day
        danger = False
    d = day + day_next  # 오늘부터 7일에 해당하는 일수
    return render_template("predict.html", month=month, day=day, day_next=day_next, danger=danger, d=d)

# # 혼잡도 예측 결과 페이지
# @app.route("/prediction", methods=["POST"]) # form태그랑 route 모두 post로 하면 post
# def prediction():
#     place = request.form["place"]
#     month = request.form["month"]
#     if int(month) == datetime.now().month:   # select 태그로 받아온 월이 이번달이면
#         day = request.form["day"]
#     else:
#         day = request.form["day_next"]
#     value = month + "\n" + day + "\n" + place
#     return value
#


# 혼잡도 예측페이지에서 Ajax 이용하여 비동기로 예측 결과 출력
# 즉, 화면전환 없이 이 서버를 거치고 바로 현재 페이지에 출력!!
# redirect 하는 경우와는 다름, redirect는 새로고침과 같은 일시적인 화면전환이 일어나지만 Ajax는 전혀 화면전환이 없음
@app.route("/testing/<int:month>/<int:day>/<int:day_next>/<string:place>")   # 입력된 월, 일, 장소 데이터 가져옴
def testing(month, day, day_next, place):
    if month == datetime.now().month:   # 이번달일 경우
        day = day
    else:
        day = day_next
    # app.logger.debug(month)
    # app.logger.debug(day)

    # input 날짜 입력
    mo = month
    da = day
    if place == "롯데월드":
        place = "lotte"
        encode = dataEncoding.dataencoding(int(mo), int(da), place)
        data = encode["data"]
        bst = lgb.Booster(model_file='model/model_lotte.txt')
        weather = encode["weather"]
        tmax = encode["tmax"]
        tmin = encode["tmin"]
    elif place == "어린이대공원":
        place = "park"
        encode = dataEncoding.dataencoding(int(mo), int(da), place)
        data = encode["data"]
        bst = lgb.Booster(model_file='model/model_park.txt')
        weather = encode["weather"]
        tmax = encode["tmax"]
        tmin = encode["tmin"]
    elif place == "경복궁":
        place = "gyeongbok"
        encode = dataEncoding.dataencoding(int(mo), int(da), place)
        data = encode["data"]
        bst = lgb.Booster(model_file='model/model_gyeong.txt')
        weather = encode["weather"]
        tmax = encode["tmax"]
        tmin = encode["tmin"]
    elif place == "덕수궁":
        place = "duksu"
        encode = dataEncoding.dataencoding(int(mo), int(da), place)
        data = encode["data"]
        bst = lgb.Booster(model_file='model/model_duk.txt')
        weather = encode["weather"]
        tmax = encode["tmax"]
        tmin = encode["tmin"]
    elif place == "남산":
        place = "nam"
        encode = dataEncoding.dataencoding(int(mo), int(da), place)
        data = encode["data"]
        bst = lgb.Booster(model_file='model/model_nam.txt')
        weather = encode["weather"]
        tmax = encode["tmax"]
        tmin = encode["tmin"]
    else:
        place = "buk"
        encode = dataEncoding.dataencoding(int(mo), int(da), place)
        data = encode["data"]
        bst = lgb.Booster(model_file='model/model_buk.txt')
        weather = encode["weather"]
        tmax = encode["tmax"]
        tmin = encode["tmin"]

    # 조건에 해당하는 예측 model로 predict
    y_pred = bst.predict(data)

    # 4분위수로 값을 4단계의 값으로 구분 (한산, 적정, 다소혼잡, 혼잡)
    if place == "park":
        if y_pred < 20851:
            pred = "한산"
            img = "../static/img/c1.png"
        elif y_pred < 23378:
            pred = "적정"
            img = "../static/img/b1.png"
        elif y_pred < 24488:
            pred = "다소혼잡"
            img = "../static/img/a1.png"
        else:
            pred = "혼잡"
            img = "../static/img/s1.png"
    elif place == "lotte":
        if y_pred < 54092:
            pred = "한산"
            img = "../static/img/c1.png"
        elif y_pred < 60393:
            pred = "적정"
            img = "../static/img/b1.png"
        elif y_pred < 65424:
            pred = "다소혼잡"
            img = "../static/img/a1.png"
        else:
            pred = "혼잡"
            img = "../static/img/s1.png"
    elif place == "nam":
        if y_pred < 23801:
            pred = "한산"
            img = "../static/img/c1.png"
        elif y_pred < 30866:
            pred = "적정"
            img = "../static/img/b1.png"
        elif y_pred < 32208:
            pred = "다소혼잡"
            img = "../static/img/a1.png"
        else:
            pred = "혼잡"
            img = "../static/img/s1.png"
    elif place == "gyeongbok":
        if y_pred < 19469:
            pred = "한산"
            img = "../static/img/c1.png"
        elif y_pred < 21697:
            pred = "적정"
            img = "../static/img/b1.png"
        elif y_pred < 23005:
            pred = "다소혼잡"
            img = "../static/img/a1.png"
        else:
            pred = "혼잡"
            img = "../static/img/s1.png"
    elif place == "duksu":
        if y_pred < 49204:
            pred = "한산"
            img = "../static/img/c1.png"
        elif y_pred < 72569:
            pred = "적정"
            img = "../static/img/b1.png"
        elif y_pred < 76118:
            pred = "다소혼잡"
            img = "../static/img/a1.png"
        else:
            pred = "혼잡"
            img = "../static/img/s1.png"
    elif place == "buk":
        if y_pred < 10571:
            pred = "한산"
            img = "../static/img/c1.png"
        elif y_pred < 12624:
            pred = "적정"
            img = "../static/img/b1.png"
        elif y_pred < 13075:
            pred = "다소혼잡"
            img = "../static/img/a1.png"
        else:
            pred = "혼잡"
            img = "../static/img/s1.png"

    # 해당 날짜에 대응되는 날씨 이미지와 단어 출력하기 위해
    if weather == 1:
        weather = "../static/img/sunny.png"
        wea_status = "맑음"
    elif weather == 2:
        weather = "../static/img/cloudy.png"
        wea_status = "흐림"
    elif weather == 3:
        weather = "../static/img/rainy.png"
        wea_status = "비"
    else:
        weather = "../static/img/snowy.png"
        wea_status = "눈"

    if (datetime.now().month == 12) & (mo == 1):    # 오늘은 12월인데 예측하고 싶은 날은 내년 1월일 때
        year = datetime.now().year + 1
    else:
        year = datetime.now().year
    if len(str(da)) == 1:   # 1~9일인 경우에는 "09"로 표현하기 위함
        da = "0" + str(da)
    time = str(year) + "." + str(mo) + "." + da  # ex) 2018.11.30

    # 위에서 정리한 데이터를 묶어서 json 형태로 값을 서버에서 보내줌
    data = {
        "value": float(y_pred),      # 예측값
        "pred": pred,                # 예측값에 해당하는 단어 (ex) 한산)
        "img": img,                  # 단계로 구분된 예측값에 해당하는 이미지
        "weather": weather,          # 날씨
        "tmax": tmax,                # 최고기온
        "tmin": tmin,                # 최저기온
        "wea_status": wea_status,    # 날씨 상태 (ex) 구름많음)
        "time": time                 # 날짜
    }

    res = encode["data"]    # input 데이터, DB에 저장하기 위해

    # input값과 결과값 DB에 저장
    conjest = Congest(date=time, people=int(y_pred), hol=int(res[0]),mon=int(res[1]), tue=int(res[2]), wed=int(res[3]), thu=int(res[4]),fri=int(res[5]), sat=int(res[6]), sun=int(res[7]), trend=int(res[8]),sunny=int(res[9]), cloudy=int(res[10]), rainy=int(res[11]), snowy=int(res[12]))
    db.session.add(conjest)
    db.session.commit()

    return json.dumps(data)     # data를 json형태로 보냄


# flask 서버를 구동시키는 부분
if __name__ == '__main__':
    # app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug=True)
    app.run(debug=True)     # 코드가 수정되면 자동으로 서버가 다시 시작됨