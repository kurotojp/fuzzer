#!/usr/bin/python3

from typing import NoReturn
import os
import subprocess
import sys
import flask

SERVER_PORT :int = 8000
DETECT_PORT :int = 8001
app = flask.Flask(__name__)
TEST_NUM = 0;


@app.route("/")
def get():
    print("XSS DETECT!")
    return "XSS DETECT!"

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=DETECT_PORT)

