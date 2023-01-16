from data_manager import DataManager
from flight_search import FlightSearch
# from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint


datamanger = DataManager()
flightsearch = FlightSearch()
notification_manager = NotificationManager()
# flight_data = FlightData()


print("Welcome to Jim's Flight Club.")
print("We find the best flight deals and email you.")

# Get users
# user_first_name = input("What is your first name?\n")
# user_last_name = input("What is your last name?\n")
# user_email1 = input("What is your email?\n")
# user_email2 = input("Type your email again.\n")
# # if user_email1 == user_email2:
# #     user_email = user_email1
# # else:
# #     print("Email verification error.")
# user_email = user_email2

user_first_name = "Angela"
user_last_name = "Yu"
user_email = "angela@email.com"

id = 2
# datamanger.edit_user(user_first_name, user_last_name, user_email, id)
users_data = datamanger.get_users()
# print(users_data)

# Getting prices
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
        # pass
        continue
    elif flight_data.price < sheet_row['lowestPrice']:
        # print(flight_data.price)
        notification_manager.send_emails(
           price=flight_data.price, 
           city_from=flight_data.city_from, 
           fly_from=flight_data.fly_from, 
           city_to=flight_data.city_to, 
           fly_to=flight_data.fly_to, 
           out_date=flight_data.out_date, 
           return_date=flight_data.return_date,
           stop_overs=flight_data.stop_overs,
           via_city=flight_data.via_city,
           to_addrs= users_data[0]["email"]
        )


