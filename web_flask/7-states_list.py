#!/usr/bin/python3
""" Starts up a Flask web app"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
