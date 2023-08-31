#!/usr/bin/python3
'''
Script that starts a Flask web application.
'''

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
   return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return f"C {text}"

@app.route("python")
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    text = text.replace("_", " ")
    return f"Python {text}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
