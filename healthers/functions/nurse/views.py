from . import nurse
from flask import render_template, flash, redirect, url_for, request, session

@nurse.route('/nurse/dashboard')
def nurseDashboard():
    return render_template('users/nurse/panels/dashboard.html', legend="Lumban RHU", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientMedicalInfo/manage')
def medicalManage():
    return render_template('users/nurse/panels/patientMedical/medical_manage.html', legend="Manage patients medical info", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientMedicalInfo/add')
def medicalAdd():
    return render_template('users/nurse/panels/patientMedical/medical_add.html', legend="Add patient medical info", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientMedicalInfo/edit')
def medicalEdit():
    return render_template('users/nurse/panels/patientMedical/medical_edit.html', legend="Edit patient medical info", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientMedicalInfo/archived')
def medicalArchive():
    return render_template('users/nurse/panels/patientMedical/medical_archived.html', legend="Archive patient medical info", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientsList/manage')
def patientsListManage():
    return render_template('users/nurse/panels/patientsList/patientsList_manage.html', legend="Manage patients list", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientsList/add')
def patientsListAdd():
    return render_template('users/nurse/panels/patientsList/patientsList_add.html', legend="Add patients to list", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientsList/edit')
def patientsListEdit():
    return render_template('users/nurse/panels/patientsList/patientsList_edit.html', legend="Edit patients in list", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientsList/archive')
def patientsListArchive():
    return render_template('users/nurse/panels/patientsList/patientsList_archived.html', legend="Archive patients", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/diagnoses')
def maintenanceDiagnoses():
    return render_template('users/nurse/panels/maintenance/diagnoses.html', legend="Diagnoses", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/findings')
def maintenanceFindings():
    return render_template('users/nurse/panels/maintenance/findings.html', legend="Findings", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/illnesses')
def maintenanceIllnesses():
    return render_template('users/nurse/panels/maintenance/illnesses.html', legend="Illnesses", fname=session['fname'], lname=session['lname'], userID=session['userID'])