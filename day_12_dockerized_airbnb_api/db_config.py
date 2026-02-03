import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="airbnb_db"
    )
