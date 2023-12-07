from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("student.html")


@app.route("/result", methods=["POST", "GET"])
def show():
    if request.method == "POST":
        n = request.form.get("name")
        m = request.form.get("maths")
        c = request.form.get("coding")
        l = request.form.get("language")
        return render_template("result.html", name=n, maths=m, coding=c, language=l)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)