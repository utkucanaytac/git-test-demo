import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

def hello():
    return render_template('hello.html')

