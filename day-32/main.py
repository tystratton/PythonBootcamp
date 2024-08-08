import smtplib
import time
import datetime as dt
import random

password = "eujacxmckvtfiprx"
my_email = "occultupdates@gmail.com"
to_email = "nelsonmj242@gmail.com"

# while True:

def get_hour():
    now = dt.datetime.now()
    hour = now.hour
    return hour

def send_email():
    if get_hour() == 20:
        with open("day-32/quotes.txt") as file:
            all_quotes = file.readlines()
            quote = random.choice(all_quotes)
        try:
            connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Manson Quote of the Day\n\n{quote}")
            connection.close()
        except TimeoutError as e:
            print("Error: unable to send email")


send_email()