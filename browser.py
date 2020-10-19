#!/usr/bin/python3

from typing import NoReturn
import os
import subprocess
import sys
import http.server
import webbrowser
import time
import pwn


SERVER_PORT :int = 8000
DETECT_PORT :int = 8001
default_url :str = "http://127.0.0.1"
target_url :str = default_url + ":" + str(SERVER_PORT)
fuzz_url :str = default_url + ":" + str(DETECT_PORT) 
chrome = webbrowser.get("google-chrome")



def fuzzing(fuzz : str):
    chrome.open(target_url + "#" + fuzz)

def test():
    while(True):
        try:
            io = pwn.remote('127.0.0.1', SERVER_PORT)
            io.send('GET /\r\n\r\n')
            req = io.recv()
            print("[*]server.pyの起動を確認！")
            break
        except:
            print("[-]server.pyがうまく起動していません")
            time.sleep(5)

    while(True):
        try:
            io = pwn.remote('127.0.0.1', DETECT_PORT)
            io.send('GET /\r\n\r\n')
            req = io.recv()
            print("[*]detect.pyの起動を確認！")
            break
        except:
            print("[-]detect.pyがうまく起動していません")
            time.sleep(5)


if __name__ == '__main__':
    test()
    fuzz :str = "location.href='" + fuzz_url + "';" 
    fuzzing(fuzz)

