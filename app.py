import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

class Forecast:
    def __init__(self, city):
        self.city = city
        self.url = f"https://api.tomorrow.io/v4/weather/realtime?location={self.city}&units=metric&apikey={config["API_KEY"]}"
        self.headers = {"accept": "application/json"}
        self.response = None
        self.values = None

    def find_values(self):
        self.values = self.response["data"]["values"]

    def get_temperature(self):
        print(f"Temperature: {self.values["temperature"]} C")

    def get_humidity(self):
        print(f"Humidity: {self.values["humidity"]} %")

    def get_wind_speed(self):
        print(f"Wind Speed: {self.values["windSpeed"]} km/h")

    def get_forecast(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            self.response = response.json()
            
            if response.status_code != 200:
                raise ValueError("\nInvalid city name. Please try again.")
            else:
                self.find_values()
                print(f"\n{"*"*30} Weather Forecast {"*"*30}")
                print(self.response["location"]["name"])
                self.get_temperature()
                self.get_humidity()
                self.get_wind_speed()
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print("\nAn error occurred while fetching the weather data. Please try again later.")  

def main():  
    while True:
        print(f"\n{"*"*30} Weather Forecast App {"*"*30}")
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