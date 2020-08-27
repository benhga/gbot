from . import app
from .import bot_view, send_contact_view


@app.route('/', methods=['GET', 'POST'])
def root():
    return "I'm working"
