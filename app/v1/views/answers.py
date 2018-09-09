"""File for view functions pertaining to answers"""

from flask import Blueprint, jsonify, request

from app.utilities import validate_answer
from app.v1.models import Answer, Question

answers = Blueprint("answers_blueprint", __name__,
                    url_prefix="/stackoverflowlite/api/v1/questions")

answer_instance = Answer()
question_instance = Question()


@answers.route('/<question_id>/answers', methods=['POST'])
def post_answer(question_id):
    """method to post a new answer"""
    answer_info = request.get_json()

    # Validation checks
    if validate_answer(answer_info):
        return validate_answer(answer_info)

    # Check if question with id exists
    all_questions = question_instance.questions
    for qn_id in all_questions:
        if question_id not in question[qn_id]["question_id"]:
            response = jsonify(
                {"Error": "Question with that id doesn't exist"})
            return response, 404

    # Save answer
    answer_instance.save(answer_info, question_id)

    response = jsonify(
        {"message": "Answer successfully posted", "Answers": answer_instance.answers})
    return response, 201
