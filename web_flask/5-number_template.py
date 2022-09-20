#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb_2():
    """hello HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def hello_hbnb_3(text):
    """hello HBNB"""
    return "C " + text.replace("_", " ")


@app.route("/python")
def hello_hbnb_5():
    """hello HBNB"""
    return "Python is cool"


@app.route("/python/<text>")
def hello_hbnb_4(text):
    """hello HBNB"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>")
def hello_hbnb_6(n):
    """hello HBNB"""
    return str(n) + " is a number"


@app.route("/number_template/<int:n>")
def hello_hbnb_7(n):
    """hello HBNB"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
