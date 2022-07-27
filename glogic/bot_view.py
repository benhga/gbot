from . import app, db
from .gresponses import Dictionary, survey_questions
from .models import Responses, User
from flask import request, session, url_for
from twilio.twiml.messaging_response import MessagingResponse
import pandas as pd

@app.route('/message', methods=['GET', 'POST'])
def bot():
    # del session['view']
    # del session['question_id']
    # session.pop('q1')
    #
    # session.pop('q2')
    # session.modified = True
    # del session['q3']

    num = request.form.get('From')
    num = num.replace('whatsapp:', '')
    incoming_msg = request.form.get('Body').lower()

    print("INCOMING MSG: " + incoming_msg)

    resp = MessagingResponse()
    # msg = resp.message()

    if "stop" in incoming_msg:
        resp.message("We will be sad to see you go. BETTER MESSAGE HERE")

        User.query.filter(User.number==num).delete()
        # User.delete(user)
        db.session.commit()

        return resp.message()

    # if invalid_user(num):
    #     resp.message("Your number is not in our records. Please contact ASISA if you believe this to be an error")
    #     return str(resp)

    if "view" in session:
        print("Redirect to: " + session['view'])
        resp.redirect(url_for(session["view"]))
    else:

        if ('hi' in incoming_msg) or ('hello' in incoming_msg) or ('menu' in incoming_msg) or ('ok' in incoming_msg):
            resp.message(Dictionary['welcome1'])


            if not registered(num):
                out = Dictionary['welcome2'] + "\n\n" + Dictionary['welcome3']
                session['view'] = 'baseline'

            else:
                resp.message("You have completed your registration.")
                out = "You are able to take part in the monthly surveys. You can start now by replying to this message \
with *Y*. You can also restart this chat at any time to do the survey."



        elif ('are you still working' in incoming_msg):
            out = "Yes, all is well"

        elif 'y' in incoming_msg:
            out = survey_questions['question1']
            session['view'] = 'survey'
            session.modified = True

        elif "thank" in incoming_msg:
            out = "You're welcome :)"

        elif "stop" in incoming_msg:
            out = "We are sad to see you go? Please advise what this message should be"

            User.query.filter(User.num == num).delete()
            db.session.commit()

        else:
            out = f"I'm sorry, but there's been a problem. \
Please say \"Hi\" to try again."

        resp.message(out)
        # try resp.message or other format where there's no msg.body
    if session:
        print('*' * 20)
        for i in session.keys():
            print(i + ": " + str(session.get(i)))

    return str(resp)


# checks to see if user is in DB and, if not, adds them
def user_error(num):
    if Responses.query.filter(Responses.number == num).first() is not None:
        return True

    return False

def registered(num):
    user = User.query.filter(User.number == num).first()
    if user is not None:
        if user.registered == 1:
            return True
    else:
        db.save(User(number=num))

    return False

def invalid_user(num):
    demos = pd.read_csv("../demographics/ww_test_csv.csv")
