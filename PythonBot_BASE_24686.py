
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from functools import wraps
import requests
from twilio.request_validator import RequestValidator
from twilio.twiml.messaging_response import MessagingResponse
from bs4 import BeautifulSoup as bs
import numpy as np
from random import choice
from gresponses import Dictionary

import datetime
import os
# import mysql

# initialises app and creates a connection to the database
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

'''
if " Error: Could not locate Flask application. You did not provide the FLASK_APP environment variable."
go to console and type 'export FLASK_APP=PythonBot.py' in venv to recreate bash variable
'''
db = SQLAlchemy(app)
migrate = Migrate(app, db)

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

    num = request.form.get('From')
    num = num.replace('whatsapp:', '')
    incoming_msg = request.form.get('Body').lower()
    dt=datetime.datetime.now().strftime("%y%m%d--%H%M%S")
    data = BotData(number = num, user_input = incoming_msg, date = dt)

    db.session.add(data)
    db.session.commit()





    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if ('hi' in incoming_msg) or ('hello' in incoming_msg):
        msg.body(Dictionary['hello'])
        responded = True


    elif ('1' in incoming_msg) or (incoming_msg == 'africa'):
        msg.body(Dictionary['isafricaflatteningthecurve'])
        responded = True

    elif ('2' in incoming_msg) or (incoming_msg == 'healthcare'):
        msg.body(Dictionary['healthcareriskcalculator'])
        responded = True

    elif ('3' in incoming_msg) or ('info' in incoming_msg):
        covnews = news_scrape('https://www.genesis-analytics.com/covid19', 3, None)
        out = Dictionary['covidnews']
        for x, y in covnews.items():
            headline = "*" + x + "*\n"
            ref = "Read more at: " + y + "\n\n"
            out = out + "\U0001F6A9" + headline + ref

        out += '\n\n'
        msg.body(out)
        responded = True

    elif 'news' in incoming_msg:
        msg.body(Dictionary['news'])
        responded = True

    elif 'headline' in incoming_msg:
        msg.body(news_out('headlines', 'https://www.genesis-analytics.com/news', 3, 'tab1'))
        responded = True

    elif 'bulletin' in incoming_msg:
        msg.body(news_out('bulletins', 'https://www.genesis-analytics.com/news', 3, 'tab2'))
        responded = True

    elif 'report' in incoming_msg:
        msg.body(news_out('reports', 'https://www.genesis-analytics.com/news', 3,'tab3'))
        responded = True

    elif 'about' in incoming_msg:
        msg.body(Dictionary['about'])

        responded = True

    elif 'value' in incoming_msg:

        url = "https://www.genesis-analytics.com/value-unlocked-intro"
        r1 = requests.get(url)
        cont = r1.content
        soup = bs(cont, "lxml")
        articles = soup.find_all(class_='panel-title')

        out = Dictionary["value1"] + str(articles[0].get_text()) + "* and *" \
            + str(articles[1].get_text()) + Dictionary['value2']

        msg.body(out)
        responded = True

    elif 'covid' in incoming_msg:
        msg.body(Dictionary['covid'])
        responded = True

    elif 'contact' in incoming_msg:
        msg.body(Dictionary['contact'])
        responded = True

    elif 'bdu' in incoming_msg:
        msg.body(Dictionary['bdu'])
        responded = True

    elif 'careers' in incoming_msg:
        msg.body(Dictionary['careers'])
        responded = True

    elif 'offices' in incoming_msg:
        msg.body(Dictionary["offices"])
        responded = True

    elif 'corporate' in incoming_msg:
        msg.body(Dictionary['corporate'])
        responded = True

    elif 'za' in incoming_msg:
        msg.body(Dictionary['za'])
        responded = True

    elif 'ke' in incoming_msg:
        msg.body(Dictionary['ke'])
        responded = True

    elif 'uk' in incoming_msg:
        msg.body(Dictionary['uk'])
        responded = True

    elif 'ca' in incoming_msg:
        msg.body(Dictionary['za'])
        responded = True

    elif 'ae' in incoming_msg:
        msg.body(Dictionary['za'])
        responded = True

    elif 'in' in incoming_msg:
        msg.body(Dictionary['in'])
        responded = True

    elif 'ng' in incoming_msg:
        msg.body(Dictionary['ng'])
        responded = True



    else:
        msg.body("I'm sorry, I'm still young and don't understand your request. \
Please use the words in bold to talk to me.")

    return str(resp)



# for scraping headlines and links from websites
def news_scrape(url, n, tab_no):
    number_of_articles = n  # how many we want scraped
    tab = tab_no
    # creates empty lists
    articles = []
    links = []
    titles = []
    out_dict = {}

    # connects to page and saves articles in a soup
    r1 = requests.get(url)
    cont = r1.content
    soup = bs(cont, "lxml")
    articles = soup.find(class_='tab_content', id=tab)
    if articles is not None:
        articles = articles.find_all(class_='panel panel-default')
    else:
        articles = soup.find_all(class_='panel panel-default')

    # # loops through top articles, adds title and link to dictionary
    for n in np.arange(0, number_of_articles):

        # getting titles
        title = articles[n].find('h1').get_text()
        titles.append(title)

        # getting links
        link = articles[n].find('a')['href']
        links.append(link)

        out_dict[titles[n]] = links[n]
    return out_dict

def news_out(msg, url, n, tab):
    out = Dictionary[msg]
    news = news_scrape(url, n, tab)
    emoji = ["\U0001F6A9"]
    for x, y in news.items():
        headline = "*" + x + "*\n"
        ref = "Read more at: " + y + "\n\n"
        out = out + choice(emoji) + headline + ref

    return out

if __name__ == '__main__':
    app.run(debug=True)
