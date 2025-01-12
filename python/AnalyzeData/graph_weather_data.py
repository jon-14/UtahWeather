import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandasql as ps
import mysql.connector

# Get Mirror Lake temperature data from SQL table
sql_query = "SELECT city_name AS location, curr_temperature AS temperature_F, timestamp AS time FROM temperature WHERE city_name = 'Mirror Lake' ORDER BY timestamp DESC;"



print(sql_query)
