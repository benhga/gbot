from datetime import datetime

from . import db

class RegistrationQuestions(db.Model):
    __tablename__ = 'registration_questions'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    answers = db.relationship("RegistrationAnswers", backref='question', lazy='dynamic')

    def __init__(self, content):
        self.content = content

    def next(self):
        return self.query.filter(RegistrationQuestions.id > self.id) \
            .order_by('id').first()


class RegistrationAnswers(db.Model):
    __tablename__ = 'registration_answers'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('registration_questions.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))


    def __init__(self, content, question, user):
        self.content = content
        self.question = question
        self.user = user

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String, unique=True)
    registered = db.Column(db.Integer, default=0)

    registration = db.relationship("RegistrationAnswers", backref='user', lazy='dynamic')

    def __init__(self, number):
        self.number = number


class Responses(db.Model):
    __tablename__ = "responses"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    question_1 = db.Column(db.Integer, default=0)
    question_2 = db.Column(db.Integer, default=0)
    question_3 = db.Column(db.Integer, default=0)
    date_completed = db.Column(db.DateTime, nullable=True)

    def __init__(self, number, question_1=0, question_2=0, question_3=0):
        self.number = number
        self.month = int(datetime.now().month)
        self.question_1 = question_1
        self.question_2 = question_2
        self.question_3 = question_3
        self.date_completed = datetime.now()
        
