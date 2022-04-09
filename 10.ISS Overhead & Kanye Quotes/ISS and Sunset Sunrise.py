import requests
import datetime

ISS_LINK = "http://api.open-notify.org/iss-now.json"
SUN_LINK = "https://api.sunrise-sunset.org/json"
MY_LAT = 40.876550
MY_LONG =
parameter = {
   "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}
# response = requests.get(url=ISS_LINK)
# response.raise_for_status()
#
# data = response.json()
# lat = data["iss_position"]["latitude"]
# long = data["iss_position"]["longitude"]
# iss_position = (lat,long)
# print(iss_position)

now = datetime.datetime.now()

print(now)


response = requests.get(url=SUN_LINK,params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunset_hour = sunset.split("T")[1].split(":")[0]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
print(sunset,sunrise)
print(sunset_hour)
print(sunrise_hour)


