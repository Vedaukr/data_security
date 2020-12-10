from flask import request, abort, jsonify
from config import app, db
from auth import *
from models import User

@app.route('/login', methods=['POST'])
def login():
    try:
        user_login = request.json["login"]
        user_password = request.json["password"]
        if user_login is None or user_password is None:
            jsonify({"error_message": "Username or password is absent."}), 400
        
        user = User.query.filter_by(login = user_login).first()
        if user is None:
            jsonify({"error_message": "User is nor existing."}), 400

        if not user.verify_password(user_password):
            jsonify({"error_message": "Password is not correct."}), 401

        token = encode_auth_token(user_login)
        return jsonify({"token": str(token)})

    except Exception as e:
        return jsonify({"error_message": e}), 400    


@app.route('/register', methods=['POST'])
def register():
    try:
        user_login = request.json["login"]
        user_password = request.json["password"]
        if user_login is None or user_password is None:
            return jsonify({"error_message": "Username or password is absent."}), 400
        
        if User.query.filter_by(login = user_login).first() is not None:
            return jsonify({"error_message": "User with this login has already registered."}), 400
        
        token = encode_auth_token(user_login)
        user = User(login=user_login)
        user.set_password(user_password)
        user.set_data(request.json)
        db.session.add(user)
        db.session.commit()
        return jsonify({"token": token})

    except Exception as e:
        return jsonify({"error_message": str(e)}), 400    


@app.route('/show_info', methods=['POST'])
def show_info():
    try:
        user_token = request.json["token"]
        user_login = decode_auth_token(user_token)
        user = User.query.filter_by(login = user_login).first()
        if user is None:
            return jsonify({"error_message": "User is nor existing."}), 400

        return jsonify(user.to_obj())

    except Exception as e:
        return jsonify({"error_message": str(e)}), 400
