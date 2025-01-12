import os
import mysql.connector
import database_connection as dbc


mirror_lake_data = dbc.DatabaseConnection("localhost", "root", "jonnyboi", 'UtahWeather')

mirror_lake_query = "SELECT COUNT(*) FROM temperature WHERE city_name = 'Mirror Lake';"
results = mirror_lake_data.select_rows(mirror_lake_query)
for x in results:
    print(x)
