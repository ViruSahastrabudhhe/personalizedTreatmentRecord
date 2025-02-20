from healthers.models import get_db_connection
import mysql.connector
from mysql.connector import Error

class Authentication:
    def __init__(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    def signUpAccount(fname, lname, email, password):
        if self.conn is None:
