from flask import url_for, session, request
from twilio.twiml.messaging_response import MessagingResponse

from glogic import app, db
from glogic.models import BaselineAnswers, BaselineQuestions, User
from .gresponses import Dictionary


# view for collecting organisation details
@app.route('/baseline', methods=["GET", "POST"])
def baseline():
    session['View'] = 'baseline'
    response = MessagingResponse()

    num = request.form.get('From')
    num = num.replace('whatsapp:', '')

    if 'question_id' in session:
        return answers(session['question_id'], response, num)
    else:
        first_question = redirect_to_first_question(response)
        response.message(first_question.content)
    return str(response)


def answers(question_id, response, num):
    question = BaselineQuestions.query.get(question_id)

    incoming_msg = request.form.get('Body').lower()

    db.save(BaselineAnswers(content=incoming_msg,
                             question=question,
                             user=User.query.filter(User.number == num).first()))

    next_question = question.next()

    if next_question:
        response.message(questions(next_question.id))

    else:
        user = User.query.filter(User.number == num).first()
        user.registered = 1
        db.session.commit()
        response.message(
            'Thank you! You are now registered for our monthly surveys. It is important you complete each one over the \
next 21 months. If you want to stop receiving the surveys, please send STOP. Reply to this message with *Hi* to be returned to the main menu')
        del (session['question_id'])
        del session['view']

    return str(response)


def questions(question_id):
    question = BaselineQuestions.query.get(question_id)
    session['question_id'] = question.id
    return question.content


# goes to question view and finds first question
def redirect_to_first_question(response):
    session['question_id'] = 1
    return BaselineQuestions.query.first()