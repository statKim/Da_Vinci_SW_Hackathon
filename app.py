from flask import Flask, render_template

app = Flask(__name__)

# root page
@app.route("/")
def hello():
    return render_template("index.html")

# 게시판 page
@app.route("/board")
def board():
    return render_template("board.html")


if __name__ == '__main__':
    app.run(debug=True)