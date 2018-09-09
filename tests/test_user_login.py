"""Test file for user login"""

import unittest
import json

from app import create_app


class TestUserCanLogin(unittest.TestCase):
    """Class to test for user ability to login"""

    def setUp(self):
        """Method to create app and set up test client"""
        self.app = create_app("testing")
        self.app = self.app.test_client()

        self. new_user_details = {
            "username": "jdoe",
            "email": "john.doe@gmail.com",
            "password": "johndoe95",
            "confirm-password": "johndoe95"
        }

        self.user_login_details = {
            "email": "john.doe@gmail.com",
            "password": "johndoe95"}

    def test_user_can_login(self):
        """Method to test if the use can log in"""
        # Register user first
        register_response = self.app.post(
            '/stackoverflowlite/api/v1/auth/signup',
            data=json.dumps(self.new_user_details),
            content_type='application/json'
        )
        self.assertEqual(register_response.status_code, 201)

        # Login user
        login_response = self.app.post(
            '/stackoverflowlite/api/v1/auth/signin',
            data=json.dumps(self.user_login_details),
            content_type='application/json')

        self.assertEqual(login_response.status_code, 200)

        # Test message
        message = json.loads(login_response.get_data(as_text=True))['message']
        self.assertEqual(message, 'User login successful')
