from flask import Flask
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
