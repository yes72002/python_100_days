import requests
from bs4 import BeautifulSoup
import pprint
import smtplib
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


import os
import base64
from email.message import EmailMessage

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from secret_key import TINDER_USERNAME, TINDER_PASSWORD

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

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

URL = "https://tinder.com/"
# print(URL)
driver.get(URL)



# loggin = driver.find_element(By.CLASS_NAME, value="w1u9t036")
loggin = driver.find_element(By.CLASS_NAME, value="Expand").find_element(By.CLASS_NAME, value="Fxs(0)").find_element(By.CSS_SELECTOR, value="div a")
# loggin = driver.find_element(By.XPATH, value='//*[@id="q1434999767"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/')


loggin.click()

facebook = driver.find_element(By.CSS_SELECTOR, value='aria-label="用 Facebook 登入"')
facebook.click()

time.sleep(3)
facebook_email = driver.find_element(By.NAME, value='email')
facebook_email.send_keys(TINDER_USERNAME)

facebook_pass = driver.find_element(By.NAME, value='pass')
# facebook_pass.send_keys("ji3g4m06rup4")
facebook_pass.send_keys(TINDER_PASSWORD)

facebook_login = driver.find_element(By.NAME, value='login')
facebook_login.click()











