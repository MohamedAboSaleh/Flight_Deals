# Flight_Deals
This project is a Python-based initiative focused on discovering flight deals. The process involves extracting information from a Google Sheet containing city names, IATA codes, and our specified lowest prices of interest. Subsequently, we conduct a search for available flights, and upon finding a relevant option, we send out emails to notify all users with the pertinent flight details.

## Managing the Google Sheet:
![Screenshot 2023-12-12 185949](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/d73fe4c6-9bde-4e1a-be30-195e284bc8d7)

To handle the Google Sheet, we utilized the Sheety API from [Sheety](https://sheety.co). Through the use of GET, PUT, and POST operations, we effectively administered the sheet.

## Flight Search Process:
In the pursuit of finding flights, we employed the Tequila API from [Tequila Api](https://tequila.kiwi.com/portal/getting-started). Utilizing the search location feature, we extracted the necessary IATA code. Subsequently, our search spanned from tomorrow's date to six months ahead, facilitated by the search functionality.

## Handling Users:
Users are managed through a designated sheet, and enrollment in the club is facilitated by the users_main.py script.

![Screenshot 2023-12-12 191508](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/ee9c895b-ff22-4537-946c-bd340e9ad306)

When the flight_deals_handler/main.py script is executed and a flight is discovered, notifications are promptly emailed to all registered users.

![Screenshot 2023-12-12 191423](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/c41d5528-8464-4c53-856f-ee5ad8a6c475)
![Screenshot 2023-12-12 191447](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/7d604251-7c01-4ba1-a51c-70b633323f3d)

## The alert received upon discovering a flight:
![Screenshot 2023-12-12 191710](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/1d40464b-c82b-47dd-bc8a-1d5e383f92ea)
