from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
# from flask_react import React

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f6af74d4b2a3ed79b2f6e99f38fdc6d5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# react = React(
#    app,
#    extensions=("material", "components"),
#    jsx_folder='static/react/jsx/'
# )

@app.route('/') # homepage
def hello_world():
    return 'Welcome to Schedule Fighter <3!!!' 

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)


