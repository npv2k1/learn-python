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
options.add_experimental_option("detach", True)

def openSelenium():
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    # action = ActionChains(driver)
    driver.get("https://facebook.com")
    time.sleep(1)


if __name__ == '__main__':
   openSelenium()
