import mysql.connector
from get_weather_data import get_temperature_data
import os

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

connection = mysql.connector.connect(
    host = db_host,
    user = db_user,
    password = db_password,
    database = db_name
)

cursor = connection.cursor()

cities = [
    ["Salt Lake City", 40.4000, -111.8505],
    ["Kamas", 40.640216, -111.280745],
    ["Mirror Lake", 40.701123, -110.887579],
    ["Lucin", 41.346238, -113.905283],
    ["Brian Head", 37.692681, -112.850196]
]



insert_query = """
    INSERT INTO temperature(city_name, latitude, longitude, curr_temperature)
    VALUES (%s, %s, %s, %s)
"""

for data in cities:
    cursor.execute(insert_query, get_temperature_data(data[0], data[1], data[2]))
connection.commit()

print(f"{cursor.rowcount} rows inserted.")

cursor.close()
connection.close()