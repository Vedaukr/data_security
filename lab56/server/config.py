import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_JWT_KEY = "\xf9'\xe4p(\xa9\x12\x1a!\x94\x8d\x1c\x99l\xc7\xb7e\xc7c\x86\x02MJ\xa0"
DB_SALT = "sS7DQh9-x6V(2Cw@0njAy2uM-Vjy0S#q"

class Config(object):
    def __init__(self, name):
        self.SQLALCHEMY_DATABASE_URI =  'sqlite:///' + os.path.join(basedir, name)
        self.SQLALCHEMY_TRACK_MODIFICATIONS = True
        self.SECRET_JWT_KEY = SECRET_JWT_KEY
        self.DB_SALT = DB_SALT

app = Flask(__name__)
app.config.from_object(Config("app.db"))
db = SQLAlchemy(app)
migrate = Migrate(app, db)