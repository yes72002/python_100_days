import smtplib

# my_email = "imperialtheory@gamil.com"
# password = "yuanjin"
# password2 = "xxxx * 4"

# connect = smtplib.SMTP("smtp.gmail.com")
# connect.starttls()
# connect.login(user=my_email, password=password2)
# connect.sendmail(from_addr=my_email, to_addrs="yes72002@gmail.com", msg="Hello")
# connect.close()

# UPDATE
# https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
# UPDATE: This feature is no longer supported as of May 30th, 2022.
# See https://support.google.com/accounts/answer/6010255?hl=en&visit_id=637896899107643254-869975220&p=less-secure-apps&rd=1#zippy=%2Cuse-an-app-password


import datetime as dt
import random

# MY_EMAIL = "imperialtheory@gamil.com"
MY_EMAIL = "yes72002@gamil.com"
# password = "yuanjin"
MY_PASSWORD = "xxxx * 4"

now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday() # 0 = Monday, 1 = Tuesday
print(type(now)) # datetime.datetime
print(type(year)) # int
print(year)
print(weekday)

date_of_birth = dt.datetime(year=1995, month=12, day=15) # hour default value = 0
print(date_of_birth)
date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)

# challenge: send a quote
if weekday == 1: # Tuesday
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        # print(all_quotes)
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmal.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
