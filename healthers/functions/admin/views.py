from . import admin
from flask import render_template, flash, redirect, url_for, request, session

@admin.route('/admin/dashboard')
def adminDashboard():
    return render_template('ASDASD', legend="Lumban RHU", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@admin.route('/admin/manageCurrentUsers')
def adminManage():
    return render_template('ASD', legend="Lumban RHU", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@admin.route('/admin/manageCurrentUsers/edit')
def adminEdit():
    return render_template('ASD', legend="Lumban RHU", fname=session['fname'], lname=session['lname'], userID=session['userID'])