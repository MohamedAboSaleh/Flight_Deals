import os

import requests

USERS_ENDPOINT = os.environ["USERS_ENDPOINT"]
TOKEN = os.environ["TOKEN"]


class UsersManager:
    def __init__(self):
        self.auth = {
            "Authorization": f"Bearer {TOKEN}"
        }

    def get_users(self):
        response = requests.get(url=USERS_ENDPOINT, headers=self.auth)
        response.raise_for_status()
        return response.json()["users"]

    def add_user(self, first_name, last_name, email):
        user = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=USERS_ENDPOINT, json=user, headers=self.auth)
        response.raise_for_status()
        print("You have been added to the club!")

