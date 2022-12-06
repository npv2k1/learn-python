from threading import Thread
import threading
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium import *
import os
import time
import pyautogui
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

def openSelenium():
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    action = ActionChains(driver)
    driver.get("https://facebook.com")
    time.sleep(1)

if __name__ == '__main__':
    try:
        t = time.time()
        t1 = threading.Thread(target=openSelenium)
        t2 = threading.Thread(target=openSelenium)
        t3 = threading.Thread(target=openSelenium)
        t1.start()
        t2.start()
        t3.start()
        print("done in ", time.time() - t)
    except:
        print("error")
