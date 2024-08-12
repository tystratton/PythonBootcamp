import requests
from dotenv import load_dotenv
from datetime import datetime
import os

USERNAME = "tystratton"
ID = "graph1"
today =  datetime.now()
load_dotenv()
headers = {
    "X-USER-TOKEN": os.getenv("TOKEN")
}


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": os.getenv("TOKEN"),
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Coding Graph",
    "unit": "minute",
    "type": "int",
    "color": "shibafu",
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3" 
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

deletepixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/20240811"
response = requests.delete(url=deletepixel_endpoint,headers=headers)
print(response.text)
