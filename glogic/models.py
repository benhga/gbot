from datetime import datetime

from . import db


class User(db.Model):
    __tablename__ = "Data_for_G:Bot"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False, unique=True)
    response = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, number, response):
        self.number = number
        self.response = response

# class Vcard(db.Model):
#     __tablename__ = 'vCards'
#
#     id = db.Column(db.Integer, primary_key=True)

