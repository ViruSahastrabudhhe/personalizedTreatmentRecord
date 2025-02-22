from . import nurse
from healthers.models import get_db_connection
import mysql.connector
from mysql.connector import Error
from flask import render_template, flash, redirect, url_for, request, session

@nurse.route('/dashboard')
def dashboard():
    return render_template('users/nurse/panels/dashboard.html', legend="Lumban RHU", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/patientMedicalInformation/manage')
def medicalManage():
    return render_template('users/nurse/panels/patientMedical/medical_manage.html', legend="Manage patients medical info", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/patientMedicalInformation/add')
def medicalAdd():
    return render_template('users/nurse/panels/patientMedical/medical_add.html', legend="Add patient medical info", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/patientMedicalInformation/edit')
def medicalEdit():
    return render_template('users/nurse/panels/patientMedical/medical_edit.html', legend="Edit patient medical info", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/patientMedicalInformation/archive')
def medicalArchive():
    return render_template('users/nurse/panels/patientMedical/medical_archived.html', legend="Archive patient medical info", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/patientsList/manage')
def patientsListManage():
    return render_template('users/nurse/panels/patientsList/patientsList_manage.html', legend="Manage patients list", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/patientsList/add')
def patientsListAdd():
    return render_template('users/nurse/panels/patientsList/patientsList_add.html', legend="Add patients to list", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/patientsList/edit')
def patientsListEdit():
    return render_template('users/nurse/panels/patientsList/patientsList_edit.html', legend="Edit patients in list", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/patientsList/archive')
def patientsListArchive():
    return render_template('users/nurse/panels/patientsList/patientsList_archived.html', legend="Archive patients", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/diagnoses')
def maintenanceDiagnoses():
    return render_template('users/nurse/panels/maintenance/diagnoses.html', legend="Diagnoses", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/findings')
def maintenanceFindings():
    return render_template('users/nurse/panels/maintenance/findings.html', legend="Findings", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/illnesses')
def maintenanceIllnesses():
    return render_template('users/nurse/panels/maintenance/illnesses.html', legend="Illnesses", fname=session['fname'], lname=session['lname'], userID=session['userID'])