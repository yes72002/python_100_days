import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

MY_LAT = 24.835065
MY_LONG = 121.010480
# Environment Variables
owm_api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    # "exclude": "hourly,daily",
    "appid": owm_api_key
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
# response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
# print(weather_data)
weather_data_id = weather_data["weather"][0]["id"]
# print(weather_data_id)
if weather_data_id < 700:
    print("Bring an Umbrella.")
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an umbrella.",
                        from_='+15737790844',
                        to='+886975852779'
                    )

    # print(message.sid)
    print(message.status)

# One Call
# will_rain = False
# weather_slice = weather_data["hourly"][:12]
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
# if will_rain:
#     print("Bring an Umbrella.")
