from . import app
from .import bot_view, survey_view, registration_view, baseline_view


@app.route('/', methods=['GET', 'POST'])
def root():
    return "I'm working"
