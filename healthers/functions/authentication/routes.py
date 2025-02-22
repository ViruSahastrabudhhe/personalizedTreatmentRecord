from . import authentication
from healthers.models import get_db_connection, verifyToken
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

    return render_template('users/authentication/page_landing.html', legend="Lumban RHU")

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
                session['fname']=record['firstName']
                session['lname']=record['lastName']
                session['email']=record['email']
                session['role']=record['role']
                flash('Logged in successfully!', category='success')
                return redirect(url_for('nurse.dashboard'))
            else:
                flash('Incorrect password! Try again.', category='error')
        except Error as e:
            flash(f"{e}", category='error')
            return redirect(url_for('authentication.login'))
        finally:
            cursor.close()
            conn.close()

    return render_template('users/authentication/page_login.html', legend='Sign in to Healthers')

@authentication.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    flash("Successfully logged out!", category='success')
    return redirect(url_for('authentication.login'))

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

    return render_template('users/authentication/page_signUp.html', legend='Sign up to Healthers')

@authentication.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    if request.method=='POST':
        email=request.form['forgotPasswordEmail']
        role='user'

        conn = get_db_connection()
        if conn is None:
            flash('NO DB CONNECTION LOL', category='error')
            return redirect(url_for('authentication.welcome'))
        
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM users WHERE email=%s and role=%s", (email, role))
            record = cursor.fetchone()

            if record is None:
                flash("Email does not exist!", category='error')
                return redirect(url_for('authentication.forgotPassword'))
            
            auth.sendForgotPasswordMail(email)
            flash("Password reset request sent!", category='success')
            return redirect(url_for('authentication.login'))
        except Error as e:
            conn.rollback()
            flash(f"{e}", category='error')
            print(e)
            return redirect(url_for('authentication.welcome'))
        finally:
            cursor.close()
            conn.close()
    
    return render_template('users/authentication/page_forgotPassword.html', legend='Forgot password')

@authentication.route('/resetPassword/<token>', methods=['GET', 'POST'])
def resetPassword(token):
    email = verifyToken(token, expiration=3600)
    if email==False:
        flash('Invalid token or token has expired. Please try again!', category='error')
        return redirect(url_for('authentication.login'))

    if request.method=='POST':
        newPass=request.form['resetPasswordNewPass']
        confirmPass=request.form['resetPasswordConfirmPass']

        if newPass!=confirmPass:
            flash('Passwords do not match!', category='error')
            return redirect(url_for('authentication.resetPassword', token=token))

        conn = get_db_connection()
        if conn is None:
            flash('NO DB CONNECTION LOL', category='error')
            return redirect(url_for('authentication.welcome'))
        
        cursor = conn.cursor()
        cursor=conn.cursor()
        hashedPassword = generate_password_hash(newPass, method="pbkdf2:sha256")

        try:
            cursor.execute('UPDATE users SET password=%s WHERE email=%s', (hashedPassword, email))
            conn.commit()
            flash('Password successfully reset!', category='success')
            return redirect(url_for('authentication.login'))
        except:
            conn.rollback()
            flash('An unexpected error has occurred!', category='error')
            return redirect(url_for('authentication.login'))
        finally:
            cursor.close()
            conn.close()
    
    return render_template('users/authentication/page_resetPassword.html', legend='Reset password', token=token, userEmail=email)