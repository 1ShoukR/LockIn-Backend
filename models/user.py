from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name  = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    username = db.Column(db.String(80), unique=True)