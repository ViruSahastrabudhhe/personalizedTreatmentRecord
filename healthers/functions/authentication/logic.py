from healthers.models import get_db_connection
import mysql.connector
from mysql.connector import Error
from werkzeug.security import *

class Authentication:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def signUpAccount(fname, lname, email, password):
        conn = get_db_connection()
        if conn is None:
            return None
        
        cursor=conn.cursor()
        hashedPassword = generate_password_hash(password, method="pbkdf2:sha256")

        try:
            cursor.execute("INSERT INTO users(email, password, role) VALUES ")