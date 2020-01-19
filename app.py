# import Flask class
from flask import Flask
from flask_react import React
# set app variable to an instance of Flask class
# __name__ is a special name in Python, which is the name of module
app = Flask(__name__)
react = React(
   app,
   extensions=("material", "components"),
   jsx_folder='static/react/jsx/'
)

@app.route('/') # homepage
def hello_world():
    return 'Welcome to Schedule Fighter <3!!!'

if __name__ == '__main__':
    app.run(debug=True)
