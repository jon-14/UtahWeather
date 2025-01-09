import mysql.connector
from get_weather_data import get_temperature_data

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='jonnyboi',
    database='UtahWeather'
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