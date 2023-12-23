import sys
from users_manager import UsersManager
users_manager=UsersManager()
print("Welcome to Mohamed's Flight Club.")
print("We find the best flight deals and email you.")

first_name = input("What is your first name?")
last_name = input("What is your last name?")
email1 = "email1"
email2 = "email2"
while email1 != email2:
    email1 = input("What is your email? (or cancel)")
    if email1.lower() == "cancel":
        sys.exit()
    email2 = input("Please verify your email (or cancel):")
    if email2.lower() == "cancel":
        sys.exit()

users_manager.add_user(first_name,last_name,email1)