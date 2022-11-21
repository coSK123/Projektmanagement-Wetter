import re
from datetime import datetime
from flask import Flask, redirect, url_for, render_template, request
from test import data 

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    weather_data = {}
    if request.method == "POST":
        city = request.form["city"]
        weather_data = data(str(city))
        weather_data["city"] = city
    return render_template("index.html", data=weather_data)

@app.route("/hello")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
if __name__ == "__main__":
    app.run(debug=True)