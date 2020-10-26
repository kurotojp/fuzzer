import os
import selenium.webdriver

options = selenium.webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
#options.add_argument("--headless")
#options.add_extension("/home/cysec/extension/vulnerability-chrome-extension/dist/chrome.crx")
options.add_extension("/home/cysec/extension/xss2/dist/chrome.crx")
driver = selenium.webdriver.Chrome("/usr/bin/chromedriver", options=options)

url = "http://sample.cysec:8000/"
driver.get(url)
driver.add_cookie({"name":"key", "value":"value"})

url = "http://sample.cysec:8000/#location.href='http://sample.cysec:8001'"
driver.get(url)

