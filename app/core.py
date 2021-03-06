import os
from flask import Flask
app = Flask(__name__)
app.config.from_object(os.environ['FLASK_APP_SETTINGS'])


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
