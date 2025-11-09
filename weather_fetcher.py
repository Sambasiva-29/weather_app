# weather_fetcher.py
import requests

class WeatherFetcher:
    def __init__(self, api_key):  # FIXED: double underscores
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def fetch(self, city_name):
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric"
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            weather = {
                "city": city_name,
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["main"]
            }
            return weather
        except requests.exceptions.HTTPError:
            print("Invalid city name or API error.")
            return None
        except Exception as e:
            print("Error:", e)
            return None