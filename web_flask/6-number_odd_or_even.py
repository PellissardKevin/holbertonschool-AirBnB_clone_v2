#!/usr/bin/python3
""" Return html page """
from flask import Flask, request
from flask import render_template

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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_route(text='is cool'):
    """ Return text in page python"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """ Return text in page number"""
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Return text in page number"""
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ Return text in page number"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    """ """
    app.run(host='0.0.0.0', port=5000)
