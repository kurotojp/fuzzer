#!/usr/bin/python3

import flask

SERVER_PORT :int = 8000
DETECT_PORT :int = 8001
default_url :str = "http://127.0.0.1"

app = flask.Flask(__name__)
TEST_NUM = 0;
f = open('vuln.txt', 'w')

@app.route("/")
def get():
    global TEST_NUM
    if TEST_NUM==0:
        TEST_NUM = 1
        return "TEST"
    else:
        fuzz = flask.request.args.get("fuzz")
        f.writelines(fuzz + "\n")
        return "fuzznum = " + fuzz

@app.route("/favicon.ico")
def favicon():
    return ""

if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1", port=DETECT_PORT)

