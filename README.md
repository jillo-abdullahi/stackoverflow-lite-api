[![Build Status](https://travis-ci.org/jillo-abdullahi/stackoverflow-lite-api.svg?branch=ft-questions)](https://travis-ci.org/jillo-abdullahi/stackoverflow-lite-api)
[![Coverage Status](https://coveralls.io/repos/github/jillo-abdullahi/stackoverflow-lite-api/badge.svg?branch=ft-questions)](https://coveralls.io/github/jillo-abdullahi/stackoverflow-lite-api?branch=ft-questions)
[![Maintainability](https://api.codeclimate.com/v1/badges/bea7461d642bc57f9021/maintainability)](https://codeclimate.com/github/jillo-abdullahi/stackoverflow-lite-api/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fef2dd471f8943d09084074478a31196)](https://www.codacy.com/app/jillo-abdullahi/stackoverflow-lite-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jillo-abdullahi/stackoverflow-lite-api&amp;utm_campaign=Badge_Grade)


# stackoverflow-lite
This web application is a platform that enables you to ask programming questions for those times when you get stuck and get answers from other like-minded individuals. What's even more fun is that you can provide your answers to questions from other programmers. 

# Documentation

**EndPoint** | **Functionality**
--- | ---
POST `/auth/signup` | Register a user.
POST `/auth/login` | Login a user.
POST  `/questions` | Post a question.
POST `/questions/<questionId>/answers`| Post an answer to a question.
GET `/questions`| Fetch all questions.
GET `/questions/<questionId>`| Fetch a specific question.
PUT `/questions/<questionId>/answers/<answerId>`| Mark an answer as accepted or update an answer.
DELETE `/questions/<questionId>` | Delete a question.

## Setup

Use this guide to get this project up and running:

### Dependencies

1. [python 3.x](https://www.python.org/downloads/)
2. [Git](https://git-scm.com)
3. Working browser or [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?utm_source=chrome-app-launcher-info-dialog)
4. [virtualenv](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) for an isolated working environment.&nbsp;

### Getting started

| **Instruction** | **Command** |
| --- | --- |
| 1. Clone the repo into a folder of your choice | `git clone --depth=50 https://github.com/jillo-abdullahi/stackoverflow-lite-api.git` |
| 2. Navigate to the cloned folder | `cd stackoverflow-lite-api`|
| 3. Create a virtual environment |`virtualenv venv` |
| 4. Activate the virtual environment you just created | `source venv/bin/activate` |
| 5. Install all dependencies into your virtual environment | `pip install -r requirements.txt` |
| 6. Confirm you have all packages installed | `pip freeze` |
| 7. Set environment variables for `APP_SETTINGS` | `export APP_SETTINGS="development"` |
| 8. Set the entry point for the app | `export FLASK_APP="run.py"` |

### Run the service

Get the app running by typing
`flask run`

## Testing

To run all tests type
`nosetests --with-coverage --cover-package=app`


