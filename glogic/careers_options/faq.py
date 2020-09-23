from glogic import app, db, bot_view
from flask import url_for, request, session

from glogic.careers_view import return_to_menu
from glogic.gresponses import Dictionary, careers_dict, faq_dict
from twilio.twiml.messaging_response import MessagingResponse


@app.route('/faq', methods=['GET', 'POST'])
def faq():
    """
    Redirect for the faq view.
    :return str: response
    """
    session['View'] = 'faq'

    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    msg = response.message()

    if 'careers' in incoming_msg:
        out = return_to_careers()

    elif ('hi' in incoming_msg) or ('menu' in incoming_msg):
        out = return_to_menu()

    elif 'back' in incoming_msg:
        out = careers_dict['FAQ']

    elif incoming_msg in faq_dict:
        out = faq_dict[incoming_msg]
    #     TODO: TEST THIS WITH WIFI

    else:
        out = "I'm sorry, I'm still young and don't understand your request. \
            Please use the words in bold to talk to me."

    msg.body(out + "\n\nYou can return to the FAQ menu by typing *back*. If you would like to return to the careers menu, type *careers*.\n\nIf you would like to " +
             "return the main menu, just say *Hi* or type *Menu*.")
    return str(response)


def return_to_careers():
    """
    Main function is to remove 'View' from session.
    Should probably be put in views/bot_view and imported to each other view.

    :return str: out
    """
    out = Dictionary['careers']
    session['View'] = 'careers'
    return out
