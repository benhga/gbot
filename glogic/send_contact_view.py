from . import app, db, bot_view
from flask import url_for, request, session
from .gresponses import Dictionary
from twilio.twiml.messaging_response import MessagingResponse

import requests

from .models import Videos


@app.route('/send_video', methods=['GET', 'POST'])
def send_video():
    """
    Redirect for the careers view. Holds careers logic.
    :return str: response
    """
    session['View'] = 'send_video'

    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    msg = response.message()

    if 'send' in incoming_msg:
        out = Dictionary['send']

    elif ('hi' in incoming_msg) or ('menu' in incoming_msg):
        out = return_to_menu()

    elif request.form.get('MediaContentType0') == 'video/mp4':
        print(request.form)
        # url = request.form.get('MediaUrl0')
        # r = requests.get(url, allow_redirects=True)
        url = request.form.get(('MediaUrl0'))
        db.save(Videos(url=url))
        # open('videos/video.mp4', 'wb').write(request.form.get('MediaUrl0'))

        out = 'should be saved'


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
