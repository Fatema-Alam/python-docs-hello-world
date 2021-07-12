from flask import Flask
import json
import requests


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Booo!"


@app.route("/<solution>")
def predict(solution):
    return "solution"

