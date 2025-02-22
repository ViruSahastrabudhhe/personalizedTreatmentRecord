from . import nurse
from healthers.models import get_db_connection
import mysql.connector
from mysql.connector import Error
from flask import render_template, flash, redirect, url_for, request, session

@nurse.route('/dashboard')
def dashboard():
    return render_template('users/nurse/panels/dashboard.html', legend="Lumban RHU")

@nurse.route('/patientMedicalInformation/manage')
def medicalManage():
    return render_template('users/nurse/panels/patientMedical/medical_manage.html', legend="Lumban RHU")

@nurse.route('/patientMedicalInformation/add')
def medicalAdd():
    return render_template('users/nurse/panels/patientMedical/medical_add.html', legend="Lumban RHU")

@nurse.route('/patientMedicalInformation/edit')
def medicalEdit():
    return render_template('users/nurse/panels/patientMedical/medical_edit.html', legend="Lumban RHU")

@nurse.route('/patientMedicalInformation/archive')
def medicalArchive():
    return render_template('users/nurse/panels/patientMedical/medical_archived.html', legend="Lumban RHU")

@nurse.route('/patientMedicalInformation/delete')
def medicalDelete():
    return ""

@nurse.route('/patientsList/manage')
def patientsListManage():
    return render_template('users/nurse/panels/patientsList/patientsList_manage.html', legend="Lumban RHU")

@nurse.route('/patientsList/add')
def patientsListAdd():
    return render_template('users/nurse/panels/patientsList/patientsList_add.html', legend="Lumban RHU")

@nurse.route('/patientsList/edit')
def patientsListEdit():
    return render_template('users/nurse/panels/patientsList/patientsList_edit.html', legend="Lumban RHU")

@nurse.route('/patientsList/archive')
def patientsListArchive():
    return render_template('users/nurse/panels/patientsList/patientsList_archived.html', legend="Lumban RHU")

@nurse.route('/patientsList/delete')
def patientsListDelete():
    return ""