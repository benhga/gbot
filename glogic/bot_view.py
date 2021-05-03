from . import app, db
from .gresponses import Dictionary
from .models import Responses
from flask import request
from twilio.twiml.messaging_response import MessagingResponse


@app.route('/message', methods=['GET', 'POST'])
def bot():

    num = request.form.get('From')
    num = num.replace('whatsapp:', '')
    incoming_msg = request.form.get('Body').lower()

    resp = MessagingResponse()
    msg = resp.message()

    if ('hi' in incoming_msg) or ('hello' in incoming_msg) or ('menu' in incoming_msg):
        send_question(resp)
        out = Dictionary['welcome']

    
    elif ('are you still working' in incoming_msg):
        out = "Yes, all is well"
        
    elif 'yes' in incoming_msg:
        out = Dictionary['yes']
        db.save(Responses(number=num,
                          response="Denied entry"))

    elif ('no' in incoming_msg) or (incoming_msg == 'healthcare'):
        out = Dictionary['no']
        db.save(Responses(number=num,
                          response="Allowed entry"))

    else:
        out = "I'm sorry, I'm still young and don't understand your request. \
Please use the words in bold to talk to me."
        send_question(resp)

    msg.body(out)
    return str(resp)

def send_question(resp):
    resp.message(Dictionary['question'])
    return str(resp)