import sqlite3
from datetime import datetime


class WeatherLogger:
    def __init__(self, db_path="weather_logs.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS weather_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                city TEXT NOT NULL,
                temperature REAL,
                humidity INTEGER,
                description TEXT,
                raw_response TEXT
            )
            """
        )

        conn.commit()
        conn.close()

    def save(self, weather_data):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cur.execute(
            """
            INSERT INTO weather_logs (timestamp, city, temperature, humidity, description, raw_response)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                ts,
                weather_data.get("city"),
                weather_data.get("temp_c"),
                weather_data.get("humidity"),
                weather_data.get("description"),
                str(weather_data.get("raw")),
            ),
        )

        conn.commit()
        conn.close()
