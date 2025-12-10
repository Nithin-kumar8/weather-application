# weather-application

## Verification Summary ✅

**Strengths:**
- Clean separation of concerns with three distinct modules
- Proper error handling in the fetcher
- SQLite database with appropriate table structure
- User-friendly CLI interface
- Good code documentation

**Minor Issues:**
- No database connection cleanup in WeatherLogger
- API key is hardcoded (security concern for production)

## README.md
# Weather Application
A Python-based weather application that fetches current weather data from OpenWeatherMap API and logs it to a local SQLite database.
## Features

- Fetch real-time weather data for any city worldwide
- Display temperature, humidity, and weather conditions
- Persistent logging of weather queries to SQLite database
- Simple command-line interface
- Error handling for invalid city names and API issues

## Project Structure
weather_app/
├── main.py      
├── view_logs.py  
├── weather_api_client.py  
├── Weather_logger.py
└── weather_logs.db    
## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone or download the project files
2. Install required dependencies:
   ```bash
   pip install requests
   ```

3. Get an API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Generate an API key in your dashboard

## Usage

1. **Update the API Key** (Important):
   Replace the hardcoded API key in `weather_app.py`:
   ```python
   API_KEY = "your_actual_api_key_here"

2. **Run the application**:
   ```bash
   python weather_app.py
   ```

3. **Interact with the app**:
   - Enter a city name to get current weather information
   - Type 'exit' to quit the application
   - All queries are automatically saved to the database

## Database Schema

The application uses SQLite with the following table structure:

```sql
CREATE TABLE logs (
    id INTEGER PRIMARY KEY,
    city TEXT,
    temp REAL,
    humidity INTEGER,
    condition TEXT,
    timestamp TEXT
)
```


## Example Output

```
Enter city name (or 'exit' to quit): Guntur
city          : Guntur
temperature   : 22.52 C
Humidity      : 57 %
condition     : clear sky
```
## Screenshots
<img width="1899" height="1074" alt="Image" src="https://github.com/user-attachments/assets/72ba81ef-115d-4338-aba2-2353fe7e4d46" />

<img width="1896" height="1079" alt="Image" src="https://github.com/user-attachments/assets/f87433ba-71da-4c07-8a4d-3535c0709e84" />
## Error Handling

- Invalid city names display friendly error messages
- API connection issues are caught and reported
- Unexpected errors are handled gracefully

## Security Note

For production use, consider:
1. Storing the API key in environment variables
2. Using a configuration file (excluded from version control)
3. Implementing rate limiting for API calls

## License

This is a educational project. Please ensure compliance with OpenWeatherMap's terms of service for API usage.
```

## Important Security Recommendation 🔒

**Remove your actual API key from the code** before sharing or committing to version control. Instead, use environment variables or a config file:

```python
import os
API_KEY = os.getenv('WEATHER_API_KEY', 'your_fallback_key_here')
```
The application architecture is solid and ready for use! Just remember to secure your API key.
