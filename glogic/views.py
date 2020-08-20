from . import app
from . import bot_view, careers_view
from .careers_options import careers_current_opportunities, work_at_g, receive_alerts


@app.route('/', methods=['GET', 'POST'])
def root():
    return "I'm working"
