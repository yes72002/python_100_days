# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import requests
import datetime as dt
from newsapi import NewsApiClient
from twilio.rest import Client

# GET STOCK PRICE
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "YOUR STOCK_API_KEY"
# GETS NEWS
NEWS_API_KEY = "YOUR NEWS_API_KEY"
# SEND EMAIL
TWILIO_SID = "YOUR TWILIO_SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO_AUTH_TOKEN"
VIRTUAL_TWILIO_NUMBER = "YOUR VIRTUAL_TWILIO_NUMBER"
VERIFIED_NUMBER = "YOUR VERIFIED_NUMBER"

# GET STOCK PRICE
now = dt.datetime.now()
now_year = now.year
now_month = now.month
now_day = now.day

parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY
}
# print stock url
# print(f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval=60min&apikey={STOCK_API_KEY}")
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()

data_today = response.json()["Time Series (60min)"][f"{now_year}-{now_month}-{now_day-1} 16:00:00"]["4. close"]
try:
    data_yesterday = response.json()["Time Series (60min)"][f"{now_year}-{now_month}-{now_day-2} 16:00:00"]["1. open"]
except KeyError:
    data_yesterday = response.json()["Time Series (60min)"][f"{now_year}-{now_month}-{now_day-5} 16:00:00"]["1. open"]
data_today = float(data_today)
data_yesterday = float(data_yesterday)
# print(data_today)
# print(data_yesterday)
percentage = round((data_yesterday - data_today) * 100 / data_yesterday, 2)
# print(percentage)
if percentage >= 0:
    percentage_text = f"TSLA 🔺 {percentage}%."
    # percentage_text = f"TSLA increase {percentage}%."
else:
    percentage_text = f"TSLA 🔻 {percentage}%."
    # percentage_text = f"TSLA decrease {percentage}%."
# print(percentage_text)


# GETS NEWS
parameters = {
    "q": "tesla",
    "from": "2022-12-28",
    "to": "2022-12-28T19:12:26",
    "sortBy": "publishedAt",
    "pageSize": 3, # 3 news
    "page": 1, # content size
    "language": "en",
    # "country": "us", # error with language
    "apiKey": NEWS_API_KEY
}

response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
# print news url
# q_text = parameters["q"]
# from_text = parameters["from"]
# to_text = parameters["to"]
# sortBy_text = parameters["sortBy"]
# pageSize_text = parameters["pageSize"]
# page_text = parameters["page"]
# language_text = parameters["language"]
# apikey_text = parameters["apiKey"]
# print(f"https://newsapi.org/v2/everything?q={q_text}&from={from_text}&to={to_text}&sortBy={sortBy_text}&pageSize={pageSize_text}&page={page_text}&language={language_text}&apikey={apikey_text}")
response.raise_for_status()

news_content = response.json()["articles"]
# print(news_content)


# SEND EMAIL
account_sid = TWILIO_SID
auth_token = TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)
for i in range(0, 3):
    headline = news_content[i]["title"]
    brief = news_content[i]["description"]
    message_body = f"{percentage_text}\nHEADLINE: {headline}\nBrief: {brief}"
    print(message_body)

    message = client.messages \
                    .create(
                        # body=message_body,
                        body="test",
                        from_=VIRTUAL_TWILIO_NUMBER,
                        to=VERIFIED_NUMBER
                    )
                    
    print(message.status)
