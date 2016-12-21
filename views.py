from flask import render_template, request,flash, redirect, url_for
from app import app, db
from app.models import register
 
@app.route('/login' , methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        post=Post(request.form['username'], request.form['password'])
        db.session.add(register)
        db.session.commit()
        flash('you are successfully logged in')     
 
    return render_template('login.html')