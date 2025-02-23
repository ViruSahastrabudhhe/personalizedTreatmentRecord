from . import admin
from flask import render_template, flash, redirect, url_for, request, session

@admin.route('/admin/dashboard')
def adminDashboard():
    return render_template('/users/admin/panels/dashboard.html', legend="Admin dashboard", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@admin.route('/admin/manageCurrentUsers')
def adminManage():
    return render_template('/users/admin/panels/currentUsers/admin_users.html', legend="Manage users", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@admin.route('/admin/manageCurrentUsers/edit')
def adminEdit():
    return render_template('/users/admin/panels/currentUsers/admin_users_edit.html', legend="Edit users", fname=session['fname'], lname=session['lname'], userID=session['userID'])

@admin.route('/admin/manageCurrentUsers/archived')
def adminUserArchive():
    return render_template('/users/admin/panels/currentUsers/admin_users_archived.html', legend="Archived users", fname=session['fname'], lname=session['lname'], userID=session['userID'])