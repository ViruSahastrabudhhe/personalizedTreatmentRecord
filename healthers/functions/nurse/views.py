from . import nurse
from .getters import getPatientsList, getMedicalInfo, getDiagnosis, getFindings, getPatientNamesForArchivedMedicalInfo, getPatientNamesFromPatientInfo, getArchivedPatientsList, getArchivedMedicalInfo, getPatientCount, getMedicalCount, getFindingsCount, getDiagnosisCount
from flask import render_template, flash, redirect, url_for, request, session

@nurse.route('/nurse/dashboard')
def nurseDashboard():
    patientRows=getPatientCount()
    medicalRows=getMedicalCount()
    diagnosisRows=getDiagnosisCount()
    findingsRows=getFindingsCount()
    return render_template('users/nurse/panels/dashboard.html', patientRows=patientRows, medicalRows=medicalRows, diagnosisRows=diagnosisRows, findingsRows=findingsRows, legend="Lumban RHU", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientMedicalInfo/manage')
def medicalManage():
    rows=getMedicalInfo()
    nameRows=getPatientNamesFromPatientInfo()
    return render_template('users/nurse/panels/patientMedical/medical_manage.html', nameRows=nameRows, rows=rows, legend="Manage patients medical info", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientMedicalInfo/add')
def medicalAdd():
    rows=getPatientsList()
    return render_template('users/nurse/panels/patientMedical/medical_add.html', rows=rows, legend="Add patient medical info", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientMedicalInfo/edit')
def medicalEdit():
    rows=getPatientsList()
    return render_template('users/nurse/panels/patientMedical/medical_edit.html', rows=rows, legend="Edit patient medical info", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientMedicalInfo/archived')
def medicalArchive():
    rows=getArchivedMedicalInfo()
    nameRows=getPatientNamesForArchivedMedicalInfo()
    return render_template('users/nurse/panels/patientMedical/medical_archived.html', nameRows=nameRows, rows=rows, legend="Archive patient medical info", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientsList/manage')
def patientsListManage():
    rows=getPatientsList()
    return render_template('users/nurse/panels/patientsList/patientsList_manage.html', rows=rows, legend="Manage patients list", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientsList/add')
def patientsListAdd():
    return render_template('users/nurse/panels/patientsList/patientsList_add.html', legend="Add patients to list", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientsList/edit')
def patientsListEdit():
    return render_template('users/nurse/panels/patientsList/patientsList_edit.html', legend="Edit patients in list", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/patientsList/archive')
def patientsListArchive():
    rows=getArchivedPatientsList()
    return render_template('users/nurse/panels/patientsList/patientsList_archived.html', rows=rows, legend="Archive patients", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/requests')
def nurseRequests():
    rows=getArchivedPatientsList()
    return render_template('users/nurse/panels/requests/nurse_requests.html', rows=rows, legend="Requests", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/requests/archive')
def nurseRequestsArchive():
    rows=getArchivedPatientsList()
    return render_template('users/nurse/panels/requests/nurse_requests_archived.html', rows=rows, legend="Request archive", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/diagnoses')
def maintenanceDiagnoses():
    rows=getDiagnosis()
    return render_template('users/nurse/panels/maintenance/diagnoses.html', rows=rows, legend="Diagnoses", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/findings')
def maintenanceFindings():
    rows=getFindings()
    return render_template('users/nurse/panels/maintenance/findings.html', rows=rows, legend="Findings", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@nurse.route('/nurse/illnesses')
def maintenanceIllnesses():
    return render_template('users/nurse/panels/maintenance/illnesses.html', legend="Illnesses", fname=session['fname'], lname=session['lname'], userID=session['userID'])