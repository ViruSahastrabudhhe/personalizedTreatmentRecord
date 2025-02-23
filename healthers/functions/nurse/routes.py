from . import nurse
import mysql.connector
from mysql.connector import Error
from healthers.models import get_db_connection
from flask import render_template, flash, url_for, redirect, session, request

conn=get_db_connection()
if conn is None:
    flash('NO DB CONNECTION', category='error')
    redirect(url_for('authentication.landing'))

@nurse.route('/addMedicalInfo', methods=['GET', 'POST'])
def nurseAddMedicalInfo():
    if request.method=='POST':
        patientName=request.form['medicalInfoAddName']
        patientFindings=request.form['medicalInfoAddFindings']
        patientDiagnosis=request.form['medicalInfoAddDiagnosis']
        patientDate=request.form['medicalInfoAddDate']
        patientTreatment=request.form['medicalInfoAddTreatment']
        patientAdvice=request.form['medicalInfoAddAdvice']
        patientEvaluation=request.form['medicalInfoAddEvaluation']
        userID=session['userID']

        conn=get_db_connection()
        if conn is None:
            flash('NO DB CONNECTION', category='error')
            return redirect(url_for('authentication.landing'))

        cursor=conn.cursor()

        try:
            cursor.execute("INSERT INTO patientmedicalinfo(userID, patientInfoID, diagnosis)")