# app/v1/views/questions

from flask import Blueprint, jsonify, request

questions = Blueprint("questions_blueprint", __name__,
                      url_prefix="/stackoverflowlite/api/v1/questions")


@questions.route('/', methods=['POST'])
def post_question():
    """method to post a new question"""
    question_info = request.get_json()

    return jsonify({"Question": question_info})


@questions.route('/', methods=['GET'])
def get_questions():
    """method to fetch all questions"""

    return jsonify({"Questions": "All questions"})


@questions.route('/<question_id>', methods=['GET'])
def fetch_specific_question(question_id):
    """Method to fetch a specific question using id"""

    return jsonify({"Question": "Question matching id"})


@questions.route('/<question_id>', methods=['DELETE'])
def delete_specific_question(question_id):
    """Method to delete a specific question"""

    return jsonify({"message": "Question deleted if id matches"})


@questions.route('/<question_id>/answers', methods=['POST'])
def post_answer_to_question(question_id):
    """Method to post answer to a specific question"""

    return jsonify({"message": "Success if question exists"})


@questions.route('/<question_id>/answers/<answer_id>', methods=['PUT'])
def accept_answer(question_id, answer_id):
    """Method to accept an answer to a specific question"""

    return jsonify({"message": "Success if question and answer found"})
