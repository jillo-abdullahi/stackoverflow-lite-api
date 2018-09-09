"""Test file for posting of answers"""

import unittest
import json

from app import create_app


class TestAnswers(unittest.TestCase):
    """Class to test for answers"""

    def setUp(self):
        """Method to create app and set up test client"""
        self.app = create_app("testing")
        self.app = self.app.test_client()

        self.question_details = {
            "title": "How to exit Vim on Ubuntu 16.04",
            "description": "How does one get the exit Vim from terminal?"}

    def test_user_can_add_answer(self):
        """Method to test if user can add an answer"""
        answer_details = {"description": "Type Ctrl+O to exit"}

        # Post a question first
        question_response = self.app.post(
            '/stackoverflowlite/api/v1/questions',
            data=json.dumps(self.question_details),
            content_type='application/json')

        self.assertEqual(question_response.status_code, 201)

        # Try to post an answer
        response = self.app.post(
            '/stackoverflowlite/api/v1/questions/1/answers',
            data=json.dumps(answer_details),
            content_type='application/json')

        self.assertEqual(response.status_code, 201)

        # Test message
        message = json.loads(response.get_data(as_text=True))[
            'message']
        self.assertEqual(message, 'Answer successfully posted')
