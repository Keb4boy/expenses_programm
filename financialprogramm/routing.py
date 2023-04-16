from financialprogramm.db import insert_all, insert_categories, insert_names, select_finance
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def root(data='Hello, world'):
    return render_template("root.html", data=data)

@app.route("/url", methods=["POST"])
def button():
    return redirect(url_for("root"))


@app.route("/form")
def templates():
    return render_template("button.html")

@app.route("/urls", methods=["GET", "POST"])
def urls():
    if request.method == "POST":
        return redirect(url_for("root", data="hi"))
    else:
        return redirect(url_for("root"))
        

if __name__ == '__main__':
    app()