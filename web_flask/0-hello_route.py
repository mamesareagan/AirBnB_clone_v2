#!/usr/bin/python3
"""starts a web flask app"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hellobnb():
    """displaay helo bnb"""
    return f"Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
