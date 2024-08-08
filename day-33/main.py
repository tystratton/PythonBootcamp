import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].spplit(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].spplit(":")[0])
time_now = datetime.now()
print(data)