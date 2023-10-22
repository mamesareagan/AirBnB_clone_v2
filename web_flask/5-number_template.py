#!/usr/bin/python3
"""starts flask app"""
from flask import Flask,render_template
from markupsafe import escape

'''flask app'''


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hellobnb():
    '''returns hello bnb'''
    return f"Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def bnb():
    '''displays hbnb'''
    return f"HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    '''displays text passed'''
    text = text.replace("_", " ")
    return f"C {text}"

@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_route(text="is cool"):
    """display txt in route"""
    text = text.replace("_", " ")
    return f"Python {text}"

@app.route("/number/<n>", strict_slashes=False)
def numberonly(n):
    '''prints if n is Aa number'''
    n = int(n)
    return f"{n} is a number"

@app.route("/number_template/<n>", strict_slashes=False)
def rendertmplt(n):
    """renders a webpage if n is int"""
    n = int(n)
    if n >= 0:
        return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
