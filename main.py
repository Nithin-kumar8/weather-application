from weather_api_client import WeatherAPIClient, WeatherAPIError
from weather_logger import WeatherLogger


class WeatherApp:
    def __init__(self, api_key):
        self.client = WeatherAPIClient(api_key)
        self.logger = WeatherLogger()

    def run(self):
        print("=== Real-Time Weather App ===")
        print("Type 'exit' to quit.\n")

        while True:
            city = input("Enter city name: ").strip()

            if city.lower() == "exit":
                print("Bye!")
                break

            if not city:
                print("City name cannot be empty.\n")
                continue

            try:
                info = self.client.get_weather(city)
            except WeatherAPIError as e:
                print(f"[Error] {e}\n")
                continue
            except Exception as e:
                print(f"[Unexpected error] {e}\n")
                continue

            self._print_weather(info)
            self.logger.save(info)
            print("\n")

    @staticmethod
    def _print_weather(info):
        print("\n")
        print(f"City       : {info.get('city')}")
        print(f"Temperature: {info.get('temp_c')} °C")
        print(f"Humidity   : {info.get('humidity')} %")
        print(f"Condition  : {info.get('description').title()}")
    


if __name__ == "__main__":
    API_KEY = "61c36f646eac7adde9e8c32915dbb2df"
    app = WeatherApp(API_KEY)
    app.run()
