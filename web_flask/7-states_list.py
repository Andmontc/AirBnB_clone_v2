#!/usr/bin/python3
""" Flask module """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ function that display a page with the states """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """ Close Sql session """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
