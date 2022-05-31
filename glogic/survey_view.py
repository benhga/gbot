from urllib import response
from flask import request, session
from twilio.twiml.messaging_response import MessagingResponse

from . import app, db
from .gresponses import Dictionary, survey_questions
from .models import Responses
from .send_airtime import send_airtime_after_survey
from datetime import date, datetime
from .utils import return_to_menu


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    """
    Redirect for the careers view. Holds careers logic.
    :return str: response
    """
    num = request.form.get('From')
    num = num.replace('whatsapp:', '')
    incoming_msg = request.form.get('Body').lower()

    for i in session.keys():
        print(i)
    resp = MessagingResponse()
    msg = resp.message()
    
    if 'q3' in session:
        db.save(Responses(num, session['q1'], session['q2'], session['q3']))
        airtime = send_airtime_after_survey(num)
        if airtime > 0:
            out = "Thank you for your cooperation. We look forward to hearing from you again next month."
        else:
            out = "Unfortunately there has been an error getting you your airtime. Please contact XXXXXXXXXX to follow up."
    else:
        out = do_survey(num, incoming_msg)
    
    msg.body(out)
    return str(resp)

# fucntion for keeping track of survey space, quite hardcoded 
def do_survey(num, incoming_msg):
        
    if session['started']:
        if format_ans(incoming_msg)[1]:
            if 'q1' not in session:
                session['q1'], _ = format_ans(incoming_msg)
                out = survey_questions['question2']
            elif 'q2' not in session:
                session['q2'], _ = format_ans(incoming_msg)
                out = survey_questions['question3']
            else: 
                session['q3'], _ = format_ans(incoming_msg)
                db.save(Responses(number=num, question_1=session['q1'], question_2=session['q2'], question_3=session['q3']))
                del session['view']
                del session['q1']
                del session['q2']
                del session['q3']
                out = "Thank you for your cooperation DO AIRTIME"
        else:
            out, _ = format_ans(incoming_msg)
    else:
        out = Dictionary['question1']
        session['started'] = True
    
    return out
        
def format_ans(incoming_msg):
    if '1' in incoming_msg:
        return 1, True
    elif '2' in incoming_msg:
        return 2, True
    elif '3' in incoming_msg:
        return 3, True
    elif '4' in incoming_msg:
        return 4, True
    else:
        return 'Not sure what you\'re saying, please type number', False