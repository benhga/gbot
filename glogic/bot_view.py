from . import app, db, WebScrape
from .gresponses import Dictionary
from .models import User
from flask import request
from twilio.twiml.messaging_response import MessagingResponse


@app.route('/message', methods=['GET', 'POST'])
def bot():

    num = request.form.get('From')
    num = num.replace('whatsapp:', '')
    incoming_msg = request.form.get('Body').lower()
    db.save(User(number=num,
                 response=incoming_msg))

    resp = MessagingResponse()
    msg = resp.message()

    if ('hi' in incoming_msg) or ('hello' in incoming_msg) or ('menu' in incoming_msg):
        out = Dictionary['hello']

    elif ('1' in incoming_msg) or (incoming_msg == 'africa'):
        out = Dictionary['isafricaflatteningthecurve']

    elif ('2' in incoming_msg) or (incoming_msg == 'healthcare'):
        out = Dictionary['healthcareriskcalculator']

    elif ('3' in incoming_msg) or ('info' in incoming_msg):
        out = WebScrape.covnews

    elif 'newsletter' in incoming_msg:
        out = WebScrape.bulletins

    elif 'news' in incoming_msg:
        out = Dictionary['news']

    elif 'headline' in incoming_msg:
        out = WebScrape.headlines

    elif 'report' in incoming_msg:
        out = WebScrape.reports

    elif 'about' in incoming_msg:
        out = Dictionary['about']

    elif 'values' in incoming_msg:
        out = Dictionary['core']

    elif 'value' in incoming_msg:
        out = WebScrape.value

    elif 'covid' in incoming_msg:
        out = Dictionary['covid']

    elif 'contact' in incoming_msg:
        out = Dictionary['contact']

    elif 'bdu' in incoming_msg:
        out = Dictionary['bdu']

    elif 'careers' in incoming_msg:
        out = Dictionary['careers']

    elif 'offices' in incoming_msg:
        out = Dictionary["offices"]

    elif 'corporate' in incoming_msg:
        out = Dictionary['corporate']

    elif 'za' in incoming_msg:
        out = Dictionary['za']

    elif 'ke' in incoming_msg:
        out = Dictionary['ke']

    elif 'uk' in incoming_msg:
        out = Dictionary['uk']

    elif 'ca' in incoming_msg:
        out = Dictionary['za']

    elif 'ae' in incoming_msg:
        out = Dictionary['za']

    elif 'in' in incoming_msg:
        out = Dictionary['in']

    elif 'ng' in incoming_msg:
        out = Dictionary['ng']

    else:
        out = "I'm sorry, I'm still young and don't understand your request. \
    Please use the words in bold to talk to me."

    msg.body(out + "\n\nIf you would like to return the menu, just say *Hi* or type *Menu*.")
    return str(resp)
