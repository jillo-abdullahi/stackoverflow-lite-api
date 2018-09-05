# app/v1/views/answers.py

from flask import Blueprint, jsonify, request

from app.utilities import check_keys, check_empty_dict
from app.v1.models import Answer, Question

answers = Blueprint("answers_blueprint", __name__,
                    url_prefix="/stackoverflowlite/api/v1/questions")

answer_instance = Answer()
question_instance = Question()


@answers.route('/<question_id>/answers', methods=['POST'])
def post_answer(question_id):
    """method to post a new answer"""
    answer_info = request.get_json()

    # Check that all fields have been provided
    if check_keys(answer_info, 1):
        response = jsonify(
            {"Error": "Please provide answer description"})
        return response, 400

    # Check for empty values
    if check_empty_dict(answer_info):
        response = jsonify({"Error": "Description must not be empty"})
        return response, 400

    # Check of question with id exists
    all_questions = question_instance.questions
    for id in all_questions:
        if id not in all_questions.keys():
            response = jsonify(
                {"Error": "Question with that id doesn't exist"})
            return response, 404

    # Save answer
    answer_instance.save(answer_info, question_id)

    response = jsonify(
        {"message": "Answer successfully posted", "Answers": answer_instance.answers})
    return response, 201
