import requests
import os
import datetime
from flight_data import FlightData

from dotenv import find_dotenv, load_dotenv
from pprint import pprint

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

tequila_location_url = os.getenv("TEQUILA_LOCATION_URL")
tequila_search_url = os.getenv("TEQUILA_SEARCH_URL")
tequila_api_key = os.getenv("TEQUILA_API_KEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.today = datetime.date.today()
        self.tomorrow = self.today + datetime.timedelta(days=1)
        self.next_month = self.today + datetime.timedelta(days=31)
        # self.next_month = self.today + datetime.timedelta(days=11)
        # print(self.tomorrow.strftime("%m/%d/%Y"))
        # print(self.next_month.strftime("%m/%d/%Y"))
        self.headers = {
            "Content-Type": "application/json",
            "apikey": tequila_api_key,
        }
    
    def get_iata_code(self, city):
        location_data = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(url=tequila_location_url, params=location_data, headers=self.headers)
        # print("response.status_code =", response.status_code) # 200
        data = response.json()
        # print(data)
        iata_code = data["locations"][0]["code"]
        return iata_code
        
    def search(self, fly_to):
        # print(fly_to)
        search_data = {
            # "fly_from": "TPE", # Taiwan
            "fly_from": "LON", # London
            "fly_to": fly_to,
            "dateFrom": self.tomorrow.strftime("%d/%m/%Y"),
            "dateTo": self.next_month.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1, # returns the cheapest flights
            "max_stopovers": 0,
        }
        
        response = requests.get(url=tequila_search_url, params=search_data, headers=self.headers)
        # print("response.status_code =", response.status_code) # 200
        try:
            data = response.json()["data"][0]
            # pprint(data)
        except IndexError:
            print(f"No flights found for {fly_to}")
            return None
        
        flight_data = FlightData(
            price=data["price"],
            city_from=data["route"][0]["cityFrom"],
            fly_from=data["route"][0]["flyFrom"],
            city_to=data["route"][0]["cityTo"],
            fly_to=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data