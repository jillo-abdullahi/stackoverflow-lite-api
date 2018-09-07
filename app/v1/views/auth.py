"""File for view functions for user authentication"""

from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

from app.v1.models import User
from app.utilities import validate_login, validate_signup

auth = Blueprint(
    'auth_blueprint', __name__, url_prefix='/stackoverflowlite/api/v1/auth')

user_instance = User()


@auth.route('/signup', methods=['POST'])
def user_signup():
    """Method to register a new user"""
    user_info = request.get_json()

    # Validation checks
    if validate_signup(user_info):
        return validate_signup(user_info)

    existing_users = user_instance.users
    user_info["password"] = generate_password_hash(user_info["password"])
    user_info[
        "confirm-password"] = generate_password_hash(user_info["confirm-password"])
    user_instance.save(user_info)
    response = jsonify({"Users": existing_users,
                        "message": "User registered successfully"})
    return response, 201


@auth.route('/signin', methods=['POST'])
def user_login():
    """Method to login a user"""
    user_info = request.get_json()

    # Validation checks
    if validate_login(user_info):
        return validate_login(user_info)

    existing_users = user_instance.users
    password = user_info["password"]

    for id in existing_users:
        if user_info["email"] == existing_users[id]["email"] and check_password_hash(existing_users[id]["password"], password):

            return jsonify({"user": existing_users[id], "message": "User login successful"}), 200

    return jsonify({"Login failed": "Incorrect email or password"}), 401
