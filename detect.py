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
            #f.writelines(fuzz)
            if int(fuzz) % 2 == 1:
                f.writelines("#Fuzzing Fuzznum=" + str(int(fuzz)//2 + 1) + "\n")
            else:
                f.writelines("/?a=Fuzzing Fuzznum=" + str(int(fuzz)//2) + "\n")

            return "fuzznum = " + fuzz
        except:
            return "What!?"


@app.route("/favicon.ico")
def favicon():
    return ""

@app.route("/end")
def end():
    global f
    f.close()
    sys.exit()
    return "End"

if __name__ == '__main__':
    try:
        app.run(debug=False, host="127.0.0.1", port=DETECT_PORT)
    except:
        f.close()
