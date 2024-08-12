import requests
from flight_search import FlightSearch
import os
from dotenv import load_dotenv
load_dotenv()

sheety_url = "https://api.sheety.co/d42ef0c9fcccae63f1a8fa429c085310/flightDeals/prices"
class DataManager:
    def putrequest(self,id,data):
        payload = {
            "price": data
        }
        headers = {
            "Authorization": f"Basic {os.getenv("SHEETY_API")}",
        }
        print(payload)
        requests.put(url=f"{sheety_url}/{id}", json=payload, headers=headers)