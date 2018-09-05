# app/v1/views/auth

from flask import Blueprint, jsonify, g, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_expects_json import expects_json

from app.v1.models import User
from app.utilities import check_empty_dict, check_keys

auth = Blueprint(
    'auth_blueprint', __name__, url_prefix='/stackoverflowlite/api/v1/auth')

user_instance = User()


@auth.route('/signup', methods=['POST'])
def user_signup():
    """Method to register a new user"""
    user_info = request.get_json()

    # Check if all keys have been provided.
    if check_keys(user_info, 4):
        response = jsonify({"Error": "Please provide all fields"})
        return response, 400

    # Check for empty keys before saving
    if check_empty_dict(user_info):
        response = jsonify({"Error": "Fields should not be empty"})
        return response, 400

    user_info["password"] = generate_password_hash(user_info["password"])

    # Check if user already exists
    existing_users = user_instance.users
    for id in existing_users:
        if user_info['username'].lower() == existing_users[id]['username'].lower():
            response = jsonify(
                {"Error": "A user with username, {} already exists".format(user_info['username'])})
            return response, 400

    user_instance.save(user_info)
    response = jsonify({"Users": existing_users,
                        "message": "User registered successfully"})
    return response, 201


@auth.route('/signin', methods=['POST'])
def user_login():
    """Method to login a user"""
    user_info = request.get_json()

    # Check if all required fields have been provided
    if check_keys(user_info, 2):
        response = jsonify({"Error": "Please provide email and password"})
        return response, 400

        # Check for empty values for keys
    if check_empty_dict(user_info):
        response = jsonify({"Error": "Fields should not be empty"})
        return response, 400

    existing_users = user_instance.users
    password = user_info["password"]

    for id in existing_users:
        if user_info["email"] == existing_users[id]["email"] and check_password_hash(existing_users[id]["password"], password):

            return jsonify({"user": existing_users[id], "message": "User login successful"}), 200

    return jsonify({"Login failed": "Incorrect email or password"}), 401
