from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# from flask_react import React

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f6af74d4b2a3ed79b2f6e99f38fdc6d5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from schedulebuddy import routes
