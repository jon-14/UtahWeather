import mysql.connector
from get_weather_data import get_temperature

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='jonnyboi',
    database='UtahWeather'
)

cursor = connection.cursor()