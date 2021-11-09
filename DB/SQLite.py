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

