#!/usr/bin/python3

from typing import NoReturn
import os
import subprocess
import sys
import http.server

SERVER_PORT :int = 8000
DETECT_PORT :int = 8001

default_url :str = "http://127.0.0.1"


def server():
    server_address = ('', SERVER_PORT)
    Handler = http.server.BaseHTTPRequestHandler
    httpd = http.server.HTTPServer(server_address, Handler)
    print('serving at port', str(SERVER_PORT))
    
    httpd.serve_forever()

if __name__ == '__main__':
    server()

