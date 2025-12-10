import requests


class WeatherAPIError(Exception):
    pass


class WeatherAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city_name):
        """Return a dict with basic weather info for the given city."""
        if not city_name:
            raise WeatherAPIError("City name is empty.")

        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric",  
        }

        try:
            resp = requests.get(self.base_url, params=params, timeout=10)
        except requests.RequestException as e:
            raise WeatherAPIError(f"Network problem: {e}")

        
        if resp.status_code != 200:
            try:
                data = resp.json()
                msg = data.get("message", "Unknown error from API.")
            except ValueError:
                msg = "Could not read error details from API."
            raise WeatherAPIError(f"API error ({resp.status_code}): {msg}")

        try:
            data = resp.json()
        except ValueError:
            raise WeatherAPIError("API returned something that is not JSON.")

        try:
            main = data["main"]
            weather_list = data.get("weather", [])
            description = weather_list[0]["description"] if weather_list else "unknown"
        except (KeyError, IndexError):
            raise WeatherAPIError("API response format is not what was expected.")

        result = {
            "city": data.get("name", city_name),
            "temp_c": main.get("temp"),
            "humidity": main.get("humidity"),
            "description": description,
            "raw": data,  
        }

        return result
