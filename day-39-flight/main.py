#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from data_manager import DataManager
from dotenv import load_dotenv
import os

load_dotenv()

flightSearch = FlightSearch()
dataManager = DataManager()

sheety_endpoint = "https://api.sheety.co/d42ef0c9fcccae63f1a8fa429c085310/flightDeals/prices"
headers = {
    "Authorization": f"Basic {os.getenv("SHEETY_API")}",
}
response = requests.get(url=sheety_endpoint, headers=headers)
data = response.json()
sheet_data = data.get("prices", [])
for entry in sheet_data:
    # Does entry have an IATA Code?
    if entry["iataCode"] == "":
        # Get IATA code and update entry
        entry["iataCode"] = flightSearch.get_city(entry["city"]) 
    price = flightSearch.get_price(entry["iataCode"])
    data = entry

    # Update Google Sheet
    dataManager.putrequest(entry["id"], data)
    
