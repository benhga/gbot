import os
import urllib

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

from . import app, db
from .gresponses import Dictionary, survey_questions
from .models import Responses, User
from flask import request, session, url_for
from twilio.twiml.messaging_response import MessagingResponse
import pandas as pd

from .validation_test import get_data


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
        resp.message("We will be sad to see you go.")

        User.query.filter(User.number==num).delete()
        # User.delete(user)
        db.session.commit()

        return str(resp)

    # if invalid_user(num):
    #     resp.message("Your number is not in our records. Please contact ASISA if you believe this to be an error")
    #     return str(resp)

    if "view" in session:
        print("Redirect to: " + session['view'])
        resp.redirect(url_for(session["view"]))
    else:

        if ('hi' in incoming_msg) or ('hello' in incoming_msg) or ('menu' in incoming_msg) or ('ok' in incoming_msg):
            resp.message(Dictionary['welcome1'])

            reg = registered(num)
            if reg == 0:
                out = Dictionary['welcome2'] + "\n\n" + Dictionary['welcome3']
                session['view'] = 'baseline'
            elif reg == -1:
                out = "Your phone number is not in our database. If you have participated in the WageWise program and beleive this to be an error, please contact digital@genesis-analytics.com."
            else:
                resp.message("You have completed your registration.")
                out = "You will be notified when a new monthly survey is available."



        elif ('are you still working' in incoming_msg):
            out = "Yes, all is well"

        # elif 'y' in incoming_msg:
        #     out = survey_questions['question1']
        #     session['view'] = 'survey'
        #     session.modified = True

        elif "thank" in incoming_msg:
            out = "You're welcome :)"

        elif "stop" in incoming_msg:
            out = "We are sad to see you go? Please advise what this message should be"

            User.query.filter(User.number == num).delete()
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
    # user = db.session.execute(f"SELECT * from users where users.number = {num}")[0]
    # print(user)

    # return 0
    if user is not None:
        if user.registered == 1:
            return 1
        else:
            return 0
    else:
        allowed, num2 = get_data(num)
        # print(allowed, num2)
        if allowed:
            db.save(User(number=num, number_2=num2))
            return 0


    return -1

def invalid_user(num):
    demos = pd.read_csv("../demographics/ww_test_csv.csv")
