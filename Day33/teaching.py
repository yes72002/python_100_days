import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response) # <Response [200]>
# print(response.status_code) # 200
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")
response.raise_for_status()

data = response.json()
# print(data)

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)


# Match Sunset Times with the Current Time
import datetime as dt
# Zhubei
MY_LAT = 24.835065
MY_LONG = 121.010480
parameters = {
    "lat": MY_LAT,
    "log": MY_LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunrise_hour)
print(sunset_hour)


now = dt.datetime.now()
print(now)
year = now.year
month = now.month
weekday = now.weekday() # 0 = Monday, 1 = Tuesday