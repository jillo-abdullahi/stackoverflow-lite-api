[![Build Status](https://travis-ci.org/jillo-abdullahi/stackoverflow-lite-api.svg?branch=ft-questions)](https://travis-ci.org/jillo-abdullahi/stackoverflow-lite-api)
[![Coverage Status](https://coveralls.io/repos/github/jillo-abdullahi/stackoverflow-lite-api/badge.svg?branch=ft-questions)](https://coveralls.io/github/jillo-abdullahi/stackoverflow-lite-api?branch=ft-questions)
[![Maintainability](https://api.codeclimate.com/v1/badges/bea7461d642bc57f9021/maintainability)](https://codeclimate.com/github/jillo-abdullahi/stackoverflow-lite-api/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fef2dd471f8943d09084074478a31196)](https://www.codacy.com/app/jillo-abdullahi/stackoverflow-lite-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jillo-abdullahi/stackoverflow-lite-api&amp;utm_campaign=Badge_Grade)


# stackoverflow-lite
This web application is a platform that enables you to ask programming questions for those times when you get stuck and get answers from other like-minded individuals. What's even more fun is that you can provide your answers to questions from other programmers. 

# Installation - API

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




