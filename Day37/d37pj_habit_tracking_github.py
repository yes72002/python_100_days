import requests
from twilio.rest import Client


TOKEN = "YOUR TOKEN"
USERNAME = "YOUR USERNAME"
AGREETERMSOFSERVICE = "yes"
NOTMINOR = "yes"
GRAPHID = "graph1"

# --------------------------------------------------------------------------------
# Create a User
# --------------------------------------------------------------------------------
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": AGREETERMSOFSERVICE,
    "notMinor": NOTMINOR,
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# --------------------------------------------------------------------------------
# Create a Graphic
# --------------------------------------------------------------------------------
# POST - /v1/users/<username>/graphs
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit": "day",
    "type": "int",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# test URL
# https://pixe.la/v1/users/yes72002/graphs/graph1.html

# --------------------------------------------------------------------------------
# Post a Pixel
# --------------------------------------------------------------------------------
# POST - /v1/users/<username>/graphs/<graphID>
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
import datetime

today = datetime.datetime.now()
# print(today.strftime("%Y%m%d")) # 20221228
# print(today.strftime("%Y-%m-%d")) # 2022-12-28
# today = datetime.datetime(year=2022, month=12, day=27)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    # "quantity": "1",
    "quantity": input("How many classes did you take today?"),
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text) # {"message":"Success.","isSuccess":true}

# --------------------------------------------------------------------------------
# Update a Pixel
# --------------------------------------------------------------------------------
# PUT - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
update_date = "20221228"
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{update_date}"

update_config = {
    "quantity": "2",
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text) # {"message":"Success.","isSuccess":true}

# --------------------------------------------------------------------------------
# Delete a Pixel
# --------------------------------------------------------------------------------
# DELETE - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
delete_date = "20221227"
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{delete_date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text) # {"message":"Success.","isSuccess":true}

