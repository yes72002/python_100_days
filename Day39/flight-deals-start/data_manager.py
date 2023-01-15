import requests
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

sheet_prices_url = os.getenv("SHEET_D39_GET_URL")
sheet_users_url = os.getenv("SHEET_D40_GET_URL")
AUTHORIZATION = os.getenv("D39_AUTHORIZATION")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    # pass
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": AUTHORIZATION,
        }

    def get_prices(self):
        response = requests.get(url=sheet_prices_url, headers=self.headers)
        # print("response.status_code =", response.status_code) # 200
        data = response.json()
        # print(data)
        prices_data = data["prices"]
        # print(prices_data)
        return prices_data

    def edit_price(self, iata_code, id):
        sheet_edit_url = f"{sheet_prices_url}/{id}"
        edit_data = {
            "price":{
                # "city": "Berlin",
                "iataCode": iata_code,
                # "lowestPrice": "42",
            },
        }
        response = requests.put(url=sheet_edit_url, json=edit_data, headers=self.headers)
        print("response.status_code =", response.status_code) # 200
        data = response.json()
        print(data)

