from twilio.rest import Client
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.virtual_twilio_number = os.getenv("VIRTUAL_TWILIO_NUMBER")
        self.verified_number = os.getenv("VERIFIED_NUMBER")

    def send_sms(self, price, city_from, fly_from, city_to, fly_to, out_date, return_date):
        client = Client(self.account_sid, self.auth_token)
        message_body=f"Low price alert! Only £{price} to fly from {city_from}-{fly_from} to {city_to}-{fly_to}, from {out_date} to {return_date}."
        print(message_body)
        # message = client.messages \
        #             .create(
        #                 body=message_body,
        #                 # body="test",
        #                 from_=self.virtual_twilio_number,
        #                 to=self.verified_number
        #             )
        # print(message.status)
