import mysql.connector
from mysql.connector import Error
from healthers.models import get_db_connection
from datetime import datetime, date
from flask import render_template, flash, url_for, redirect, session, request

def getPatientsList():
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']
    try:
        sql="SELECT * FROM patientinfo where userID=%s and isArchived=0"
        val=(userID, )
        cursor.execute(sql, val)
        rows=cursor.fetchall()
        return rows
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getArchivedPatientsList():
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']
    try:
        sql="SELECT * FROM patientinfo where userID=%s and isArchived=1"
        val=(userID, )
        cursor.execute(sql, val)
        rows=cursor.fetchall()
        return rows
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getPatientsInfoToEdit(patientInfoID):
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']
    try:
        sql="SELECT * FROM patientinfo where userID=%s AND patientInfoID=%s"
        val=(userID, patientInfoID)
        cursor.execute(sql, val)
        row=cursor.fetchone()
        return row
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getMedicalInfo():
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']

    try:
        sql="SELECT * FROM patientmedicalinfo where userID=%s and isArchived=0"
        val=(userID, )
        cursor.execute(sql, val)
        rows=cursor.fetchall()
        return rows
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getArchivedMedicalInfo():
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']

    try:
        sql="SELECT * FROM patientmedicalinfo where userID=%s and isArchived=1"
        val=(userID, )
        cursor.execute(sql, val)
        rows=cursor.fetchall()
        return rows
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getPatientNamesForArchivedMedicalInfo():
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']

    try:
        sql="SELECT patientinfo.patientLname, patientinfo.patientFname FROM patientinfo JOIN patientmedicalinfo ON patientinfo.patientInfoID=patientmedicalinfo.patientInfoID WHERE patientmedicalinfo.isArchived=1 AND patientinfo.userID=%s"
        val=(userID, )
        cursor.execute(sql, val)
        rows=cursor.fetchall()
        return rows
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getMedicalInfoToEdit(medicalInfoID):
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']

    try:
        sql="SELECT * FROM patientmedicalinfo where userID=%s AND medicalInfoID=%s"
        val=(userID, medicalInfoID)
        cursor.execute(sql, val)
        row=cursor.fetchone()
        return row
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getPatientNamesToEdit(medicalInfoID):
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']

    try:
        sql="SELECT patientinfo.patientFname AS patientFirstName, patientinfo.patientLname AS patientLastName FROM patientinfo JOIN patientmedicalinfo ON patientinfo.patientInfoID=patientmedicalinfo.patientInfoID WHERE patientinfo.userID=%s AND patientinfo.isArchived=0 AND patientmedicalinfo.medicalInfoID=%s"
        val=(userID, medicalInfoID)
        cursor.execute(sql, val)
        rows=cursor.fetchall()
        return rows
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getPatientNamesFromPatientInfo():
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']

    try:
        sql="SELECT patientinfo.patientLname, patientinfo.patientFname FROM patientinfo JOIN patientmedicalinfo ON patientinfo.patientInfoID=patientmedicalinfo.patientInfoID WHERE patientinfo.userID=%s AND patientinfo.isArchived=0"
        val=(userID, )
        cursor.execute(sql, val)
        rows=cursor.fetchall()
        return rows
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getFindings():
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']
    try:
        sql="SELECT * FROM patientmedicalinfo WHERE userID=%s GROUP BY findings"
        val=(userID, )
        cursor.execute(sql, val)
        rows=cursor.fetchall()
        return rows
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getDiagnosis():
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']
    try:
        sql="SELECT * FROM patientmedicalinfo WHERE userID=%s GROUP BY diagnosis"
        val=(userID, )
        cursor.execute(sql, val)
        rows=cursor.fetchall()
        return rows
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getPatientCount():
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']
    try:
        sql="SELECT COUNT(*) FROM patientinfo where userID=%s"
        val=(userID, )
        cursor.execute(sql, val)
        count=cursor.fetchone()
        return count
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getMedicalCount():
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']
    try:
        sql="SELECT COUNT(*) FROM patientmedicalinfo where userID=%s"
        val=(userID, )
        cursor.execute(sql, val)
        count=cursor.fetchone()
        return count
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getFindingsCount():
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']
    try:
        sql="SELECT COUNT(findings) FROM patientmedicalinfo where userID=%s"
        val=(userID, )
        cursor.execute(sql, val)
        count=cursor.fetchone()
        return count
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()

def getDiagnosisCount():
    conn=get_db_connection()
    if conn is None:
        flash('NO DB CONNECTION', category='error')
        return redirect(url_for('authentication.landing'))

    cursor=conn.cursor()
    userID=session['userID']
    try:
        sql="SELECT COUNT(diagnosis) FROM patientmedicalinfo where userID=%s"
        val=(userID, )
        cursor.execute(sql, val)
        count=cursor.fetchone()
        return count
    except Error as e:
        conn.rollback()
        flash(f"{e}", category='error')
        return redirect(url_for('nurse.nurseDashboard'))
    finally:
        cursor.close()
        conn.close()