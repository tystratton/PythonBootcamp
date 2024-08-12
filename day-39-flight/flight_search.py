import requests
from dotenv import load_dotenv
import os

load_dotenv()
amadeus = "https://test.api.amadeus.com/v1"
class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
    
    def _get_new_token(self):
        token_endpoint = f"{amadeus}/security/oauth2/token"

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url=token_endpoint,data=body,headers=header)
        token = response.json()['access_token']
        return token
    
    #---------------------------------------------
    def get_city(self,data):
        city_endpoint = f"{amadeus}/reference-data/locations/cities"
        body = {
            "keyword": data
        }
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        code = requests.get(url=city_endpoint,params=body,headers=headers)
        code = code.json()["data"][0]["iataCode"]
        return code
