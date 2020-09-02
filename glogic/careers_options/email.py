from glogic import app, db, bot_view
from flask import url_for, request, session

from glogic.careers_view import return_to_menu
from glogic.gresponses import Dictionary, careers_dict, work_at_g_dict
from twilio.twiml.messaging_response import MessagingResponse

from .careers_current_opportunities import return_to_careers
from ..models import Alerts


@app.route('/email', methods=['GET', 'POST'])
def email():
    """
    Redirect for the email view view.
    :return str: response
    """
    session['View'] = 'email'

    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    msg = response.message()

    num = request.form.get('From')
    num = num.replace('whatsapp:', '')

    user = Alerts.query.filter(Alerts.number == num).first()





    if 'careers' in incoming_msg:
        out = return_to_careers()

    elif ('hi' in incoming_msg) or ('menu' in incoming_msg):
        out = return_to_menu()

    elif '@' not in incoming_msg:
        msg.body("Please enter a valid email address")
        return str(response)

    else:
        user.email = incoming_msg
        db.session.commit()
        out = "Thank you for your email address. You can opt out of alert notifications from the emails we send."

    msg.body(out + "\n\nIf you would like to return to the careers menu, type *careers*.\n\nIf you would like to " +
             "return the main menu, just say *Hi* or type *Menu*.")
    return str(response)
