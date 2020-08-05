from . import app, db, bot_view
from flask import url_for, request, session
from .gresponses import Dictionary, careers_dict
from twilio.twiml.messaging_response import MessagingResponse


@app.route('/careers', methods=['GET', 'POST'])
def careers():
    session['View'] = 'careers'

    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    msg = response.message()

    if 'careers' in incoming_msg:
        out = Dictionary['careers']

    elif ('hi' in incoming_msg) or ('menu' in incoming_msg):
        out = return_to_menu()

    elif incoming_msg in careers_dict.keys():
        out = careers_dict[incoming_msg]


    else:
        out = "I'm sorry, I'm still young and don't understand your request. \
    Please use the words in bold to talk to me."

    msg.body(out + "\n\nIf you would like to return to the careers menu, type *careers*.\n\nIf you would like to " +
                   "return the main menu, just say *Hi* or type *Menu*.")
    return str(response)


def return_to_menu():
    response = MessagingResponse()
    out = Dictionary['hello']
    if 'View' in session:
        del session['View']
    return out
