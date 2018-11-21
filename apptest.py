import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myapp.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.init_app(app)


# 게시글 table(posts)
class Post(db.Model):  # db.Model을 상속받은 것
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)  # sql문과 비슷한 형식!!
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)


# 많은 쪽에서 적은 쪽을 참조(즉, 댓글 table에서 게시글 table을 참조)
# 댓글 table(comments)
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)


db.create_all()


@app.route("/")
def index():
    # myapp.db에 있는 모든 레코드(db의 한 행)를 불러와 보여줌
    # select * fromm posts;
    posts = Post.query.all()  # 리스트 형태로 반환됨!!
    comments = Comment.query.all()
    return render_template("index.html", posts=reversed(posts), comments=comments)


@app.route("/create")
def create():
    title = request.args.get("title")
    content = request.args.get("content")
    post = Post(title=title, content=content)
    db.session.add(post)  # 데이터베이스에 내용 추가할거야!(session은 추가할 때마다 부르는 거라고 생각하면 됨)
    db.session.commit()  # commit으로 확정시킴!(확실히 저장!)
    # return render_template("create.html", title=title, content=content)
    return redirect("/")  # create.html을 거치지 않고 바로 index.html로 오는 방법


@app.route("/delete/<int:id>")  # id를 받아오는데 int로 바로 변환해줌
def delete(id):
    # 1. 지우려하는 레코드를 선택
    post = Post.query.get(id)
    # 2. 지운다
    db.session.delete(post)
    # 3. 확정하고 DB에 반영한다.
    db.session.commit()
    return redirect("/")


# 수정할 특정 컬럼값을 선택(select) -> 그 이후에 값 수정(update)
@app.route("/edit/<int:id>")
def edit(id):
    # 1. 수정하고자 하는 레코드를 선택
    post = Post.query.get(id)
    # 2. 수정한다
    # post.title = "수정해라!"
    # post.content = "수정내용!"
    # 3. 확정하고 DB에 반영한다.
    # db.session.commit()
    return render_template("edit.html", post=post)


@app.route("/update/<int:id>")
def update(id):
    # 1. 수정하고자 하는 레코드를 선택
    post = Post.query.get(id)
    # 2. 수정한다
    post.title = request.args.get("title")
    post.content = request.args.get("content")
    # 3. 확정하고 DB에 반영한다.
    db.session.commit()
    return redirect("/")


@app.route("/create_comment")
def create_comment():
    # comment 테이블에 입력받은 내용을 저장
    content = request.args.get("comment_content")
    post_id = int(request.args.get("post_id"))
    comment = Comment(content=content, post_id=post_id)
    db.session.add(comment)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)