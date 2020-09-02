from . import app, db, WebScrape, gresponses
from .models import User
from flask import request, session, url_for
from twilio.twiml.messaging_response import MessagingResponse


@app.route('/message', methods=['GET', 'POST'])
def bot():
    """
    Where the logic of the bot is filtered through. Saves response and checks if a redirect is necessary

    :return str: response
    """
    num = request.form.get('From')
    num = num.replace('whatsapp:', '')
    incoming_msg = request.form.get('Body').lower()
    db.save(User(number=num,
                 response=incoming_msg))

    response = MessagingResponse()
    # msg = response.message()
    out = ''

    # del session['Lang']  # for misconfigured endpoints
    # del session['View']

    # language check



    # checks to see what view it should be looking at
    if 'View' in session:
        response.redirect(url_for(session['View']))
    else:
        if 'Lang' not in session:
            session['View'] = 'lang'
            response.message(choose_language_text(incoming_msg))
            return str(response)
        else:
            out = run_through_main_options(incoming_msg, session['Lang'])
            response.message(out + "\n\nIf you would like to return the menu, just say *Hi* or type *Menu*.")
    return str(response)


def run_through_main_options(incoming_msg, lang):
    """
    Main menu view

    :param incoming_msg: str
    :return out: str
    """
    if lang is 'eng':
        dict = gresponses.eng
    if lang is 'zulu':
        dict = gresponses.zulu


    if ('hi' in incoming_msg) or ('hello' in incoming_msg) or ('menu' in incoming_msg):
        out = dict['hello']

    elif ('1' in incoming_msg) or (incoming_msg == 'africa'):
        out = dict['isafricaflatteningthecurve']

    elif ('2' in incoming_msg) or (incoming_msg == 'healthcare'):
        out = dict['healthcareriskcalculator']

    elif ('3' in incoming_msg) or ('info' in incoming_msg):
        out = WebScrape.covnews

    elif 'newsletter' in incoming_msg:
        out = WebScrape.bulletins

    elif 'news' in incoming_msg:
        out = dict['news']

    elif 'headline' in incoming_msg:
        out = WebScrape.headlines

    elif 'report' in incoming_msg:
        out = WebScrape.reports

    elif 'about' in incoming_msg:
        out = dict['about']

    elif 'values' in incoming_msg:
        out = dict['core']

    elif 'value' in incoming_msg:
        out = WebScrape.value

    elif 'covid' in incoming_msg:
        out = dict['covid']

    elif 'contact' in incoming_msg:
        out = dict['contact']

    elif 'bdu' in incoming_msg:
        out = dict['bdu']

    elif 'careers' in incoming_msg:
        out = dict['careers']
        session['View'] = 'careers'

    elif 'offices' in incoming_msg:
        out = dict["offices"]

    elif 'corporate' in incoming_msg:
        out = dict['corporate']

    elif 'za' in incoming_msg:
        out = dict['za']

    elif 'ke' in incoming_msg:
        out = dict['ke']

    elif 'uk' in incoming_msg:
        out = dict['uk']

    elif 'ca' in incoming_msg:
        out = dict['ca']

    elif 'ae' in incoming_msg:
        out = dict['ae']

    elif 'in' in incoming_msg:
        out = dict['in']

    elif 'ng' in incoming_msg:
        out = dict['ng']

    else:
        out = "I'm sorry, I'm still young and don't understand your request. \
    Please use the words in bold to talk to me."

    return out

def choose_language_text(incoming_msg):
    out = "Welcome to the G:Bot! Press the number of the language you would like:\n\n\
          1. English\n\
          2. IsiZulu"

    return out

def return_to_menu(lang):
    """
    Main function is to remove 'View' from session.
    Should probably be put in views/bot_view and imported to each other view.
    :return str: out
    """
    lang  = session['Lang']
    if lang is 'eng':
        dict = gresponses.eng
    if lang is 'zulu':
        dict = gresponses.zulu

    out = dict['hello']
    if 'View' in session:
        del session['View']
    return out