import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "yes72002@gamil.com"
MY_PASSWORD = "xxxx * 4"
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # test
    # iss_latitude = 51.507351
    # iss_longitude = -0.127758
    #Your position is within +5 or -5 degrees of the ISS position.
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour
    # print(hour)
    if hour >= sunset or sunrise >= hour:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    # if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        # if hour >= sunset or sunrise >= hour:
    if is_iss_overhead() and is_night():
        print("pass")
        pass
        # Send email
        # with smtplib.SMTP("smtp.gmal.com") as connection:
        #     connection.starttls()
        #     connection.login(MY_EMAIL, MY_PASSWORD)
        #     connection.sendmail(
        #         from_addr=MY_EMAIL,
        #         to_addrs=MY_EMAIL,
        #         msg=f"Subject:Look up\n\nThe ISS is above you in the sky."
        #     )