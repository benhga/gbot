from . import app, db
from .gresponses import Dictionary, survey_questions
from .models import Responses
from flask import request, session, url_for
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime


@app.route('/message', methods=['GET', 'POST'])
def bot():
    # session.pop('view')
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

    # if user_error(num):
    #     mydate = datetime.now()
    #     mon = mydate.strftime("%B")
    #     resp.message(f"Our records indicate that you have already completed the survey for {mon}. We look forward to hearing from you next month.")
    #     return str(resp)

    if "view" in session:
        print("Redirect to: " + session['view'])
        resp.redirect(url_for(session["view"]))
    else:

        if ('hi' in incoming_msg) or ('hello' in incoming_msg) or ('menu' in incoming_msg):
            # session['view'] = 'survey'
            out = Dictionary['welcome']

        elif ('are you still working' in incoming_msg):
            out = "Yes, all is well"

        elif 'y' in incoming_msg:
            out = survey_questions['question1']
            session['view'] = 'survey'
            session.modified = True

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
