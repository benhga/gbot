from . import app


@app.route('/', methods=['GET', 'POST'])
def root():
    return "I'm working"
