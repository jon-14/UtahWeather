import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandasql as ps
import mysql.connector
import database_connection as dbc
from sqlalchemy import create_engine

# set up connection with sqlalchemy's create_engine
connection_string = 'mysql://root:jonnyboi@localhost'
engine = create_engine(connection_string)

# Create database connection
weather_data_connection = dbc.DatabaseConnection("localhost", "root", "jonnyboi", "UtahWeather")

# Select data for Mirror Lake from temperature table
mirror_lake_query = "SELECT * FROM temperature WHERE city_name = 'Mirror Lake';"

df = pd.read_sql(mirror_lake_query, engine)
