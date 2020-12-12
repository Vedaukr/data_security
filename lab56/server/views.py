from flask import request, abort, jsonify
from config import app, db
from auth import *
from models import User
from flask import Blueprint, render_template, session, redirect, url_for

@app.route('/login', methods=['POST'])
def login():
    try:
        user_login = request.form.get("login")
        user_password = request.form.get("password")
        if user_login is None or user_password is None:
            return redirect_error("Username or password is absent.") 
        
        user = User.query.filter_by(login = user_login).first()
        if user is None:
            return redirect_error("User does not exist.") 

        if not user.verify_password(user_password):
            return redirect_error("Password is not correct.") 

        token = encode_auth_token(user_login)
        session["token"] = token
        return redirect(url_for('show_info'))

    except Exception as e:
        return redirect_error(str(e)) 


@app.route('/register', methods=['POST'])
def register():
    #try:
    user_login = request.form.get("login")
    user_password = request.form.get("password")
    if user_login is None or user_password is None:
        return redirect_error("Username or password is absent.") 
    
    if User.query.filter_by(login = user_login).first() is not None:
        return redirect_error("User with this login has already registered.") 
    
    token = encode_auth_token(user_login)

    user = User(login=user_login)
    user.hash_password(user_password)
    user.set_data(request.form)

    db.session.add(user)
    db.session.commit()
    session['token'] = token
    return redirect(url_for('show_info'))

    #except Exception as e:
        #print(type(e))
        #return redirect_error(str(e))


@app.route('/show_info', methods=['GET'])
def show_info():
    #try:
    if not session['token']:
        return redirect(url_for('login'))
    user_login = decode_auth_token(session['token'])
    user = User.query.filter_by(login = user_login).first()
    return render_template('profile.html', user=user) 
    #except Exception as e:
        #print(type(e))
        #return redirect_error(str(e))
    
@app.route('/register', methods=['GET'])
def get_register():
    return render_template('signup.html') 

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html') 

@app.route('/logout', methods=['GET'])
def logout():
    session['token'] = None
    return redirect(url_for('login'))


def redirect_error(msg):
    return render_template('error.html', error_message=msg) 