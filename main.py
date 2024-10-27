import os
import requests
from datetime import datetime

GENDER = "MALE"
WEIGHT_KG = "64"
HEIGHT_CM = "172"
AGE = "25"

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

nutritionist_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

user_input = input("Tell me which exercise you did: ")

parameters = {
    "query": user_input,
    "gender": GENDER,
    "age": AGE,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM
}

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

response = requests.post(url=nutritionist_endpoint, json=parameters, headers=headers)
print(response.json())

sheety_endpoint = os.environ["sheety_endpoint"]

today = (datetime.now()).strftime("%m/%d/%Y")
time = (datetime.now()).strftime("%X")

for exercise in response.json()["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

headers1 = {
    "Authorization": f"Bearer {os.environ["token"]}"
}

response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=headers1)
