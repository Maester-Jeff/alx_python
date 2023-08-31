#!/usr/bin/python3
'''
Script that starts a Flask web application.
'''

from flask import Flask, render_template

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

@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    text = text.replace("_", " ")
    return f"Python {text}"

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f'{n} is a number'

@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
