#!/usr/bin/python3

import os
import json
import flask

SERVER_PORT :int = 8000
DETECT_PORT :int = 8001
default_url :str = "http://127.0.0.1"
https = False
def http_or_https():
    json_file = open(os.environ['HOME'] + '/extension/xss2/dist/chrome/manifest.json', 'r')
    json_manifest = json.load(json_file)
    for element in json_manifest['permissions']:
        if "https" in element:
            if "http:" in element:
                https = False
            else:
                https = True

    json_file.close()


app = flask.Flask(__name__)

@app.route("/")
def get():
    return "Normal Response"

@app.route("/favicon.ico")
def favicon():
    return ""

@app.route("/fuzz", methods=['GET'])
def fuzzing():
    fuzz = flask.request.args.get('fuzz')
    return fuzz


if __name__ == '__main__':
    http_or_https()
    if https is False:
        app.run(debug=False, host="127.0.0.1", port=SERVER_PORT)
    else:
        app.run(debug=False, host="127.0.0.1", port=SERVER_PORT, ssl_context=(os.environ['HOME'] + '/openssl/server.crt', os.environ['HOME'] + '/openssl/server.key'))

