# app/v1/views/questions

from flask import Blueprint, jsonify, request

from app.utilities import check_keys, check_empty_dict
from app.v1.models import Question

questions = Blueprint("questions_blueprint", __name__,
                      url_prefix="/stackoverflowlite/api/v1")

question_instance = Question()


@questions.route('/questions', methods=['POST'])
def post_question():
    """method to post a new question"""
    question_info = request.get_json()

    # Check that all fields have been provided
    if check_keys(question_info, 2):
        response = jsonify(
            {"Error": "Please provide question title and description"})
        return response, 400

    # Check for empty values
    if check_empty_dict(question_info):
        response = jsonify({"Error": "Fields must not be empty"})
        return response, 400

    # Check if question's already been asked
    existing_questions = question_instance.questions
    for id in existing_questions:
        if question_info['title'].lower() == existing_questions[id]['title'].lower():
            response = jsonify(
                {"Error": "That question has already been asked"})
            return response, 400
    # Add question
    question_instance.save(question_info)
    response = jsonify(
        {"message": "Question added successfully", "Questions": existing_questions})
    return response, 201


@questions.route('/questions', methods=['GET'])
def get_questions():
    """method to fetch all questions"""

    return jsonify({"Questions": "All questions"})


@questions.route('questions/<question_id>', methods=['GET'])
def fetch_specific_question(question_id):
    """Method to fetch a specific question using id"""

    return jsonify({"Question": "Question matching id"})
