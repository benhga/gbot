from flask import session
from .gresponses import survey_questions
from . import db
from .models import Responses

# fucntion for keeping track of survey space, quite hardcoded
def do_survey(incoming_msg, num):
    done = False

    if format_ans(incoming_msg)[1]:
        if 'q1' not in session:
            session['q1'] = format_ans(incoming_msg)[0]

            out = survey_questions['question2']
        elif 'q2' not in session:
            session['q2'] = format_ans(incoming_msg)[0]
            out = survey_questions['question3']
        else:
            session['q3'] = format_ans(incoming_msg)[0]
            db.save(Responses(number=num, question_1=session['q1'], question_2=session['q2'], question_3=session['q3']))
            print('-'*20)
            print("TO DB: "+ str(session['q1']) + " " + str(session['q2']) + " "+ str(session['q3']))

            # airtime = send_airtime_after_survey(num)
            airtime = 0
            if airtime > 0:
                out = "Thank you for your cooperation. We look forward to hearing from you again next month. If " \
                      "you have not received your airtime, please contact XXXXXXXXXX for assistance "
            else:
                out = "Unfortunately there has been an error getting you your airtime. Please contact XXXXXXXXXX to follow up."
            done = True

    else:
        out, _ = format_ans(incoming_msg)  # "not sure what you're saying"

    session.modified = True
    return out, done


def format_ans(incoming_msg):
    if '1' in incoming_msg:
        return 1, True
    elif '2' in incoming_msg:
        return 2, True
    elif '3' in incoming_msg:
        return 3, True
    elif '4' in incoming_msg:
        return 4, True
    elif '5' in incoming_msg:
        return 5, True
    elif '6' in incoming_msg:
        return 6, True
    elif '7' in incoming_msg:
        return 7, True
    elif '8' in incoming_msg:
        return 8, True
    elif '9' in incoming_msg:
        return 9, True
    else:
        return 'Not sure what you\'re saying, please type number', False