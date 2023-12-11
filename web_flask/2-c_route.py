#!/usr/bin/python3
""" Return html page """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Return Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """ Return HBNB"""
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ Return text in page c"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    """ """
    app.run(host='0.0.0.0', port=5000)