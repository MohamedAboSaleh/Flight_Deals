import os

import requests
# Add your Sheety endpoint and bearer token.
PRICES_ENDPOINT = os.environ["PRICES_ENDPOINT"]
TOKEN = os.environ["TOKEN"]


class DataManager:
    def __init__(self):
        self.auth = {
            "Authorization": f"Bearer {TOKEN}"
        }

    def get_flights_from_sheet(self) -> dict:
        """Utilizing the Sheety API, this function requests information for all flights stored in the Google Sheet."""
        response = requests.get(url=PRICES_ENDPOINT, headers=self.auth)
        response.raise_for_status()
        return response.json()["prices"]

    def update_city_code(self, city_code, flight_id):
        flight = {
            "price": {
                "iataCode": city_code,
            }
        }
        response = requests.put(url=f"{PRICES_ENDPOINT}/{flight_id}", json=flight, headers=self.auth)
        response.raise_for_status()