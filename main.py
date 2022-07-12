from flask import Flask, request, redirect, render_template, url_for
import math

from timeit import default_timer as timer

import sqlite3

import setuptable 

con = sqlite3.connect('login.db')

app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        a = setuptable.verifyuser(request.form['username'], request.form['password'])
        if not (a):
                message = 'Error: Invalid Credentials. Please try again.'
        else:
                message = 'Success: Login Sucessful.'
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)