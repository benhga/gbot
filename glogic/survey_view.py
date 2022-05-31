from urllib import response
from flask import request, session
from twilio.twiml.messaging_response import MessagingResponse

from . import app, db
from .gresponses import Dictionary, survey_questions
from .models import Responses
from .send_airtime import send_airtime_after_survey
from datetime import date, datetime

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
    incoming_msg = request.form.get('Body').lower()

    resp = MessagingResponse()
    msg = resp.message()

    out, done = do_survey(incoming_msg)

    msg.body(out)

    if done:
        session.pop('view')
        session.pop('q1')
        session.pop('q2')
        session.pop('q3')

        if len(session) > 0:
            print("DELETION UNSUCCESSFUL")
        else:
            print("NO SESSION VARS")

    print('*' * 20)
    for i in session.keys():
        print(i + ": " + str(session.get(i)))

    return str(resp)
