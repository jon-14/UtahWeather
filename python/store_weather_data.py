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

data = get_temperature_data("Salt Lake City",40.4000,-111.8505)

insert_query = """
    INSERT INTO temperature(city_name, latitude, longitude, curr_temperature)
    VALUES (%s, %s, %s, %s)
"""

cursor.execute(insert_query, data)
connection.commit()

print(f"{cursor.rowcount} rows inserted.")

cursor.close()
connection.close()