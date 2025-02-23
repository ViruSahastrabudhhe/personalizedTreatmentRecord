from . import nurse
from .getters import getPatientNamesToEdit, getPatientsInfoToEdit, getMedicalInfoToEdit
import mysql.connector
from mysql.connector import Error
from healthers.models import get_db_connection
from datetime import datetime, date
from flask import render_template, flash, url_for, redirect, session, request

conn=get_db_connection()
if conn is None:
    flash('NO DB CONNECTION', category='error')
    redirect(url_for('authentication.landing'))

@nurse.route('/addPatientInfo', methods=['GET', 'POST'])
def nurseAddPatientInfo():
    if request.method=='POST':
        patientFname = request.form['patientsListAddFname']
        patientLname = request.form['patientsListAddLname']
        patientContactNo = request.form['patientsListAddContactNo']
        patientSex = request.form['patientsListAddSex']
        patientBirthday = request.form['patientsListAddBirthday']
        patientProvince = request.form['patientsListAddProvince']
        patientCity = request.form['patientsListAddCity']
        patientBarangay = request.form['patientsListAddBrgy']
        patientTown = request.form['patientsListAddTown']
        patientStreet = request.form['patientsListAddSt']
        patientDateReg = request.form['patientsListAddDateReg']
        patientDateCons = request.form.get('patientsListAddDateCons', None)
        userID = session['userID']

        conn=get_db_connection()
        if conn is None:
            flash('NO DB CONNECTION', category='error')
            redirect(url_for('authentication.landing'))
        cursor=conn.cursor()

        try:
            sql = "INSERT INTO patientinfo(userID, patientFname, patientLname, patientContactNo, patientSex, patientBirthday, patientProvince, patientCity, patientBarangay, patientTown, patientStreet, patientDateRegistered, patientDateConsulted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (userID, patientFname, patientLname, patientContactNo, patientSex, patientBirthday, patientProvince, patientCity, patientBarangay, patientTown, patientStreet, patientDateReg, patientDateCons)
            cursor.execute(sql, val)
            conn.commit()
            flash("Successfully added new patient!", category='success')
            return redirect(url_for('nurse.patientsListManage'))
        except Error as e:
            conn.rollback()
            flash(f"{e}", category='error')
            return redirect(url_for('nurse.patientsListManage'))
        finally:
            cursor.close()
            conn.close()

@nurse.route('/editPatientInfo/<patientInfoID>', methods=['GET', 'POST'])
def nurseEditPatientInfo(patientInfoID):
    row=getPatientsInfoToEdit(patientInfoID)

    if request.method=='POST':
        patientFname = request.form['patientsListEditFname']
        patientLname = request.form['patientsListEditLname']
        patientContactNo = request.form['patientsListEditContactNo']
        patientSex = request.form['patientsListEditSex']
        patientBirthday = request.form['patientsListEditBirthday']
        patientProvince = request.form['patientsListEditProvince']
        patientCity = request.form['patientsListEditCity']
        patientBarangay = request.form['patientsListEditBrgy']
        patientTown = request.form['patientsListEditTown']
        patientStreet = request.form['patientsListEditSt']
        patientDateReg = request.form['patientsListEditDateReg']
        patientDateCons = request.form.get('patientsListEditDateCons', None)
        patientDateUpd = datetime.now()
        userID=session['userID']      

        conn=get_db_connection()
        if conn is None:
            flash('NO DB CONNECTION', category='error')
            redirect(url_for('authentication.landing'))

        cursor=conn.cursor()

        try:
            sql = "UPDATE patientinfo SET patientFname=%s, patientLname=%s, patientContactNo=%s, patientSex=%s, patientBirthday=%s, patientProvince=%s, patientCity=%s, patientBarangay=%s, patientTown=%s, patientStreet=%s, patientDateRegistered=%s, patientDateUpdated=%s, patientDateConsulted=%s WHERE userID=%s AND patientInfoID=%s"
            val = (patientFname, patientLname, patientContactNo, patientSex, patientBirthday, patientProvince, patientCity, patientBarangay, patientTown, patientStreet, patientDateReg, patientDateUpd, patientDateCons, userID, patientInfoID)
            cursor.execute(sql, val)
            conn.commit()
            flash("Successfully edited patient information!", category='success')
            return redirect(url_for('nurse.patientsListManage'))
        except Error as e:
            conn.rollback()
            flash(f"{e}", category='error')
            return redirect(url_for('nurse.patientsListManage'))
        finally:
            cursor.close()
            conn.close()

    return render_template('users/nurse/panels/patientsList/patientsList_edit.html', row=row, legend="Edit patients in list", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/archivePatientInfo/<patientInfoID>', methods=['GET', 'POST'])
def nurseArchivePatientInfo(patientInfoID):
    if request.method=='POST':
        userID=session['userID']

        conn=get_db_connection()
        if conn is None:
            flash('NO DB CONNECTION', category='error')
            redirect(url_for('authentication.landing'))
        cursor=conn.cursor()

        try:
            sql="UPDATE patientinfo SET isArchived=1 WHERE patientInfoID=%s AND userID=%s"
            val=(patientInfoID, userID)
            cursor.execute(sql, val)
            conn.commit()
            flash("Successfully archived patient info!", category='success')
            return redirect(url_for('nurse.patientsListManage'))
        except Error as e:
            conn.rollback()
            flash(f"{e}", category='error')
            return redirect(url_for('nurse.patientsListManage'))
        finally:
            cursor.close()
            conn.close()

@nurse.route('/restorePatientInfo/<patientInfoID>', methods=['GET', 'POST'])
def nurseRestorePatientInfo(patientInfoID):
    if request.method=='POST':
        userID=session['userID']

        conn=get_db_connection()
        if conn is None:
            flash('NO DB CONNECTION', category='error')
            redirect(url_for('authentication.landing'))
        cursor=conn.cursor()

        try:
            sql="UPDATE patientinfo SET isArchived=0 WHERE patientInfoID=%s AND userID=%s"
            val=(patientInfoID, userID)
            cursor.execute(sql, val)
            conn.commit()
            flash("Successfully restored patient info!", category='success')
            return redirect(url_for('nurse.patientsListManage'))
        except Error as e:
            conn.rollback()
            flash(f"{e}", category='error')
            return redirect(url_for('nurse.patientsListManage'))
        finally:
            cursor.close()
            conn.close()

@nurse.route('/deletePatientInfo/<patientInfoID>', methods=['GET', 'POST'])
def nurseDeletePatientInfo(patientInfoID):
    if request.method=='POST':
        userID=session['userID']

        conn=get_db_connection()
        if conn is None:
            flash('NO DB CONNECTION', category='error')
            redirect(url_for('authentication.landing'))
        cursor=conn.cursor()

        try:
            sql="DELETE FROM patientinfo WHERE patientInfoID=%s AND userID=%s"
            val=(patientInfoID, userID)
            cursor.execute(sql, val)
            conn.commit()
            flash("Successfully deleted patient info!", category='success')
            return redirect(url_for('nurse.patientsListManage'))
        except Error as e:
            conn.rollback()
            flash(f"{e}", category='error') 
            return redirect(url_for('nurse.patientsListManage'))
        finally:
            cursor.close()
            conn.close()

@nurse.route('/addMedicalInfo', methods=['GET', 'POST'])
def nurseAddMedicalInfo():
    if request.method=='POST':
        patientInfoID=request.form['medicalInfoAddName']
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
            sql="INSERT INTO patientmedicalinfo(userID, patientInfoID, diagnosis, findings, advice, treatment, evaluation, medicalInfoDateCreated) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val=(userID, patientInfoID, patientDiagnosis, patientFindings, patientAdvice, patientTreatment, patientEvaluation, patientDate)
            cursor.execute(sql, val) 
            conn.commit()
            flash("Successfully added patient medical record!", category='success')
            return redirect(url_for('nurse.medicalManage'))
        except Error as e:
            conn.rollback()
            flash(f"{e}", category='error')
            return redirect(url_for('nurse.medicalManage'))
        finally:
            cursor.close()
            conn.close()

@nurse.route('/editMedicalInfo/<medicalInfoID>', methods=['GET', 'POST'])
def nurseEditMedicalInfo(medicalInfoID):
    row=getMedicalInfoToEdit(medicalInfoID)
    nameRow=getPatientNamesToEdit(medicalInfoID)

    if request.method=='POST':
        patientFindings=request.form['medicalInfoEditFindings']
        patientDiagnosis=request.form['medicalInfoEditDiagnosis']
        patientTreatment=request.form['medicalInfoEditTreatment']
        patientAdvice=request.form['medicalInfoEditAdvice']
        patientEvaluation=request.form['medicalInfoEditEvaluation']
        patientDateCheckedUp=request.form['medicalInfoEditDate']
        patientDateUpd = datetime.now()
        userID=session['userID']      

        conn=get_db_connection()
        if conn is None:
            flash('NO DB CONNECTION', category='error')
            redirect(url_for('authentication.landing'))

        cursor=conn.cursor()

        try:
            sql = "UPDATE patientmedicalinfo SET diagnosis=%s, findings=%s, advice=%s, treatment=%s, evaluation=%s, medicalInfoDateCreated=%s, medicalInfoDateUpdated=%s WHERE medicalInfoID=%s AND userID=%s"
            val = (patientDiagnosis, patientFindings, patientAdvice, patientTreatment, patientEvaluation, patientDateCheckedUp, patientDateUpd, medicalInfoID, userID)
            cursor.execute(sql, val)
            conn.commit()
            flash("Successfully edited patient medical record!", category='success')
            return redirect(url_for('nurse.medicalManage'))
        except Error as e:
            conn.rollback()
            flash(f"{e}", category='error')
            return redirect(url_for('nurse.medicalManage'))
        finally:
            cursor.close()
            conn.close()

    return render_template('users/nurse/panels/patientMedical/medical_edit.html', nameRow=nameRow, row=row, legend="Edit patients in list", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/archiveMedicalInfo/<medicalInfoID>', methods=['GET', 'POST'])
def nurseArchiveMedicalInfo(medicalInfoID):
    if request.method=='POST':
        userID=session['userID']

        conn=get_db_connection()
        if conn is None:
            flash('NO DB CONNECTION', category='error')
            redirect(url_for('authentication.landing'))
        cursor=conn.cursor()

        try:
            sql="UPDATE patientmedicalinfo SET isArchived=1 WHERE medicalInfoID=%s AND userID=%s"
            val=(medicalInfoID, userID)
            cursor.execute(sql, val)
            conn.commit()
            flash("Successfully archived patient medical record!", category='success')
            return redirect(url_for('nurse.medicalManage'))
        except Error as e:
            conn.rollback()
            flash(f"{e}", category='error')
            return redirect(url_for('nurse.medicalManage'))
        finally:
            cursor.close()
            conn.close()

@nurse.route('/restoreMedicalInfo/<medicalInfoID>', methods=['GET', 'POST'])
def nurseRestoreMedicalInfo(medicalInfoID):
    if request.method=='POST':
        userID=session['userID']

        conn=get_db_connection()
        if conn is None:
            flash('NO DB CONNECTION', category='error')
            redirect(url_for('authentication.landing'))
        cursor=conn.cursor()

        try:
            sql="UPDATE patientmedicalinfo SET isArchived=0 WHERE medicalInfoID=%s AND userID=%s"
            val=(medicalInfoID, userID)
            cursor.execute(sql, val)
            conn.commit()
            flash("Successfully restored patient medical record!", category='success')
            return redirect(url_for('nurse.medicalManage'))
        except Error as e:
            conn.rollback()
            flash(f"{e}", category='error')
            return redirect(url_for('nurse.medicalManage'))
        finally:
            cursor.close()
            conn.close()

@nurse.route('/deleteMedicalInfo/<medicalInfoID>', methods=['GET', 'POST'])
def nurseDeleteMedicalInfo(medicalInfoID):
    if request.method=='POST':
        userID=session['userID']

        conn=get_db_connection()
        if conn is None:
            flash('NO DB CONNECTION', category='error')
            redirect(url_for('authentication.landing'))
        cursor=conn.cursor()

        try:
            sql="DELETE FROM patientmedicalinfo WHERE medicalInfoID=%s AND userID=%s"
            val=(medicalInfoID, userID)
            cursor.execute(sql, val)
            conn.commit()
            flash("Successfully deleted patient medical record!", category='success')
            return redirect(url_for('nurse.medicalManage'))
        except Error as e:
            conn.rollback()
            flash(f"{e}", category='error') 
            return redirect(url_for('nurse.medicalManage'))
        finally:
            cursor.close()
            conn.close()
