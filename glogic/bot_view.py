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

from .sql_stuff import del_from_db
from .validation_test import get_data


@app.route('/message', methods=['GET', 'POST'])
def bot():

    # del session['view']
    # del session['question_id']
    # del session['count']


    num = request.form.get('From')
    num = num.replace('whatsapp:', '')
    incoming_msg = request.form.get('Body').lower()

    print("INCOMING MSG: " + incoming_msg)

    resp = MessagingResponse()
    # msg = resp.message()



    # if registered(num) == 0:
    #     resp.message("Your number is not in our records. Please contact digital@genesis-analytics.com if you believe this to be an error")
    #     return str(resp)

    if "view" in session:
        print("Redirect to: " + session['view'])
        resp.redirect(url_for(session["view"]))
    else:
        # resp.message("The registration period has ended. If you have registered, you will be notified when a new monthly survey is available.")
        if ('hi' in incoming_msg) or ('hello' in incoming_msg) or ('menu' in incoming_msg) or ('ok' in incoming_msg):
            # resp.message(Dictionary['welcome1'])
#             if num == "+27822205729":
#             out = "The registration period has ended. If you have registered, you will be notified when a new monthly survey is available."

            reg = registered(num)
            if reg == 1:
                session['view'] = 'survey'
                session['count'] = 0
                out = "Thank you for participating in the WageWise 3 year survey. " + Dictionary['welcome3']



                # out = Dictionary['welcome2'] + "\n\n" + Dictionary['welcome3']
                # session['view'] = 'baseline'
            # elif reg == -1:
            #     out = "Your phone number is not in our database. If you have participated in the WageWise program and completed the registration, please contact digital@genesis-analytics.com."
            else:
                out = "Your phone number is not in our database. If you have participated in the WageWise program and completed the registration, please contact digital@genesis-analytics.com."

                # resp.message("You have completed your registration.")
                # out = "You will be notified when a new monthly survey is available."



        elif ('are you still working' in incoming_msg):
            out = "Yes, all is well"


        # if True:
        #     out = "Hi, the bot is currently inactive. If you were part of the WageWise program, you will be notified when new surveys are ready."

        # elif "thank" in incoming_msg:
        #     out = "You're welcome :)"

        else:
            out = f"I'm sorry, but there's been a problem. \
Please say \"Hi\" to try again."

        resp.message(out)
        # try resp.message or other format where there's no msg.body
    # if session:
    #     print('*' * 20)
    #     for i in session.keys():
    #         print(i + ": " + str(session.get(i)))

    return str(resp)


# checks to see if user is in DB and, if not, adds them
def user_error(num):
    if Responses.query.filter(Responses.number == num).first() is not None:
        return True

    return False

def registered(num):
    """
    Returns -1 if user not in demos, 0 if user is not registered, 1 if registered
    """
    user = User.query.filter(User.number == num).first()

    # allowed, _ = get_data(num)
    # print("Allowed: ", allowed)
    # if allowed:
    # if True:
    if user is not None:
        if user.registered == 1:
            return 1
        else:
            return 0
    else:
        # allowed, num2 = get_data(num)
        # # print(allowed, num2)
        # if allowed:
        #     db.save(User(number=num, number_2=num2))
        return 0


    return -1

def invalid_user(num):
    demos = pd.read_csv("../demographics/ww_test_csv.csv")
