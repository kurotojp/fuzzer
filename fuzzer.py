import selenium.common.exceptions
import selenium.webdriver
import pwn
import time
import json
import os
import argparse
import subprocess


SERVER_PORT :int = 8000
DETECT_PORT :int = 8001
default_url :str = "http://127.0.0.1"
target_url :str = default_url + ":" + str(SERVER_PORT)
fuzz_url :str = default_url + ":" + str(DETECT_PORT)
https = False
http = False
target_http_domain = "http://127.0.0.1"
target_https_domain = "https://127.0.0.1"


options = selenium.webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
#options.add_argument("--headless")
options.add_extension("~/extension/xss2/dist/chrome.crx")
#options.add_extension("/home/cysec/Downloads/5000-trillion-yen-converter/app.crx")
driver = selenium.webdriver.Chrome("/usr/bin/chromedriver", options=options)
driver.set_page_load_timeout(3)

def test():
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
    start_time = time.time()

    '''
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
    '''

    f = open('fuzz.txt', 'r')
    fuzz_num = 1
    while True:
        fuzz = f.readline().format(fuzz_url, str(fuzz_num))
        if fuzz != "" and fuzz != "\n":
            url_hash_Fuzzing(fuzz)
            fuzz_num += 1
            get_Fuzzing(fuzz)
            fuzz_num += 1
        else:
            break
    f.close()

    stop_time = time.time() - start_time
    end()
    print("Fuzzing Finish!\nCheck vuln.txt!\nTime:{0}".format(stop_time) + "[sec]")
