from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")  # 기본 root 페이지
def hello():
    return "hello"


# root 페이지인 "http://127.0.0.1:5000/" 뒤에 단어를 입력하면 페이지에 출력됩니다.
# 예를 들어, "http://127.0.0.1:5000/다섯명" => 페이지에 "hello 다섯명" 출력
@app.route("/<name>")
def john(name):
    return "hello {}".format(name)  # "hello %s" % name  과 같은 결과입니다!!


# "http://127.0.0.1:5000/search"를 주소창에 입력하면
# "templates" 폴더 안의 "search.html"이 페이지로 출력됩니다.
# 그래서 render_template() 함수는 페이지를 이동시켜서 화면을 바꿀 때 사용합니다.
@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/test")
def test():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)