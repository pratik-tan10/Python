import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB created.")
    except Error as e:
        print(f"The error '{e}' occured")
        
    return connection

connection = create_connection(r"C:\Users\Research Lab\Desktop\Pratik\WEB\chuck\sqlite\sm_app.sqlite")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  FullName TEXT NOT NULL, 
  Age INTEGER,
  Sex TEXT,
  Country TEXT
)
"""       
execute_query(connection, create_users_table)  
