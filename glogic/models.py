from datetime import datetime

from . import db


class User(db.Model):
    __tablename__ = "Data_from_Recruitment_Bot"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)
    response = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, number, response):
        self.number = number
        self.response = response

class Alerts(db.Model):
    __tablename__ = "Alerts"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(60), nullable=False, default="")
    AA = db.Column(db.Boolean, default=False)
    ABE = db.Column(db.Boolean, default=False)
    BSGS = db.Column(db.Boolean, default=False)
    C0DE = db.Column(db.Boolean, default=False)
    CE = db.Column(db.Boolean, default=False)
    FSS = db.Column(db.Boolean, default=False)
    HEL = db.Column(db.Boolean, default=False)
    HD = db.Column(db.Boolean, default=False)
    IPPP = db.Column(db.Boolean, default=False)
    ME = db.Column(db.Boolean, default=False)
    SVI = db.Column(db.Boolean, default=False)

    def __init__(self, number):
        self.number = number

