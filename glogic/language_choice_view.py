from . import app, db, bot_view
from flask import url_for, request, session
from .gresponses import eng, zulu
from twilio.twiml.messaging_response import MessagingResponse

@app.route('/lang', methods=['GET', 'POST'])
def lang():
    """
    Redirect for language choice
    :return str: response
    """
    session['View']='lang'


    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    msg = response.message()

    if '1' in incoming_msg:
        session['Lang'] = 'eng'
        out = 'You have chosen English'

    elif '2' in incoming_msg:
        session['Lang'] = 'zulu'
        out = 'Ukhethe isiZulu'

    else:
        out = "I'm sorry, I'm still young and don't understand your request. \
            Please press *1* for English or *2* for isiZulu."

    out2 = bot_view.return_to_menu(session['Lang'])
    msg.body(out + '\n\n' + out2)

    return str(response)