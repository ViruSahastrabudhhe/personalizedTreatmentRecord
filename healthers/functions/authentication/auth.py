from healthers.models import get_db_connection
import mysql.connector
from mysql.connector import Error
from werkzeug.security import *

class Authentication:
    def __init__(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    def isConn(self):
        if self.conn:
            return True
        else:
            return False

    def selectUserEmail(self, email):
        if self.conn is None:
            return "NO DB CONNECTION"
        
        cursor=self.conn.cursor()
        
        try:
            cursor.execute("SELECT * FROM users WHERE email=%s", (email, ))
            record=cursor.fetchone()    
            if record is None:
                return 404
        except Error as e:
            return e
        finally:
            cursor.close()
            self.conn.close()

        return record

    def signUpAccount(self, fname, lname, email, password, role):
        if self.conn is None:
            return "NO DB CONNECTION"
        
        cursor=self.cursor
        hashedPassword = generate_password_hash(password, method="pbkdf2:sha256")

        try:
            cursor.execute("INSERT INTO users(firstName, lastName, email, password, role) VALUES (%s, %s, %s, %s, %s)", (fname, lname, email, hashedPassword, role))
            self.conn.commit()
            return True
        except mysql.connector.IntegrityError:
            self.conn.rollback()
            return False
        finally:
            self.cursor.close()
            self.conn.close()

    def isSignUpFormEmpty(self, fname, lname, email, password):
        if fname=="" and lname=="" and email=="" and password=="":
            return True