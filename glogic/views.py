from . import app
from .import bot_view, language_choice_view


@app.route('/', methods=['GET', 'POST'])
def root():
    return "I'm working"
