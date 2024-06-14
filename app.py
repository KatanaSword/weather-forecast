import requests
import os
from dotenv import load_dotenv

load_dotenv()

class forecast:
    def __init__(self, city):
        self.city = city
        try:
            url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&units=metric&apikey={os.getenv("API_KEY")}"
            headers = {"accept": "application/json"}
            response = requests.get(url, headers=headers)
            res = response.json()
            
            if response.status_code != 200:
                raise ValueError("\nInvalid city name. Please try again.")
            else:
                print(f"\n{"*"*30} Weather Forecast {"*"*30}")
                print(res["location"]["name"])
                print(f"Temperature: {res["data"]["values"]["temperature"]} C")
                print(f"Humidity: {res["data"]["values"]["humidity"]} %")
                print(f"Wind Speed: {res["data"]["values"]["windSpeed"]} km/h")
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
                forecast(location)
            case "0":
                break
            case _:
                print("\nInvalid choice")

if __name__ == "__main__":
    main()