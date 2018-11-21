import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myapp.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.init_app(app)

# 게시글 table(posts)
class Post(db.Model): # db.Model을 상속받은 것
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True) # sql문과 비슷한 형식!!
    name = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

# 많은 쪽에서 적은 쪽을 참조(즉, 댓글 table에서 게시글 table을 참조)
# 댓글 table(comments)
# class Comment(db.Model):
#     __tablename__ = "comments"
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String, nullable=False)
#     post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)

db.create_all()


# root page
@app.route("/")
def hello():
    return render_template("index.html")

# 게시판 page
@app.route("/board")
def board():
    # myapp.db에 있는 모든 레코드(db의 한 행)를 불러와 보여줌
    # select * from posts;
    posts = Post.query.all() # 리스트 형태로 반환됨!!
    return render_template("board.html", posts=reversed(posts))
    
# 게시판 글쓰기 page
@app.route("/write")
def write():
    return render_template("write.html")

# 게시판 글읽기 page
@app.route("/read")
def read():
    return render_template("read.html")

# 게시판 글 쓸 때 잠깐 스치는 페이지
@app.route("/create")
def create():
    name = request.args.get("name")
    title = request.args.get("title")
    content = request.args.get("content")
    post = Post(name=name, title=title, content=content)
    db.session.add(post) # 데이터베이스에 내용 추가할거야!(session은 추가할 때마다 부르는 거라고 생각하면 됨)
    db.session.commit() # commit으로 확정시킴!(확실히 저장!)
    # return render_template("create.html", name=name, title=title, content=content)
    return redirect("/board") # create.html을 거치지 않고 바로 board.html로 오는 방법

# 게시글 삭제
@app.route("/delete/<int:id>") # id를 받아오는데 int로 바로 변환해줌
def delete(id):
    # 1. 지우려하는 레코드를 선택
    post = Post.query.get(id)
    # 2. 지운다
    db.session.delete(post)
    # 3. 확정하고 DB에 반영한다.
    db.session.commit()
    return redirect("/board")

# 게시글 보기
@app.route("/readpost/<int:id>")
def readpost(id):
    post = Post.query.get(id)
    return render_template("read.html", post=post)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug=True)