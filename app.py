
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from functools import wraps
from twilio.request_validator import RequestValidator
from twilio.twiml.messaging_response import MessagingResponse
from gresponses import Dictionary
import  WebScrape

import datetime
import os

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
@app.route("/")
def hello():
    return "Hello world!"

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




if __name__ == '__main__':
    app.run(debug=True)
