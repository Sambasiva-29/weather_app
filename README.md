# weather_app

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
├── weather_app.py      # Main application and user interface
├── weather_fetcher.py  # API communication module
├── weather_logger.py   # Database logging module
└── weather_log.db      # SQLite database (created automatically)

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

## Modules Overview

### WeatherFetcher (`weather_fetcher.py`)
- Handles API communication with OpenWeatherMap
- Parses JSON responses into structured data
- Implements error handling for HTTP requests

### WeatherLogger (`weather_logger.py`)
- Manages SQLite database operations
- Automatically creates required tables
- Logs weather data with timestamps

### WeatherApp (`weather_app.py`)
- Main application controller
- User interface and input handling
- Coordinates between fetcher and logger

## Example Output

```
Enter city name (or 'exit' to quit): London
London: 15.5°C, Humidity: 65%, Conditions: Clouds

Enter city name (or 'exit' to quit): Tokyo
Tokyo: 22.1°C, Humidity: 48%, Conditions: Clear

Enter city name (or 'exit' to quit): exit
Exiting application.
```
## Screenshots
<img width="1896" height="877" alt="Image" src="https://github.com/user-attachments/assets/38465cb3-1c4a-40ed-a5bf-74d5d822c661" />

<img width="1619" height="521" alt="Image" src="https://github.com/user-attachments/assets/b4f31d57-3e3f-4afd-a090-549f20814fca" />

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
