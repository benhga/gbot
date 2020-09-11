from . import app, db, bot_view
from flask import url_for, request, session
from .gresponses import Dictionary, careers_dict
from twilio.twiml.messaging_response import MessagingResponse


@app.route('/careers', methods=['GET', 'POST'])
def careers():
    """
    Redirect for the careers view. Holds careers logic.
    :return str: response
    """
    session['View'] = 'careers'

    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    msg = response.message()

    if 'careers' in incoming_msg:
        out = Dictionary['careers']

    elif ('hi' in incoming_msg) or ('menu' in incoming_msg):
        out = return_to_menu()

    elif '1' in incoming_msg:
        out = careers_dict['current_opportunities']
        session['View'] = 'current_opportunities'

    elif '2' in incoming_msg:
        out = careers_dict['work_at_g']

    elif '3' in incoming_msg:
        out = careers_dict['practice_areas']

    elif '4' in incoming_msg:
        out = Dictionary['core']

    elif '5' in incoming_msg:
        out = "Do FAQs"

    elif '6' in incoming_msg:
        out = careers_dict['alerts']
        session['View'] = 'alerts'

    elif 'apply' in incoming_msg:
        out = careers_dict['apply']
    else:
        out = "I'm sorry, I'm still young and don't understand your request. \
    Please use the words in bold to talk to me."

    msg.body(out + "\n\nIf you would like to return to the careers menu, type *careers*.\n\nIf you would like to " +
                   "return the main menu, just say *Hi* or type *Menu*.")
    return str(response)


def return_to_menu():
    """
    Main function is to remove 'View' from session.
    Should probably be put in views/bot_view and imported to each other view.

    :return str: out
    """
    out = Dictionary['hello']
    if 'View' in session:
        del session['View']
    return out
