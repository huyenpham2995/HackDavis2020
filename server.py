#!/usr/bin/env python

import os
from flask import Flask, render_template
app = Flask(__name__)

app.config['SECRET_KEY'] = ''

@app.route("/")
def index():
    # return "welcome to schedule fighter"
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)
