#!/bin/python3

from flask import Flask

app = Flask(__name__)

#Python decorator
@app.route("/")

def index():
    return "Toto si necakal"


app.run(host="0.0.0.0", port=80)
