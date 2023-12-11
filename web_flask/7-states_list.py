#!/usr/bin/python3
<<<<<<< HEAD
=======
"""Module for the different pages with Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    """Close storage"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states():
    """List all states"""
    return render_template("7-states_list.html", states=storage.all(State))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> adc5db0d26aaccb4cea9a4f05ab38b52617ed356
