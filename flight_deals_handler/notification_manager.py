import html
import os
import smtplib

import requests

# Add your email and password that you got from email security
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


# Add your Sheety endpoint and bearer token.
USERS_ENDPOINT = os.environ["USERS_ENDPOINT"]
TOKEN = os.environ["TOKEN"]


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.email = EMAIL
        self.password = PASSWORD

    def send_emails(self, body):
        """Using SMTP, this function sends an email containing flight data to all users listed in the Google Sheet."""
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            users = self.get_users()
            for user in users:
                connection.sendmail(from_addr=self.email,
                                    to_addrs=user["email"],
                                    msg=f"Subject:Low price alert!\n\n{body}".encode("utf-8"))

    def get_users(self):
        auth = {
            "Authorization": f"Bearer {TOKEN}"
        }
        response = requests.get(url=USERS_ENDPOINT, headers=auth)
        response.raise_for_status()
        return response.json()["users"]
