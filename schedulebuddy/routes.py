from flask import render_template, request, make_response, jsonify
from schedulebuddy import app
from schedulebuddy.forms import RegistrationForm, LoginForm
from schedulebuddy.models import Course

from schedulebuddy.database import TestFun

@app.route('/')
def hello_world():
    TestFun()
    return 'Welcome to Schedule Fighter <3!!!'

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    # return render_template('login.html', title='Login', form=form)
    return render_template('student.html', title='Login', form=form)

@app.route('/get_quarters/', methods=['POST'])
def quarters():
    if request.method == 'POST':
        print("incoming..")
        message = request.get_json()
        course = message['course']
        print(course)

        quarters = getQuarters(course)

        res = make_response(jsonify({"quarters": quarters}), 200)
        return res
