# import Flask class
from flask import Flask, render_template
# set app variable to an instance of Flask class
# __name__ is a special name in Python, which is the name of module
app = Flask(__name__)

app.config['SECRET_KEY'] = ''

@app.route('/') # homepage
def home():
    return 'Welcome to Schedule Fighter <3!!!'

@app.route('/about') # homepage
def about():
    return 'We are here to help optimized your schedule and get you out the door as quickly as possible.'

if __name__ == '__main__':
    app.run(debug=True)
