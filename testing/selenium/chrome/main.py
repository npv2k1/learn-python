import time
from selenium import webdriver
from selenium import *
import time
from selenium.webdriver.chrome.service import Service


def openSelenium():
    options = webdriver.ChromeOptions()
    service = Service(executable_path=r'chromedriver')
    options.add_argument("--disable-notifications")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://facebook.com")


if __name__ == '__main__':
    openSelenium()
