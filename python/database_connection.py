import mysql.connector
import os

# Class for handling database connection, querying, and inserting values.
class DatabaseConnection:
    def __init__(self, db_host: str, db_user: str, db_password: str, db_name: str):
        self.connection = mysql.connector.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_name
        )
        self.cursor = self.connection.cursor()
    
    """
    select_rows
    Parameters: 
        query (string)
    Return: 
        cursor object containing query results.
    """
    def select_rows(self, query: str):
        try:
            self.cursor.execute(query)
            return self.cursor
        except Exception as e:
            print(f"Error in query: {e}")
            return
    
    """
    insert_rows
    Parameters: 
        table_name          (name of the table)
        column_names        (1D array containing column names)
        vals_to_insert      (1D array containing values of one row)
    Return:
    """
    def insert_rows(self, table_name, cols_to_insert, vals_to_insert):
        if cols_to_insert.len != vals_to_insert.len:
            print("Error: Column count and item count need to match.")
            return
        else:
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
                return
            except Exception as e:
                print(f"Error in query: {e}")
                return



