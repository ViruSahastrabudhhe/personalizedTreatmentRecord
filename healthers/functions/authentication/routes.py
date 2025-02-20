from . import authentication
from healthers.models import get_db_connection
from .logic import calculate
from flask import render_template

@authentication.route('/')
def home():
    conn = get_db_connection()
    if conn:
        return "HELLO JAJAJJAJA"

    return render_template('users/homepage/page_login.html')