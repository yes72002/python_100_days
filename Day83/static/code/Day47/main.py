import requests
from bs4 import BeautifulSoup
import pprint
import smtplib

import os
import base64
from email.message import EmailMessage

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

def gmail_send_message(message_subject, message_content):
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

    credentials_json = "C:/Users/jimli/OneDrive - NVIDIA Corporation/NVIDIA/Python/python 100 days/Day47/yes72002.json"
    credentials_json = "C:/Users/jimli/OneDrive - NVIDIA Corporation/NVIDIA/Python/python 100 days/Day47/imperialtheory.json"
    credentials_json = "C:/Users/Jim/OneDrive - 國立陽明交通大學/python_100_days/Day47/imperialtheory.json"

    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_json, SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()

        message.set_content(message_content)
        message["To"] = "imperialtheory@gmail.com"
        message["From"] = "imperialtheory@gmail.com"
        message["Subject"] = message_subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        # pylint: disable=E1101
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        print(f'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(f"An error occurred: {error}")
        send_message = None
    return send_message



# Belkin
URL = "https://www.amazon.com/-/zh_TW/Belkin-MagSafe-%E7%9B%B8%E6%A9%9F%E6%94%AF%E6%9E%B6-%E9%81%A9%E7%94%A8%E6%96%BC-MacBook%E3%80%81iPhone/dp/B0BJNHF6WJ?th=1"
# Insatnt Pot
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# print(URL)

response = requests.get(URL)
yc_web_page = response.text
# print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")

# songs = soup.select(selector="span[aria-hidden='true']")
price_tag = soup.select_one(selector="._p13n-desktop-sims-fbt_price_p13n-sc-price-animation-wrapper__3PzN2 .a-row .a-price .a-offscreen")
price = price_tag.get_text() # $99.95
price = float(price[1::]) # 99.95
print(f"price = {price}")

purchase = soup.title.string
print(f"purchase = {purchase}")


# send email
if price <= 10:
    message_subject = f"Subject:Monday Motivation"
    message_content = f"{purchase} is now ${price}\n{URL}"
    gmail_send_message(message_subject, message_content)
    print("Send Email Succeed!")