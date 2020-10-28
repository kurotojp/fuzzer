import selenium.webdriver
import pwn
import time

SERVER_PORT :int = 8000
DETECT_PORT :int = 8001
default_url :str = "http://127.0.0.1"
target_url :str = default_url + ":" + str(SERVER_PORT)
fuzz_url :str = default_url + ":" + str(DETECT_PORT)

options = selenium.webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
#options.add_argument("--headless")
options.add_extension("~/extension/xss2/dist/chrome.crx")
driver = selenium.webdriver.Chrome("/usr/bin/chromedriver", options=options)


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

def urlFuzzing(fuzz1, fuzz2):
    driver.get(target_url + "#" + fuzz1 + fuzz_url + fuzz2)
    print(driver.page_source)
    #driver.add_cookie({"name":"key", "value":"value"})


if __name__ == '__main__':
    test()

    fuzz1 = "location.href='"
    fuzz2 = "';"
    urlFuzzing(fuzz1, fuzz2)
