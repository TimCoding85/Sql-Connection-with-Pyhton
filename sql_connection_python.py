from sqlalchemy import create_engine
import pyodbc
import pandas as pd

def execute_sql_query(sql_query, params=None):
    try:
        return pd.read_sql(sql_query, engine, params=params)
    except Exception as e:
        print(e)



server = "IP"
database = "db"
username = "user"
password = "pw"

# Connection setup
connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Initialization of the connection object
connection = None

try:
    connection = pyodbc.connect(connection_string)
    print("Connection successfully established.")
except pyodbc.Error as ex:
    print("Error when establishing the connection:")
    print(ex)

    exit()
if connection is not None:
    engine = create_engine(
        f"mssql+pyodbc:///?odbc_connect={connection_string}"
    )

query =""" 
SELECT *  FROM TABLE
"""

df = execute_sql_query(query)
