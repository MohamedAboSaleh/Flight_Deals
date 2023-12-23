# Flight_Deals
This project is a Python-based initiative focused on discovering flight deals. The process involves extracting information from a Google Sheet containing city names, IATA codes, and our specified lowest prices of interest. Subsequently, we conduct a search for available flights, and upon finding a relevant option, we send out emails to notify all users with the pertinent flight details.

## Managing the Google Sheet:
![Screenshot 2023-12-23 215857](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/5e026fd5-55e5-446b-9909-e65a06b733e6)

To handle the Google Sheet, we utilized the Sheety API from [Sheety](https://sheety.co). Through the use of GET, PUT, and POST operations, we effectively administered the sheet.

## Flight Search Process:
In the pursuit of finding flights, we employed the Tequila API from [Tequila Api](https://tequila.kiwi.com/portal/getting-started). Utilizing the search location feature, we extracted the necessary IATA code. Subsequently, our search spanned from tomorrow's date to six months ahead, facilitated by the search functionality.

## Handling Users:
Users are managed through a designated sheet, and enrollment in the club is facilitated by the users_main.py script.

![Screenshot 2023-12-23 220315](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/e740155f-5881-40c7-a2da-cae92f190f86)

When the flight_deals_handler/main.py script is executed and a flight is discovered, notifications are promptly emailed to all registered users.

![Screenshot 2023-12-23 220705](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/6e9b0337-63b2-4eb4-94d0-c420fe9b5872)

![Screenshot 2023-12-23 220642](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/a8016ef2-356a-4ec8-b41a-912f44e1c1fb)


## The alert received upon discovering a flight:
![Screenshot 2023-12-23 220812](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/4332f078-13d0-4f65-8318-abdb8ddadd85)
