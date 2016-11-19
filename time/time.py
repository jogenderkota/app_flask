
from flask import Flask, flash, redirect, render_template, url_for, request
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time/')
def time():
    utc_time = datetime.utcnow()
    print(utc_time)
    return 'TIME : %s'%utc_time

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash(u'Invalid password provided', 'error')
            return redirect(url_for('index'))
    return render_template('login.html', error = error)
 
if __name__ == "__main__":
    app.run(debug = True)


