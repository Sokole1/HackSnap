from flask import Flask, render_template, request, redirect
#import scrape

app = Flask(__name__)

items = []

@app.route("/", methods=["GET", "POST"])
def HackSnap():
    if request.method == "GET":
        return render_template("HackSnap2.html")
    else:
        group = request.form.get("subjectGroup")
        month = request.form.get("examMonth")
        year = request.form.get("examYear")
        items.clear()
        items.append(group)
        items.append(month)
        items.append(year)
        return redirect("/select")

    

@app.route("/select")
def Choose():
    return render_template("HackSnap.html", items=items)



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