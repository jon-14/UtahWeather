import mysql.connector
import os

# @TODO: implement this in store_weather_data.py

# Class for handling database connection, querying, and inserting values.
class DatabaseConnection:
    def __init__(self, db_host: str, db_user: str, db_password: str, db_name: str):
        self.connection = mysql.connector.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_name
        )
    

    # Returns cursor object containing query results.
    def select_rows(self, query: str):
        self.cursor = self.connection.cursor()
        result_set = []
        try:
            self.cursor.execute(query)
            results = self.cursor
            for x in results:
                result_set.append(x)
            self.cursor.close()
            return result_set
        except Exception as e:
            print(f"Error in query: {e}")
            self.cursor.close()
            return
    

    # Inserts one row into the specified table and column values.
    # cols_to_insert: array containing column names.
    # vals_to_insert: array containing values to insert.
    def insert_rows(self, table_name, cols_to_insert, vals_to_insert):
        if cols_to_insert.len != vals_to_insert.len:
            print("Error: Column count and item count need to match.")
            return
        else:
            self.cursor = self.connection.cursor()
            col_string = ""
            val_string = ""
            for x in cols_to_insert:
                col_string += x + ", "
            for x in vals_to_insert:
                val_string += x + ", "
            query = """
                INSERT INTO {table_name}({col_string})
                VALUES {val_string};
            """
            try:
                self.cursor.execute(query)
                print(f"{self.cursor.rowcount} rows inserted.")
                self.cursor.close()
                return
            except Exception as e:
                print(f"Error in query: {e}")
                self.cursor.close()
                return



