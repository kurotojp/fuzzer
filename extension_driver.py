import selenium.webdriver
import pwn
import time
import json

SERVER_PORT :int = 8000
DETECT_PORT :int = 8001
default_url :str = "http://127.0.0.1"
target_url :str = default_url + ":" + str(SERVER_PORT)
fuzz_url :str = default_url + ":" + str(DETECT_PORT)
https = False
http = False

options = selenium.webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
#options.add_argument("--headless")
options.add_extension("~/extension/xss2/dist/chrome.crx")
#driver = selenium.webdriver.Chrome("/usr/bin/chromedriver", options=options)


def test():
    while(True):
        try:
            io = pwn.remote('127.0.0.1', SERVER_PORT)
            io.send('GET /\r\n\r\n')
            req = io.recv()
            #print("[*]server.pyの起動を確認！")
            break
        except:
            #print("[-]server.pyがうまく起動していません")
            time.sleep(5)

    while(True):
        try:
            io = pwn.remote('127.0.0.1', DETECT_PORT)
            io.send('GET /\r\n\r\n')
            req = io.recv()
            #print("[*]detect.pyの起動を確認！")
            break
        except:
            #print("[-]detect.pyがうまく起動していません")
            time.sleep(5)

def url_hash_Fuzzing(fuzz):
    driver = selenium.webdriver.Chrome("/usr/bin/chromedriver", options=options)
    driver.get(target_url + "#" + fuzz)
    #detect(driver.page_source)


def cookie_Fuzzing(fuzz):
    driver = selenium.webdriver.Chrome("/usr/bin/chromedriver", options=options)
    driver.get(target_url)
    driver.add_cookie({"name":str(fuzz), "value":str(fuzz)})

def post_Fuzzing(fuzz):
    driver = selenium.webdriver.Chrome("/usr/bin/chromedriver", options=options)


if __name__ == '__main__':
    test()

    json_file = open('/home/cysec/extension/xss2/dist/chrome/manifest.json', 'r')
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
        if target_http_domain is None:
            #all
            print("all")
        else:
            target_url = target_http_domain + str(SERVER_PORT)
    else:
        if https is True:
            if target_https_domain is None:
                #all
                target_url = "https://127.0.0.1" + str(SERVER_PORT)
            else:
                target_url = target_https_domain + str(SERVER_PORT)
        else:
           print("What!?") 



    f = open('fuzz.txt', 'r')
    fuzz_num = 1
    while True:
        fuzz = f.readline().format(fuzz_url, str(fuzz_num))
        if fuzz != "" and fuzz != "\n":
            url_hash_Fuzzing(fuzz)
            #cookie_Fuzzing(fuzz)
            fuzz_num += 1
            #print("fuzz = " + fuzz)
        else:
            break
    f.close()
