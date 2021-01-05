import selenium.common.exceptions
import selenium.webdriver
import pwn
import time
import os
import argparse
from pynput import mouse
import pyautogui
import json

SERVER_PORT :int = 8000
DETECT_PORT :int = 8001
default_url :str = "http://127.0.0.1"
target_url :str = default_url + ":" + str(SERVER_PORT)
fuzz_url :str = default_url + ":" + str(DETECT_PORT)
https = False
http = False
target_http_domain = "http://127.0.0.1"
target_https_domain = "https://127.0.0.1"
click_num = 0
fuzzing_number = 0
click_position = []
click_x = None
click_y = None
click_button = None

options = selenium.webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
#options.add_argument("--headless")
#options.add_extension("~/extension/xss2/dist/chrome.crx")
#options.add_extension("/home/cysec/Downloads/5000-trillion-yen-converter/app.crx")
driver = None
#driver = selenium.webdriver.Chrome("/usr/bin/chromedriver", options=options)
#driver.set_page_load_timeout(3)
#driver.close()

def add_click_position():
    global click_position
    global click_x
    global click_y
    global click_button
    click_position.append((click_x, click_y, click_button))


def on_click(x, y, button, pressed):
    global click_x
    global click_y
    global click_button 
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    click_x = x
    click_y = y
    click_button = button
    if not pressed:
        # Stop listener
        return False

def test():
    global driver
    global target_url
    while(True):
        try:
            io = pwn.remote('127.0.0.1', SERVER_PORT)
            io.send('GET /\r\n\r\n')
            break
        except:
            time.sleep(5)

    while(True):
        try:
            io = pwn.remote('127.0.0.1', DETECT_PORT)
            io.send('GET /\r\n\r\n')
            break
        except:
            time.sleep(5)
    driver = selenium.webdriver.Chrome("/usr/bin/chromedriver", options=options)
    driver.set_page_load_timeout(3)
    driver.get(target_url)

def url_hash_Fuzzing(fuzz):
    global driver
    try:
        driver.get(target_url + "#" + fuzz)
    except:
        driver.get(target_url + "#" + fuzz)

def get_Fuzzing(fuzz):
    global driver
    try:
        driver.get(target_url + "?a=" + fuzz)
    except:
        driver.get(target_url + "?a=" + fuzz)

def cookie_Fuzzing(fuzz):
    global driver
    try:
        driver.add_cookie({"name":str(fuzz), "value":str(fuzz)})
        driver.get(target_url)
    except:
        driver.add_cookie({"name":str(fuzz), "value":str(fuzz)})
        driver.get(target_url)

def nomal_response_Fuzzing(fuzz):
    try:
        driver.get(target_url + "/fuzz?fuzz=" + fuzz)
    except:
        driver.get(target_url + "/fuzz?fuzz=" + fuzz)


def end():
    global driver
    try:
        driver.get(target_url + "/end")
        driver.get(fuzz_url + "/end")
    except:
        driver.get(target_url + "/end")
        driver.get(fuzz_url + "/end")
    end_close()

def end_close():
    global driver
    driver.close()

def extension_Fuzzing(fuzz):
    try:
        driver.get(target_url + "#" + fuzz)
    except:
        driver.get(target_url + "#" + fuzz)

    for num in range(click_num):
        pos_x = click_position[num][0]
        pos_y = click_position[num][1]
        pos_button = click_position[num][2]
        if "right" in str(pos_button):
            pyautogui.click(x=pos_x, y=pos_y, button="right")
        else:
            pyautogui.click(x=pos_x, y=pos_y, button="left")

        if num == fuzzing_number - 1:
            pyautogui.typewrite(fuzz)
            pyautogui.press("enter")

        time.sleep(0.5)

if __name__ == '__main__':
    parser = argparse.ArgumentParser("python3 fuzzer.py extension")
    parser.add_argument('extension', help="Where extension")

    try:
        args = parser.parse_args()
    except:
        print("[-] No extension selected")
        end_close()
        exit(1)

    if os.path.exists(args.extension) is False:
        print("[-] No extension! Path miss?")
        end_close()
        exit(1)

    options.add_extension(args.extension)
    test()
    click_num = int(input("click_num = "))
    fuzzing_number = int(input("fuzzing_num = "))

    if fuzzing_number > click_num:
        print("[-] fuzzing_num > click_num")
        exit(1)

    if click_num > 0:
        for num in range(click_num):
            with mouse.Listener(
                    on_click=on_click
                    ) as listener:
                listener.join()
            add_click_position()
        if click_num > 0:
            print(click_position)

    start_time = time.time()

    json_file = open(os.environ['HOME'] + '/extension/xss2/dist/chrome/manifest.json', 'r')
    json_manifest = json.load(json_file)
    for element in json_manifest['permissions']:
        if "https" in element:
            https = True
            if "https://*" in element:
                print("https all domain")
            elif "https://" in element:
                target_https_domain = element
                
        elif "http" in element:
            http = True
            if "http://*" in element:
                http = True
            elif "http://" in element:
                target_http_domain = element
                
    if http is True:
        target_url = target_http_domain + str(SERVER_PORT)
        print(target_http_domain)
    else:
        if https is True:
            target_url = target_https_domain + str(SERVER_PORT)
        else:
           print("What!?") 

    json_file.close()

    f = open('fuzz.txt', 'r')
    fuzz_num = 1
    while True:
        fuzz = f.readline().format(fuzz_url, str(fuzz_num))
        if fuzz != "" and fuzz != "\n":
            url_hash_Fuzzing(fuzz)
            fuzz_num += 1
            get_Fuzzing(fuzz)
            fuzz_num += 1
            if click_num > 0:
                extension_Fuzzing(fuzz)

            fuzz_num += 1
        else:
            break
    f.close()

    stop_time = time.time() - start_time
    end()
    print("Fuzzing Finish!\nCheck vuln.txt!\nTime:{0}".format(stop_time) + "[sec]")
