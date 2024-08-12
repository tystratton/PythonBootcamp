from dotenv import load_dotenv
import os
import requests
from datetime import datetime as dt, timedelta
import smtplib
import re
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

password = "eujacxmckvtfiprx"
my_email = "occultupdates@gmail.com"
to_email = "tysonthetyrant@gmail.com"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": os.getenv("STOCK_API_KEY")
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()
#2 days ago
date_yesterday = str(dt.now() - timedelta(days=2))
date_yesterday = date_yesterday.split(" ")[0]

#1 day ago
date_today = str(dt.now() - timedelta(days=1))
date_today = date_today.split(" ")[0]

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
price_today = float(stock_data["Time Series (Daily)"][date_today]["4. close"])

#TODO 2. - Get the day before yesterday's closing stock price
price_yesterday = float(stock_data["Time Series (Daily)"][date_yesterday]["4. close"])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = abs(price_today - price_yesterday)



#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent = diff/price_yesterday * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent > 4: 
#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_parameters = {
    "apiKey": os.getenv("NEWS_API_KEY"),
    "q": COMPANY_NAME,
    }

    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()
#7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    article = news_data["articles"]
#8. - Send each article as a separate message via Twilio. 
    try:
        connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        connection.login(user=my_email,password=password)
        message = (
            "Subject: Price Change Alert\n"
            "From: " + my_email + "\n"
            "To: " + to_email + "\n\n"
            "Price change for: " + STOCK_NAME + "\n" +
            article[0]["title"] + " " + article[0]["url"] + "\n" +
            article[1]["title"] + " " + article[1]["url"] + "\n" +
            article[2]["title"] + " " + article[2]["url"]
        )
        message = re.sub(r'[^\x00-\x7F]+', '', message)
        print(message)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
        connection.close()
    except TimeoutError as e:
        print("Error: unable to send email")

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

