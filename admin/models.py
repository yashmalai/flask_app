from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(255))
    email = db.Column("email", db.String(255))

    def __init__(self, name, email):
        self.name = name
        self.email = email
