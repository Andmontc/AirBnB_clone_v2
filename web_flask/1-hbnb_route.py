#!/usr/bin/python3
""" Flask module """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ function that display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display on route hbnb """
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
