#!/usr/bin/python3
""" Flask module """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_states_cities():
    """ function that display a page with the city of the states """
    s = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=s)


@app.teardown_appcontext
def teardown(self):
    """ Close Sql session """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
