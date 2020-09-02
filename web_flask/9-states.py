#!/usr/bin/python3
""" script that starts a Flask web application """


from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_and_state(id=None):
    """ function that display a page with the states
        or the cities with an id """
    state = None
    states = storage.all(State)
    if id:
        idgiven = "State." + id
        if idgiven in states.keys():
            state = states[idgiven]
    return render_template('9-states.html', id=id, state=state, states=states)

@app.teardown_appcontext
def teardown(self):
    """ Close Sql session """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")