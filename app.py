import requests
import os
from dotenv import load_dotenv

# load_dotenv()

from dotenv import dotenv_values
config = dotenv_values(".env")

# class name should be Pascal case
class Forecast:
    def __init__(self, city):
        self.city = city
        self.url = f"https://api.tomorrow.io/v4/weather/realtime?location={self.city}&units=metric&apikey={config['API_KEY']}"
        self.headers = {"accept": "application/json"}
        self.response = None
        self.values = None

    # Make different methods for each attribute, so in future if you have to change any functionality
    # you can change that particular method itself instead of making all changes in `get_forecast()`
    def extract_values(self):
        self.values = self.response["data"]["values"]

    def display_temperature(self):
        print(f"Temperature: {self.values['temperature']} C")
        
    def display_humidity(self):
        print(f"Humidity: {self.values['humidity']} %")
        
    def display_wind_speed(self):
        print(f"Wind Speed: {self.values['windSpeed']} km/h")


    def get_forecast(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            
            if response.status_code != 200:
                # The API key can be invalid as well
                raise ValueError("\nInvalid city name or API KEY. Please try again.")
            else:
                self.response  = response.json()
                self.extract_values()
                print(f'\n{"*"*30} Weather Forecast {"*"*30}')
                print(self.response["location"]["name"])
                self.display_temperature()
                self.display_humidity()
                self.display_wind_speed()

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print("\nAn error occurred while fetching the weather data. Please try again later.")  
                


def main():  
    while True:
        print(f'\n{"*"*30} Weather Forecast App {"*"*30}')
        print("1. Enter to get weather forecast.")
        print("0. Exit app.")
        choice = input("\nPlease enter your choice: ")

        match choice:
            case "1":
                location = input("\nPlease enter city name: ")
                forecast = Forecast(location)
                forecast.get_forecast()
            case "0":
                break
            case _:
                print("\nInvalid choice")

if __name__ == "__main__":
    main()
