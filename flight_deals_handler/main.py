from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

FROM_CITY_CODE = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_flights_from_sheet()

for flight in sheet_data:
    if flight["iataCode"] == "":
        city_code = flight_search.get_city_code(flight["city"])
        data_manager.update_city_code(city_code, flight["id"])

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_month_from_today = (datetime.now() + timedelta(days=(6 * 30))).strftime("%d/%m/%Y")

for flight in sheet_data:
    flight_data = flight_search.get_flights(FROM_CITY_CODE, flight["iataCode"], tomorrow, six_month_from_today)
    if flight_data:
        if flight_data.price < flight["lowestPrice"]:
            message = (f"Only {flight_data.price} £ to fly from "
                       f"{flight_data.from_city}-{flight_data.from_airport}"
                       f" to {flight_data.to_city}-{flight_data.to_airport}, "
                       f"from {flight_data.takeoff_date} to {flight_data.return_date}.")
            if flight_data.stop_overs>0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            notification_manager.send_emails(message)
            # print(str(message.encode("utf-8")))


