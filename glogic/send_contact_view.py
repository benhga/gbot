from . import app, db, bot_view
from flask import url_for, request, session
from .gresponses import Dictionary
from twilio.twiml.messaging_response import MessagingResponse

import  requests
import vobject

from .models import Vcard


@app.route('/send_contact', methods=['GET', 'POST'])
def send_contact():
    """
    Redirect for the careers view. Holds careers logic.
    :return str: response
    """
    session['View'] = 'send_contact'

    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    msg = response.message()

    if 'send' in incoming_msg:
        out = Dictionary['send']

    elif ('hi' in incoming_msg) or ('menu' in incoming_msg):
        out = return_to_menu()

    elif request.form.get('MediaContentType0') == 'text/vcard':
        print(request.form)
        url = request.form.get('MediaUrl0')
        r = requests.get(url, allow_redirects=True)
        open('vcards/contacts.vcf', 'wb').write(r.content)
        print(parse_vcard('vcards/contacts.vcf'))
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

def parse_vcard(path):
    with open(path, 'r') as f:
        vcard = vobject.readOne(f.read())
        db.save(Vcard(name=vcard.contents['fn'][0].value,
                      number=str([tel.value for tel in vcard.contents])))
        return {vcard.contents['fn'][0].value: [tel.value for tel in vcard.contents['tel']] }