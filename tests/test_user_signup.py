# Test for user signup
import unittest
import json

from app import create_app


class TestUserCanSignup(unittest.TestCase):
    """Class to test for user ability to register"""

    def setUp(self):
        """Method to create app and set up test client"""
        self.app = create_app("testing")
        self.app = self.app.test_client()

    def test_user_can_signup(self):
        """Method to test if user can register"""
        register_response = self.register_user()
        self.assertEqual(register_response.status_code, 201)

        # Test message
        message = json.loads(register_response.get_data(as_text=True))[
            'message']
        self.assertEqual(message, 'User registered successfully')

    def register_user(self):
        """Method to try to register a new user"""
        new_user_details = {
            "username": "MJane",
            "full-name": "Mary Jane",
            "email": "mary.jane@gmail.com",
            "password": "maryJane95"
        }

        response = self.app.post(
            '/stackoverflowlite/api/v1/auth/signup',
            data=json.dumps(new_user_details),
            content_type='application/json'
        )

        return response
