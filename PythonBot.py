
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import requests
from twilio.request_validator import RequestValidator
from twilio.twiml.messaging_response import MessagingResponse
from bs4 import BeautifulSoup as bs
import numpy as np
from random import choice
from gresponses import Dictionary
import io
import datetime
import os

# import mysql.connector

app = Flask(__name__)
app.config["DEBUG"]  = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="korstiaan",
    password="MI5Ql0G:",
    hostname="korstiaan.mysql.pythonanywhere-services.com",
    databasename="korstiaan$gbotdata",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class BotData(db.Model):

    __tablename__ = "gdata"

    id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.String(4096))
    user_input = db.Column(db.String(4096))
    date = db.Column(db.String(4096))

# validates Twilio requests
def validate_twilio_request(f):
    """Validates that incoming requests genuinely originated from Twilio"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Create an instance of the RequestValidator class
        validator = RequestValidator(os.environ.get('TWILIO_AUTH_TOKEN'))

        # Validate the request using its URL, POST data,
        # and X-TWILIO-SIGNATURE header
        request_valid = validator.validate(
            request.url,
            request.form,
            request.headers.get('X-TWILIO-SIGNATURE', ''))

        # Continue processing the request if it's valid, return a 403 error if
        # it's not
        if request_valid:
            return f(*args, **kwargs)
        else:
            return abort(403)
    return decorated_function

# initialises some variables
out_dict = {}
out = ''

# tester to see response
# @app.route("/")
# def hello():
#     return "Hello world!"

# actual bot logic
@app.route('/bot', methods=['GET', 'POST'])
def bot():
    # writes data to a csv (will be modified to interact with MySQL)

    incoming_msg = request.form.get('Body').lower()
    num = request.form.get('From')
    num = num.replace('whatsapp:', '')
    dt=datetime.datetime.now().strftime("%y%m%d--%H%M%S")
    data = num + ',' + incoming_msg + ',' + dt + '\n'





    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if ('hi' in incoming_msg) or ('hello' in incoming_msg):
        msg.body(Dictionary['hello'])
        responded = True

    if 'covid' in incoming_msg:
        msg.body(Dictionary['covid'])
        responded = True

    if ('1' in incoming_msg) or (incoming_msg == 'isafricaflatteningthecurve'):
        msg.body(Dictionary['isafricaflatteningthecurve'])
        responded = True

    if ('2' in incoming_msg) or (incoming_msg == 'healthcareriskcalculator'):
        msg.body(Dictionary['healthcareriskcalculator'])
        responded = True

    if ('3' in incoming_msg) or ('covidnews' in incoming_msg):
        covnews = news_scrape('https://www.genesis-analytics.com/covid19', 3)
        out = Dictionary['covidnews']
        for x, y in covnews.items():
            headline = "*" + x + "*\n"
            ref = "Read more at: " + y + "\n\n"
            out = out + "\U0001F6A9" + headline + ref

        out += '\n\n'
        msg.body(out)
        responded = True

    if 'news' in incoming_msg:

        news = news_scrape("https://www.genesis-analytics.com/news", 3)
        out = Dictionary['news']
        emoji = ["\U0001F6A9"]
        for x, y in news.items():
            headline = "*" + x + "*\n"
            ref = "Read more at: " + y + "\n\n"
            out = out + choice(emoji) + headline + ref

        out += '\n\n'
        msg.body(out)
        responded = True

    if 'about' in incoming_msg:
        msg.body(Dictionary['about'])

        responded = True

    if 'value' in incoming_msg:

        url = "https://www.genesis-analytics.com/value-unlocked-intro"
        r1 = requests.get(url)
        cont = r1.content
        soup = bs(cont, "lxml")
        articles = soup.find_all(class_='panel-title')

        out = Dictionary["value1"] + str(articles[0].get_text()) + "* and *" \
            + str(articles[1].get_text()) + Dictionary['value2']

        msg.body(out)
        responded = True

    if 'contact' in incoming_msg:
        msg.body(Dictionary['contact'])
        responded = True

    if 'bdu' in incoming_msg:
        msg.body(Dictionary['bdu'])
        responded = True

    if 'careers' in incoming_msg:
        msg.body(Dictionary['careers'])
        responded = True

    if 'offices' in incoming_msg:
        msg.body(Dictionary["offices"])
        responded = True

    if 'corporate' in incoming_msg:
        msg.body(Dictionary['corporate'])
        responded = True

    if responded:
        nl = '\n\n'
#             msg.body(nl +
# "You can navigate back to the main menu at any time by saying *Hi*. \
# You can also visit our website at www.genesis-analytics.com")
    else:
        msg.body("I'm sorry, I'm still young and don't understand your request. \
Please use the words in bold to talk to me.")

    return str(resp)



# for scraping headlines and links from websites
def news_scrape(url, n):
    number_of_articles = n  # how many we want scraped

    # creates empty lists
    articles = []
    links = []
    titles = []
    out_dict = {}

    # connects to page and saves articles in a soup
    r1 = requests.get(url)
    cont = r1.content
    soup = bs(cont, "lxml")
    articles = soup.find_all(class_='panel panel-default')

    # loops through top articles, adds title and link to dictionary
    for n in np.arange(0, number_of_articles):

        # getting titles
        title = articles[n].find('h1').get_text()
        titles.append(title)

        # getting links
        link = articles[n].find('a')['href']
        links.append(link)

        out_dict[titles[n]] = links[n]

    return out_dict


if __name__ == '__main__':
    app.run(debug=True)
