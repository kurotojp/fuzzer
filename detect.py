#!/usr/bin/python3

import flask
import os
import sys

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
        try:
            fuzz = flask.request.args.get("fuzz")
            if fuzz % 2 == 0:
                f.writelines("#Fuzzing Fuzznum=" + fuzz/2 + 1)
            else:
                f.writelines("/?a=Fuzzing Fuzznum=" + fuzz/2)

            return "fuzznum = " + fuzz
        except:
            return "What!?"


@app.route("/favicon.ico")
def favicon():
    return ""

@app.route("/end")
def end():
    sys.exit()
    return "End"

if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1", port=DETECT_PORT)

