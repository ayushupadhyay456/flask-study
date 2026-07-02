from app import db

from flask_login import UserMixin  #login using flask
from sqlalchemy.sql import func

class Note(db.model):
    id=db.Column(db.Integer,primaryKey=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))  #as the class will be referenced by user therefore lowercase u



class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primaryKey=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    notes=db.relationship('Note')















