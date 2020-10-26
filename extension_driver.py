import selenium.webdriver
import pwn

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

driver.get(target_url)
driver.add_cookie({"name":"key", "value":"value"})

fuzz = "location.href="

driver.get(target_url + "#" + fuzz + fuzz_url)
