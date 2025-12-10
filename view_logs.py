import sqlite3

conn = sqlite3.connect("weather_logs.db")
cur = conn.cursor()

cur.execute("SELECT id, timestamp, city, temperature, humidity, description FROM weather_logs")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
