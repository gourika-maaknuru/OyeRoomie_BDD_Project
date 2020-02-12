import logging
from selenium import webdriver
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--headless")
chrome_options=options

def before_all(context):
    selenium_logger = logging.getLogger(
        'selenium.webdriver.remote.remote_connection')
    selenium_logger.setLevel(logging.WARN)
    context.browser = webdriver.Chrome(chrome_options=options, executable_path="C:\\Users\\gouri\\PycharmProjects\\FirstWebdriverTest\\test\\Selenium _practise\\Drivers\\chromedriver.exe")
    print("chrome Headless Browser Invoked")
    context.browser.get('https://www.Oyeroomie.com/')
    print("OyeRoomie page opened")
    context.browser.implicitly_wait(3)


def after_all(context):
    context.browser.quit()