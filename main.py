from flask import Flask, request, redirect, render_template, jsonify
import math
from timeit import default_timer as timer
import sqlite3
import setuptable 
import usercreator

# con = sqlite3.connect('login.db')

def create_app():
    app = Flask(__name__)
    return app
    
app = create_app()

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

@app.route('/createtables', methods=['GET'])
def create():
    setuptable.createtable()
    usercreator.add()
    return jsonify(
        msg="tables created"
    )

@app.route('/droptables', methods=['GET'])
def drop():
    setuptable.droptable()
    return jsonify(
        msg="tables dropped"
    )

@app.route("/factorial/<n>")
def factorial(n=None):
    n = int(n)
    start = timer()

    factorial = math.factorial(n) # uses a c funcion, faster

    end = timer()

    time = end-start
    
    return jsonify(
        value=factorial,
        t=time
    )
    # return render_template('a.html', n=factorial, t = time)

@app.route("/fibonacci/<n>")
def fibonacci(n=None):
    n = int(n)
    start = timer()
    
    # binet formula
    fibonacci =  round((math.pow(1.618033988749895, n) - math.pow(-0.6180339887498949, n)) / 2.23606797749979, 5)

    end = timer()

    time = end-start

    return jsonify(
        value=fibonacci,
        t=time
    )

    # return render_template('b.html', n=fibonacci, t = time)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)