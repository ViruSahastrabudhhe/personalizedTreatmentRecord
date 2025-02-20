from . import authentication
from healthers.models import get_db_connection
from .auth import Authentication
import mysql.connector
from mysql.connector import Error
from flask import render_template, flash, redirect, url_for, request, session
from werkzeug.security import *

auth=Authentication()

@authentication.route('/')
def welcome():
    conn = get_db_connection()
    if conn is None:
        flash("NO DB CONNECTION", category='error')
        return redirect(url_for('authentication.welcome'))

    return render_template('users/beforeLogin/page_landing.html', legend="Health record system")

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        email=request.form['loginEmail']
        password=request.form['loginPassword']

        conn=get_db_connection()
        if conn is None:
            flash("NO DB CONNECTION", category='error')
            return redirect(url_for('authentication.login'))
        
        cursor=conn.cursor(dictionary=True)
        
        try:
            cursor.execute("SELECT * FROM users WHERE email=%s", (email, ))
            record=cursor.fetchone()

            if record is None:
                flash("Account does not exist!", category='error')
                return redirect(url_for('authentication.login'))
            
            if check_password_hash(record['password'], password):
                session['loggedIn']=True
                session['userID']=record['userID']
                session['email']=record['email']
                session['role']=record['role']
                flash('Logged in successfully!', category='success')
                return redirect(url_for('authentication.login'))
            else:
                flash('Incorrect password! Try again.', category='error')
        except Error as e:
            flash(f"{e}", category='error')
            return redirect(url_for('authentication.login'))
        finally:
            cursor.close()
            conn.close()

    return render_template('users/beforeLogin/page_login.html', legend='Sign in to Healthers')

@authentication.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method=='POST':
        fname=request.form['signUpFname']
        lname=request.form['signUpLname']
        email=request.form['signUpEmail']
        password=request.form['signUpPassword']
        role='user'

        if auth.isConn()==False:
            flash("NO DB CONNECTION", category='error')
            return redirect(url_for('authentication.login'))

        if auth.isSignUpFormEmpty(fname, lname, email, password):
            flash("Please input in the fields!", category='error')
            return redirect(url_for('authentication.signUp'))

        if auth.signUpAccount(fname, lname, email, password, role):
            flash("Created new account!", category='success')
            return redirect(url_for('authentication.login'))

        flash("Email already exists!", category='error')

    return render_template('users/beforeLogin/page_signUp.html', legend='Sign up to Healthers')

@authentication.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    return render_template('users/beforeLogin/page_forgotPassword.html', legend='Forgot password')

@authentication.route('/resetPassword', methods=['GET', 'POST'])
def resetPassword():
    return render_template('users/beforeLogin/page_resetPassword.html', legend='Reset password')