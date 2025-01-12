#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
import mysql.connector
from get_weather_data import get_temperature_data
import os
import logging
import schedule
import time

# Function representing the action to schedule
def schedule_data_upload():
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')

    # Connect to database
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

    logging.basicConfig(filename='/Users/joncox/logs/weather_script.log', level=logging.DEBUG)
    logging.debug('Script started')

# Schedule the function to run every minute
schedule.every(5).minutes.do(schedule_data_upload)

while True:
    schedule.run_pending()  # Run the scheduled task
    time.sleep(1)  # Sleep for 1 second to avoid maxing out the CPU