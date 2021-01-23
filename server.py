#!/usr/bin/python3

import os
import json
import flask
import sys
import argparse

SERVER_PORT :int = 8000
DETECT_PORT :int = 8001
default_url :str = "http://127.0.0.1"
https = False

f = open('escape.txt', 'w')
write_num = 0

def http_or_https(manifest):
    json_file = open(manifest, 'r')
    
    json_manifest = json.load(json_file)
    try:
        for element in json_manifest['permissions']:
            if "https" in element:
                if "http:" in element:
                    https = False
                else:
                    https = True
    except:
        print("permissions is none")


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

@app.route("/end")
def end():
    sys.exit()
    return "End"

@app.route("/x")
def escape():
    if write_num == 0:
        f.writelines("This extension wasn't escaped.")
    return flask.Response(response="", status=404)

if __name__ == '__main__':
    parser = argparse.ArgumentParser("python3 server.py extension")
    parser.add_argument("extension", help="Where extension")

    try:
        args = parser.parse_args()
    except:
        print("[-] No extension selected")
        exit(1)

    if os.path.exists(args.extension) is False:
        print("[-] No extension! Path miss?")
        exit(1)

    manifest = args.extension.split(".crx")[0] + "/manifest.json"
    if os.path.exists(manifest) is False:
        print("[-] manifestfile is not found!")
        exit(1)

    http_or_https(manifest)
    if https is False:
        app.run(debug=False, host="127.0.0.1", port=SERVER_PORT)
    else:
        app.run(debug=False, host="127.0.0.1", port=SERVER_PORT, ssl_context=(os.environ['HOME'] + '/openssl/server.crt', os.environ['HOME'] + '/openssl/server.key'))

