import requests
import os
from dotenv import find_dotenv, load_dotenv
from pprint import pprint

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

TEQUILA_GET_URL = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_API_KEY = "p9MwIzZ_VjQUaiaEd2Mg8iBIXPWQlxE4"

# tequila_get_url = os.getenv("TEQUILA_GET_URL")
# tequila_get_url = TEQUILA_GET_URL
# tequila_api_key = os.getenv("TEQUILA_API_KEY")
# print(tequila_api_key)
headers = {
    "Content-Type": "application/json",
    "apikey": TEQUILA_API_KEY,
}

location_data = {
    "term": "Paris",
    "location_types": "city",
}
response = requests.get(url=TEQUILA_GET_URL, params=location_data, headers=headers)
print("response.status_code =", response.status_code) # 200
# print("response.text =", response.text) # data
pprint(response.json())
iata_code = response.json()["locations"][0]["code"]
pprint(iata_code)
