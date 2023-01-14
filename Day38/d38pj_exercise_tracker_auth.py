import requests
import os
import datetime
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# --------------------------------------------------------------------------------
# Nutritionix Endpoints
# --------------------------------------------------------------------------------
Nutritionix_APP_ID = os.getenv("Nutritionix_APP_ID")
Nutritionix_API_KEY = os.getenv("Nutritionix_API_KEY")

headers = {
    "Content-Type": "application/json",
    "x-app-id": Nutritionix_APP_ID,
    "x-app-key": Nutritionix_API_KEY,
}

# --------------------------------------------------------------------------------
# Food Lookup Endpoints
# --------------------------------------------------------------------------------
user_params = {
    "query": "for breakfast i ate 2 eggs, bacon, and french toast",
    "timezone": "US/Eastern"
}

food_url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

# response = requests.post(url=food_url, json=user_params, headers=headers)
# print(response.text)

# --------------------------------------------------------------------------------
# Exercise Endpoints
# --------------------------------------------------------------------------------
user_params = {
    # "query": "Run 2 miles and walked for 5km.",
    "query": input("Tell me which exercises you did: "),
}

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_url, json=user_params, headers=headers)
response.raise_for_status()
# print(response.text)
exercise_data = response.json()["exercises"]
# print(exercise_data)
exercise_name = [data["name"] for data in exercise_data]
# print(exercise_name)
exercise_duration = [data["duration_min"] for data in exercise_data]
exercise_calories = [data["nf_calories"] for data in exercise_data]

# --------------------------------------------------------------------------------
# Sheety Endpoints
# --------------------------------------------------------------------------------
# Getting rows
# --------------------------------------------------------------------------------
# GET: https://api.sheety.co/{username}/{projectName}/{sheetName}
sheet_get_url = os.getenv("SHEET_D38_GET_URL")
AUTHORIZATION = os.getenv("D38_AUTHORIZATION")

# print(sheet_get_url)
headers = {
        "Content-Type": "application/json",
        "Authorization": AUTHORIZATION,
    }

response = requests.get(url=sheet_get_url, headers=headers)
# print("response.status_code =", response.status_code) # 200
# print("response.text =", response.text) # data

# --------------------------------------------------------------------------------
# Add a row
# --------------------------------------------------------------------------------
today = datetime.datetime.now()
for i in range(len(exercise_name)):
    exercise_data = {
        "workout":{
            "date": today.strftime("%m/%d/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise_name[i].title(),
            "duration": exercise_duration[i],
            "calories": exercise_calories[i],
        },
    }

    # response = requests.post(url=sheet_get_url, json=exercise_data, headers=headers)
    # print("response.status_code =", response.status_code)
    # print("response.text =", response.text)




