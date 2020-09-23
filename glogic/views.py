from . import app
from . import bot_view, careers_view
from .careers_options import careers_current_opportunities, receive_alerts, email, faq


@app.route('/', methods=['GET', 'POST'])
def root():
    return "I'm working"
