#!/usr/bin/python3
<<<<<<< HEAD
=======
""" Return html page """
>>>>>>> adc5db0d26aaccb4cea9a4f05ab38b52617ed356
from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
@app.route("/")
def hello_world():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======

@app.route("/", strict_slashes=False)
def hello_world():
    """ Return Hello HBNB"""
    return "Hello HBNB!"


if __name__ == '__main__':
    """ """
    app.run(host='0.0.0.0', port=5000)
>>>>>>> adc5db0d26aaccb4cea9a4f05ab38b52617ed356
