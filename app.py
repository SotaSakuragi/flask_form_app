from flask import Flask, render_template, request

app = Flask(__name__)


# GETメソッド、POSTメソッドの追記
# @app.route("/", methods=["GET"])
@app.route("/")
def index_get():
    return render_template("index.html")


# @app.route("/", methods=["POST"])
@app.route("/")
def index_post():
    message = request.form["message"]
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
