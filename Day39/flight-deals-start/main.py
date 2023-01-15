#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
# from flight_data import FlightData
from notification_manager import NotificationManager

datamanger = DataManager()
flightsearch = FlightSearch()
notification_manager = NotificationManager()
# flight_data = FlightData()

# Getting rows
sheet_data = datamanger.get_prices()
# print(sheet_data)

# Edit a row, add IATA Code
id = 2
for country in sheet_data:
    # print(country)
    if country["iataCode"] == "":
        iata = flightsearch.get_iata_code(country["city"])
        # print(iata)
        datamanger.edit_price(iata, country["id"])

# Search lowest price
for sheet_row in sheet_data[:]:
    fly_to_country = sheet_row["iataCode"]
    flight_data = flightsearch.search(fly_to_country)
    # print(flight_data)
    
    if flight_data == None: # No flights
        pass
    elif flight_data.price < sheet_row['lowestPrice']:
        print(flight_data.price)
        notification_manager.send_sms(
           price=flight_data.price, 
           city_from=flight_data.city_from, 
           fly_from=flight_data.fly_from, 
           city_to=flight_data.city_to, 
           fly_to=flight_data.fly_to, 
           out_date=flight_data.out_date, 
           return_date=flight_data.return_date
        )



