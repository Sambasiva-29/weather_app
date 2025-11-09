
import sqlite3
from datetime import datetime

class WeatherLogger:
    def __init__(self, db_path="weather_log.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY,
                    city TEXT,
                    temp REAL,
                    humidity INTEGER,
                    condition TEXT,
                    timestamp TEXT
                )
            """)

    def log(self, weather_data):
        with self.conn:
            self.conn.execute("""
                INSERT INTO logs (city, temp, humidity, condition, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (
                weather_data["city"],
                weather_data["temp"],
                weather_data["humidity"],
                weather_data["condition"],
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ))