from dotenv import load_dotenv
import os
import requests
load_dotenv()

parameters = {
    "lat": 39.9970,
    "lon": 86.3469,
    "appid": os.getenv("API_KEY"),
    "cnt": 4
    }

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")

# int = 0
# weather_list = []

# for x in list:
#     weather_id = list[int]["weather"][0]["id"]
#     description = list[int]["weather"][0]["description"]
#     weather = [int,weather_id,description]
#     weather_list.append(weather)
#     int+=1

# print(weather_list)