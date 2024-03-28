import requests

SHEETY_GET_API = "https://api.sheety.co/sheety/flightDeals/prices/3"


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self, SHEETY_GET_API):
        response = requests.get(SHEETY_GET_API)
        response_data = response.json()
        self.destination_data = response_data["prices"]
        return self.destination_data

    def update_destination(self):
        for row in self.destination_data:
            print(row)
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }

            sheety_put_url = f"https://api.sheety.co/sheety/flightDeals/prices/{row['id']}"
            reponse = requests.put(sheety_put_url,json=new_data)

        # reponse = requests.put(f"{SHEETY_GET_API}/{row['id']}",json=new_data)
        print(reponse.text)





