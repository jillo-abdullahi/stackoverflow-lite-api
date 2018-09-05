# Test for user login
import unittest
import json

from app import create_app


class TestUserCanLogin(unittest.TestCase):
    """Class to test for user ability to login"""

    def setUp(self):
        """Method to create app and set up test client"""
        self.app = create_app("testing")
        self.app = self.app.test_client()

    def test_user_can_login(self):
        """Method to test if the use can log in"""
        # Register user first
        register_response = self.register_user()
        self.assertEqual(register_response.status_code, 201)

        # Login user
        login_response = self.signin_user()
        self.assertEqual(login_response.status_code, 200)

        # Test message
        message = json.loads(login_response.get_data(as_text=True))['message']
        self.assertEqual(message, 'User login successful')

    def register_user(self):
        """Method to try to register a new user"""
        new_user_details = {
            "username": "jdoe",
            "full-name": "John Doe",
            "email": "john.doe@gmail.com",
            "password": "johndoe95"
        }

        response = self.app.post(
            '/stackoverflowlite/api/v1/auth/signup',
            data=json.dumps(new_user_details),
            content_type='application/json'
        )

        return response

    def signin_user(self):
        """Method to try to login registered user"""
        user_login_details = {
            "email": "john.doe@gmail.com",
            "password": "johndoe95"}

        response = self.app.post(
            '/stackoverflowlite/api/v1/auth/signin',
            data=json.dumps(user_login_details),
            content_type='application/json')

        return response
