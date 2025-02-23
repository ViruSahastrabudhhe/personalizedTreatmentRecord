from . import patient
from flask import render_template, flash, redirect, url_for, request, session

@patient.route('/patient/dashboard')
def patientDashboard():
    return render_template('users/patient/panels/dashboard.html', legend="Patient dashboard", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@patient.route('/patient/medicalRecords')
def patientMedicalRecords():
    return render_template('users/patient/panels/records/records.html', legend="Medical records", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@patient.route('/patient/medicalRecords/archive')
def patientMedicalRecordsArchive():
    return render_template('users/patient/panels/records/records_archived.html', legend="Archived medical records", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@patient.route('/patient/requests/add')
def patientCreateRequest():
    return render_template('users/patient/panels/requests/requests_add.html', legend="Create request", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@patient.route('/patient/requests/archived')
def patientRequestArchive():
    return render_template('users/patient/panels/requests/requests_archived.html', legend="Archived requests", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@patient.route('/patient/requests/history')
def patientRequestHistory():
    return render_template('users/patient/panels/requests/requests_history.html', legend="Request history", fname=session['fname'], lname=session['lname'], userID=session['userID'])
