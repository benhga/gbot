from flask import url_for, session, request
from twilio.twiml.messaging_response import MessagingResponse

from glogic import app, db
from glogic.models import BaselineAnswers, BaselineQuestions, User
from .gresponses import Dictionary

# view for collecting organisation details
from .send_airtime import send_airtime_after_survey

@app.route('/baseline', methods=["GET", "POST"])
def baseline():
    session['View'] = 'baseline'
    response = MessagingResponse()

    num = request.form.get('From')
    num = num.replace('whatsapp:', '')

    if 'question_id' in session:
        return answers(session['question_id'], response, num)
    # else:
    #     first_question = redirect_to_first_question(response)
    #     response.message(first_question.content)

    else:
        # response.message("Please type _only the number_ of your answer.")
        if "YES" not in request.form.get('Body'):
            response.message(Dictionary["welcome3"])

        else:
            first_question = redirect_to_first_question(response)
            response.message(first_question.content)

    return str(response)








def answers(question_id, response, num):
    question = BaselineQuestions.query.get(question_id)

    incoming_msg = request.form.get('Body').lower()
    next_question = question.next()

    if question_id == 14:
        if incoming_msg == 'skip':
            response.message(questions(next_question.id))
    #

    db.save(BaselineAnswers(content=incoming_msg,
                            question=question,
                            user=User.query.filter(User.number == num).first()))

    if next_question:
        response.message(questions(next_question.id))

    else:
        user = User.query.filter(User.number == num).first()
        user.registered = 1
        db.session.commit()

        airtime = send_airtime_after_survey(num)
        # airtime = 0

        response.message(
            'Thank you! You have completed our first survey and you’ve earned R75 airtime which is on its way to you '
            'now.')
        response.message("You are now registered for our monthly surveys and we kindly ask you to complete the 3 "
                         "questions every month, for the next one and a half years. You will be notified when a new "
                         "survey is available.\n\nIf you want to stop receiving the surveys, please send *STOP*.")
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
