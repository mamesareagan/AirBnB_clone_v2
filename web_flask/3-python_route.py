from flask import Flask
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
