##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import smtplib
import random

MY_EMAIL = "yes72002@gamil.com"
MY_PASSWORD = "xxxx * 4"

now = dt.datetime.now()
now_year = now.year
now_month = now.month
now_day = now.day
# now_weekday = now.weekday()

data = pandas.read_csv("birthdays.csv")
birthday = data.to_dict(orient="records")
# print(birthday)

letter_temp = ["letter_1", "letter_2", "letter_3"]

for date in birthday:
    # print(date)
    if now_month == date["month"] and now_day == date["day"]:
        letter_choose = random.choice(letter_temp)
        with open(f"letter_templates/{letter_choose}.txt") as letter:
            contents = letter.read()
        contents_new = contents.replace("[NAME]", date["name"])
        # print(contents_new)

        # Send email
        # with smtplib.SMTP("smtp.gmal.com") as connection:
        #     connection.starttls()
        #     connection.login(MY_EMAIL, MY_PASSWORD)
        #     connection.sendmail(
        #         from_addr=MY_EMAIL,
        #         to_addrs=date["email"],
        #         msg=f"Subject:Monday Motivation\n\n{contents_new}"
        #     )



