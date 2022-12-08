import re
from datetime import datetime
from flask import Flask, redirect, url_for, render_template, request
from test import data

app = Flask(__name__)

data_to_images = {"Clouds": ["/icons/wi-cloudy.svg", "cloud_bg.jpg"], "Rain": ["/icons/wi-showers.svg", "rain_bg.jpg"],
                  "Clear": ["/icons/wi-day-sunny.svg", "clear_bg.jpg"], "Snow": ["/icons/wi-snow.svg", "snow_bg.jpg"], "Drizzle":  ["/icons/wi-showers.svg", "rain_bg.jpg"]}


def fillData(weather_data):
    try:
        weather_data["img"], weather_data["bg"] = data_to_images[weather_data["main"]]
    except:
        weather_data["img"], weather_data["bg"] = [
            "/icons/wi-cloudy.svg", "cloud_bg.jpg"]
        print("not in dict yet")

    return weather_data["img"]


@app.route("/", methods=["POST", "GET"])
def home():
    weather_data = {}
    if request.method == "POST":
        city = request.form["city"].strip()
        weather_data = data(str(city))

        fillData(weather_data)

        if weather_data["desc"] == "error":
            weather_data = "error"

        print(weather_data)
    return render_template("index.html", data=weather_data)


@app.route("/hello")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


if __name__ == "__main__":
    app.run(debug=True)
