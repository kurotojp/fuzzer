#!/usr/bin/python3

import flask

SERVER_PORT :int = 8000
DETECT_PORT :int = 8001
app = flask.Flask(__name__)
TEST_NUM = 0;


@app.route("/")
def get():
    global TEST_NUM
    if TEST_NUM==0:
        TEST_NUM = 1
        print("TEST")
        return "TEST"
    else:
        print("XSS DETECT!")
        return "XSS DETECT!"

if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1", port=DETECT_PORT)

