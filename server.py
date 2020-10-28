#!/usr/bin/python3

import flask

SERVER_PORT :int = 8000
DETECT_PORT :int = 8001

app = flask.Flask(__name__)

@app.route("/")
def get():
    return "Test"

if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1", port=SERVER_PORT)

