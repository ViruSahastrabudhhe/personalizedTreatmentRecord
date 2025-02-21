from healthers.models import get_db_connection, generateToken, verifyToken
from healthers import mail
from flask_mail import Message
from flask import url_for
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

    def sendForgotPasswordMail(self, email: str):
        token=generateToken(email)
        msg=Message(
            subject='Password reset request!',
            sender='noreply@gmail.com',
            recipients=[f"{email}"]
        )
        msg.body = f''' To reset your password, please follow the link below.

        {url_for('authentication.resetPassword', token=token, _external=True)}

        ...

        If you didn't send a password reset request, please ignore this message.

        '''
        mail.send(msg)

    def isSignUpFormEmpty(self, fname, lname, email, password):
        if fname=="" and lname=="" and email=="" and password=="":
            return True