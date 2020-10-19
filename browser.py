#!/usr/bin/python3

from typing import NoReturn
import os
import subprocess
import sys
import http.server
import webbrowser

SERVER_PORT :int = 8000
DETECT_PORT :int = 8001
default_url :str = "http://127.0.0.1"

def browse():
    #webbrowser.register("chrome")
    chrome = webbrowser.get("google-chrome")
    chrome.open_new_tab(default_url + str(SERVER_PORT))

if __name__ == '__main__':
    browse()

