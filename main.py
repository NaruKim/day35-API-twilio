import requests
from twilio.rest import Client

api_key = "4d169e0498485cfa84507e94f4f9512b"

LATITUDE = 13.756331
LONGITUDE = 100.501762

account_sid = 'AC5fb6a8d0670c958f4c6d3e9f200998e0'
auth_token = '35addb36245f3a0fcf44d6b9b1c33593'


parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Python test message from Naru. Raining in Bangkok",
        from_='+15103302089',
        to='+'
    )
    print(message.status)