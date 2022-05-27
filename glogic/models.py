from datetime import datetime

from . import db

            
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
        
