import os
import requests
from flight_data import FlightData

FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com"
# Add your Tequila Search Key
FLIGHT_SEARCH_APIKEY = os.environ["FLIGHT_SEARCH_APIKEY"]


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {
            "apikey": FLIGHT_SEARCH_APIKEY
        }

    def get_city_code(self, city_name):
        """This function utilizes the Tequila Search Locations API to obtain the IATA code associated with a given
        city."""
        parameters = {
            "term": city_name,
            "location_types": "city"
        }
        query_endpoint = f"{FLIGHT_SEARCH_ENDPOINT}/locations/query"
        response = requests.get(url=query_endpoint, params=parameters, headers=self.headers)
        print(response.request.url)
        response.raise_for_status()
        data = response.json()["locations"]
        return data[0]["code"]

    def get_flights(self, from_city_code, to_city_code, from_date, to_date):
        """ Returns flight data if available between two specified cities and within a specified date range."""
        parameters = {
            "fly_from": from_city_code,
            "fly_to": to_city_code,
            "date_from": from_date,
            "date_to": to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        search_endpoint = f"{FLIGHT_SEARCH_ENDPOINT}/v2/search"
        response = requests.get(url=search_endpoint, params=parameters, headers=self.headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:

            # return None
            parameters["max_stopovers"]=1
            response = requests.get(url=search_endpoint, params=parameters, headers=self.headers)
            response.raise_for_status()
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {to_city_code}.")
                return None
            flight_data = FlightData(
                price=data["price"],
                from_city=data["route"][0]["cityFrom"],
                from_airport=data["route"][0]["flyFrom"],
                to_city=data["route"][1]["cityTo"],
                to_airport=data["route"][1]["flyTo"],
                takeoff_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data

        flight_data = FlightData(
            price=data["price"],
            from_city=data["route"][0]["cityFrom"],
            from_airport=data["route"][0]["flyFrom"],
            to_city=data["route"][0]["cityTo"],
            to_airport=data["route"][0]["flyTo"],
            takeoff_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(flight_data.get_formatted_data())
        return flight_data


