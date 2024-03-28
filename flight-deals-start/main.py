import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime,timedelta


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


data_manager = DataManager()
flight_search = FlightSearch()
ORIGIN_CITY_IATA = 'LON'

sheety_api = "https://api.sheety.co/b715d9d72a4b58b1dd86fa26f57b1f03/flightDeals/prices"
response = requests.get(sheety_api)
sheet_data =  (response.json())["prices"]
# print(sheet_data)




if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.getDestination(row["city"])
    data_manager.update_destination()

data_manager.destination_data = sheet_data
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta (days = 6*30)

for destination in sheet_data:
    flight = flight_search.check_flights(
       ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time = tomorrow,
        to_time = six_months_from_today
    )



