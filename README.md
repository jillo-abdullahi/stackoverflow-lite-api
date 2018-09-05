# stackoverflow-lite
This web application is a platform that enables you to ask programming questions for those times when you get stuck and get answers from other like-minded individuals. What's even more fun is that you can provide your answers to questions from other programmers. 

# Installation - UI
To get a view of the front-end UI, do the following:&nbsp;

Clone the repository into your local environment: &nbsp;
`git clone https://github.com/jillo-abdullahi/stackoverflow-lite`&nbsp;

Switch to stackoverflow-lite directory you just cloned:&nbsp;
`cd stackoverflow-lite/UI`&nbsp;

Run `index.html` file in your browser.&nbsp;

#### UI link to gh-pages:

https://jillo-abdullahi.github.io/stackoverflow-lite/ui/ &nbsp; 

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




