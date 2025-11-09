# weather app 
from weather_fetcher import WeatherFetcher
from weather_logger import WeatherLogger

class WeatherApp:
    def __init__(self, api_key):  
        self.fetcher = WeatherFetcher(api_key)
        self.logger = WeatherLogger()

    def run(self):
        while True:
            city = input("Enter city name (or 'exit' to quit): ").strip()
            if city.lower() == "exit":
                print("Exiting application.")
                break
            weather = self.fetcher.fetch(city)
            if weather:
                print(f"{weather['city']}: {weather['temp']}°C, Humidity: {weather['humidity']}%, Conditions: {weather['condition']}")
                self.logger.log(weather)

if __name__ == "__main__":  
    API_KEY = "13d96dc742885b9cc27a8b702294cd9d"  
    app = WeatherApp(API_KEY)
    app.run()