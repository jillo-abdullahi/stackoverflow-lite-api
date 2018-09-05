# models.py
class User(object):
    """Class for users"""

    def __init__(self):
        self.users = {}

    def save(self, user_details):
        """Method to create user and add to user dictionary"""
        id = str(len(self.users) + 1)
        self.users[str(id)] = user_details


class Question(object):
    """Class for questions"""

    def __init__(self):
        self.questions = {}

    def save(self, question_details):
        """Method to add questions to questions dictionary"""
        id = str(len(self.questions) + 1)
        self.questions[str(id)] = question_details
