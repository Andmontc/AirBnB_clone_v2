#!/usr/bin/python3
""" script that starts a Flask web application """


from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_display():
    """ function that display in the hbnb clone """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenity = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)
    return render_template('100-hbnb.html', states=states,
                           amenity=amenity, places=places)


@app.teardown_appcontext
def teardown(self):
    """ Close Sql session """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
