from flask import Flask, render_template, request, redirect
from geturl import get_link
from data import *

app = Flask(__name__)

items = []
url_history = {}


@app.route("/", methods=["GET", "POST"])
def HackSnap():
    if request.method == "GET":
        return render_template("HackSnap2.html", items=items, url=url_history)
    else:
        group = request.form.get("subjectGroup")
        subject = request.form.get("specificSubject")
        subject = subject.capitalize()
        level = request.form.get("levelSelect")
        monthYear = request.form.get("examMonthYear") 
        month, year = monthYear.split(" ", 1)
        # month = request.form.get("examMonth")
        # year = request.form.get("examYear")re
        items.clear()
        #items.append(group)
        items.append(subject)
        items.append(level)
        items.append(year)
        items.append(month)
        url = get_link(group, subject, level, month, year)
        url_history[" ".join(items)] = url
        return render_template("HackSnap2.html", items=items, url=url_history)

    

# @app.route("/select")
# def Choose():
#     return render_template("HackSnap2.html", items=items, url=url_history)

if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/")
# def index():
#     return render_template("index.html", items=items)

# @app.route("/og")
# def og():
#     name = request.args.get("name")
#     return render_template("og.html", name=name)

# @app.route("/hello", methods=["GET", "POST"])
# def hello():
#     if request.method == "GET":
#         return render_template("hello.html")
#     else:
#         item = request.form.get("cars")
#         item2 = request.form.get("year")
#         items.clear()
#         items.append(item)
#         items.append(item2)
#         return redirect("/")


    # cars = request.args.get("cars")
    # return render_template("hello.html", cars=cars)