from glogic import app, db, bot_view
from flask import url_for, request, session

from glogic.careers_view import return_to_menu
from glogic.gresponses import careers_dict
from twilio.twiml.messaging_response import MessagingResponse

from ..models import Alerts
from .careers_current_opportunities import return_to_careers


@app.route('/alerts', methods=['GET', 'POST'])
def alerts():
    """
    Redirect for the current opportunities view.
    :return str: response
    """
    session['View'] = 'alerts'

    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    msg = response.message()

    num = request.form.get('From')
    num = num.replace('whatsapp:', '')
    if not user_in_db(num):
        db.save(Alerts(number=num))

    user = Alerts.query.filter(Alerts.number == num).first()
    out = 'Your message: {}\n\n'.format(incoming_msg)
    counter = 0

    if '10' in incoming_msg:
        user.ME = 1
        counter += 1
        incoming_msg = incoming_msg.replace('10', " ")

    if '11' in incoming_msg:
        user.SVI = 1
        counter += 1
        incoming_msg = incoming_msg.replace('11', " ")

    if '1' in incoming_msg:
        user.AA = 1
        counter += 1

    if '2' in incoming_msg:
        user.ABE = 1
        counter += 1

    if '3' in incoming_msg:
        user.BSGS = 1
        counter += 1

    if '4' in incoming_msg:
        user.C0DE = 1
        counter += 1

    if '5' in incoming_msg:
        user.CE = 1
        counter += 1

    if '6' in incoming_msg:
        user.FSS = 1
        counter += 1

    if '7' in incoming_msg:
        user.HEL = 1
        counter += 1

    if '8' in incoming_msg:
        user.HD = 1
        counter += 1

    if '9' in incoming_msg:
        user.IPPP = 1
        counter += 1

    if counter > 0:
        out += 'Thank you for signing up. If you would like to add more practice areas, type *alerts*.'
        db.session.commit()

    elif 'careers' in incoming_msg:
        out = return_to_careers()

    elif ('hi' in incoming_msg) or ('menu' in incoming_msg):
        out = return_to_menu()

    elif 'alerts' in incoming_msg:
        out = careers_dict['alerts']
    else:
        out = "I'm sorry, I'm still young and don't understand your request. \
            Please use the words in bold or the numbered options to talk to me."

    msg.body(out + "\n\nIf you would like to return to the careers menu, type *careers*.\n\nIf you would like to " +
             "return the main menu, just say *Hi* or type *Menu*.")
    return str(response)


def user_in_db(num):
    if Alerts.query.filter(Alerts.number == num).first() is not None:
        return True
