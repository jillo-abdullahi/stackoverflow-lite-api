# models.py
class User(object):
    """Class for users"""

    def __init__(self):
        self.users = {}

    def save(self, user_details):
        """Method to create user and add to user dictionary"""
        id = str(len(self.users) + 1)
        self.users[str(id)] = user_details
