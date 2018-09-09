"""File for view functions for getting and posting questions"""

from flask import Blueprint, jsonify, request

from app.utilities import validate_question
from app.v1.models import Question

questions = Blueprint("questions_blueprint", __name__,
                      url_prefix="/stackoverflowlite/api/v1")

question_instance = Question()


@questions.route('/questions', methods=['POST'])
def post_question():
    """method to post a new question"""
    question_info = request.get_json()

    # validate question
    if validate_question(question_info):
        return validate_question(question_info)

    # Check if question already exists
    existing_questions = question_instance.questions
    for qn_id in existing_questions:
        if question_info['title'].lower() == existing_questions[qn_id]['title'].lower():
            response = jsonify(
                {"Error": "That question has already been asked"})
            return response, 400

    # Add question
    existing_questions = question_instance.questions
    question_instance.save(question_info)
    response = jsonify(
        {"message": "Question added successfully", "Questions": existing_questions})
    return response, 201


@questions.route('/questions', methods=['GET'])
def get_questions():
    """method to fetch all questions"""
    all_questions = question_instance.questions

    response = jsonify({"All questions": all_questions})
    return response, 200


@questions.route('/questions/<question_id>', methods=['GET'])
def fetch_specific_question(question_id):
    """Method to fetch a specific question using id"""
    all_questions = question_instance.questions

    # Check if question exists
    for qn_id in all_questions:
        if question_id == qn_id:
            response = jsonify({"message": all_questions[qn_id]})
            return response, 200
    response = jsonify({"Error": "A question with that id doesn't exist"})
    return response, 404
