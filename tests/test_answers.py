"""All tests for posting answers to questions"""

import unittest
import json

from app import create_app


class TestQuestions(unittest.TestCase):
    """Class to test for answers"""

    def setUp(self):
        """Method to create app and set up test client"""
        self.app = create_app("testing")
        self.app = self.app.test_client()

    def test_user_can_add_answer(self):
        """Method to test if user can add an answer"""
        answer_details = {"description": "Type Ctrl+O to exit"}

        question_response = self.add_question()
        self.assertEqual(question_response.status_code, 201)

        response = self.app.post(
            '/stackoverflowlite/api/v1/questions/1/answers',
            data=json.dumps(answer_details),
            content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def add_question(self):
        """Method to add new question"""
        question_details = {
            "title": "How to exit Vim on Ubuntu 16.04",
            "description": "How does one get the hell out of Vim from terminal?"}

        response = self.app.post(
            '/stackoverflowlite/api/v1/questions',
            data=json.dumps(question_details),
            content_type='application/json')

        return response
