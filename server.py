#!/usr/bin/python3

from typing import NoReturn
import os
import subprocess
import sys
import http.server

SERVER_PORT :int = 8000
DETECT_PORT :int = 8001

default_url :str = "http://127.0.0.1"




if __name__ == '__main__':
    print("起動")

