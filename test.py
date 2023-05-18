# import required modules
import json

import requests
def data(city_name):
    try:
        # Enter your API key here
        api_key = ""

        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # Give city name


        # complete_url variable to store
        # complete url address
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        # get method of requests module
        # return response object
        response = requests.get(complete_url)

        # json method of response object
        # convert json format data into
        # python format data
        x = response.json()

        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if x["cod"] != "404":

            # store the value of "main"
            # key in variable y
            y = x["main"]

            main = x["weather"][0]["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]
            current_temperature = round(current_temperature-273)
            temp_min = round(y["temp_min"]-273)
            temp_max = round(y["temp_max"]-273)
            feels_like = round(y["feels_like"]-273)
            wind = x["wind"]["speed"]

            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
            current_humidity = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]
            nm = [x for x in city_name]
            nm[0] = nm[0].upper()
            city_name = "".join(nm)

            # print following values
            c = {"city": city_name, "main": main, "temp": current_temperature, "pres": current_pressure, "humd": current_humidity, 
                "desc": weather_description, "feel": feels_like, "mint": temp_min, "maxt": temp_max, "wind": wind}
            print(c)
            return c

        else:
            print(" City Not Found ")
            return {"temp": 0, "pres": 0, "humd": 0, "desc": "error", "feel": 0, }
        
    except Exception as e:
        print("except" + str(e))
        return {"temp": 0, "pres": 0, "humd": 0, "desc": "error", "feel": 0, }

if __name__ == "__main__":
	data(input("Enter city name : "))
 

