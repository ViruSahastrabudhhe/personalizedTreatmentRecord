from . import authentication
from healthers.models import get_db_connection
from .logic import calculate
from flask import render_template, flash, redirect, url_for, request, session
from werkzeug.security import *

@authentication.route('/')
def welcome():
    conn = get_db_connection()
    if conn is None:
        flash("NO DB CONNECTION", category='error')
        return redirect(url_for('authentication.welcome'))

    return render_template('users/beforeLogin/page_landing.html', legend="Health record system")

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('users/beforeLogin/page_login.html', legend='Sign in to Healthers')

@authentication.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method=='POST':
        fname=request.form['signUpFname']
        lname=request.form['signUpLname']
        email=request.form['signUpEmail']
        password=request.form['signUpPassword']


    return render_template('users/beforeLogin/page_signUp.html', legend='Sign up to Healthers')

@authentication.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    return render_template('users/beforeLogin/page_forgotPassword.html', legend='Forgot password')

@authentication.route('/resetPassword', methods=['GET', 'POST'])
def resetPassword():
    return render_template('users/beforeLogin/page_signUp.html', legend='Reset password')