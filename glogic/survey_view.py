from datetime import datetime

from flask import request, session
from twilio.twiml.messaging_response import MessagingResponse

from . import app, db
from .models import MonthlyQuestions, MonthlyAnswers, User
from .send_airtime import send_airtime_after_survey

from .survey_runner import do_survey
from .utils import return_to_menu


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    session['view'] = 'survey'
    """
    Redirect for the careers view. Holds careers logic.
    :return str: response
    """
    num = request.form.get('From')
    num = num.replace('whatsapp:', '')

    incoming_msg = request.form.get('Body')
    resp = MessagingResponse()

    if incoming_msg == "STOP":
        resp.message("We will be sad to see you go. BETTER MESSAGE HERE")

        #TODO: write this not in pseudocode
        """
        user = User.query.filter(User.number = num).first()
        Users.delete(user)
        """
        return resp.message()





    incoming_msg = incoming_msg.lower()
    if 'question_id' in session:
        return answers(session['question_id'], resp, num)
    else:
        if user_error(num):
            mydate = datetime.now()
            mon = mydate.strftime("%B")
            resp.message(f"Our records indicate that you have already completed the survey for {mon}. We look forward to hearing from you next month.")
            return str(resp)
        first_question = redirect_to_first_question(resp)
        resp.message(first_question.content)
    return str(resp)

def answers(question_id, response, num):
    question = MonthlyQuestions.query.get(question_id)

    incoming_msg = request.form.get('Body').lower()

    # multi select for all
    for i in incoming_msg:
        if i == " " or i == ',':
            continue
        else:
            try:
                int(i)
            except ValueError:
                response.message(
                    "Please respond with the number of your response. Separate multiple options with a space or a comma only.")
                return str(response)
            else:
                if int(i) > question.num_ops:
                    response.message("Your answer is invalid. Please respond with one of the given options.")
                    return str(response)

    db.save(MonthlyAnswers(content=incoming_msg,
                             question=question,
                             user=User.query.filter(User.number == num).first()))

    next_question = question.next()

    if next_question:
        response.message(questions(next_question.id))

    else:
        user = User.query.filter(User.number == num).first()
        user.last_month_completed = int(datetime.now().month)
        db.session.commit()
        airtime = send_airtime_after_survey(num)
        # airtime = 0

        response.message("Thank you for completing the survey. Your R17 is on its way to you now. If " \
"you have not received your airtime or you would like to give feedback for the bot, please contact digital@genesis-analytics.com")

        del (session['question_id'])
        del session["view"]



    return str(response)


def questions(question_id):
    question = MonthlyQuestions.query.get(question_id)
    session['question_id'] = question.id
    return question.content


# goes to question view and finds first question
def redirect_to_first_question(response):
    current_month = int(datetime.now().month)

    # for running every 3 months
    # starting_q_mo = current_month % 3
    #
    # if starting_q_mo == 1:
    #     starting_q = 1
    # elif starting_q_mo == 2:
    #     stating_q = 4
    # else:
    #     starting_q = 7

    starting_q = 1
    session['question_id'] = starting_q

    return MonthlyQuestions.query.filter(MonthlyQuestions.id == starting_q).first()


# checks to see if user is in DB and, if not, adds them
def user_error(num):
    user = User.query.filter(User.number == num).first()

    if user is not None:
        current_month = int(datetime.now().month)
        if user.last_month_completed >= current_month:
            return True

    return False