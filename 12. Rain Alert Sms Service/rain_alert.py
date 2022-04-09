import time
import os
from twilio.rest import Client

API_KEY = os.environ.get("OWN_API_KEY")


LAT = 40.741895

LONG = -73.989308

account_sid = os.environ.get("OWN_SID")
auth_token = os.environ.get("OWN_AUTH_TOKEN")

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
parameter = {
    "lat" : LAT,
    "lon" : LONG,
    "exclude" : "current,minutely,daily,alerts",
    "appid" : API_KEY
}
import requests

response = requests.get(ENDPOINT,params=parameter)
response.raise_for_status()
# print(response)
data = response.json()
# print(data)

hourly_data = data["hourly"]
hourly_data = hourly_data[:12]      #only 12 Hours needed
# print(hourly_data)

weather_code_list = [hourly_data[i]["weather"][0]["id"] for i in range(len(hourly_data))]
# print(weather_code_list)

def is_umbrella_needed()->bool:
    for data in weather_code_list :
        if data<700 :
            return True
    return  False

print(weather_code_list)
will_rain = is_umbrella_needed()
if will_rain :
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's Going To Rain! Bring An Umbrella",
        from_='+12542326917',
        to='+19734755307'
    )

    print(message.status)
print(auth_token)