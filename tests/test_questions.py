# Tests for questions

import unittest
import json

from app import create_app


class TestQuestions(unittest.TestCase):
    """Class to test for user ability to login"""

    def setUp(self):
        """Method to create app and set up test client"""
        self.app = create_app("testing")
        self.app = self.app.test_client()

    def test_user_can_post_question(self):
        """Method to test if a new question can be added"""
        response = self.add_question()
        self.assertEqual(response.status_code, 201)

    def test_user_can_get_all_questions(self):
        """Method to test if user can get all questions"""
        # First add a question
        response = add_question()
        self.assertEqual(response.status_code, 201)

        # Attempt to get all questions
        get_response = self.app.get('/stackoverflowlite/api/v1/questions',
                                    headers={
                                        "content-type": "application/json"})
        self.assertEqual(get_response.status, 200)

    def test_user_can_get_specific_question(self):
        """Method to test if a user can get a specific question"""
        # First add a question
        response = add_question()
        self.assertEqual(response.status_code, 201)

        # Attempt to get specific question
        get_response = self.app.get('/stackoverflowlite/api/v1/questions/1',
                                    headers={
                                        "content-type": "application/json"})
        self.assertEqual(get_response.status, 200)

    def add_question(self):
        """Method to add new question"""
        question_details = {
            "title": "How to exit Vim on Ubuntu",
            "description": "How does one get the hell out of Vim from terminal?"}

            response = self.app.post(
                '/stackoverflowlite/api/v1/questions',
                data=json.dumps(question_details),
                content_type='application/json'
            )

        return response
