from flask import Flask, render_template, request

app = Flask(__name__)


# GETメソッド、POSTメソッドの追記
@app.route("/", methods=["GET", "POST"])
def index():
    # もしGETリクエストだった場合はindex.htmlを表示
    if request.method == "GET":
        return render_template("index.html")
    else:
        # もしPOSTリクエストだった場合はindex.htmlでmessage変数を使う
        message = request.form['message']
        return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
