from glogic import app, db, bot_view
from flask import url_for, request, session

from glogic.careers_view import return_to_menu
from glogic.gresponses import Dictionary, careers_dict, work_at_g_dict
from twilio.twiml.messaging_response import MessagingResponse

from .careers_current_opportunities import return_to_careers


@app.route('/work_at_g', methods=['GET', 'POST'])
def work_at_g():
    """
    Redirect for the current opportunities view.
    :return str: response
    """
    session['View'] = 'work_at_g'

    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    msg = response.message()

    if 'careers' in incoming_msg:
        out = return_to_careers()

    elif ('hi' in incoming_msg) or ('menu' in incoming_msg):
        out = return_to_menu()

    elif incoming_msg in work_at_g_dict:
        out = work_at_g_dict[incoming_msg]

    else:
        out = "I'm sorry, I'm still young and don't understand your request. \
            Please use the words in bold to talk to me."

    msg.body(out + "\n\nIf you would like to return to the careers menu, type *careers*.\n\nIf you would like to " +
             "return the main menu, just say *Hi* or type *Menu*.")
    return str(response)
