from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",  
            user="root",       
            password="",       
            database="healthers"
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None