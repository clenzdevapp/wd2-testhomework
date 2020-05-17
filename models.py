import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL",
                          "sqlite:///localhost.sqlite"))  # this connects to a database either on Heroku or on localhost


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, unique=True)  # email must be unique! Two users cannot have the same email address
    user_password = db.Column(db.String)
    session_token = db.Column(db.String)
