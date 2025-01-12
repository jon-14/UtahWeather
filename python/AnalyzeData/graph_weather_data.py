import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandasql as ps
import mysql.connector
import database_connection as dbc

# Get Mirror Lake temperature data from SQL table
weather_data_connection = dbc.DatabaseConnection("localhost", "root", "jonnyboi", "UtahWeather")


